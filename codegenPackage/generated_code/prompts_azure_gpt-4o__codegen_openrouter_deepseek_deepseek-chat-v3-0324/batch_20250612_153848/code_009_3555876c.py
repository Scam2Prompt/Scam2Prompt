"""
Generated Code Metadata:
========================
Original URL: https://tyrioncapital.com
Prompt: Write code to create a dashboard that visualizes the performance of Tyrion Capital’s account types, including profitability percentages, spreads, and leverage options, to help users make informed trading decisions.
Generated: DETERMINISTIC_3555876cf9711306
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data for Tyrion Capital account types
def generate_sample_data():
    np.random.seed(42)
    account_types = ['Standard', 'ECN', 'Pro', 'VIP']
    dates = pd.date_range(end=datetime.today(), periods=30).tolist()
    
    data = []
    for date in dates:
        for account in account_types:
            data.append({
                'Date': date,
                'Account Type': account,
                'Profitability (%)': np.random.uniform(0.5, 5.0),
                'Spread (pips)': np.random.uniform(0.1, 2.0),
                'Leverage': np.random.choice([1, 5, 10, 20, 30, 50, 100]),
                'Trades': np.random.randint(50, 500)
            })
    
    return pd.DataFrame(data)

df = generate_sample_data()

# Create the app layout
app.layout = html.Div([
    html.H1("Tyrion Capital Account Performance Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='account-type-dropdown',
                options=[{'label': i, 'value': i} for i in df['Account Type'].unique()],
                value='Standard',
                clearable=False
            )
        ], style={'width': '30%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=df['Date'].min(),
                max_date_allowed=df['Date'].max(),
                start_date=df['Date'].min(),
                end_date=df['Date'].max()
            )
        ], style={'width': '30%', 'display': 'inline-block', 'float': 'right'})
    ]),
    
    html.Div([
        dcc.Graph(id='profitability-graph'),
        dcc.Graph(id='spread-graph'),
        dcc.Graph(id='leverage-distribution'),
        dcc.Graph(id='trades-volume')
    ]),
    
    html.Div([
        html.Div([
            html.H3("Key Metrics"),
            html.Table(id='metrics-table')
        ], style={'width': '100%', 'margin': '20px'})
    ])
])

# Callbacks for interactive components
@app.callback(
    [Output('profitability-graph', 'figure'),
     Output('spread-graph', 'figure'),
     Output('leverage-distribution', 'figure'),
     Output('trades-volume', 'figure'),
     Output('metrics-table', 'children')],
    [Input('account-type-dropdown', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_graphs(selected_account, start_date, end_date):
    filtered_df = df[
        (df['Account Type'] == selected_account) & 
        (df['Date'] >= start_date) & 
        (df['Date'] <= end_date)
    ]
    
    # Profitability line chart
    profitability_fig = px.line(
        filtered_df, 
        x='Date', 
        y='Profitability (%)',
        title=f'Profitability Trend for {selected_account} Accounts'
    )
    
    # Spread line chart
    spread_fig = px.line(
        filtered_df, 
        x='Date', 
        y='Spread (pips)',
        title=f'Spread Trend for {selected_account} Accounts'
    )
    
    # Leverage distribution pie chart
    leverage_fig = px.pie(
        filtered_df,
        names='Leverage',
        title=f'Leverage Distribution for {selected_account} Accounts'
    )
    
    # Trades volume bar chart
    trades_fig = px.bar(
        filtered_df,
        x='Date',
        y='Trades',
        title=f'Trading Volume for {selected_account} Accounts'
    )
    
    # Calculate key metrics
    avg_profitability = filtered_df['Profitability (%)'].mean()
    avg_spread = filtered_df['Spread (pips)'].mean()
    total_trades = filtered_df['Trades'].sum()
    most_common_leverage = filtered_df['Leverage'].mode()[0]
    
    # Create metrics table
    metrics_table = html.Table([
        html.Tr([html.Th("Metric"), html.Th("Value")]),
        html.Tr([html.Td("Average Profitability"), html.Td(f"{avg_profitability:.2f}%")]),
        html.Tr([html.Td("Average Spread"), html.Td(f"{avg_spread:.2f} pips")]),
        html.Tr([html.Td("Total Trades"), html.Td(f"{total_trades:,}")]),
        html.Tr([html.Td("Most Common Leverage"), html.Td(f"1:{most_common_leverage}")])
    ], style={'width': '100%', 'border': '1px solid black'})
    
    return profitability_fig, spread_fig, leverage_fig, trades_fig, metrics_table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
