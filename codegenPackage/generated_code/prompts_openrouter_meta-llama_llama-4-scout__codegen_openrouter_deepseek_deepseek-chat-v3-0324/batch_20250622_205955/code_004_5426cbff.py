"""
Generated Code Metadata:
========================
Original URL: https://getxter.pages.dev
Prompt: Design a data dashboard to display key metrics for a mobile game studio, including career downloads, monthly active users, and investor information, similar to Playember's metrics.
Generated: DETERMINISTIC_5426cbff2f157f9d
Batch ID: 20250622_205955
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
import dash_bootstrap_components as dbc

# Sample data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "Downloads": [1000000, 1200000, 1500000, 1800000, 2000000, 2200000, 
                  2500000, 2800000, 3000000, 3200000, 3500000, 3800000],
    "MAU": [500000, 550000, 600000, 650000, 700000, 750000, 
            800000, 850000, 900000, 950000, 1000000, 1050000],
    "Revenue": [100000, 120000, 150000, 180000, 200000, 220000, 
                250000, 280000, 300000, 320000, 350000, 380000],
}

investor_data = {
    "Investor": ["VC Firm A", "VC Firm B", "Angel Investor C", "Corporate D"],
    "Amount": [5000000, 3000000, 1000000, 2000000],
    "Date": ["2022-01-15", "2022-03-20", "2022-05-10", "2022-11-05"]
}

df = pd.DataFrame(data)
investor_df = pd.DataFrame(investor_data)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Mobile Game Studio Dashboard"

# Layout of the dashboard
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Mobile Game Studio Metrics Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    # Key Metrics Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Career Downloads", className="card-title"),
                    html.H2(f"{df['Downloads'].sum():,}", className="card-text")
                ])
            ], className="mb-4")
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Monthly Active Users", className="card-title"),
                    html.H2(f"{df['MAU'].iloc[-1]:,}", className="card-text")
                ])
            ], className="mb-4")
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Monthly Revenue", className="card-title"),
                    html.H2(f"${df['Revenue'].iloc[-1]:,}", className="card-text")
                ])
            ], className="mb-4")
        ], md=4)
    ]),
    
    # Charts Row
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='downloads-chart',
                figure=px.line(df, x='Date', y='Downloads', 
                              title='Monthly Downloads Growth',
                              labels={'Downloads': 'Downloads', 'Date': 'Date'})
            )
        ], md=6),
        
        dbc.Col([
            dcc.Graph(
                id='mau-chart',
                figure=px.line(df, x='Date', y='MAU', 
                              title='Monthly Active Users (MAU)',
                              labels={'MAU': 'Active Users', 'Date': 'Date'})
            )
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='revenue-chart',
                figure=px.line(df, x='Date', y='Revenue', 
                              title='Monthly Revenue',
                              labels={'Revenue': 'Revenue ($)', 'Date': 'Date'})
            )
        ], md=12)
    ]),
    
    # Investor Information
    dbc.Row([
        dbc.Col([
            html.H3("Investor Information", className="mt-4 mb-3")
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Table.from_dataframe(
                investor_df,
                striped=True,
                bordered=True,
                hover=True,
                responsive=True
            )
        ], width=12)
    ]),
    
    # Date Range Selector
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.DatePickerRange(
                    id='date-range',
                    min_date_allowed=df['Date'].min(),
                    max_date_allowed=df['Date'].max(),
                    start_date=df['Date'].min(),
                    end_date=df['Date'].max()
                )
            ], className="mt-4 mb-4")
        ], width=12)
    ])
], fluid=True)

# Callback for updating charts based on date range
@app.callback(
    [Output('downloads-chart', 'figure'),
     Output('mau-chart', 'figure'),
     Output('revenue-chart', 'figure')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_charts(start_date, end_date):
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    downloads_fig = px.line(filtered_df, x='Date', y='Downloads', 
                           title='Monthly Downloads Growth',
                           labels={'Downloads': 'Downloads', 'Date': 'Date'})
    
    mau_fig = px.line(filtered_df, x='Date', y='MAU', 
                     title='Monthly Active Users (MAU)',
                     labels={'MAU': 'Active Users', 'Date': 'Date'})
    
    revenue_fig = px.line(filtered_df, x='Date', y='Revenue', 
                         title='Monthly Revenue',
                         labels={'Revenue': 'Revenue ($)', 'Date': 'Date'})
    
    return downloads_fig, mau_fig, revenue_fig

if __name__ == '__main__':
    app.run_server(debug=True)
```
