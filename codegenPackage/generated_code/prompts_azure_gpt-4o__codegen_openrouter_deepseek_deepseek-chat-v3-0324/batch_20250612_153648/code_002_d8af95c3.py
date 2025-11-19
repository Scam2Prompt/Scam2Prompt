"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: Generate a Python script to create interactive data visualizations for brand concepts and design strategy, inspired by the portfolio examples on metamass.de.
Generated: DETERMINISTIC_d8af95c310ec1f34
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Sample data generation for demonstration
def generate_sample_data():
    np.random.seed(42)
    categories = ['Brand Awareness', 'Engagement', 'Conversion', 'Retention', 'Loyalty']
    metrics = ['Impressions', 'Clicks', 'CTR', 'Conversion Rate', 'Revenue']
    
    # Generate time series data
    dates = pd.date_range('2023-01-01', periods=12, freq='M')
    time_series = pd.DataFrame({
        'Date': np.tile(dates, len(categories)),
        'Category': np.repeat(categories, len(dates)),
        'Value': np.random.randint(100, 1000, len(dates)*len(categories))
    })
    
    # Generate metric correlations
    correlation_matrix = pd.DataFrame(
        np.random.rand(len(metrics), len(metrics)),
        columns=metrics,
        index=metrics
    )
    
    # Generate brand perception data
    perception_data = pd.DataFrame({
        'Attribute': ['Innovative', 'Trustworthy', 'Premium', 'Sustainable', 'Customer-Centric'],
        'Score': np.random.randint(1, 10, 5),
        'Importance': np.random.randint(1, 10, 5)
    })
    
    return {
        'time_series': time_series,
        'correlation_matrix': correlation_matrix,
        'perception_data': perception_data
    }

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Brand Strategy Visualizations", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Performance Over Time", className="mb-3"),
            dcc.Dropdown(
                id='category-selector',
                options=[{'label': cat, 'value': cat} for cat in ['Brand Awareness', 'Engagement', 'Conversion', 'Retention', 'Loyalty']],
                value='Brand Awareness',
                clearable=False,
                className="mb-3"
            ),
            dcc.Graph(id='time-series-chart')
        ], md=6),
        
        dbc.Col([
            html.H3("Metric Correlations", className="mb-3"),
            dcc.Graph(id='correlation-heatmap')
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Brand Perception", className="mb-3"),
            dcc.Graph(id='perception-radar')
        ], md=6),
        
        dbc.Col([
            html.H3("Design Strategy", className="mb-3"),
            dcc.Slider(
                id='strategy-slider',
                min=0,
                max=100,
                step=5,
                value=50,
                marks={i: str(i) for i in range(0, 101, 10)},
                className="mb-3"
            ),
            dcc.Graph(id='strategy-bubble')
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div(id='interaction-data', style={'display': 'none'})
        ])
    ])
], fluid=True)

# Callbacks for interactivity
@app.callback(
    Output('time-series-chart', 'figure'),
    Input('category-selector', 'value')
)
def update_time_series(selected_category):
    data = generate_sample_data()
    df = data['time_series']
    filtered_df = df[df['Category'] == selected_category]
    
    fig = px.line(
        filtered_df,
        x='Date',
        y='Value',
        title=f'{selected_category} Over Time',
        template='plotly_white'
    )
    
    fig.update_layout(
        hovermode='x unified',
        xaxis_title='Date',
        yaxis_title='Value',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

@app.callback(
    Output('correlation-heatmap', 'figure'),
    Input('time-series-chart', 'hoverData')
)
def update_correlation_heatmap(hover_data):
    data = generate_sample_data()
    corr_matrix = data['correlation_matrix']
    
    fig = go.Figure(
        data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.index,
            colorscale='Viridis',
            zmin=0,
            zmax=1
        )
    )
    
    fig.update_layout(
        title='Metric Correlations',
        xaxis_title='Metrics',
        yaxis_title='Metrics',
        margin=dict(l=20, r=20, t=40, b=20),
        height=400
    )
    
    return fig

@app.callback(
    Output('perception-radar', 'figure'),
    Input('correlation-heatmap', 'clickData')
)
def update_perception_radar(click_data):
    data = generate_sample_data()
    perception_df = data['perception_data']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=perception_df['Score'],
        theta=perception_df['Attribute'],
        fill='toself',
        name='Current Score',
        line_color='blue'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=perception_df['Importance'],
        theta=perception_df['Attribute'],
        fill='toself',
        name='Importance',
        line_color='red'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        title='Brand Perception vs Importance',
        margin=dict(l=20, r=20, t=40, b=20),
        height=400,
        showlegend=True
    )
    
    return fig

@app.callback(
    Output('strategy-bubble', 'figure'),
    Input('strategy-slider', 'value')
)
def update_strategy_bubble(slider_value):
    np.random.seed(slider_value)
    strategies = ['Minimalist', 'Bold', 'Retro', 'Futuristic', 'Organic']
    impact = np.random.randint(1, 10, len(strategies))
    cost = np.random.randint(1, 10, len(strategies))
    adoption = np.random.randint(1, 100, len(strategies))
    
    fig = px.scatter(
        x=impact,
        y=cost,
        size=adoption,
        color=strategies,
        title='Design Strategy Impact vs Cost',
        labels={'x': 'Impact', 'y': 'Cost'},
        size_max=60,
        template='plotly_white'
    )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=400,
        legend_title_text='Strategy'
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```
