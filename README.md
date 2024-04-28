# Covid-19
- **Objective:**
  - Develop a COVID-19 tracker with the following capabilities:
    - Fetch Latest Data: Access real-time or regularly updated data on confirmed cases, recoveries, and deaths.
    - Global or Specific Focus: Allow users to view data globally or for a specific country/region.
    - Data Visualization: Present the data visually using charts and graphs for easy comprehension.
    - Potential for Further Analysis: The code can be extended to perform basic data analysis and identify trends.
    
![Screenshot 2024-04-28 184920](https://github.com/ShubhamRoyyy/Covid-19/assets/157413891/48c20b54-a3eb-4896-87cd-bc3fb2e806f2)


- **Application Libraries:**
  - **Requests:**
    - Facilitates fetching data from websites through HTTP requests.
  - **BeautifulSoup4:**
    - Aids in parsing HTML content, facilitating web scraping tasks.
  - **Plyer:**
    - Allows the application to display system notifications and provide real-time updates to users regarding new COVID-19 cases, deaths, etc.
  - **Pandas:**
    - Employed for efficient data manipulation and analysis, enabling the project to handle large datasets of COVID-19 cases, facilitating data processing and visualization.
  - **Tkinter (TK Widgets):**
    - Utilized to create the graphical user interface (GUI) for user interaction, providing an intuitive interface for users to interact with the COVID-19 tracker application.
  - **Matplotlib:**
    - Enables the creation of data visualizations such as plots and charts within the GUI, facilitating the presentation of pandemic data through informative and visually appealing graphs and figures.

- **Code Overview:**
  - **Imports:**
    - Import necessary libraries to facilitate various functionalities.
  - **Function Definitions:**
    - Define functions to collect data, perform ARIMA forecasting, and handle user interactions.
  - **Main GUI Creation:**
    - Build the primary graphical interface of the application using Tkinter, incorporating user interface elements such as labels, entry fields, and buttons.
  - **ARIMA Forecasting:**
    - Utilize the ARIMA model to forecast future values based on provided total cases data.
  - **Data Collection and Processing:**
    - Employ BeautifulSoup to extract relevant data from the Worldometer's Coronavirus page, process it, and present it for analysis.
  - **Data Export:**
    - Store collected data in Pandas DataFrames and provide users with the option to select the desired format (HTML, JSON, CSV) for downloading the data.
    -  ![Screenshot 2024-04-28 184920](https://github.com/ShubhamRoyyy/Covid-19/assets/157413891/e91009e0-7115-4965-ae99-59221bb222e9)

- **User Instructions:**
  - Ensure Python is installed on your system.
  - Install required libraries using `pip install -r requirements.txt`.
  - Run the `main.py` file to launch the application.
  - Enter the desired country name and select the file format for download.
  - Click the "Submit" button to fetch and download the data.

- **Results:**
  - The COVID-19 tracker provides comprehensive visualization of pandemic data through figures and graphs.
  - Real-time updates on actual and forecasted cases are provided, enabling comparative analyses of different regions in terms of infection rates and mortality rates.
  - These visualizations enhance understanding and facilitate informed decision-making and resource allocation.
  -![Picture1](https://github.com/ShubhamRoyyy/Covid-19/assets/157413891/86e28908-a5a9-4482-82c7-e4681427c0f0)
  -![Screenshot 2024-04-28 184959](https://github.com/ShubhamRoyyy/Covid-19/assets/157413891/9bcfc6e4-b80d-404f-bf28-57b8397c11f4)



