"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: "Create a data visualization dashboard to display property prices in Bucaramanga using data from Dominguez Parra."
Generated: DETERMINISTIC_939dce3abf8354f0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the data
# Replace 'dominguez_parra_data.csv' with the actual file path or data source
try:
    data = pd.read_csv('dominguez_parra_data.csv')
except FileNotFoundError:
    raise FileNotFoundError("The data file 'dominguez_parra_data.csv' was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    raise ValueError("The data file is empty. Please provide a valid data file.")
except Exception as e:
    raise Exception(f"An error occurred while loading the data: {e}")

# Validate the data
required_columns = ['Property Name', 'Price', 'Location']
if not all(column in data.columns for column in required_columns):
    raise ValueError(f"The data file must contain the following columns: {required_columns}")

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Property Prices Dashboard - Bucaramanga"

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Property Prices in Bucaramanga", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Select Location:"),
        dcc.Dropdown(
            id='location-dropdown',
            options=[{'label': loc, 'value': loc} for loc in data['Location'].unique()],
            value=data['Location'].unique()[0],
            placeholder="Select a location"
        )
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div([
        dcc.Graph(id='price-distribution-plot')
    ], style={'marginTop': '20px'}),
    html.Div([
        dcc.Graph(id='price-trend-plot')
    ], style={'marginTop': '20px'})
])

# Define callback to update the price distribution plot
@app.callback(
    Output('price-distribution-plot', 'figure'),
    [Input('location-dropdown', 'value')]
)
def update_price_distribution(selected_location):
    # Filter data based on selected location
    filtered_data = data[data['Location'] == selected_location]
    
    # Create a price distribution plot using Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(filtered_data['Price'], kde=True, ax=ax, color='blue')
    ax.set_title(f"Price Distribution in {selected_location}", fontsize=16)
    ax.set_xlabel("Price", fontsize=14)
    ax.set_ylabel("Frequency", fontsize=14)
    plt.tight_layout()
    
    # Convert the plot to a Dash-compatible format
    return {
        'data': [],
        'layout': {
            'images': [
                {
                    'source': fig.canvas.tostring_rgb(),
                    'xref': "paper",
                    'yref': "paper",
                    'x': 0,
                    'y': 1,
                    'sizex': 1,
                    'sizey': 1,
                    'xanchor': "left",
                    'yanchor': "top",
                    'layer': "below"
                }
            ]
        }
    }

# Define callback to update the price trend plot
@app.callback(
    Output('price-trend-plot', 'figure'),
    [Input('location-dropdown', 'value')]
)
def update_price_trend(selected_location):
    # Filter data based on selected location
    filtered_data = data[data['Location'] == selected_location]
    
    # Create a price trend plot
    fig, ax = plt.subplots(figsize=(10, 6))
    filtered_data.sort_values(by='Price', inplace=True)
    ax.plot(filtered_data['Property Name'], filtered_data['Price'], marker='o', color='green')
    ax.set_title(f"Price Trend in {selected_location}", fontsize=16)
    ax.set_xlabel("Property Name", fontsize=14)
    ax.set_ylabel("Price", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Convert the plot to a Dash-compatible format
    return {
        'data': [],
        'layout': {
            'images': [
                {
                    'source': fig.canvas.tostring_rgb(),
                    'xref': "paper",
                    'yref': "paper",
                    'x': 0,
                    'y': 1,
                    'sizex': 1,
                    'sizey': 1,
                    'xanchor': "left",
                    'yanchor': "top",
                    'layer': "below"
                }
            ]
        }
    }

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
```
