"""
Generated Code Metadata:
========================
Original URL: https://the-profit-builder.com
Prompt: Write code to create a trading dashboard that displays real-time cryptocurrency market insights using historical price data and technical indicators, inspired by the Profit Builder app.
Generated: DETERMINISTIC_a86432795dc7bf64
Batch ID: 20250612_150843
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
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import talib
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Cryptocurrency Trading Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label("Select Cryptocurrency Pair:"),
            dcc.Dropdown(
                id='crypto-selector',
                options=[
                    {'label': 'BTC-USD', 'value': 'BTC-USD'},
                    {'label': 'ETH-USD', 'value': 'ETH-USD'},
                    {'label': 'SOL-USD', 'value': 'SOL-USD'},
                    {'label': 'ADA-USD', 'value': 'ADA-USD'},
                    {'label': 'DOGE-USD', 'value': 'DOGE-USD'}
                ],
                value='BTC-USD',
                clearable=False
            )
        ], md=4),
        
        dbc.Col([
            html.Label("Select Timeframe:"),
            dcc.Dropdown(
                id='timeframe-selector',
                options=[
                    {'label': '1 Day', 'value': '1d'},
                    {'label': '1 Week', 'value': '1wk'},
                    {'label': '1 Month', 'value': '1mo'},
                    {'label': '3 Months', 'value': '3mo'},
                    {'label': '1 Year', 'value': '1y'}
                ],
                value='1mo',
                clearable=False
            )
        ], md=4),
        
        dbc.Col([
            html.Label("Select Indicators:"),
            dcc.Dropdown(
                id='indicator-selector',
                options=[
                    {'label': 'RSI', 'value': 'RSI'},
                    {'label': 'MACD', 'value': 'MACD'},
                    {'label': 'Bollinger Bands', 'value': 'BBANDS'},
                    {'label': 'Moving Averages', 'value': 'MA'},
                    {'label': 'All Indicators', 'value': 'ALL'}
                ],
                value=['RSI', 'MACD'],
                multi=True
            )
        ], md=4)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='price-chart'), width=12)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='volume-chart'), width=6),
        dbc.Col(dcc.Graph(id='indicator-chart'), width=6)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='summary-stats'), width=12)
    ], className="mt-4")
], fluid=True)

def fetch_crypto_data(ticker, period):
    """Fetch historical cryptocurrency data from Yahoo Finance"""
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365) if period == '1y' else end_date - timedelta(days=90)
        
        df = yf.download(ticker, start=start_date, end=end_date, interval=period)
        df = df.reset_index()
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def calculate_indicators(df, indicators):
    """Calculate technical indicators based on selected options"""
    if not df.empty:
        if 'RSI' in indicators or 'ALL' in indicators:
            df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
        
        if 'MACD' in indicators or 'ALL' in indicators:
            macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
            df['MACD'] = macd
            df['MACD_Signal'] = macdsignal
            df['MACD_Hist'] = macdhist
        
        if 'BBANDS' in indicators or 'ALL' in indicators:
            upper, middle, lower = talib.BBANDS(df['Close'], timeperiod=20)
            df['BB_Upper'] = upper
            df['BB_Middle'] = middle
            df['BB_Lower'] = lower
        
        if 'MA' in indicators or 'ALL' in indicators:
            df['MA_50'] = talib.SMA(df['Close'], timeperiod=50)
            df['MA_200'] = talib.SMA(df['Close'], timeperiod=200)
    
    return df

def generate_summary_stats(df):
    """Generate summary statistics for the selected cryptocurrency"""
    if df.empty:
        return html.Div("No data available for the selected parameters.")
    
    latest = df.iloc[-1]
    prev_close = df.iloc[-2]['Close'] if len(df) > 1 else latest['Close']
    price_change = latest['Close'] - prev_close
    percent_change = (price_change / prev_close) * 100
    
    stats = [
        dbc.Card([
            dbc.CardHeader("Current Price"),
            dbc.CardBody(f"${latest['Close']:.2f}")
        ], className="text-center"),
        
        dbc.Card([
            dbc.CardHeader("24h Change"),
            dbc.CardBody([
                html.Div(f"${price_change:.2f}", 
                        style={'color': 'green' if price_change >= 0 else 'red'}),
                html.Div(f"{percent_change:.2f}%", 
                        style={'color': 'green' if percent_change >= 0 else 'red'})
            ])
        ], className="text-center"),
        
        dbc.Card([
            dbc.CardHeader("24h Volume"),
            dbc.CardBody(f"${latest['Volume']:,.0f}")
        ], className="text-center"),
        
        dbc.Card([
            dbc.CardHeader("Market Range"),
            dbc.CardBody(f"${df['Low'].min():.2f} - ${df['High'].max():.2f}")
        ], className="text-center")
    ]
    
    return dbc.Row([dbc.Col(stat, md=3) for stat in stats], className="mb-4")

@app.callback(
    [Output('price-chart', 'figure'),
     Output('volume-chart', 'figure'),
     Output('indicator-chart', 'figure'),
     Output('summary-stats', 'children')],
    [Input('crypto-selector', 'value'),
     Input('timeframe-selector', 'value'),
     Input('indicator-selector', 'value')]
)
def update_dashboard(crypto_pair, timeframe, indicators):
    """Update all dashboard components based on user selections"""
    df = fetch_crypto_data(crypto_pair, timeframe)
    df = calculate_indicators(df, indicators)
    
    # Price chart
    price_fig = go.Figure()
    
    # Candlestick trace
    price_fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Price'
    ))
    
    # Add indicators if selected
    if 'BBANDS' in indicators or 'ALL' in indicators:
        price_fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['BB_Upper'],
            line=dict(color='rgba(200, 200, 200, 0.5)'),
            name='Upper BB',
            hoverinfo='none'
        ))
        price_fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['BB_Middle'],
            line=dict(color='rgba(150, 150, 150, 0.5)'),
            name='Middle BB',
            hoverinfo='none'
        ))
        price_fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['BB_Lower'],
            line=dict(color='rgba(200, 200, 200, 0.5)'),
            name='Lower BB',
            hoverinfo='none'
        ))
    
    if 'MA' in indicators or 'ALL' in indicators:
        price_fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['MA_50'],
            line=dict(color='blue', width=1),
            name='50 MA'
        ))
        price_fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['MA_200'],
            line=dict(color='orange', width=1),
            name='200 MA'
        ))
    
    price
