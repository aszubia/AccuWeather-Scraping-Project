# EIT-Takehome-Project
This is a project for developing a comprehensive understanding of weather patterns by scraping, cleaning, analyzing and visualizing weather data.

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
  - **Temperature Trend**: Visualizes the changes in temperature over time using a line chart or area chart to highlight daily highs and lows.
  - **Precipitation Probability**: Displays the probability of precipitation as a line chart, potentially showing variations over time.
  - **Wind Speed**: Illustrates the wind speed distribution using a bar chart to the range and typical values. A color was used to differentiate the intensity of the wind. 
  - **UV Index**: Presents the UV index as a bar chart with different colors represent varying levels of UV radiation.
  - **Correlation Matrix**: The correlation matrix heatmap visualizes the relationships between different weather variables. Values closer to 1 or -1 indicate strong correlations, either positive or negative, respectively.
  - **Feature Importance**: This bar chart shows the importance of each feature in predicting the average temperature. Features with higher values are more significant in the model's predictions.
  - **Dash**: This also includes a interactive dashboard on the last part of the Jupyter File.
- [`interactiveDashboard.py`](interactiveDashboard.py): This Python file creates a dynamic, interactive dashboard using the Dash framework. The dashboard allows users to explore the cleaned weather data. 
