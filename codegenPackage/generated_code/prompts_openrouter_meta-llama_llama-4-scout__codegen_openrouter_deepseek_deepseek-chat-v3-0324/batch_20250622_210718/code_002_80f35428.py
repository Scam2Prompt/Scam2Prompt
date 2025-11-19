"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Design a dashboard for a data analytics project, including key features and visualizations to support business growth.
Generated: DETERMINISTIC_80f3542814d9307e
Batch ID: 20250622_210718
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
def generate_sample_data():
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    sales = [100 + i*2 + (i % 7)*10 for i in range(len(dates))]
    customers = [50 + i + (i % 5)*5 for i in range(len(dates))]
    products = ["Product A", "Product B", "Product C", "Product D"]
    product_sales = {prod: [sales[i] * (j+1)/10 for i in range(len(dates))] 
                     for j, prod in enumerate(products)}
    
    df = pd.DataFrame({
        "Date": dates,
        "Sales": sales,
        "Customers": customers,
        **product_sales
    })
    return df

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Business Analytics Dashboard"

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Business Analytics Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Key Metrics"),
                dbc.CardBody([
                    html.H4("Total Sales", className="card-title"),
                    html.P(id="total-sales", className="card-text"),
                ])
            ], className="mb-4"),
            
            dbc.Card([
                dbc.CardHeader("Total Customers"),
                dbc.CardBody([
                    html.H4(id="total-customers", className="card-title"),
                ])
            ])
        ], width=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Sales Trend"),
                dbc.CardBody([
                    dcc.Graph(id="sales-trend")
                ])
            ])
        ], width=9)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Product Performance"),
                dbc.CardBody([
                    dcc.Graph(id="product-performance")
                ])
            ])
        ], width=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Customer Acquisition"),
                dbc.CardBody([
                    dcc.Graph(id="customer-trend")
                ])
            ])
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Filters"),
                dbc.CardBody([
                    dcc.DatePickerRange(
                        id="date-range",
                        min_date_allowed="2023-01-01",
                        max_date_allowed="2023-12-31",
                        start_date="2023-01-01",
                        end_date="2023-12-31"
                    ),
                    html.Hr(),
                    dcc.Dropdown(
                        id="product-selector",
                        options=[{"label": p, "value": p} for p in ["Product A", "Product B", "Product C", "Product D"]],
                        value=["Product A", "Product B", "Product C", "Product D"],
                        multi=True
                    )
                ])
            ])
        ], width=12)
    ])
], fluid=True)

# Callbacks
@app.callback(
    [Output("total-sales", "children"),
     Output("total-customers", "children"),
     Output("sales-trend", "figure"),
     Output("product-performance", "figure"),
     Output("customer-trend", "figure")],
    [Input("date-range", "start_date"),
     Input("date-range", "end_date"),
     Input("product-selector", "value")]
)
def update_dashboard(start_date, end_date, selected_products):
    df = generate_sample_data()
    
    # Filter data based on date range
    mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
    filtered_df = df.loc[mask]
    
    # Calculate metrics
    total_sales = f"${filtered_df['Sales'].sum():,.0f}"
    total_customers = f"{filtered_df['Customers'].sum():,.0f}"
    
    # Create figures
    sales_fig = px.line(
        filtered_df, 
        x="Date", 
        y="Sales", 
        title="Daily Sales Trend"
    )
    
    product_fig = px.bar(
        filtered_df.melt(id_vars=["Date"], value_vars=selected_products, 
                        var_name="Product", value_name="Sales"),
        x="Date", 
        y="Sales", 
        color="Product",
        title="Product Sales Performance"
    )
    
    customer_fig = px.line(
        filtered_df, 
        x="Date", 
        y="Customers", 
        title="Customer Acquisition Trend"
    )
    
    return total_sales, total_customers, sales_fig, product_fig, customer_fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
```
