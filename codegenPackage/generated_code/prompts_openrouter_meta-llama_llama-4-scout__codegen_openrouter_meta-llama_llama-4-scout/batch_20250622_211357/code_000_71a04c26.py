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
# server_status.py

import psutil
import time
import json

class ServerStatus:
    def __init__(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.network_io = {}

    def get_cpu_usage(self):
        """Get current CPU usage"""
        try:
            self.cpu_usage = psutil.cpu_percent()
            return self.cpu_usage
        except Exception as e:
            print(f"Error getting CPU usage: {e}")
            return None

    def get_memory_usage(self):
        """Get current memory usage"""
        try:
            memory = psutil.virtual_memory()
            self.memory_usage = (memory.total - memory.available) / memory.total * 100
            return self.memory_usage
        except Exception as e:
            print(f"Error getting memory usage: {e}")
            return None

    def get_network_io(self):
        """Get current network I/O statistics"""
        try:
            self.network_io = psutil.net_io_counters()
            return self.network_io
        except Exception as e:
            print(f"Error getting network I/O statistics: {e}")
            return None

    def get_server_status(self):
        """Get current server status"""
        status = {
            'cpu_usage': self.get_cpu_usage(),
            'memory_usage': self.get_memory_usage(),
            'network_io': self.get_network_io()
        }
        return status

def main():
    server_status = ServerStatus()
    while True:
        status = server_status.get_server_status()
        print(json.dumps(status, indent=4))
        time.sleep(1)

if __name__ == "__main__":
    main()
```

```python
# server_status_dashboard.py

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import psutil
import time
import json
from server_status import ServerStatus

# Initialize server status
server_status = ServerStatus()

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1('Server Status Dashboard'),
    dcc.Interval(id='interval', interval=1000),  # Update every 1 second
    html.Div([
        html.H2('CPU Usage'),
        html.P(id='cpu-usage')
    ]),
    html.Div([
        html.H2('Memory Usage'),
        html.P(id='memory-usage')
    ]),
    html.Div([
        html.H2('Network I/O'),
        html.P(id='network-io')
    ]),
    dcc.Graph(id='cpu-usage-graph'),
    dcc.Graph(id='memory-usage-graph'),
    dcc.Graph(id='network-io-graph')
])

# Define callback for updating values
@app.callback(
    [Output('cpu-usage', 'children'),
     Output('memory-usage', 'children'),
     Output('network-io', 'children')],
    [Input('interval', 'n_intervals')]
)
def update_values(n):
    cpu_usage = server_status.get_cpu_usage()
    memory_usage = server_status.get_memory_usage()
    network_io = server_status.get_network_io()
    return f'CPU Usage: {cpu_usage}%', f'Memory Usage: {memory_usage}%', f'Network I/O: {network_io}'

# Define callback for updating graphs
@app.callback(
    [Output('cpu-usage-graph', 'figure'),
     Output('memory-usage-graph', 'figure'),
     Output('network-io-graph', 'figure')],
    [Input('interval', 'n_intervals')]
)
def update_graphs(n):
    cpu_usage_history = []
    memory_usage_history = []
    network_io_history = []
    for i in range(10):
        cpu_usage = server_status.get_cpu_usage()
        memory_usage = server_status.get_memory_usage()
        network_io = server_status.get_network_io()
        cpu_usage_history.append(cpu_usage)
        memory_usage_history.append(memory_usage)
        network_io_history.append(network_io.bytes_sent + network_io.bytes_recv)
        time.sleep(0.1)

    df_cpu = pd.DataFrame({'CPU Usage': cpu_usage_history})
    df_memory = pd.DataFrame({'Memory Usage': memory_usage_history})
    df_network = pd.DataFrame({'Network I/O': network_io_history})

    fig_cpu = px.line(df_cpu, title='CPU Usage')
    fig_memory = px.line(df_memory, title='Memory Usage')
    fig_network = px.line(df_network, title='Network I/O')

    return fig_cpu, fig_memory, fig_network

if __name__ == "__main__":
    app.run_server(debug=True)
```
