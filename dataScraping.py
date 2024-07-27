import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 

# Add the url of AccuWeather website
url = 'https://www.accuweather.com/en/ph/baguio-city/1-262309_1_al/daily-weather-forecast/1-262309_1_al'

# Initialize the webdriver
driver = webdriver.Chrome()
driver.get(url)

title = driver.title

if "AccuWeather" in title: 
    print("Successfully opened AccuWeather website")
else:
    print("Failed to open AccuWeather website")

# Find all the elements containing daily forecast data
weather_information = driver.find_elements(By.CLASS_NAME, 'daily-wrapper')

if weather_information:
    print("Successfully collected weather data variables")
else:
    print("Failed to collect weather data variables")


weather_data = []   # Initialize an empty list to store the data

# Collect the weather information variables for each day. 
# This includes date, subdate, temp_high, temp_low, condition, precip, real_feel, real_feelShade, uv_index, wind_speed
for information in weather_information:
    try:
        date = information.find_element(By.CLASS_NAME, 'date').text
        temp_high = information.find_element(By.CLASS_NAME, 'high').text
        temp_low = information.find_element(By.CLASS_NAME, 'low').text
        condition = information.find_element(By.CLASS_NAME, 'phrase').text
        precip = information.find_element(By.CLASS_NAME, 'precip').text
        real_feel = information.find_element(By.XPATH, ".//p[contains(text(), 'RealFeel')]/span[@class='value']").text
        real_feelShade = information.find_element(By.XPATH, ".//p[contains(text(), 'RealFeel Shade™')]/span[@class='value']").text
        uv_index = information.find_element(By.XPATH, ".//p[contains(text(), 'Max UV Index')]/span[@class='value']").text
        wind_speed = information.find_element(By.XPATH, ".//p[contains(text(), 'Wind')]/span[@class='value']").text
        
        weather_data.append([date, temp_high, temp_low, condition, precip, real_feel, uv_index, wind_speed])
        
    except Exception as e:
        print(f"Error occurred: {e}")

#Set the name of the csv file
filename = 'weather_data.csv'

# Save the weather data to a csv file        
if weather_data:
    print(f"\nSuccessfully extracted weather data for {len(weather_data)} days!\n")
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'High Temperature', 'Low Temperature', 'Condition', 'Precipitation Probability', 'Real Feel', 'UV Index', 'Wind Speed'])
        writer.writerows(weather_data)
    
    print("Data extracted and saved to " + filename)
else:
    print("No weather data extracted. Please check if the website structure or CSS classes have changed.")
    

    