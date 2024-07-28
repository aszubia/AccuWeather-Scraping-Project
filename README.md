# EIT-Takehome-Project
This is a project for developing a comprehensive understanding of weather patterns by scarping, cleaning and analyzing and visualizing weather data.

# Necessary Libraries
- **Selenium:** Web scraping framework for automating browser interactions.
- **Pandas:** Powerful library for data analysis and manipulation.
- **Matplotlib:** A plotting library used for data visualization. 
- **Scikit-Learn:** Machine learning library provides model building and evaluation tools. It was used for the Random Forest Model.
- **Plotly:** Interactive charting library used within Dash.
- **Dash:** Framework for building interactive web applications and dashboards.
- **Dash Bootstrap Components:** Library for styling and enhancing Dash layouts.

# Project Files
- [`dataScraping.py`](dataScraping.py): This is the python file for gathering weather data, this includes Date, Temperature(High/Low), Condition, Precipitation Probability, Real Feel, Real Feel Shade, UV Index and Wind Speed. The data will then be saved into [`weather_data.csv`](weather_data.csv) which will be then prepared for data cleaning.
- [`dataCleaning.py`](dataCleaning.py): This is a python file that will ensure that all the data from [`weather_data.csv`](weather_data.csv) are in the correct format such as removing non-numeric characters, correcting the date format and converting it into an other variables into a data type. The cleaned data will be then saved into [`cleaned_weather_data.csv`](cleaned_weather_data.csv)
- [`dataVisualization.ipynb`](dataVisualization.ipynb): It is a Jupyter Notebook that displays the graphical representation of the weather data. It generates the following graphs:
  - **Temperature Trend**
