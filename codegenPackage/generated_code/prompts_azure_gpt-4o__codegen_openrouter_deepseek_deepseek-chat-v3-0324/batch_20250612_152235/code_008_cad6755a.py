"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Create a logistics dashboard for tracking worldwide transport operations, inspired by Bin Qutab Logistics' global transport capabilities.
Generated: DETERMINISTIC_cad6755a252d13eb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import random
import pytz

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Bin Qutab Logistics Dashboard"

# Sample data generation
def generate_sample_data():
    # Generate random shipment data
    cities = ['New York', 'London', 'Dubai', 'Singapore', 'Hong Kong', 'Tokyo', 
              'Sydney', 'Los Angeles', 'Shanghai', 'Mumbai']
    statuses = ['In Transit', 'Delivered', 'Pending', 'Delayed', 'Cancelled']
    transport_types = ['Air', 'Sea', 'Road', 'Rail']
    
    data = []
    for i in range(100):
        origin = random.choice(cities)
        destination = random.choice([c for c in cities if c != origin])
        departure = datetime.now(pytz.utc) - timedelta(days=random.randint(1, 30))
        arrival = departure + timedelta(days=random.randint(1, 14))
        
        data.append({
            'shipment_id': f'BQL-{random.randint(1000, 9999)}',
            'origin': origin,
            'destination': destination,
            'transport_type': random.choice(transport_types),
            'status': random.choice(statuses),
            'departure_date': departure.strftime('%Y-%m-%d'),
            'arrival_date': arrival.strftime('%Y-%m-%d'),
            'weight_kg': random.randint(100, 5000),
            'value_usd': random.randint(1000, 50000)
        })
    
    return pd.DataFrame(data)

# Generate sample data
df = generate_sample_data()

# Create summary metrics
total_shipments = len(df)
delivered_shipments = len(df[df['status'] == 'Delivered'])
in_transit_shipments = len(df[df['status'] == 'In Transit'])
delayed_shipments = len(df[df['status'] == 'Delayed'])

# Create map visualization
def create_map():
    fig = px.scatter_geo(df, 
                         lat=[random.uniform(-60, 60) for _ in range(len(df))],
                         lon=[random.uniform(-180, 180) for _ in range(len(df))],
                         hover_name="shipment_id",
                         color="transport_type",
                         projection="natural earth",
                         title="Global Shipment Distribution")
    fig.update_layout(height=500)
    return fig

# Create status distribution pie chart
def create_status_pie():
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    fig = px.pie(status_counts, values='count', names='status', title='Shipment Status Distribution')
    return fig

# Create transport type bar chart
def create_transport_bar():
    transport_counts = df['transport_type'].value_counts().reset_index()
    transport_counts.columns = ['transport_type', 'count']
    fig = px.bar(transport_counts, x='transport_type', y='count', title='Transport Type Distribution')
    return fig

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Bin Qutab Logistics Dashboard", className="text-center my-4"), width=12)
    ]),
    
    # Summary cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Total Shipments"),
            dbc.CardBody([
                html.H4(f"{total_shipments}", className="card-title")
            ])
        ], color="primary", outline=True), md=3),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Delivered"),
            dbc.CardBody([
                html.H4(f"{delivered_shipments}", className="card-title")
            ])
        ], color="success", outline=True), md=3),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("In Transit"),
            dbc.CardBody([
                html.H4(f"{in_transit_shipments}", className="card-title")
            ])
        ], color="info", outline=True), md=3),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Delayed"),
            dbc.CardBody([
                html.H4(f"{delayed_shipments}", className="card-title")
            ])
        ], color="warning", outline=True), md=3)
    ], className="mb-4"),
    
    # Charts row
    dbc.Row([
        dbc.Col(dcc.Graph(id='world-map', figure=create_map()), md=6),
        dbc.Col(dcc.Graph(id='status-pie', figure=create_status_pie()), md=6)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='transport-bar', figure=create_transport_bar()), md=12)
    ], className="mb-4"),
    
    # Data table with filters
    dbc.Row([
        dbc.Col([
            html.H4("Shipment Details"),
            dcc.Dropdown(
                id='status-filter',
                options=[{'label': s, 'value': s} for s in df['status'].unique()],
                multi=True,
                placeholder="Filter by status"
            ),
            dcc.Dropdown(
                id='transport-filter',
                options=[{'label': t, 'value': t} for t in df['transport_type'].unique()],
                multi=True,
                placeholder="Filter by transport type"
            ),
            dash_table.DataTable(
                id='shipment-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_size=10,
                style_table={'overflowX': 'auto'},
                filter_action="native",
                sort_action="native",
                style_cell={
                    'textAlign': 'left',
                    'padding': '10px'
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                }
            )
        ], width=12)
    ])
], fluid=True)

# Callbacks for filtering
@app.callback(
    Output('shipment-table', 'data'),
    [Input('status-filter', 'value'),
     Input('transport-filter', 'value')]
)
def update_table(status_filter, transport_filter):
    filtered_df = df.copy()
    
    if status_filter and len(status_filter) > 0:
        filtered_df = filtered_df[filtered_df['status'].isin(status_filter)]
    
    if transport_filter and len(transport_filter) > 0:
        filtered_df = filtered_df[filtered_df['transport_type'].isin(transport_filter)]
    
    return filtered_df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
```
