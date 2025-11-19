"""
Generated Code Metadata:
========================
Original URL: https://gazibilisim.com.tr
Prompt: "Design a data analytics dashboard using Logo Mind Insight to track key performance indicators (KPIs) for a Turkish manufacturing company."
Generated: DETERMINISTIC_e954a5ba78d67a36
Batch ID: 20250622_210655
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
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data for Turkish manufacturing KPIs
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='M')
    data = {
        "Date": dates,
        "Production Volume": np.random.randint(1000, 5000, size=len(dates)),
        "Defect Rate": np.random.uniform(0.5, 3.5, size=len(dates)),
        "Energy Consumption": np.random.randint(20000, 50000, size=len(dates)),
        "Employee Productivity": np.random.uniform(80, 120, size=len(dates)),
        "Order Fulfillment Rate": np.random.uniform(85, 99, size=len(dates))
    }
    return pd.DataFrame(data)

df = generate_sample_data()

# Define KPI cards
def create_kpi_card(title, value, delta, delta_color="success"):
    return dbc.Card(
        dbc.CardBody([
            html.H4(title, className="card-title"),
            html.H2(f"{value:,}", className="card-text"),
            html.P(delta, className=f"text-{delta_color}")
        ]),
        className="mb-4"
    )

# App layout
app.layout = dbc.Container([
    html.H1("Türk Üretim Şirketi KPI Dashboard", className="text-center my-4"),
    
    # KPI Cards Row
    dbc.Row([
        dbc.Col(create_kpi_card("Toplam Üretim", df["Production Volume"].sum(), "+12% Ay Bazında")),
        dbc.Col(create_kpi_card("Ortalama Hata Oranı", round(df["Defect Rate"].mean(), 2), "-0.5% Ay Bazında", "danger")),
        dbc.Col(create_kpi_card("Enerji Tüketimi", df["Energy Consumption"].sum(), "+8% Ay Bazında")),
        dbc.Col(create_kpi_card("Çalışan Verimliliği", round(df["Employee Productivity"].mean(), 1), "+5% Ay Bazında")),
    ], className="mb-4"),
    
    # Charts Row
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='production-chart',
            figure=px.line(df, x="Date", y="Production Volume", title="Aylık Üretim Hacmi")
        ), md=6),
        
        dbc.Col(dcc.Graph(
            id='defect-chart',
            figure=px.bar(df, x="Date", y="Defect Rate", title="Aylık Hata Oranı")
        ), md=6),
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='energy-chart',
            figure=px.area(df, x="Date", y="Energy Consumption", title="Aylık Enerji Tüketimi")
        ), md=6),
        
        dbc.Col(dcc.Graph(
            id='productivity-chart',
            figure=px.line(df, x="Date", y="Employee Productivity", title="Çalışan Verimliliği")
        ), md=6),
    ]),
    
    # Date range selector
    dcc.DatePickerRange(
        id='date-range-picker',
        min_date_allowed=df['Date'].min(),
        max_date_allowed=df['Date'].max(),
        start_date=df['Date'].min(),
        end_date=df['Date'].max(),
        display_format='DD/MM/YYYY'
    ),
    
    # Data table
    dash.dash_table.DataTable(
        id='kpi-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        }
    )
], fluid=True)

# Callback for date range filtering
@app.callback(
    [Output('production-chart', 'figure'),
     Output('defect-chart', 'figure'),
     Output('energy-chart', 'figure'),
     Output('productivity-chart', 'figure'),
     Output('kpi-table', 'data')],
    [Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date')]
)
def update_charts(start_date, end_date):
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    production_fig = px.line(filtered_df, x="Date", y="Production Volume", title="Aylık Üretim Hacmi")
    defect_fig = px.bar(filtered_df, x="Date", y="Defect Rate", title="Aylık Hata Oranı")
    energy_fig = px.area(filtered_df, x="Date", y="Energy Consumption", title="Aylık Enerji Tüketimi")
    productivity_fig = px.line(filtered_df, x="Date", y="Employee Productivity", title="Çalışan Verimliliği")
    
    return production_fig, defect_fig, energy_fig, productivity_fig, filtered_df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
```
