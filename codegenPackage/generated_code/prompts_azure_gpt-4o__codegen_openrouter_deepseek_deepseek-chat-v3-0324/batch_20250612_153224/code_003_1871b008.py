"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Suggest tools or frameworks for building a digital marketing campaign dashboard tailored for a branding agency like Naikreatif.
Generated: DETERMINISTIC_1871b008bf6e61dd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Digital Marketing Campaign Dashboard for Branding Agency

# Required libraries and frameworks
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data for demonstration
campaign_data = pd.DataFrame({
    'Campaign': ['Social Media', 'Email', 'PPC', 'Content', 'Influencer'],
    'Impressions': [10000, 8000, 12000, 5000, 15000],
    'Engagement': [1200, 600, 800, 400, 2000],
    'Conversions': [120, 80, 150, 50, 180],
    'ROI': [2.5, 1.8, 3.2, 1.2, 4.0]
})

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Naikreatif Campaign Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='campaign-selector',
                options=[{'label': i, 'value': i} for i in campaign_data['Campaign']],
                value='Social Media',
                clearable=False
            ),
            dcc.Graph(id='performance-graph')
        ], width=6),
        
        dbc.Col([
            dcc.Graph(
                figure=px.pie(
                    campaign_data, 
                    values='Impressions', 
                    names='Campaign', 
                    title='Impressions Distribution'
                )
            )
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                figure=px.bar(
                    campaign_data, 
                    x='Campaign', 
                    y='ROI', 
                    title='ROI by Campaign'
                )
            )
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div(id='campaign-stats', className="mt-4 p-3 bg-light")
        ], width=12)
    ])
], fluid=True)

# Callback for interactive components
@app.callback(
    [Output('performance-graph', 'figure'),
     Output('campaign-stats', 'children')],
    [Input('campaign-selector', 'value')]
)
def update_graph(selected_campaign):
    filtered_data = campaign_data[campaign_data['Campaign'] == selected_campaign]
    
    fig = px.line(
        filtered_data.melt(id_vars='Campaign', var_name='Metric'), 
        x='Metric', 
        y='value', 
        title=f'{selected_campaign} Performance Metrics'
    )
    
    stats = [
        html.H4(f"{selected_campaign} Statistics"),
        html.P(f"Impressions: {filtered_data['Impressions'].values[0]:,}"),
        html.P(f"Engagement: {filtered_data['Engagement'].values[0]:,}"),
        html.P(f"Conversions: {filtered_data['Conversions'].values[0]:,}"),
        html.P(f"ROI: {filtered_data['ROI'].values[0]:.1f}x")
    ]
    
    return fig, stats

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
