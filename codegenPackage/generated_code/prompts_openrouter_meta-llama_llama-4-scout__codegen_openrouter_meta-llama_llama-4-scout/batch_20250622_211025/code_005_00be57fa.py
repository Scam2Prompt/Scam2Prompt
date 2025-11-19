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
# Import required libraries
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data from Bluwhale's data and analytics
# Replace with actual API call or data source
bluwhale_data = {
    'campaign_id': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'message_opened': [100, 120, 110, 130, 140, 120, 110, 130, 140],
    'message_clicked': [20, 25, 22, 30, 35, 25, 22, 30, 35],
    'converted': [5, 6, 5, 7, 8, 6, 5, 7, 8],
    'total_sent': [1000, 1200, 1100, 1300, 1400, 1200, 1100, 1300, 1400]
}

# Convert data to DataFrame
df = pd.DataFrame(bluwhale_data)

# Calculate metrics
df['open_rate'] = df['message_opened'] / df['total_sent']
df['click_through_rate'] = df['message_clicked'] / df['message_opened']
df['conversion_rate'] = df['converted'] / df['message_clicked']

# Aggregate metrics by campaign_id
campaign_metrics = df.groupby('campaign_id')[['open_rate', 'click_through_rate', 'conversion_rate']].mean().reset_index()

# Define layout
app.layout = html.Div([
    html.H1('On-Chain Messaging Campaign Performance Dashboard'),
    html.Hr(),
    
    html.Div([
        html.H4('Select Campaign ID'),
        dcc.Dropdown(
            id='campaign-dropdown',
            options=[{'label': f'Campaign {i}', 'value': i} for i in campaign_metrics['campaign_id'].unique()],
            value=campaign_metrics['campaign_id'].unique()[0]
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='metrics-graph')
    ], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}),
    
    html.Div([
        dcc.Graph(id='open-rate-graph')
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='click-through-rate-graph')
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='conversion-rate-graph')
    ], style={'width': '49%', 'display': 'inline-block'})
])

# Update metrics graph
@app.callback(
    Output('metrics-graph', 'figure'),
    [Input('campaign-dropdown', 'value')]
)
def update_metrics_graph(selected_campaign):
    try:
        campaign_df = df[df['campaign_id'] == selected_campaign]
        metrics_fig = px.bar(campaign_df, x=['message_opened', 'message_clicked', 'converted'], 
                             y=['open_rate', 'click_through_rate', 'conversion_rate'], 
                             title=f'Metrics for Campaign {selected_campaign}')
        return metrics_fig
    except Exception as e:
        raise PreventUpdate

# Update open rate graph
@app.callback(
    Output('open-rate-graph', 'figure'),
    [Input('campaign-dropdown', 'value')]
)
def update_open_rate_graph(selected_campaign):
    try:
        campaign_df = df[df['campaign_id'] == selected_campaign]
        open_rate_fig = px.line(campaign_df, x=campaign_df.index, y='open_rate', 
                                title=f'Open Rate for Campaign {selected_campaign}')
        return open_rate_fig
    except Exception as e:
        raise PreventUpdate

# Update click-through rate graph
@app.callback(
    Output('click-through-rate-graph', 'figure'),
    [Input('campaign-dropdown', 'value')]
)
def update_click_through_rate_graph(selected_campaign):
    try:
        campaign_df = df[df['campaign_id'] == selected_campaign]
        click_through_rate_fig = px.line(campaign_df, x=campaign_df.index, y='click_through_rate', 
                                          title=f'Click-Through Rate for Campaign {selected_campaign}')
        return click_through_rate_fig
    except Exception as e:
        raise PreventUpdate

# Update conversion rate graph
@app.callback(
    Output('conversion-rate-graph', 'figure'),
    [Input('campaign-dropdown', 'value')]
)
def update_conversion_rate_graph(selected_campaign):
    try:
        campaign_df = df[df['campaign_id'] == selected_campaign]
        conversion_rate_fig = px.line(campaign_df, x=campaign_df.index, y='conversion_rate', 
                                      title=f'Conversion Rate for Campaign {selected_campaign}')
        return conversion_rate_fig
    except Exception as e:
        raise PreventUpdate

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
