"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Create a data visualization dashboard to showcase the impact of the organization's programs, such as the number of beneficiaries, partnerships, and initiatives.
Generated: DETERMINISTIC_56414252a65d0a5f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

# Sample data (in production, this would come from a database or API)
data = {
    "Program": ["Education", "Healthcare", "Environment", "Livelihood"],
    "Beneficiaries": [5000, 3000, 2000, 4000],
    "Partnerships": [15, 10, 8, 12],
    "Initiatives": [20, 15, 10, 18],
    "Year": [2023, 2023, 2023, 2023]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Organization Program Impact Dashboard"), className="mb-4 text-center")
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label("Select Metric:"),
            dcc.Dropdown(
                id='metric-selector',
                options=[
                    {'label': 'Beneficiaries', 'value': 'Beneficiaries'},
                    {'label': 'Partnerships', 'value': 'Partnerships'},
                    {'label': 'Initiatives', 'value': 'Initiatives'}
                ],
                value='Beneficiaries',
                clearable=False
            )
        ], width=4)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='bar-chart'), width=6),
        dbc.Col(dcc.Graph(id='pie-chart'), width=6)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='trend-chart'), width=12)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='summary-stats'), className="mt-4")
    ])
], fluid=True)

# Callback for updating charts based on selected metric
@callback(
    [Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure'),
     Output('trend-chart', 'figure'),
     Output('summary-stats', 'children')],
    [Input('metric-selector', 'value')]
)
def update_charts(selected_metric):
    try:
        # Bar chart
        bar_fig = px.bar(
            df, 
            x='Program', 
            y=selected_metric,
            title=f'{selected_metric} by Program',
            color='Program',
            text=selected_metric
        )
        bar_fig.update_layout(transition_duration=500)
        
        # Pie chart
        pie_fig = px.pie(
            df,
            names='Program',
            values=selected_metric,
            title=f'Distribution of {selected_metric}'
        )
        
        # Trend chart (using sample multi-year data)
        trend_data = df.copy()
        trend_data['Year'] = [2021, 2021, 2021, 2021]
        trend_data[selected_metric] = [val * 0.6 for val in trend_data[selected_metric]]
        trend_df = pd.concat([df, trend_data])
        
        trend_fig = px.line(
            trend_df,
            x='Year',
            y=selected_metric,
            color='Program',
            title=f'{selected_metric} Trend Over Years',
            markers=True
        )
        
        # Summary statistics
        total = df[selected_metric].sum()
        avg = df[selected_metric].mean()
        max_program = df.loc[df[selected_metric].idxmax(), 'Program']
        
        stats = [
            html.H4("Summary Statistics"),
            html.P(f"Total {selected_metric}: {total:,}"),
            html.P(f"Average per program: {avg:,.1f}"),
            html.P(f"Program with highest {selected_metric}: {max_program}")
        ]
        
        return bar_fig, pie_fig, trend_fig, stats
    
    except Exception as e:
        # Error handling
        error_msg = html.Div([
            html.H4("An error occurred while processing the data"),
            html.P(str(e))
        ], className="alert alert-danger")
        
        empty_fig = go.Figure()
        empty_fig.update_layout(title="Error loading data")
        
        return empty_fig, empty_fig, empty_fig, error_msg

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
