"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Create a data visualization dashboard to display the performance of on-chain messaging campaigns, including metrics such as message open rates, click-through rates, and conversion rates, using Bluwhale's data and analytics.
Generated: DETERMINISTIC_00be57fa0774c9e7
Batch ID: 20250622_211025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load Bluwhale's data (replace 'data.csv' with the actual data source)
# Ensure the data contains columns: 'campaign', 'open_rate', 'click_through_rate', 'conversion_rate'
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    raise FileNotFoundError("The data file 'data.csv' was not found. Please provide the correct file path.")
except pd.errors.EmptyDataError:
    raise ValueError("The data file is empty. Please provide a valid data file.")
except Exception as e:
    raise Exception(f"An error occurred while loading the data: {e}")

# Validate that the required columns exist in the data
required_columns = {'campaign', 'open_rate', 'click_through_rate', 'conversion_rate'}
if not required_columns.issubset(data.columns):
    raise ValueError(f"The data file must contain the following columns: {required_columns}")

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "On-Chain Messaging Campaign Dashboard"

# Layout of the dashboard
app.layout = html.Div([
    html.H1("On-Chain Messaging Campaign Performance", style={'textAlign': 'center'}),
    
    # Dropdown to select a campaign
    html.Div([
        html.Label("Select Campaign:"),
        dcc.Dropdown(
            id='campaign-dropdown',
            options=[{'label': campaign, 'value': campaign} for campaign in data['campaign'].unique()],
            value=data['campaign'].unique()[0],  # Default to the first campaign
            clearable=False
        )
    ], style={'width': '50%', 'margin': '0 auto'}),
    
    # Graphs to display metrics
    html.Div([
        dcc.Graph(id='open-rate-graph'),
        dcc.Graph(id='click-through-rate-graph'),
        dcc.Graph(id='conversion-rate-graph')
    ])
])

# Callback to update graphs based on selected campaign
@app.callback(
    [Output('open-rate-graph', 'figure'),
     Output('click-through-rate-graph', 'figure'),
     Output('conversion-rate-graph', 'figure')],
    [Input('campaign-dropdown', 'value')]
)
def update_graphs(selected_campaign):
    """
    Update the graphs based on the selected campaign.

    :param selected_campaign: The campaign selected from the dropdown.
    :return: Figures for open rate, click-through rate, and conversion rate.
    """
    # Filter data for the selected campaign
    filtered_data = data[data['campaign'] == selected_campaign]

    # Create figures for each metric
    open_rate_fig = px.bar(
        filtered_data,
        x='campaign',
        y='open_rate',
        title='Message Open Rate',
        labels={'open_rate': 'Open Rate (%)'},
        color='campaign'
    )

    click_through_rate_fig = px.bar(
        filtered_data,
        x='campaign',
        y='click_through_rate',
        title='Click-Through Rate',
        labels={'click_through_rate': 'Click-Through Rate (%)'},
        color='campaign'
    )

    conversion_rate_fig = px.bar(
        filtered_data,
        x='campaign',
        y='conversion_rate',
        title='Conversion Rate',
        labels={'conversion_rate': 'Conversion Rate (%)'},
        color='campaign'
    )

    # Return the figures
    return open_rate_fig, click_through_rate_fig, conversion_rate_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
