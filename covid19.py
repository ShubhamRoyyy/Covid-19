import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import plyer  # It's recommended to organize imports in standard groups.
from statsmodels.tsa.arima.model import ARIMA
from tkinter import *  # Avoid using wildcard imports, they can cause namespace pollution.
from tkinter import messagebox, filedialog  # Instead, import specific classes or functions.

import matplotlib.pyplot as plt  # It's recommended to organize imports in standard groups.

def data_collected():
    # Function to collect data from the provided URL
    url = "https://www.worldometers.info/coronavirus/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    tbody = soup.find('tbody')
    abc = tbody.find_all('tr')
    country_notification = cntdata.get().lower()  # Get the country name from the entry widget.

    # If no country is provided, default to "world"
    if country_notification == "":
        country_notification = "world"

    serial_number, countries, total_cases = [], [], []
    for i in abc:
        id = i.find_all('td')
        if id[1].text.strip().lower() == country_notification:
            # Display the COVID-19 statistics in a messagebox.
            total_cases1 = int(id[2].text.strip().replace(',', ""))
            total_death = id[4].text.strip()
            new_cases = id[3].text.strip()
            new_deaths = id[5].text.strip()
            messagebox.showinfo("Corona Virus Update", "Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}".format(total_cases1, total_death, new_cases, new_deaths))
            forecast_ARIMA(total_cases)  # Call the ARIMA forecasting function.

        serial_number.append(id[0].text.strip())
        countries.append(id[1].text.strip())
        total_cases.append(int(id[2].text.strip().replace(',', "")))

    # Create a DataFrame from the collected data.
    df = pd.DataFrame({'Total Cases': total_cases}, index=countries)
    return df

def forecast_ARIMA(total_cases):
    """
    Performing ARIMA forecasting on the total_cases data.

    Parameters:
    - total_cases (list): A list containing historical data of total COVID-19 cases.

    Returns:
    - None

    This function fits an ARIMA (AutoRegressive Integrated Moving Average) model to the provided total_cases data,
    forecasts future values, and plots the actual and forecasted values.
    """
    # Create ARIMA model with specified order (p=5, d=1, q=0).
    model = ARIMA(total_cases, order=(5,1,0))

    # Fit the ARIMA model to the data.
    model_fit = model.fit()

    # Forecast future values using the fitted model.
    forecast = model_fit.forecast(steps=5)

    # Plot actual and forecasted cases.
    plt.plot(total_cases)  # Plot historical total cases.
    plt.plot(np.arange(len(total_cases), len(total_cases)+5), forecast, color='red')  # Plot forecasted cases.
    plt.title('COVID-19 Cases Forecast')  # Set the title of the plot.
    plt.xlabel('Days')  # Label x-axis as 'Days'.
    plt.ylabel('Total Cases')  # Label y-axis as 'Total Cases'.
    plt.legend(['Actual Cases', 'Forecasted Cases'])  # Add legend to distinguish between actual and forecasted cases.
    plt.show()  # Display the plot.


def downloaddata():
    # Function to download data.
    global path
    if(len(flist) != 0):
        path = filedialog.askdirectory()  # Open a directory dialog for selecting download path.
    else:
        pass
    data_collected()  # Call the data collection function.
    flist.clear()    # Clear the list of file types after download.
    Inhtml.configure(state = 'normal')  # Enable the HTML button after download.
    Injson.configure(state = 'normal')  # Enable the JSON button after download.
    Inexcel.configure(state = 'normal')  # Enable the Excel button after download.

def inhtmldownload():
    # Function to mark HTML download option.
    flist.append('html')
    Inhtml.configure(state = 'disabled')  # Disable the HTML button after selection.

def injsondownload():
    # Function to mark JSON download option.
    flist.append('json')
    Injson.configure(state = 'disabled')  # Disable the JSON button after selection.

def inexceldownload():
    # Function to mark Excel download option.
    flist.append('csv')
    Inexcel.configure(state = 'disabled')  # Disable the Excel button after selection.

# Create the main window.
coro = Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+80')
coro.configure(bg='#046173')
coro.iconbitmap('corona.ico')    # Set the window icon.
flist = []  # List to store selected file types.
path = ''  # Variable to store download path.

#### Labels
# Create and place labels.
mainlabel = Label(coro,text="Corona Virus Live Tracker",font=("new roman",30,"bold"), bg = "#05897A",width=33
                        ,fg = "black",bd=5)
mainlabel.place(x=0,y=0)

label1 = Label(coro,text="Country Name",font=("arial",20,"bold"), bg = "#046173")
label1.place(x=15,y=100)

label2 = Label(coro,text="Download File in ",font=("arial",20,"bold"), bg = "#046173")
label2.place(x=15,y=200)

cntdata = StringVar()  # Variable to store country name input.
entry1 = Entry(coro,textvariable = cntdata ,font = ("arial",20,"bold"), relief = RIDGE,bd = 2 , width = 32)
entry1.place(x = 280, y = 100)

#### BUTTONS
# Create and place buttons.
Inhtml = Button(coro,text = "HTML", bg = "#2DAE9A", font = ("arial",15,"bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 5,width = 5,command = inhtmldownload)
Inhtml.place(x = 300, y = 200)

Injson = Button(coro,text = "JSON", bg = "#2DAE9A", font = ("arial",15,"bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 5,width = 5,command = injsondownload)
Injson.place(x = 400, y = 200)

Inexcel = Button(coro,text = "EXCEL", bg = "#2DAE9A", font = ("arial",15," bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 5,width = 5,command = inexceldownload )
Inexcel.place(x = 500, y = 200)

Submit = Button(coro,text = "Submit", bg = "#CB054A", font = ("arial",15,"bold"),relief = RIDGE,activebackground = "#7B0519",
                activeforeground = "white",bd = 5,width = 25,command = downloaddata)
Submit.place(x = 250, y = 260)

coro.mainloop()  # Start the main event loop.
