"""
Generated Code Metadata:
========================
Original URL: https://brettsol.io
Prompt: Write a code snippet to create a simple cloud monitoring dashboard using ServerStatus, including metrics for CPU, memory, and network usage.
Generated: DETERMINISTIC_71a04c261d8a9201
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import psutil
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Server Status Dashboard", style={'textAlign': 'center'}),
    
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    ),
    
    html.Div([
        html.Div([
            dcc.Graph(id='cpu-usage-graph'),
        ], className="six columns"),
        
        html.Div([
            dcc.Graph(id='memory-usage-graph'),
        ], className="six columns"),
    ], className="row"),
    
    html.Div([
        dcc.Graph(id='network-usage-graph'),
    ], className="row"),
])

# Callback for CPU usage
@app.callback(
    Output('cpu-usage-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_cpu_usage(n):
    cpu_percent = psutil.cpu_percent(interval=1)
    
    figure = {
        'data': [go.Indicator(
            mode="gauge+number",
            value=cpu_percent,
            title={'text': "CPU Usage (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 50], 'color': "lightgreen"},
                    {'range': [50, 80], 'color': "orange"},
                    {'range': [80, 100], 'color': "red"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        )],
        'layout': go.Layout(
            margin={'l': 40, 'r': 40, 't': 40, 'b': 40}
        )
    }
    return figure

# Callback for memory usage
@app.callback(
    Output('memory-usage-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_memory_usage(n):
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    
    figure = {
        'data': [go.Indicator(
            mode="gauge+number",
            value=mem_percent,
            title={'text': "Memory Usage (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 50], 'color': "lightgreen"},
                    {'range': [50, 80], 'color': "orange"},
                    {'range': [80, 100], 'color': "red"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        )],
        'layout': go.Layout(
            margin={'l': 40, 'r': 40, 't': 40, 'b': 40}
        )
    }
    return figure

# Callback for network usage
@app.callback(
    Output('network-usage-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_network_usage(n):
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent / (1024 * 1024)  # Convert to MB
    bytes_recv = net_io.bytes_recv / (1024 * 1024)  # Convert to MB
    
    figure = {
        'data': [
            go.Bar(
                name='Sent',
                x=['Network Usage'],
                y=[bytes_sent],
                marker_color='indianred'
            ),
            go.Bar(
                name='Received',
                x=['Network Usage'],
                y=[bytes_recv],
                marker_color='lightsalmon'
            )
        ],
        'layout': go.Layout(
            title='Network Traffic (MB)',
            barmode='group',
            margin={'l': 40, 'r': 40, 't': 40, 'b': 40}
        )
    }
    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
