"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: "Generate a Python code snippet to create an interactive COVID-19 case trend chart using a library like Plotly, with a similar layout to the one showing exponential growth as a straight line."
Generated: DETERMINISTIC_01fcaef6f1d688ee
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample COVID-19 data (in production, replace with real API/data source)
def get_covid_data():
    return pd.DataFrame({
        'date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
        'cases': [2**i for i in range(1, 101)],  # Exponential growth for demo
        'log_cases': [i for i in range(1, 101)]  # Linear in log scale
    })

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("COVID-19 Case Trend Analysis", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='scale-selector',
        options=[
            {'label': 'Linear Scale', 'value': 'linear'},
            {'label': 'Logarithmic Scale', 'value': 'log'}
        ],
        value='log',
        style={'width': '50%', 'margin': '0 auto'}
    ),
    dcc.Graph(id='covid-trend-chart'),
    html.Div(id='hover-info', style={'textAlign': 'center', 'marginTop': 20})
])

# Callback to update chart based on scale selection
@app.callback(
    [Output('covid-trend-chart', 'figure'),
     Output('hover-info', 'children')],
    [Input('scale-selector', 'value')]
)
def update_chart(scale_type):
    df = get_covid_data()
    
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add traces
    fig.add_trace(
        go.Scatter(
            x=df['date'],
            y=df['cases'],
            name='Daily Cases',
            mode='lines+markers',
            line=dict(color='royalblue', width=2)
        ),
        secondary_y=False
    )
    
    # Configure axes
    fig.update_xaxes(title_text="Date")
    
    if scale_type == 'log':
        fig.update_yaxes(
            title_text="Cases (Log Scale)",
            type='log',
            secondary_y=False
        )
        hover_text = "Note: Exponential growth appears linear on log scale"
    else:
        fig.update_yaxes(
            title_text="Cases (Linear Scale)",
            type='linear',
            secondary_y=False
        )
        hover_text = "Note: Exponential growth curve is visible on linear scale"
    
    # Update layout
    fig.update_layout(
        title="COVID-19 Case Growth Trend",
        hovermode='x unified',
        template='plotly_white',
        height=600
    )
    
    return fig, hover_text

if __name__ == '__main__':
    app.run_server(debug=True)
```
