"""
Generated Code Metadata:
========================
Original URL: https://opensea.io
Prompt: Design a data visualization dashboard to display trends and insights on OpenSea's NFT marketplace, including metrics such as sales volume, floor prices, and collection popularity.
Generated: DETERMINISTIC_03c49f1262e42d83
Batch ID: 20250622_205139
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1": {
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
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime, timedelta
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# API configuration
OPENSEA_API_BASE = "https://api.opensea.io/api/v1"
API_KEY = "your-opensea-api-key"  # Replace with your actual API key
HEADERS = {"Accept": "application/json", "X-API-KEY": API_KEY}

# Cache timeout
CACHE_TIMEOUT = 3600  # 1 hour in seconds

# Layout components
def create_navbar():
    return dbc.NavbarSimple(
        brand="OpenSea NFT Dashboard",
        brand_href="#",
        color="primary",
        dark=True,
    )

def create_filters():
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5("Filters", className="card-title"),
                    dcc.Dropdown(
                        id="timeframe-dropdown",
                        options=[
                            {"label": "24 Hours", "value": "24h"},
                            {"label": "7 Days", "value": "7d"},
                            {"label": "30 Days", "value": "30d"},
                        ],
                        value="7d",
                        clearable=False,
                    ),
                    html.Br(),
                    dcc.Dropdown(
                        id="collection-dropdown",
                        options=[],
                        placeholder="Select Collection...",
                        multi=True,
                    ),
                ]
            )
        ]
    )

# App layout
app.layout = dbc.Container(
    [
        create_navbar(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(create_filters(), width=3),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Total Sales Volume"),
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        id="total-sales-volume",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "ETH",
                                                        className="card-text",
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    width=3,
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Total Transactions"),
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        id="total-transactions",
                                                        className="card-title",
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    width=3,
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Avg. Sale Price"),
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        id="avg-sale-price",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "ETH",
                                                        className="card-text",
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    width=3,
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Unique Buyers"),
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        id="unique-buyers",
                                                        className="card-title",
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    width=3,
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(id="sales-volume-chart"), width=12
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(id="floor-price-chart"), width=6
                                ),
                                dbc.Col(
                                    dcc.Graph(id="popular-collections-chart"),
                                    width=6,
                                ),
                            ]
                        ),
                    ],
                    width=9,
                ),
            ]
        ),
    ],
    fluid=True,
)

# Helper functions
def fetch_collections():
    """Fetch top NFT collections from OpenSea"""
    try:
        url = f"{OPENSEA_API_BASE}/collections?offset=0&limit=50"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        collections = response.json().get("collections", [])
        return [
            {"label": col["name"], "value": col["slug"]}
            for col in collections
            if col.get("slug")
        ]
    except Exception as e:
        print(f"Error fetching collections: {e}")
        return []

def fetch_stats(timeframe="7d"):
    """Fetch marketplace statistics based on timeframe"""
    try:
        end_date = datetime.now()
        
        if timeframe == "24h":
            start_date = end_date - timedelta(days=1)
        elif timeframe == "7d":
            start_date = end_date - timedelta(days=7)
        else:  # 30d
            start_date = end_date - timedelta(days=30)
            
        params = {
            "occurred_after": int(start_date.timestamp()),
            "occurred_before": int(end_date.timestamp()),
            "limit": 200
        }
        
        url = f"{OPENSEA_API_BASE}/events"
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json().get("asset_events", [])
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return []

def process_stats(events):
    """Process raw event data into structured metrics"""
    if not events:
        return pd.DataFrame()
    
    data = []
    for event in events:
        if event.get("event_type") == "successful":
            sale = {
                "timestamp": event.get("created_date"),
                "collection": event.get("collection_slug"),
                "price": float(event.get("total_price", 0)) / 1e18,  # Convert from wei to ETH
                "buyer": event.get("winner_account", {}).get("address"),
                "seller": event.get("seller", {}).get("address"),
                "token_id": event.get("asset", {}).get("token_id"),
            }
            data.append(sale)
    
    df = pd.DataFrame(data)
    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["date"] = df["timestamp"].dt.date
    return df

# Callbacks
@app.callback(
    Output("collection-dropdown", "options"),
    Input("timeframe-dropdown", "value"),
)
def update_collections(_):
    return fetch_collections()

@app.callback(
    [
        Output("total-sales-volume", "children"),
        Output("total-transactions", "children"),
        Output("avg-sale-price", "children"),
        Output("unique-buyers", "children"),
        Output("sales-volume-chart", "figure"),
        Output("floor-price-chart", "figure"),
        Output("popular-collections-chart", "figure"),
    ],
    [
        Input("timeframe-dropdown", "value"),
        Input("collection-dropdown", "value"),
    ],
)
def update_dashboard(timeframe, selected_collections):
    events = fetch_stats(timeframe)
    df = process_stats(events)
    
    if df.empty:
        return [0, 0, 0, 0, px.line(), px.line(), px.bar()]
    
    # Filter by selected collections if any
    if selected_collections:
        df = df[df["collection"].isin(selected_collections)]
    
    # Calculate metrics
    total_volume = round(df["price"].sum(), 2)
    total_transactions = len(df)
    avg_sale_price = round(df["price"].mean(), 4)
    unique_buyers = df["buyer"].nunique()
    
    # Sales volume chart
    volume_df = df.groupby("date")["price"].sum().reset_index()
    sales_fig = px.line(
        volume_df,
        x="date",
        y="price",
        title="Daily Sales Volume (ETH)",
        labels={"price": "Volume (ETH)", "date": "Date"},
    )
    
    # Floor price chart
    floor_df = df.groupby(["date", "collection"])["price"].min().reset_index()
    floor_fig = px.line(
        floor_df,
        x="date",
        y="price",
        color="collection",
        title="Collection Floor Prices (ETH)",
        labels={"price": "Floor Price (ETH)", "date": "Date"},
    )
    
    # Popular collections chart
    popular_df = (
        df.groupby("collection")["price"]
        .agg(["count", "sum"])
        .reset_index()
        .sort_values("sum", ascending=False)
        .head(10)
    )
    popular_fig = px.bar(
        popular_df,
        x="collection",
        y="sum",
        title="Top Collections by Volume (ETH)",
        labels={"sum": "Volume (ETH)", "collection": "Collection"},
    )
    
    return [
        f"{total_volume:,}",
        f"{total_transactions:,}",
        f"{avg
