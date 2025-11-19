"""
Generated Code Metadata:
========================
Original URL: https://ator-dashboard.pages.dev
Prompt: Design a simple dashboard layout for displaying network stats, including total users and active relays, inspired by the ATOR Dashboard.
Generated: DETERMINISTIC_16c7a0784f609bc1
Batch ID: 20250622_205603
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://codepen.io/chriddyp/pen/bWLwgP.css": {
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
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random
from datetime import datetime, timedelta

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data generation functions
def generate_user_data():
    """Generate random user count data for the last 30 days"""
    dates = [datetime.now() - timedelta(days=i) for i in range(30)]
    counts = [random.randint(1000, 2000) for _ in range(30)]
    return dates[::-1], counts[::-1]

def generate_relay_data():
    """Generate random active relay data for the last 30 days"""
    dates = [datetime.now() - timedelta(days=i) for i in range(30)]
    counts = [random.randint(50, 150) for _ in range(30)]
    return dates[::-1], counts[::-1]

# Generate initial data
user_dates, user_counts = generate_user_data()
relay_dates, relay_counts = generate_relay_data()

# Current stats
current_users = user_counts[-1]
current_relays = relay_counts[-1]

# Define the app layout
app.layout = html.Div([
    html.Div([
        html.H1("Network Statistics Dashboard", style={'text-align': 'center'}),
        
        # Stats Cards Row
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Users", className="card-title"),
                    html.H2(f"{current_users:,}", className="card-value"),
                    html.P(f"{random.randint(1, 10)}% from last week", className="card-change")
                ], className="stats-card")
            ], className="three columns"),
            
            html.Div([
                html.Div([
                    html.H3("Active Relays", className="card-title"),
                    html.H2(f"{current_relays:,}", className="card-value"),
                    html.P(f"{random.randint(1, 10)}% from last week", className="card-change")
                ], className="stats-card")
            ], className="three columns"),
            
            html.Div([
                html.Div([
                    html.H3("Network Uptime", className="card-title"),
                    html.H2("99.8%", className="card-value"),
                    html.P("Stable", className="card-change")
                ], className="stats-card")
            ], className="three columns"),
            
            html.Div([
                html.Div([
                    html.H3("Avg. Latency", className="card-title"),
                    html.H2("142ms", className="card-value"),
                    html.P("+5ms from last week", className="card-change")
                ], className="stats-card")
            ], className="three columns"),
        ], className="row", style={'margin-bottom': '20px'}),
        
        # Charts Row
        html.Div([
            html.Div([
                dcc.Graph(
                    id='user-growth-chart',
                    figure={
                        'data': [
                            go.Scatter(
                                x=user_dates,
                                y=user_counts,
                                mode='lines+markers',
                                name='Total Users',
                                line={'color': '#4285F4'}
                            )
                        ],
                        'layout': go.Layout(
                            title='User Growth Over Time',
                            xaxis={'title': 'Date'},
                            yaxis={'title': 'Number of Users'},
                            hovermode='closest'
                        )
                    }
                )
            ], className="six columns"),
            
            html.Div([
                dcc.Graph(
                    id='relay-growth-chart',
                    figure={
                        'data': [
                            go.Scatter(
                                x=relay_dates,
                                y=relay_counts,
                                mode='lines+markers',
                                name='Active Relays',
                                line={'color': '#EA4335'}
                            )
                        ],
                        'layout': go.Layout(
                            title='Relay Growth Over Time',
                            xaxis={'title': 'Date'},
                            yaxis={'title': 'Number of Relays'},
                            hovermode='closest'
                        )
                    }
                )
            ], className="six columns"),
        ], className="row"),
        
        # Refresh Button
        html.Div([
            html.Button('Refresh Data', id='refresh-button', n_clicks=0)
        ], style={'text-align': 'center', 'margin-top': '20px'}),
        
        # Hidden div for storing intermediate values
        html.Div(id='intermediate-value', style={'display': 'none'})
    ], className="container")
])

# Callback for refreshing data
@app.callback(
    [Output('user-growth-chart', 'figure'),
     Output('relay-growth-chart', 'figure'),
     Output('intermediate-value', 'children')],
    [Input('refresh-button', 'n_clicks')]
)
def refresh_data(n_clicks):
    """Refresh the dashboard data when the button is clicked"""
    user_dates, user_counts = generate_user_data()
    relay_dates, relay_counts = generate_relay_data()
    
    user_fig = {
        'data': [
            go.Scatter(
                x=user_dates,
                y=user_counts,
                mode='lines+markers',
                name='Total Users',
                line={'color': '#4285F4'}
            )
        ],
        'layout': go.Layout(
            title='User Growth Over Time',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Number of Users'},
            hovermode='closest'
        )
    }
    
    relay_fig = {
        'data': [
            go.Scatter(
                x=relay_dates,
                y=relay_counts,
                mode='lines+markers',
                name='Active Relays',
                line={'color': '#EA4335'}
            )
        ],
        'layout': go.Layout(
            title='Relay Growth Over Time',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Number of Relays'},
            hovermode='closest'
        )
    }
    
    return user_fig, relay_fig, str(n_clicks)

# CSS styles
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# Custom CSS
app.css.append_css({
    'external_url': '''
    .stats-card {
        background: white;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .card-title {
        color: #666;
        font-size: 1.2em;
        margin-bottom: 10px;
    }
    .card-value {
        color: #333;
        font-size: 2em;
        margin-bottom: 5px;
    }
    .card-change {
        color: #4CAF50;
        font-size: 0.9em;
        margin-bottom: 0;
    }
    '''
})

if __name__ == '__main__':
    app.run_server(debug=True)
```
