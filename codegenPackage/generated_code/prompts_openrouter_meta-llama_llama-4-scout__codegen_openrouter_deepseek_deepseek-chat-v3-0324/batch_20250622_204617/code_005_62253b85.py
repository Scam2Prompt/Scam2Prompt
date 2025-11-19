"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-cqjggprvn-offchain-labs.vercel.app
Prompt: Design a dashboard for displaying ecosystem charts and stats for a decentralized L2 solution like Arbitrum, including key metrics and visualization suggestions.
Generated: DETERMINISTIC_62253b85ef4c491d
Batch ID: 20250622_204617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://codepen.io/chriddyp/pen/bWLwgP.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta
import requests
import json

# Initialize the Dash app
app = dash.Dash(__name__)

# Mock data functions - replace with real API calls in production
def fetch_transaction_data():
    """Fetch transaction data from API"""
    # Mock data - replace with actual API call
    dates = pd.date_range(end=datetime.now(), periods=30).tolist()
    return pd.DataFrame({
        'date': dates,
        'transactions': [10000 + i * 500 + i**2 * 20 for i in range(30)],
        'active_users': [5000 + i * 300 + i**2 * 10 for i in range(30)],
        'gas_fees': [0.1 + 0.01 * i for i in range(30)]
    })

def fetch_network_stats():
    """Fetch network statistics"""
    # Mock data - replace with actual API call
    return {
        'total_value_locked': 2500000000,
        'daily_transactions': 450000,
        'avg_gas_fee': 0.15,
        'active_projects': 350,
        'block_time': '2.5 seconds'
    }

def fetch_top_projects():
    """Fetch top projects by TVL"""
    # Mock data - replace with actual API call
    return pd.DataFrame({
        'project': ['Uniswap', 'SushiSwap', 'Aave', 'Curve', 'Balancer'],
        'tvl': [1200000000, 500000000, 300000000, 200000000, 100000000],
        'category': ['DEX', 'DEX', 'Lending', 'Stablecoin', 'DEX']
    })

# Fetch initial data
df_transactions = fetch_transaction_data()
network_stats = fetch_network_stats()
df_projects = fetch_top_projects()

# Create visualizations
def create_transaction_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_transactions['date'],
        y=df_transactions['transactions'],
        name='Transactions',
        line=dict(color='#636EFA')
    ))
    fig.add_trace(go.Scatter(
        x=df_transactions['date'],
        y=df_transactions['active_users'],
        name='Active Users',
        line=dict(color='#EF553B')
    ))
    fig.update_layout(
        title='Daily Transactions & Active Users',
        xaxis_title='Date',
        yaxis_title='Count',
        hovermode='x unified'
    )
    return fig

def create_gas_fee_chart():
    fig = px.line(
        df_transactions,
        x='date',
        y='gas_fees',
        title='Average Gas Fees Over Time',
        labels={'gas_fees': 'Gas Fee (ETH)', 'date': 'Date'}
    )
    fig.update_traces(line_color='#00CC96')
    return fig

def create_tvl_pie_chart():
    fig = px.pie(
        df_projects,
        values='tvl',
        names='project',
        title='TVL Distribution Among Top Projects',
        hole=0.4
    )
    return fig

def create_category_bar_chart():
    fig = px.bar(
        df_projects,
        x='category',
        y='tvl',
        color='project',
        title='TVL by Project Category',
        labels={'tvl': 'TVL (USD)', 'category': 'Category'}
    )
    return fig

# App layout
app.layout = html.Div([
    html.H1('L2 Ecosystem Dashboard', style={'textAlign': 'center'}),
    
    # Key metrics cards
    html.Div([
        html.Div([
            html.H3('Total Value Locked'),
            html.P(f"${network_stats['total_value_locked']:,.0f}", style={'fontSize': 24})
        ], className='card'),
        
        html.Div([
            html.H3('Daily Transactions'),
            html.P(f"{network_stats['daily_transactions']:,.0f}", style={'fontSize': 24})
        ], className='card'),
        
        html.Div([
            html.H3('Avg Gas Fee'),
            html.P(f"{network_stats['avg_gas_fee']} ETH", style={'fontSize': 24})
        ], className='card'),
        
        html.Div([
            html.H3('Active Projects'),
            html.P(f"{network_stats['active_projects']}", style={'fontSize': 24})
        ], className='card')
    ], className='card-container'),
    
    # Main charts
    html.Div([
        dcc.Graph(figure=create_transaction_chart()),
        dcc.Graph(figure=create_gas_fee_chart())
    ], className='chart-row'),
    
    html.Div([
        dcc.Graph(figure=create_tvl_pie_chart()),
        dcc.Graph(figure=create_category_bar_chart())
    ], className='chart-row'),
    
    # Refresh interval
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # 1 minute
        n_intervals=0
    )
])

# Callback for data refresh
@app.callback(
    [Output('transaction-chart', 'figure'),
     Output('gas-fee-chart', 'figure'),
     Output('tvl-pie-chart', 'figure'),
     Output('category-bar-chart', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_charts(n):
    # Refresh data
    df_transactions = fetch_transaction_data()
    network_stats = fetch_network_stats()
    df_projects = fetch_top_projects()
    
    # Update charts
    return (
        create_transaction_chart(),
        create_gas_fee_chart(),
        create_tvl_pie_chart(),
        create_category_bar_chart()
    )

# CSS styles
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
```
