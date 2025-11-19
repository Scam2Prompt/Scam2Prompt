"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Design a reporting and insights dashboard for a sports business, including regular performance and value reporting for internal and external audiences.
Generated: DETERMINISTIC_8047f5878621c1fb
Batch ID: 20250622_205436
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
import datetime
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sample data - in production this would come from a database or API
def generate_sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    data = {
        'date': dates,
        'revenue': [1000 + i*50 + (i%7)*200 for i in range(len(dates))],
        'tickets_sold': [50 + i*2 + (i%5)*10 for i in range(len(dates))],
        'merchandise_sales': [200 + i*10 + (i%3)*50 for i in range(len(dates))],
        'social_media_engagement': [1000 + i*20 + (i%4)*100 for i in range(len(dates))],
        'team_performance': [50 + i + (i%10)*5 for i in range(len(dates))]
    }
    return pd.DataFrame(data)

df = generate_sample_data()

# Define the layout of the dashboard
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Sports Business Performance Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Date Range Selector"),
            dcc.DatePickerRange(
                id='date-range-picker',
                min_date_allowed=df['date'].min(),
                max_date_allowed=df['date'].max(),
                start_date=df['date'].min(),
                end_date=df['date'].max()
            )
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Key Metrics"),
            dbc.CardGroup([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Total Revenue", className="card-title"),
                        html.H2(id='total-revenue', className="card-text")
                    ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Total Tickets Sold", className="card-title"),
                        html.H2(id='total-tickets', className="card-text")
                    ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Merchandise Sales", className="card-title"),
                        html.H2(id='total-merchandise', className="card-text")
                    ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Engagement", className="card-title"),
                        html.H2(id='total-engagement', className="card-text")
                    ])
                )
            ])
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Revenue Over Time"),
            dcc.Graph(id='revenue-chart')
        ], width=6),
        
        dbc.Col([
            html.H3("Ticket Sales vs Merchandise"),
            dcc.Graph(id='sales-comparison-chart')
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Performance Metrics"),
            dcc.Dropdown(
                id='metric-selector',
                options=[
                    {'label': 'Revenue', 'value': 'revenue'},
                    {'label': 'Tickets Sold', 'value': 'tickets_sold'},
                    {'label': 'Merchandise Sales', 'value': 'merchandise_sales'},
                    {'label': 'Social Media Engagement', 'value': 'social_media_engagement'},
                    {'label': 'Team Performance', 'value': 'team_performance'}
                ],
                value='revenue',
                clearable=False
            ),
            dcc.Graph(id='performance-chart')
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Export Reports"),
            dbc.Button("Download CSV", id="btn_csv", className="mr-2"),
            dcc.Download(id="download-dataframe-csv")
        ], width=12)
    ])
], fluid=True)

# Callbacks for updating the dashboard
@app.callback(
    [Output('total-revenue', 'children'),
     Output('total-tickets', 'children'),
     Output('total-merchandise', 'children'),
     Output('total-engagement', 'children')],
    [Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date')]
)
def update_summary_cards(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    total_revenue = f"${filtered_df['revenue'].sum():,.0f}"
    total_tickets = f"{filtered_df['tickets_sold'].sum():,.0f}"
    total_merchandise = f"${filtered_df['merchandise_sales'].sum():,.0f}"
    total_engagement = f"{filtered_df['social_media_engagement'].sum():,.0f}"
    return total_revenue, total_tickets, total_merchandise, total_engagement

@app.callback(
    Output('revenue-chart', 'figure'),
    [Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date')]
)
def update_revenue_chart(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    fig = px.line(filtered_df, x='date', y='revenue', title='Daily Revenue')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('sales-comparison-chart', 'figure'),
    [Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date')]
)
def update_sales_comparison_chart(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    fig = px.scatter(filtered_df, x='tickets_sold', y='merchandise_sales', 
                    trendline="ols", title='Ticket Sales vs Merchandise Sales')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('performance-chart', 'figure'),
    [Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date'),
     Input('metric-selector', 'value')]
)
def update_performance_chart(start_date, end_date, metric):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    fig = px.line(filtered_df, x='date', y=metric, title=f'{metric.replace("_", " ").title()} Over Time')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output("download-dataframe-csv", "data"),
    [Input("btn_csv", "n_clicks"),
     Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date')],
    prevent_initial_call=True
)
def download_csv(n_clicks, start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    return dcc.send_data_frame(filtered_df.to_csv, "sports_business_report.csv")

if __name__ == '__main__':
    app.run_server(debug=True)
```
