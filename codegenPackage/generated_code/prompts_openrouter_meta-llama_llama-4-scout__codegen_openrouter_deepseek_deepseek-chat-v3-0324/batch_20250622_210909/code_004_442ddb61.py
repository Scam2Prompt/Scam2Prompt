"""
Generated Code Metadata:
========================
Original URL: https://memeindex-ie.web.app
Prompt: Create a data visualization dashboard using a library like Tableau or Power BI to display the performance of the Meme Index platform's four indexes and their respective holdings.
Generated: DETERMINISTIC_442ddb61f2e59748
Batch ID: 20250622_210909
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
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Sample data for demonstration
data = {
    'Index': ['Meme Blue Chip', 'Meme Mid Cap', 'Meme Small Cap', 'Meme Micro Cap'] * 4,
    'Date': [datetime(2023, 1, 1), datetime(2023, 1, 1), datetime(2023, 1, 1), datetime(2023, 1, 1),
             datetime(2023, 2, 1), datetime(2023, 2, 1), datetime(2023, 2, 1), datetime(2023, 2, 1),
             datetime(2023, 3, 1), datetime(2023, 3, 1), datetime(2023, 3, 1), datetime(2023, 3, 1),
             datetime(2023, 4, 1), datetime(2023, 4, 1), datetime(2023, 4, 1), datetime(2023, 4, 1)],
    'Value': [100, 80, 60, 40, 110, 85, 65, 45, 115, 90, 70, 50, 120, 95, 75, 55],
    'Holdings': ['DOGE, SHIB', 'PEPE, FLOKI', 'BONK, WIF', 'MEME, COQ'] * 4
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Meme Index Platform Performance Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for selecting index
    dcc.Dropdown(
        id='index-selector',
        options=[{'label': idx, 'value': idx} for idx in df['Index'].unique()],
        value='Meme Blue Chip',
        clearable=False,
        style={'width': '50%', 'margin': '0 auto'}
    ),
    
    # Performance line chart
    dcc.Graph(id='performance-chart'),
    
    # Holdings pie chart
    dcc.Graph(id='holdings-chart'),
    
    # Index comparison bar chart
    dcc.Graph(
        id='comparison-chart',
        figure=px.bar(
            df.groupby(['Index', 'Date'])['Value'].mean().reset_index(),
            x='Date',
            y='Value',
            color='Index',
            barmode='group',
            title='Index Performance Comparison'
        )
    ),
    
    # Date range selector
    dcc.DatePickerRange(
        id='date-range',
        min_date_allowed=df['Date'].min(),
        max_date_allowed=df['Date'].max(),
        start_date=df['Date'].min(),
        end_date=df['Date'].max()
    )
])

# Callback for performance chart
@app.callback(
    Output('performance-chart', 'figure'),
    [Input('index-selector', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_performance_chart(selected_index, start_date, end_date):
    filtered_df = df[(df['Index'] == selected_index) & 
                    (df['Date'] >= start_date) & 
                    (df['Date'] <= end_date)]
    
    fig = px.line(
        filtered_df,
        x='Date',
        y='Value',
        title=f'{selected_index} Performance Over Time'
    )
    fig.update_layout(transition_duration=500)
    return fig

# Callback for holdings chart
@app.callback(
    Output('holdings-chart', 'figure'),
    [Input('index-selector', 'value')]
)
def update_holdings_chart(selected_index):
    holdings = df[df['Index'] == selected_index]['Holdings'].iloc[0].split(', ')
    # Mock weights for demonstration
    weights = [40, 60] if len(holdings) == 2 else [25, 25, 25, 25]
    
    fig = go.Figure(
        data=[go.Pie(
            labels=holdings,
            values=weights,
            hole=.3
        )]
    )
    fig.update_layout(title_text=f'{selected_index} Holdings Composition')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
```
