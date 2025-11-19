"""
Generated Code Metadata:
========================
Original URL: https://opterisglobal.com
Prompt: Write code to generate a user-friendly dashboard for managing investments, inspired by Opteris Global's integrated application design.
Generated: DETERMINISTIC_66589d9fa76d94f9
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Investment Dashboard"

# Sample portfolio data (in a real app, this would come from a database)
portfolio_data = {
    "Asset": ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"],
    "Shares": [10, 5, 8, 15, 3],
    "Avg Cost": [150.25, 2850.50, 300.75, 700.30, 3500.00],
    "Current Price": [0] * 5,  # Will be updated with real-time data
    "Value": [0] * 5,
    "Gain/Loss": [0] * 5,
    "Sector": ["Technology", "Technology", "Technology", "Automotive", "Retail"]
}

# Create DataFrame from portfolio data
df = pd.DataFrame(portfolio_data)

# Fetch current prices from Yahoo Finance
def update_prices():
    try:
        tickers = " ".join(df["Asset"].tolist())
        data = yf.download(tickers, period="1d", group_by="ticker")
        
        for i, asset in enumerate(df["Asset"]):
            if asset in data:
                current_price = data[asset]["Close"].iloc[-1]
                df.at[i, "Current Price"] = current_price
                df.at[i, "Value"] = current_price * df.at[i, "Shares"]
                df.at[i, "Gain/Loss"] = (current_price - df.at[i, "Avg Cost"]) * df.at[i, "Shares"]
    except Exception as e:
        print(f"Error fetching prices: {e}")

update_prices()

# Calculate summary metrics
total_value = df["Value"].sum()
total_gain_loss = df["Gain/Loss"].sum()
total_invested = (df["Avg Cost"] * df["Shares"]).sum()
portfolio_return = (total_gain_loss / total_invested) * 100 if total_invested != 0 else 0

# Create time series data for historical performance
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
historical_data = pd.DataFrame()

try:
    for asset in df["Asset"]:
        asset_data = yf.download(asset, start=start_date, end=end_date)
        asset_data["Asset"] = asset
        historical_data = pd.concat([historical_data, asset_data])
except Exception as e:
    print(f"Error fetching historical data: {e}")

# Create the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Investment Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    # Summary Cards
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Portfolio Value"),
                dbc.CardBody([
                    html.H4(f"${total_value:,.2f}", className="card-title"),
                    html.P(f"{portfolio_return:.2f}% overall return", className="card-text")
                ])
            ], className="shadow-sm"),
            md=4
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Total Gain/Loss"),
                dbc.CardBody([
                    html.H4(f"${total_gain_loss:,.2f}", className="card-title"),
                    html.P("All time", className="card-text")
                ])
            ], className="shadow-sm"),
            md=4
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Diversification"),
                dbc.CardBody([
                    html.H4(f"{len(df)} assets", className="card-title"),
                    html.P(f"{len(df['Sector'].unique())} sectors", className="card-text")
                ])
            ], className="shadow-sm"),
            md=4
        )
    ], className="mb-4"),
    
    # Charts and Tables
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='portfolio-performance',
                figure=px.line(
                    historical_data.reset_index(),
                    x="Date",
                    y="Close",
                    color="Asset",
                    title="Portfolio Performance (Last 12 Months)"
                ).update_layout(showlegend=True)
            ),
            dcc.Interval(
                id='interval-component',
                interval=60*60*1000,  # 1 hour in milliseconds
                n_intervals=0
            )
        ], md=8),
        
        dbc.Col([
            dcc.Graph(
                id='sector-allocation',
                figure=px.pie(
                    df,
                    values="Value",
                    names="Sector",
                    title="Sector Allocation",
                    hole=0.4
                )
            )
        ], md=4)
    ], className="mb-4"),
    
    # Portfolio Table
    dbc.Row([
        dbc.Col([
            html.H4("Portfolio Holdings", className="mb-3"),
            dbc.Table.from_dataframe(
                df.sort_values("Value", ascending=False),
                striped=True,
                bordered=True,
                hover=True,
                responsive=True
            )
        ], width=12)
    ]),
    
    # Transaction Form
    dbc.Row([
        dbc.Col([
            html.H4("Add Transaction", className="mb-3"),
            dbc.Form([
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Asset Ticker"),
                        dbc.Input(id="asset-input", type="text", placeholder="e.g. AAPL")
                    ], md=3),
                    dbc.Col([
                        dbc.Label("Shares"),
                        dbc.Input(id="shares-input", type="number", min=0, step=0.1)
                    ], md=2),
                    dbc.Col([
                        dbc.Label("Price per Share"),
                        dbc.Input(id="price-input", type="number", min=0, step=0.01)
                    ], md=2),
                    dbc.Col([
                        dbc.Label("Sector"),
                        dbc.Select(
                            id="sector-input",
                            options=[
                                {"label": "Technology", "value": "Technology"},
                                {"label": "Healthcare", "value": "Healthcare"},
                                {"label": "Financial", "value": "Financial"},
                                {"label": "Consumer", "value": "Consumer"},
                                {"label": "Industrial", "value": "Industrial"},
                                {"label": "Other", "value": "Other"}
                            ]
                        )
                    ], md=3),
                    dbc.Col([
                        dbc.Button("Add", id="add-button", color="primary", className="mt-4")
                    ], md=2)
                ])
            ])
        ], width=12)
    ], className="mb-4")
], fluid=True)

# Callback for adding transactions
@callback(
    Output('portfolio-performance', 'figure'),
    Output('sector-allocation', 'figure'),
    Input('add-button', 'n_clicks'),
    Input('interval-component', 'n_intervals'),
    Input('asset-input', 'value'),
    Input('shares-input', 'value'),
    Input('price-input', 'value'),
    Input('sector-input', 'value')
)
def update_portfolio(n_clicks, n_intervals, asset, shares, price, sector):
    ctx = dash.callback_context
    
    # Handle price updates from interval
    if ctx.triggered[0]['prop_id'] == 'interval-component.n_intervals':
        update_prices()
    
    # Handle new transaction
    elif ctx.triggered[0]['prop_id'] == 'add-button.n_clicks':
        if all([asset, shares, price, sector]):
            try:
                new_row = {
                    "Asset": asset.upper(),
                    "Shares": float(shares),
                    "Avg Cost": float(price),
                    "Current Price": float(price),  # Initial price
                    "Value": float(shares) * float(price),
                    "Gain/Loss": 0,
                    "Sector": sector
                }
                
                global df
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                update_prices()
            except Exception as e:
                print(f"Error adding transaction: {e}")
    
    # Update figures
    performance_fig = px.line(
        historical_data.reset_index(),
        x="Date",
        y="Close",
        color="Asset",
        title="Portfolio Performance (Last 12 Months)"
    )
    
    allocation_fig = px.pie(
        df,
        values="Value",
        names="Sector",
        title="Sector Allocation",
        hole=0.4
    )
    
    return performance_fig, allocation_fig

if __name__ == '__main__':
    app.run_server(debug=True)
```
