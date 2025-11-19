"""
Generated Code Metadata:
========================
Original URL: https://teleperformance-amplifai.com
Prompt: Create a script to simulate an AI-powered operational efficiency dashboard inspired by AmplifAI's solutions.
Generated: DETERMINISTIC_65cc7f62bca14d03
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "AI-Powered Operational Efficiency Dashboard"

# Sample data generation
def generate_sample_data():
    np.random.seed(42)
    date_range = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')
    teams = ['Team A', 'Team B', 'Team C', 'Team D']
    metrics = ['Productivity', 'Quality', 'Adherence', 'Engagement']
    
    data = []
    for date in date_range:
        for team in teams:
            for metric in metrics:
                value = np.random.normal(loc=80, scale=10)
                value = max(0, min(100, value))  # Ensure value is between 0-100
                data.append({
                    'Date': date,
                    'Team': team,
                    'Metric': metric,
                    'Value': round(value, 2)
                })
    
    return pd.DataFrame(data)

df = generate_sample_data()

# Calculate summary statistics
def calculate_summary(df):
    summary = df.groupby(['Team', 'Metric'])['Value'].agg(['mean', 'std', 'count']).reset_index()
    summary['mean'] = summary['mean'].round(2)
    summary['std'] = summary['std'].round(2)
    return summary

summary_df = calculate_summary(df)

# Generate AI insights
def generate_insights(df):
    insights = []
    
    # Productivity insights
    prod_df = df[df['Metric'] == 'Productivity']
    top_team = prod_df.groupby('Team')['Value'].mean().idxmax()
    bottom_team = prod_df.groupby('Team')['Value'].mean().idxmin()
    insights.append(f"🔹 {top_team} leads in Productivity with {prod_df[prod_df['Team'] == top_team]['Value'].mean():.1f}%")
    insights.append(f"🔹 {bottom_team} needs improvement in Productivity ({prod_df[prod_df['Team'] == bottom_team]['Value'].mean():.1f}%)")
    
    # Quality insights
    qual_df = df[df['Metric'] == 'Quality']
    if qual_df['Value'].mean() < 85:
        insights.append("🔹 Quality scores are below target (85%) across teams")
    
    # Trend analysis
    recent_data = df[df['Date'] > (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')]
    trend = recent_data.groupby('Metric')['Value'].mean().diff().mean()
    if trend > 0:
        insights.append("🔹 Positive trend observed in recent performance")
    elif trend < 0:
        insights.append("🔹 Negative trend detected - review needed")
    
    return insights

insights = generate_insights(df)

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("AI-Powered Operational Efficiency Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Key Metrics", className="text-center"),
                dcc.Dropdown(
                    id='team-selector',
                    options=[{'label': team, 'value': team} for team in df['Team'].unique()],
                    value='Team A',
                    clearable=False
                ),
                dcc.Graph(id='metrics-radar')
            ], className="card p-3 mb-4")
        ], md=6),
        
        dbc.Col([
            html.Div([
                html.H3("Performance Trends", className="text-center"),
                dcc.Dropdown(
                    id='metric-selector',
                    options=[{'label': metric, 'value': metric} for metric in df['Metric'].unique()],
                    value='Productivity',
                    clearable=False
                ),
                dcc.Graph(id='trend-chart')
            ], className="card p-3 mb-4")
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("AI Insights", className="text-center"),
                html.Ul([html.Li(insight) for insight in insights], className="list-unstyled p-3")
            ], className="card p-3 mb-4")
        ], md=6),
        
        dbc.Col([
            html.Div([
                html.H3("Team Comparison", className="text-center"),
                dcc.Dropdown(
                    id='comparison-metric',
                    options=[{'label': metric, 'value': metric} for metric in df['Metric'].unique()],
                    value='Productivity',
                    clearable=False
                ),
                dcc.Graph(id='comparison-chart')
            ], className="card p-3 mb-4")
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Performance Distribution", className="text-center"),
                dcc.Graph(
                    id='distribution-chart',
                    figure=px.box(df, x='Team', y='Value', color='Metric', 
                                title="Performance Distribution by Team and Metric")
                )
            ], className="card p-3")
        ], width=12)
    ])
], fluid=True)

# Callbacks
@app.callback(
    Output('metrics-radar', 'figure'),
    Input('team-selector', 'value')
)
def update_radar_chart(selected_team):
    team_data = df[df['Team'] == selected_team]
    avg_metrics = team_data.groupby('Metric')['Value'].mean().reset_index()
    
    fig = px.line_polar(
        avg_metrics, 
        r='Value', 
        theta='Metric', 
        line_close=True,
        title=f"Performance Metrics for {selected_team}",
        template="plotly_white"
    )
    fig.update_traces(fill='toself')
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])))
    return fig

@app.callback(
    Output('trend-chart', 'figure'),
    Input('metric-selector', 'value')
)
def update_trend_chart(selected_metric):
    metric_data = df[df['Metric'] == selected_metric]
    avg_trend = metric_data.groupby(['Date', 'Team'])['Value'].mean().reset_index()
    
    fig = px.line(
        avg_trend, 
        x='Date', 
        y='Value', 
        color='Team',
        title=f"{selected_metric} Trend Over Time",
        template="plotly_white"
    )
    fig.update_layout(yaxis_range=[0, 100])
    return fig

@app.callback(
    Output('comparison-chart', 'figure'),
    Input('comparison-metric', 'value')
)
def update_comparison_chart(selected_metric):
    metric_data = df[df['Metric'] == selected_metric]
    team_comparison = metric_data.groupby('Team')['Value'].mean().reset_index().sort_values('Value')
    
    fig = px.bar(
        team_comparison, 
        x='Team', 
        y='Value', 
        color='Team',
        title=f"Team Comparison: {selected_metric}",
        text='Value',
        template="plotly_white"
    )
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(yaxis_range=[0, 100], uniformtext_minsize=8, uniformtext_mode='hide')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```
