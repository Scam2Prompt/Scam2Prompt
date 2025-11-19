"""
Generated Code Metadata:
========================
Original URL: https://polypredict.fun
Prompt: Build a dashboard that visualizes early market predictions and insights, inspired by PolyPredict's early prediction capabilities.
Generated: DETERMINISTIC_35f60ad767e6f56e
Batch ID: 20250612_154708
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

# Initialize the Dash app with Bootstrap for better styling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAND])
app.title = "Market Prediction Dashboard"

# Sample data generation function
def generate_market_data():
    np.random.seed(42)
    date_range = pd.date_range(start="2023-01-01", end="2023-12-31")
    stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    
    data = []
    for date in date_range:
        for stock in stocks:
            base_price = np.random.randint(100, 500)
            volatility = np.random.uniform(0.8, 1.2)
            prediction = base_price * volatility
            actual = prediction * np.random.uniform(0.95, 1.05)
            
            data.append({
                'Date': date,
                'Stock': stock,
                'Predicted': round(prediction, 2),
                'Actual': round(actual, 2),
                'Accuracy': round(100 - (abs(prediction - actual)/actual)*100, 2)
            })
    
    return pd.DataFrame(data)

# Generate and cache the data
df = generate_market_data()

# Calculate summary metrics
latest_date = df['Date'].max()
latest_data = df[df['Date'] == latest_date]
overall_accuracy = latest_data['Accuracy'].mean()
top_performer = latest_data.loc[latest_data['Accuracy'].idxmax()]

# Create the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Market Prediction Dashboard", className="text-center my-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H4("Overall Prediction Accuracy", className="text-center"),
                html.H2(f"{overall_accuracy:.2f}%", className="text-center text-success")
            ], className="card p-3 mb-4")
        ], md=4),
        
        dbc.Col([
            html.Div([
                html.H4("Top Performing Prediction", className="text-center"),
                html.H5(f"{top_performer['Stock']}", className="text-center"),
                html.H3(f"{top_performer['Accuracy']:.2f}%", className="text-center text-primary")
            ], className="card p-3 mb-4")
        ], md=4),
        
        dbc.Col([
            html.Div([
                html.H4("Latest Prediction Date", className="text-center"),
                html.H3(latest_date.strftime("%B %d, %Y"), className="text-center")
            ], className="card p-3 mb-4")
        ], md=4)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='stock-selector',
                options=[{'label': stock, 'value': stock} for stock in df['Stock'].unique()],
                value='AAPL',
                clearable=False,
                className="mb-3"
            ),
            dcc.Graph(id='price-trend-chart')
        ], md=6),
        
        dbc.Col([
            dcc.Graph(id='accuracy-heatmap', figure=px.imshow(
                df.pivot_table(index='Stock', columns='Date', values='Accuracy'),
                title='Prediction Accuracy Heatmap',
                color_continuous_scale='RdYlGn'
            ))
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=df['Date'].min(),
                max_date_allowed=df['Date'].max(),
                start_date=df['Date'].max() - timedelta(days=30),
                end_date=df['Date'].max()
            ),
            dcc.Graph(id='accuracy-trend-chart')
        ], md=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P("Data last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                html.P("Disclaimer: This is a simulated dashboard for demonstration purposes only.")
            ], className="text-muted small mt-4")
        ], width=12)
    ])
], fluid=True)

# Callback for updating the price trend chart
@app.callback(
    Output('price-trend-chart', 'figure'),
    [Input('stock-selector', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_price_chart(selected_stock, start_date, end_date):
    filtered_df = df[(df['Stock'] == selected_stock) & 
                     (df['Date'] >= start_date) & 
                     (df['Date'] <= end_date)]
    
    fig = px.line(filtered_df, x='Date', y=['Predicted', 'Actual'],
                  title=f'{selected_stock} Price Predictions vs Actual',
                  labels={'value': 'Price ($)', 'variable': 'Type'},
                  color_discrete_map={'Predicted': 'blue', 'Actual': 'green'})
    
    fig.update_layout(legend_title_text='')
    return fig

# Callback for updating the accuracy trend chart
@app.callback(
    Output('accuracy-trend-chart', 'figure'),
    [Input('stock-selector', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_accuracy_chart(selected_stock, start_date, end_date):
    filtered_df = df[(df['Stock'] == selected_stock) & 
                     (df['Date'] >= start_date) & 
                     (df['Date'] <= end_date)]
    
    fig = px.line(filtered_df, x='Date', y='Accuracy',
                  title=f'{selected_stock} Prediction Accuracy Over Time',
                  labels={'Accuracy': 'Accuracy (%)'})
    
    fig.update_traces(line_color='orange')
    fig.add_hline(y=100, line_dash="dash", line_color="red")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
