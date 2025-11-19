"""
Generated Code Metadata:
========================
Original URL: https://stonex.markets
Prompt: "Design a simple dashboard to display StoneX market insights on fertilizers, including price trends and forecasts."
Generated: DETERMINISTIC_1f3432840dbecd8e
Batch ID: 20250622_212906
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
from datetime import datetime, timedelta

# Sample data generation function
def generate_sample_data():
    dates = pd.date_range(start=datetime.now() - timedelta(days=365), end=datetime.now())
    np.random.seed(42)
    urea_prices = np.random.normal(300, 20, len(dates)).cumsum()
    dap_prices = np.random.normal(400, 25, len(dates)).cumsum()
    potash_prices = np.random.normal(350, 15, len(dates)).cumsum()
    
    forecast_dates = pd.date_range(start=datetime.now(), end=datetime.now() + timedelta(days=90))
    urea_forecast = np.random.normal(0, 5, len(forecast_dates)).cumsum() + urea_prices[-1]
    dap_forecast = np.random.normal(0, 6, len(forecast_dates)).cumsum() + dap_prices[-1]
    potash_forecast = np.random.normal(0, 4, len(forecast_dates)).cumsum() + potash_prices[-1]
    
    return {
        'historical': pd.DataFrame({
            'date': dates,
            'urea': urea_prices,
            'dap': dap_prices,
            'potash': potash_prices
        }),
        'forecast': pd.DataFrame({
            'date': forecast_dates,
            'urea': urea_forecast,
            'dap': dap_forecast,
            'potash': potash_forecast
        })
    }

# Initialize the Dash app
app = dash.Dash(__name__, title="StoneX Fertilizer Market Insights")
server = app.server

# Generate sample data
data = generate_sample_data()

# Define app layout
app.layout = html.Div([
    html.Div([
        html.H1("StoneX Fertilizer Market Insights", style={'text-align': 'center'}),
        html.P("Latest market trends and forecasts for key fertilizer products", 
               style={'text-align': 'center', 'margin-bottom': '30px'})
    ]),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='product-selector',
                options=[
                    {'label': 'Urea', 'value': 'urea'},
                    {'label': 'DAP', 'value': 'dap'},
                    {'label': 'Potash', 'value': 'potash'}
                ],
                value='urea',
                clearable=False,
                style={'width': '200px'}
            )
        ], style={'width': '20%', 'display': 'inline-block', 'margin-right': '20px'}),
        
        html.Div([
            dcc.RadioItems(
                id='timeframe-selector',
                options=[
                    {'label': '1 Year', 'value': 365},
                    {'label': '6 Months', 'value': 180},
                    {'label': '3 Months', 'value': 90}
                ],
                value=365,
                inline=True,
                labelStyle={'margin-right': '15px'}
            )
        ], style={'width': '75%', 'display': 'inline-block'})
    ], style={'margin-bottom': '30px'}),
    
    dcc.Graph(id='price-chart'),
    
    html.Div([
        html.Div([
            html.H3("Current Prices"),
            html.Table([
                html.Tr([
                    html.Th("Product"),
                    html.Th("Price (USD/ton)"),
                    html.Th("30d Change"),
                    html.Th("90d Forecast")
                ]),
                html.Tr([
                    html.Td("Urea"),
                    html.Td(f"${data['historical']['urea'].iloc[-1]:.2f}"),
                    html.Td(f"{(data['historical']['urea'].iloc[-1] - data['historical']['urea'].iloc[-30])/data['historical']['urea'].iloc[-30]*100:.2f}%"),
                    html.Td(f"{(data['forecast']['urea'].iloc[-1] - data['historical']['urea'].iloc[-1])/data['historical']['urea'].iloc[-1]*100:.2f}%")
                ]),
                html.Tr([
                    html.Td("DAP"),
                    html.Td(f"${data['historical']['dap'].iloc[-1]:.2f}"),
                    html.Td(f"{(data['historical']['dap'].iloc[-1] - data['historical']['dap'].iloc[-30])/data['historical']['dap'].iloc[-30]*100:.2f}%"),
                    html.Td(f"{(data['forecast']['dap'].iloc[-1] - data['historical']['dap'].iloc[-1])/data['historical']['dap'].iloc[-1]*100:.2f}%")
                ]),
                html.Tr([
                    html.Td("Potash"),
                    html.Td(f"${data['historical']['potash'].iloc[-1]:.2f}"),
                    html.Td(f"{(data['historical']['potash'].iloc[-1] - data['historical']['potash'].iloc[-30])/data['historical']['potash'].iloc[-30]*100:.2f}%"),
                    html.Td(f"{(data['forecast']['potash'].iloc[-1] - data['historical']['potash'].iloc[-1])/data['historical']['potash'].iloc[-1]*100:.2f}%")
                ])
            ], style={'width': '100%', 'border-collapse': 'collapse'})
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '20px', 'border': '1px solid #ddd', 'border-radius': '5px'}),
        
        html.Div([
            html.H3("Market Commentary"),
            dcc.Markdown('''
                - **Urea**: Prices have shown steady growth over the past quarter due to increased demand from North America.
                - **DAP**: Supply constraints from Morocco have led to price volatility in recent weeks.
                - **Potash**: Stable production from Canada has maintained price equilibrium despite seasonal demand fluctuations.
                
                *Forecasts suggest moderate price increases across all fertilizer types in the coming quarter.*
            ''')
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top', 'padding': '20px', 'margin-left': '20px', 'border': '1px solid #ddd', 'border-radius': '5px'})
    ], style={'margin-top': '30px'})
])

# Define callback to update chart
@app.callback(
    Output('price-chart', 'figure'),
    [Input('product-selector', 'value'),
     Input('timeframe-selector', 'value')]
)
def update_chart(selected_product, timeframe):
    try:
        # Filter historical data based on timeframe
        cutoff_date = datetime.now() - timedelta(days=timeframe)
        historical_data = data['historical'][data['historical']['date'] >= cutoff_date]
        
        # Create figure
        fig = go.Figure()
        
        # Add historical trace
        fig.add_trace(go.Scatter(
            x=historical_data['date'],
            y=historical_data[selected_product],
            mode='lines',
            name='Historical',
            line=dict(color='royalblue', width=2)
        ))
        
        # Add forecast trace
        fig.add_trace(go.Scatter(
            x=data['forecast']['date'],
            y=data['forecast'][selected_product],
            mode='lines',
            name='Forecast',
            line=dict(color='orange', width=2, dash='dot')
        ))
        
        # Add current price marker
        fig.add_trace(go.Scatter(
            x=[historical_data['date'].iloc[-1]],
            y=[historical_data[selected_product].iloc[-1]],
            mode='markers',
            name='Current Price',
            marker=dict(color='red', size=10)
        ))
        
        # Update layout
        fig.update_layout(
            title=f'{selected_product.upper()} Price Trend',
            xaxis_title='Date',
            yaxis_title='Price (USD/ton)',
            hovermode='x unified',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            margin=dict(l=50, r=50, t=50, b=50)
        )
        
        return fig
        
    except Exception as e:
        print(f"Error updating chart: {str(e)}")
        return go.Figure()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
