# Import the required libraries
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

#Load the Dataset to prepare it for data cleaning
file_path = 'weather_data.csv'

df = pd.read_csv(file_path)

# Convert the weather variables columns into integers using str.extract
df['High Temperature'] = df['High Temperature'].str.extract(r'(\d+)').astype(int)
df['Low Temperature'] = df['Low Temperature'].str.extract(r'(\d+)').astype(int)
df['Precipitation Probability'] = df['Precipitation Probability'].str.extract(r'(\d+)').astype(int)
df['Real Feel'] = df['Real Feel'].str.extract(r'(\d+)').astype(int)
df['UV Index'] = df['UV Index'].str.extract(r'(\d+)').astype(int)
df['Wind Speed'] = df['Wind Speed'].str.extract(r'(\d+)').astype(int)

# Drop the Condition Column from the dataset
df.drop(columns=['Condition'], inplace=True)

# Convert the Date column into proper datetime format
df['Date'] = pd.to_datetime(df['Date'].str.split('\n').str[1] + '/2024', format='%m/%d/%Y')

# Save the cleaned data to a new CSV file named 'cleaned_weather_data.csv'
cleaned_file_path = 'cleaned_weather_data.csv'
df.to_csv(cleaned_file_path, index=False)
print("Cleaned data saved to", cleaned_file_path)