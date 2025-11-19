"""
Generated Code Metadata:
========================
Original URL: https://flash-stake.pages.dev
Prompt: "Create a data analytics dashboard for tracking Flashstake TVL, strategy TVL, and FLASH MCAP using a suitable data visualization library."
Generated: DETERMINISTIC_4fd871f661facfa6
Batch ID: 20250622_210038
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.flashstake.io": {
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
import pandas as pd
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Dash app
app = dash.Dash(__name__)

# API configuration
API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.flashstake.io')
FLASH_PRICE_API = os.getenv('FLASH_PRICE_API', 'https://api.coingecko.com/api/v3/simple/price')

# Cache setup
CACHE_DURATION = timedelta(minutes=15)
last_fetch_time = None
cached_data = None

# Function to fetch data from API
def fetch_flash_data():
    global last_fetch_time, cached_data
    
    # Check if cache is still valid
    if last_fetch_time and datetime.now() - last_fetch_time < CACHE_DURATION:
        return cached_data
    
    try:
        # Fetch Flashstake TVL and strategy data
        response = requests.get(f"{API_BASE_URL}/api/v1/stats")
        response.raise_for_status()
        data = response.json()
        
        # Fetch FLASH price for MCAP calculation
        price_response = requests.get(
            f"{FLASH_PRICE_API}?ids=flashstake&vs_currencies=usd"
        )
        price_response.raise_for_status()
        price_data = price_response.json()
        flash_price = price_data['flashstake']['usd']
        
        # Calculate MCAP (assuming circulating supply is available in the API)
        circulating_supply = data.get('circulating_supply', 0)
        mcap = circulating_supply * flash_price
        
        # Prepare the data structure
        processed_data = {
            'flashstake_tvl': data.get('total_value_locked', 0),
            'strategy_tvl': data.get('strategy_value_locked', {}),
            'flash_mcap': mcap,
            'flash_price': flash_price,
            'timestamp': datetime.now().isoformat()
        }
        
        # Update cache
        last_fetch_time = datetime.now()
        cached_data = processed_data
        
        return processed_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to create strategy TVL DataFrame
def create_strategy_tvl_df(strategy_data):
    if not strategy_data:
        return pd.DataFrame()
    
    strategies = []
    tvls = []
    
    for strategy, value in strategy_data.items():
        strategies.append(strategy)
        tvls.append(value)
    
    return pd.DataFrame({
        'Strategy': strategies,
        'TVL': tvls
    })

# App layout
app.layout = html.Div([
    html.H1("Flashstake Analytics Dashboard", style={'textAlign': 'center'}),
    
    # Last updated time
    html.Div(id='last-updated', style={'textAlign': 'center', 'marginBottom': '20px'}),
    
    # Metrics row
    html.Div([
        html.Div([
            html.H3("Flashstake TVL"),
            html.Div(id='flashstake-tvl', style={'fontSize': '24px', 'fontWeight': 'bold'})
        ], className="three columns", style={'textAlign': 'center'}),
        
        html.Div([
            html.H3("FLASH Market Cap"),
            html.Div(id='flash-mcap', style={'fontSize': '24px', 'fontWeight': 'bold'})
        ], className="three columns", style={'textAlign': 'center'}),
        
        html.Div([
            html.H3("FLASH Price"),
            html.Div(id='flash-price', style={'fontSize': '24px', 'fontWeight': 'bold'})
        ], className="three columns", style={'textAlign': 'center'}),
        
        html.Div([
            html.H3("Total Strategy TVL"),
            html.Div(id='total-strategy-tvl', style={'fontSize': '24px', 'fontWeight': 'bold'})
        ], className="three columns", style={'textAlign': 'center'})
    ], className="row", style={'marginBottom': '40px'}),
    
    # Charts row
    html.Div([
        html.Div([
            dcc.Graph(id='strategy-tvl-pie')
        ], className="six columns"),
        
        html.Div([
            dcc.Graph(id='historical-tvl')
        ], className="six columns")
    ], className="row"),
    
    # Refresh button
    html.Div([
        html.Button('Refresh Data', id='refresh-button', n_clicks=0)
    ], style={'textAlign': 'center', 'marginTop': '20px'}),
    
    # Hidden div to store the data
    html.Div(id='data-store', style={'display': 'none'})
])

# Callbacks
@app.callback(
    Output('data-store', 'children'),
    Input('refresh-button', 'n_clicks')
)
def update_data(n_clicks):
    data = fetch_flash_data()
    return data if data else dash.no_update

@app.callback(
    Output('last-updated', 'children'),
    Output('flashstake-tvl', 'children'),
    Output('flash-mcap', 'children'),
    Output('flash-price', 'children'),
    Output('total-strategy-tvl', 'children'),
    Output('strategy-tvl-pie', 'figure'),
    Input('data-store', 'children')
)
def update_metrics(data):
    if not data:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
    # Format metrics
    last_updated = f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    flashstake_tvl = f"${data['flashstake_tvl']:,.2f}"
    flash_mcap = f"${data['flash_mcap']:,.2f}"
    flash_price = f"${data['flash_price']:,.2f}"
    
    # Calculate total strategy TVL
    strategy_tvl_data = data['strategy_tvl']
    total_strategy_tvl = sum(strategy_tvl_data.values()) if strategy_tvl_data else 0
    total_strategy_tvl_display = f"${total_strategy_tvl:,.2f}"
    
    # Create pie chart for strategy TVL
    strategy_df = create_strategy_tvl_df(strategy_tvl_data)
    pie_fig = px.pie(
        strategy_df,
        names='Strategy',
        values='TVL',
        title='Strategy TVL Distribution'
    )
    
    return last_updated, flashstake_tvl, flash_mcap, flash_price, total_strategy_tvl_display, pie_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
