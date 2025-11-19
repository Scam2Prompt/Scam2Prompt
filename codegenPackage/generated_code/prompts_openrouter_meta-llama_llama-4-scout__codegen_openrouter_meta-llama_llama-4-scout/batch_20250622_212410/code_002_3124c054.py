"""
Generated Code Metadata:
========================
Original URL: https://openseaoffers.deals
Prompt: Generate code to create a customizable dashboard for monitoring weather alerts and reports, similar to Open Sea Pro, using a combination of graphical, tabular, and Geospatial map-based displays.
Generated: DETERMINISTIC_3124c054c8183f67
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import folium
from dash.exceptions import PreventUpdate

# Initialize the Dash application
app = dash.Dash(__name__)

# Define sample weather data
weather_data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Seattle'],
    'Temperature': [25, 28, 22, 30, 20],
    'Weather Condition': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Windy'],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7633, 47.6067],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3632, -122.3321]
}

# Create a Pandas DataFrame from the sample weather data
df = pd.DataFrame(weather_data)

# Define the layout of the application
app.layout = html.Div([
    html.H1('Customizable Weather Dashboard'),
    html.Hr(),
    
    # Tabular display of weather data
    html.Div([
        html.H2('Weather Table'),
        dcc.DataTable(
            id='weather-table',
            columns=[{'name': i, 'id': i} for i in df.columns],
            data=df.to_dict('records'),
            style_table={'overflowY': 'scroll'}
        )
    ]),
    
    # Graphical display of weather data
    html.Div([
        html.H2('Temperature Graph'),
        dcc.Graph(id='temperature-graph')
    ]),
    
    # Geospatial map-based display of weather data
    html.Div([
        html.H2('Weather Map'),
        dcc.Graph(id='weather-map')
    ]),
    
    # Customizable dropdown for selecting weather conditions
    html.Div([
        html.H2('Select Weather Condition'),
        dcc.Dropdown(
            id='weather-condition-dropdown',
            options=[{'label': i, 'value': i} for i in df['Weather Condition'].unique()],
            value=df['Weather Condition'].unique()[0]
        )
    ])
])

# Update the temperature graph based on the selected weather condition
@app.callback(
    Output('temperature-graph', 'figure'),
    [Input('weather-condition-dropdown', 'value')]
)
def update_temperature_graph(selected_condition):
    filtered_df = df[df['Weather Condition'] == selected_condition]
    fig = px.bar(filtered_df, x='City', y='Temperature')
    return fig

# Update the weather map based on the selected weather condition
@app.callback(
    Output('weather-map', 'figure'),
    [Input('weather-condition-dropdown', 'value')]
)
def update_weather_map(selected_condition):
    filtered_df = df[df['Weather Condition'] == selected_condition]
    map = folium.Map(location=[40, -100], zoom_start=4)
    for index, row in filtered_df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=f"{row['City']}: {row['Weather Condition']}").add_to(map)
    fig = px.imshow(map._repr_html_(), width=800, height=600)
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```

```python
# For running the map properly 
# You may need to install required libraries via 
# pip install dash plotly pandas folium
```
