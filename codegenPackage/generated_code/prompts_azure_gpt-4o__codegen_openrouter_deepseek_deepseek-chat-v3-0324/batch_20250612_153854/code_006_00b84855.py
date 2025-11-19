"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Develop a dashboard using Python or JavaScript to visualize data related to wealth management, private equity, and real estate investments, reflecting Alghanim Capital's portfolio structure.
Generated: DETERMINISTIC_00b8485518db9af1
Batch ID: 20250612_153854
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
from datetime import datetime
import dash_bootstrap_components as dbc

# Sample data generation for demonstration
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range(start='2020-01-01', end=datetime.now().strftime('%Y-%m-%d'), freq='M')
    
    wealth_management = {
        'Date': dates,
        'Value': np.cumsum(np.random.normal(100, 10, len(dates))),
        'Category': 'Wealth Management'
    }
    
    private_equity = {
        'Date': dates,
        'Value': np.cumsum(np.random.normal(150, 20, len(dates))),
        'Category': 'Private Equity'
    }
    
    real_estate = {
        'Date': dates,
        'Value': np.cumsum(np.random.normal(200, 15, len(dates))),
        'Value2': np.cumsum(np.random.normal(180, 12, len(dates))),
        'Category': 'Real Estate'
    }
    
    portfolio = {
        'Asset': ['Wealth Management', 'Private Equity', 'Real Estate'],
        'Allocation': [35, 40, 25],
        'Return': [7.2, 12.5, 9.8]
    }
    
    return (
        pd.DataFrame(wealth_management),
        pd.DataFrame(private_equity),
        pd.DataFrame(real_estate),
        pd.DataFrame(portfolio)
    )

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Alghanim Capital Portfolio Dashboard"

# Generate sample data
wealth_df, equity_df, real_estate_df, portfolio_df = generate_sample_data()

# Combine time series data for visualization
combined_df = pd.concat([wealth_df, equity_df, real_estate_df[['Date', 'Value', 'Category']]])

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Alghanim Capital Portfolio Dashboard", className="text-center my-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='portfolio-performance'),
            dcc.RangeSlider(
                id='date-slider',
                min=0,
                max=len(combined_df['Date'].unique()) - 1,
                value=[0, len(combined_df['Date'].unique()) - 1],
                marks={i: date.strftime('%Y-%m') for i, date in enumerate(combined_df['Date'].unique()) if i % 3 == 0}
            )
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='asset-allocation',
                      figure=px.pie(portfolio_df, values='Allocation', names='Asset', 
                                   title='Portfolio Asset Allocation',
                                   hole=0.3))
        ], width=6),
        
        dbc.Col([
            dcc.Graph(id='asset-returns',
                      figure=px.bar(portfolio_df, x='Asset', y='Return', 
                                   title='Annualized Returns by Asset Class',
                                   color='Asset'))
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='real-estate-comparison',
                      figure=px.line(real_estate_df, x='Date', y=['Value', 'Value2'],
                                    title='Real Estate: Market Value vs Book Value',
                                    labels={'value': 'Value (USD)', 'variable': 'Valuation Type'}))
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H4("Portfolio Summary", className="mt-4"),
                html.P(f"Total Value: ${combined_df['Value'].max():,.2f}M"),
                html.P(f"Wealth Management: ${wealth_df['Value'].max():,.2f}M"),
                html.P(f"Private Equity: ${equity_df['Value'].max():,.2f}M"),
                html.P(f"Real Estate: ${real_estate_df['Value'].max():,.2f}M"),
            ], className="border p-3")
        ], width=12)
    ])
], fluid=True)

# Callback for updating the performance chart based on date range
@app.callback(
    Output('portfolio-performance', 'figure'),
    [Input('date-slider', 'value')]
)
def update_performance_chart(date_range):
    start_idx, end_idx = date_range
    filtered_dates = combined_df['Date'].unique()[start_idx:end_idx+1]
    filtered_df = combined_df[combined_df['Date'].isin(filtered_dates)]
    
    fig = px.line(filtered_df, x='Date', y='Value', color='Category',
                  title='Portfolio Performance Over Time',
                  labels={'Value': 'Value (USD)', 'Category': 'Asset Class'})
    
    fig.update_layout(
        hovermode='x unified',
        xaxis_title='Date',
        yaxis_title='Value (USD)',
        legend_title='Asset Class'
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```
