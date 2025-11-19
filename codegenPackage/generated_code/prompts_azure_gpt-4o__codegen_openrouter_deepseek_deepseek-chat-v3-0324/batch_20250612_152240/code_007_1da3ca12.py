"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Provide code for a reporting dashboard that visualizes RM’s impact metrics, such as the number of lives impacted, food packs distributed, and scholarships awarded.
Generated: DETERMINISTIC_1da3ca128bc0e0eb
Batch ID: 20250612_152240
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

# Sample data for visualization
data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Lives Impacted": [1000, 2500, 5000, 7500, 10000],
    "Food Packs Distributed": [500, 1500, 3000, 6000, 9000],
    "Scholarships Awarded": [10, 25, 50, 75, 100]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("RM Impact Metrics Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': 'Lives Impacted', 'value': 'Lives Impacted'},
                    {'label': 'Food Packs Distributed', 'value': 'Food Packs Distributed'},
                    {'label': 'Scholarships Awarded', 'value': 'Scholarships Awarded'}
                ],
                value='Lives Impacted',
                clearable=False
            ),
            dcc.Graph(id='impact-graph')
        ], width=12, md=6),
        
        dbc.Col([
            dcc.Graph(
                id='all-metrics',
                figure=px.bar(
                    df,
                    x='Year',
                    y=['Lives Impacted', 'Food Packs Distributed', 'Scholarships Awarded'],
                    barmode='group',
                    title='All Impact Metrics Over Time'
                )
            )
        ], width=12, md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='pie-chart',
                figure=px.pie(
                    df,
                    values='Lives Impacted',
                    names='Year',
                    title='Percentage of Lives Impacted by Year'
                )
            )
        ], width=12, md=6),
        
        dbc.Col([
            html.Div([
                html.H3("Summary Statistics", className="text-center"),
                html.Div(id='summary-stats', className="mt-3 p-3 bg-light rounded")
            ])
        ], width=12, md=6)
    ])
], fluid=True)

# Callback for updating the line graph based on dropdown selection
@app.callback(
    Output('impact-graph', 'figure'),
    Input('metric-dropdown', 'value')
)
def update_graph(selected_metric):
    fig = px.line(
        df,
        x='Year',
        y=selected_metric,
        title=f'{selected_metric} Over Time',
        markers=True
    )
    fig.update_traces(line=dict(width=4))
    return fig

# Callback for updating summary statistics
@app.callback(
    Output('summary-stats', 'children'),
    Input('metric-dropdown', 'value')
)
def update_stats(selected_metric):
    total = df[selected_metric].sum()
    avg = df[selected_metric].mean()
    max_val = df[selected_metric].max()
    max_year = df.loc[df[selected_metric] == max_val, 'Year'].values[0]
    
    return [
        html.P(f"Total {selected_metric}: {total:,}"),
        html.P(f"Average per year: {avg:,.1f}"),
        html.P(f"Highest in {max_year}: {max_val:,}")
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
```
