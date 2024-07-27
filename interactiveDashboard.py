import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the data
cleaned_file_path = 'cleaned_weather_data.csv'
df = pd.read_csv(cleaned_file_path)

def wind_speed_color(wind_speed):
    if wind_speed <= 2:
        return 'blue'  # Calm
    elif wind_speed <= 4:
        return '#007FFF'  # Light
    elif wind_speed <= 6:
        return 'green'  # Moderate
    elif wind_speed <= 8:
        return 'orange'  # Fresh
    else:
        return 'red'  # Strong
    
def uv_color(uv_index):
    if uv_index <= 2:
        return 'blue'
    elif uv_index <= 5:
        return '#007FFF'
    elif uv_index <= 7:
        return 'green'
    elif uv_index <= 10:
        return 'orange'
    else:
        return 'red'

# Set the color functions for the graphs
df['UV Color'] = df['UV Index'].apply(uv_color)
df['Wind Speed Color'] = df['Wind Speed'].apply(wind_speed_color)

# Collect the data to be used for correlation analysis
data = {
    'Date': df['Date'],
    'High Temperature': df['High Temperature'],
    'Low Temperature': df['Low Temperature'],
    'Precipitation Probability': df['Precipitation Probability'],
    'UV Index': df['UV Index'],
    'Wind Speed': df['Wind Speed']
}

df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Calculate the average temperature
df['Average Temperature'] = (df['High Temperature'] + df['Low Temperature']) / 2

# Separate features and target variable. Target variable is 'Average Temperature'
X = df[['Date', 'Precipitation Probability', 'UV Index', 'Wind Speed']].copy()
y = df['Average Temperature']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RF Regressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
importances = rf.feature_importances_

feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = dbc.Container([
    html.H1("Weather Data Dashboard"),
    
    # Dropdown Configuration for selecting the graph to display
    dcc.Dropdown(
        id='graph-dropdown',
        options=[
            {'label': 'Temperature over Time', 'value': 'temperature'},
            {'label': 'Precipitation over Time', 'value': 'precipitation'},
            {'label': 'UV Index over Time', 'value': 'uv_index'},
            {'label': 'Wind Speed over Time', 'value': 'wind_speed'},
            {'label': 'Correlation Matrix', 'value': 'correlation'},
            {'label': 'Feature Importance', 'value': 'feature_importance'},
            
        ],
        value='temperature', 
        clearable=False
    ),
    
    # Graph to display based on the weather variables
    dcc.Graph(id='weather-graph'),
    
    # Div configurations for displaying the interpretation
    html.Div(id='interpretation', style={'margin-top': '20px'})
])

# Define callback for updating the graph
@app.callback(
    [Output('weather-graph', 'figure'),
     Output('interpretation', 'children')],
    [Input('graph-dropdown', 'value')]
)

# Define the function to update the graph
def update_graph(selected_graph):
    interpretation_text = ""
    
    # Temperature Graph Configuration
    if selected_graph == 'temperature':
        fig = px.line(df, x='Date', y=['High Temperature', 'Low Temperature'],
                      labels={'value': 'Temperature (°C)', 'Date': 'Date'},
                      title='High and Low Temperatures Over Time')
        interpretation_text = "This graph shows the variations in high and low temperatures over time. " \
                              "It can help identify patterns and trends in temperature changes."
                              
    # Precipitation Probability Graph Configuration
    elif selected_graph == 'precipitation':
        fig = px.line(df, x='Date', y='Precipitation Probability',
                      labels={'value': 'Precipitation (%)', 'Date': 'Date'},
                      title='Precipitation over Time')
        interpretation_text = "This graph displays the probability of precipitation over time. " \
                              "Higher values indicate a greater likelihood of rain or other forms of precipitation."
                              
    # UV Index Graph Configuration
    elif selected_graph == 'uv_index':
        fig = px.bar(df, x='Date', y='UV Index',
                     labels={'value': 'UV Index', 'Date': 'Date'},
                     title='UV Index Over Time',
                     text_auto=True,
                     color=df['UV Color'], 
                     color_discrete_map='identity')  
        fig.update_layout(showlegend=True, legend_title_text='UV Index Levels')
        interpretation_text = html.Div([
            "This bar chart illustrates the UV Index levels over time. Different colors represent varying levels of UV radiation:",
            html.Ul([
                html.Li("Low (0-2): ", style={'color': 'blue'}),
                html.Li("Moderate (3-5): ", style={'color': '#007FFF'}),
                html.Li("High (6-7): ", style={'color': 'green'}),
                html.Li("Very High (8-10): ", style={'color': 'orange'}),
                html.Li("Extreme (11+): ", style={'color': 'red'}),
            ])
        ])
        
    # Wind Speed Graph Configuration
    elif selected_graph == 'wind_speed':
        fig = px.bar(df, x='Date', y='Wind Speed',
                     labels={'value': 'Wind Speed (m/s)', 'Date': 'Date'},
                     title='Wind Speed Over Time',
                     text_auto=True,
                     color=df['Wind Speed Color'],  
                     color_discrete_map='identity')
        interpretation_text = html.Div([
            "This bar chart shows wind speed over time. The colors indicate the intensity of the wind:",
            html.Ul([
                html.Li("Calm (0-2 m/s): ", style={'color': 'blue'}),
                html.Li("Light (3-4 m/s): ", style={'color': '#007FFF'}),
                html.Li("Moderate (5-6 m/s): ", style={'color': 'green'}),
                html.Li("Fresh (7-8 m/s): ", style={'color': 'orange'}),
                html.Li("Strong (9+ m/s): ", style={'color': 'red'}),
            ])
        ])
        
    # Correlation Graph Configuration
    elif selected_graph == 'correlation':
        fig = px.imshow(correlation_matrix,
                        labels=dict(color="Correlation"),
                        title='Correlation Matrix Heatmap',
                        text_auto=True)
        interpretation_text = "The correlation matrix heatmap visualizes the relationships between different weather variables. " \
                              "Values closer to 1 or -1 indicate strong correlations, either positive or negative, respectively." 
                                
    # Feature Importance Graph Configuration
    elif selected_graph == 'feature_importance':
        fig = px.bar(feature_importance_df, x='Feature', y='Importance',
                     labels={'Importance': 'Importance', 'Feature': 'Feature'},
                     title='Feature Importances in Random Forest Model')
        fig.update_layout(xaxis_title='Feature', yaxis_title='Importance', xaxis_tickangle=-45)
        interpretation_text = "This bar chart shows the importance of each feature in predicting the average temperature. " \
                              "Features with higher values are more significant in the model's predictions."
    
    
    return fig, interpretation_text

# Run the app
if __name__ == '__main__':
    app.run_server(port=4080)
