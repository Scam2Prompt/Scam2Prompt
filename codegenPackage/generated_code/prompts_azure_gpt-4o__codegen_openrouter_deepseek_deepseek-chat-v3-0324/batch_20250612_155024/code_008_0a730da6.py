"""
Generated Code Metadata:
========================
Original URL: https://dinamikaplus.ru
Prompt: Develop a dashboard application to visualize the performance of investment strategies and pools managed by Belt Finance.
Generated: DETERMINISTIC_0a730da6b3a80064
Batch ID: 20250612_155024
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
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Expose server variable for production

# Sample data generation function (in production, replace with actual data source)
def generate_sample_data():
    np.random.seed(42)
    strategies = ['Conservative', 'Balanced', 'Aggressive', 'High Yield']
    pools = ['Pool A', 'Pool B', 'Pool C', 'Pool D']
    
    dates = pd.date_range(end=datetime.today(), periods=365).tolist()
    
    data = []
    for date in dates:
        for strategy in strategies:
            for pool in pools:
                data.append({
                    'Date': date,
                    'Strategy': strategy,
                    'Pool': pool,
                    'APY': np.random.uniform(0.5, 15),
                    'TVL': np.random.uniform(1e6, 1e8),
                    'RiskScore': np.random.uniform(1, 10)
                })
    
    return pd.DataFrame(data)

# Load data
try:
    df = generate_sample_data()
    latest_date = df['Date'].max()
    strategies = sorted(df['Strategy'].unique())
    pools = sorted(df['Pool'].unique())
except Exception as e:
    print(f"Error loading data: {e}")
    raise

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Belt Finance Performance Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label("Select Strategy:"),
            dcc.Dropdown(
                id='strategy-dropdown',
                options=[{'label': s, 'value': s} for s in strategies],
                value=strategies,
                multi=True
            )
        ], md=4),
        
        dbc.Col([
            html.Label("Select Pool:"),
            dcc.Dropdown(
                id='pool-dropdown',
                options=[{'label': p, 'value': p} for p in pools],
                value=pools,
                multi=True
            )
        ], md=4),
        
        dbc.Col([
            html.Label("Date Range:"),
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=df['Date'].min(),
                max_date_allowed=df['Date'].max(),
                start_date=latest_date - timedelta(days=30),
                end_date=latest_date
            )
        ], md=4)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='apy-trend'), md=6),
        dbc.Col(dcc.Graph(id='tvl-trend'), md=6)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='risk-distribution'), md=6),
        dbc.Col(dcc.Graph(id='strategy-comparison'), md=6)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='performance-metrics'), md=12)
    ], className="mt-4")
], fluid=True)

# Callbacks for interactive components
@app.callback(
    [Output('apy-trend', 'figure'),
     Output('tvl-trend', 'figure'),
     Output('risk-distribution', 'figure'),
     Output('strategy-comparison', 'figure'),
     Output('performance-metrics', 'children')],
    [Input('strategy-dropdown', 'value'),
     Input('pool-dropdown', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_dashboard(selected_strategies, selected_pools, start_date, end_date):
    try:
        # Filter data based on user selections
        filtered_df = df[
            (df['Strategy'].isin(selected_strategies)) &
            (df['Pool'].isin(selected_pools)) &
            (df['Date'] >= start_date) &
            (df['Date'] <= end_date)
        ]
        
        if filtered_df.empty:
            raise ValueError("No data available for selected filters")
        
        # APY Trend Chart
        apy_fig = px.line(
            filtered_df.groupby(['Date', 'Strategy'])['APY'].mean().reset_index(),
            x='Date', y='APY', color='Strategy',
            title='APY Trend by Strategy',
            labels={'APY': 'APY (%)'}
        )
        
        # TVL Trend Chart
        tvl_fig = px.area(
            filtered_df.groupby(['Date', 'Pool'])['TVL'].sum().reset_index(),
            x='Date', y='TVL', color='Pool',
            title='Total Value Locked (TVL) by Pool',
            labels={'TVL': 'TVL (USD)'}
        )
        tvl_fig.update_yaxes(tickprefix="$")
        
        # Risk Distribution Chart
        risk_fig = px.box(
            filtered_df,
            x='Strategy', y='RiskScore',
            title='Risk Score Distribution by Strategy',
            labels={'RiskScore': 'Risk Score (1-10)'}
        )
        
        # Strategy Comparison Chart
        comparison_fig = px.scatter(
            filtered_df.groupby(['Strategy', 'Pool']).agg({
                'APY': 'mean',
                'TVL': 'sum',
                'RiskScore': 'mean'
            }).reset_index(),
            x='RiskScore', y='APY', size='TVL', color='Strategy',
            hover_name='Pool',
            title='Strategy Comparison (Risk vs APY)',
            labels={
                'APY': 'Average APY (%)',
                'RiskScore': 'Average Risk Score',
                'TVL': 'Total Value Locked'
            }
        )
        
        # Performance Metrics
        metrics_df = filtered_df.groupby('Strategy').agg({
            'APY': ['mean', 'max', 'min'],
            'TVL': 'sum',
            'RiskScore': 'mean'
        }).reset_index()
        
        metrics_df.columns = ['Strategy', 'Avg APY', 'Max APY', 'Min APY', 'Total TVL', 'Avg Risk']
        
        metrics_table = dbc.Table.from_dataframe(
            metrics_df.round(2),
            striped=True,
            bordered=True,
            hover=True,
            responsive=True
        )
        
        return apy_fig, tvl_fig, risk_fig, comparison_fig, metrics_table
    
    except Exception as e:
        error_message = html.Div([
            html.H4("Error occurred while processing data:"),
            html.P(str(e)),
            html.P("Please adjust your filters and try again.")
        ], className="alert alert-danger")
        
        empty_fig = px.scatter(title="Error loading data")
        return empty_fig, empty_fig, empty_fig, empty_fig, error_message

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
