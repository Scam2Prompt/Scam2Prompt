"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Generate code for a dashboard to monitor the progress of engineering projects, emphasizing quality and continuous improvement as outlined by SET Ingeniería.
Generated: DETERMINISTIC_d4458d637905595e
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dashboard.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

# Initialize the Dash application
app = dash.Dash(__name__)

# Sample data for demonstration purposes
# In a real application, this data would likely come from a database
data = {
    'Project': ['Project A', 'Project B', 'Project C', 'Project A', 'Project B', 'Project C'],
    'Phase': ['Design', 'Design', 'Design', 'Implementation', 'Implementation', 'Implementation'],
    'Status': ['In Progress', 'Completed', 'In Progress', 'In Progress', 'Completed', 'In Progress'],
    'Quality Rating': [8, 9, 7, 8, 9, 7],
    'Improvement Actions': [2, 1, 3, 2, 1, 3]
}

df = pd.DataFrame(data)

# Define the layout of the application
app.layout = html.Div([
    html.H1('Engineering Projects Dashboard'),
    html.Hr(),
    
    # Project selection dropdown
    html.Div([
        html.Label('Select Project:'),
        dcc.Dropdown(
            id='project-dropdown',
            options=[{'label': project, 'value': project} for project in df['Project'].unique()],
            value=df['Project'].unique()[0]
        )
    ]),
    
    # Phase selection dropdown
    html.Div([
        html.Label('Select Phase:'),
        dcc.Dropdown(
            id='phase-dropdown',
            options=[{'label': phase, 'value': phase} for phase in df['Phase'].unique()],
            value=df['Phase'].unique()[0]
        )
    ]),
    
    # Status metrics
    html.Div([
        html.H2('Status Metrics'),
        html.Div(id='status-metrics')
    ]),
    
    # Quality and improvement metrics
    html.Div([
        html.H2('Quality and Improvement Metrics'),
        html.Div(id='quality-metrics')
    ]),
    
    # Bar chart for quality ratings
    html.Div([
        dcc.Graph(id='quality-graph')
    ]),
    
    # Bar chart for improvement actions
    html.Div([
        dcc.Graph(id='improvement-graph')
    ])
])

# Update status metrics based on project and phase selection
@app.callback(
    Output('status-metrics', 'children'),
    [Input('project-dropdown', 'value'),
     Input('phase-dropdown', 'value')]
)
def update_status_metrics(project, phase):
    filtered_df = df[(df['Project'] == project) & (df['Phase'] == phase)]
    if filtered_df.empty:
        raise PreventUpdate
    status_counts = filtered_df['Status'].value_counts().to_dict()
    return html.Div([
        html.P(f'In Progress: {status_counts.get("In Progress", 0)}'),
        html.P(f'Completed: {status_counts.get("Completed", 0)}')
    ])

# Update quality and improvement metrics based on project and phase selection
@app.callback(
    Output('quality-metrics', 'children'),
    [Input('project-dropdown', 'value'),
     Input('phase-dropdown', 'value')]
)
def update_quality_metrics(project, phase):
    filtered_df = df[(df['Project'] == project) & (df['Phase'] == phase)]
    if filtered_df.empty:
        raise PreventUpdate
    avg_quality_rating = filtered_df['Quality Rating'].mean()
    avg_improvement_actions = filtered_df['Improvement Actions'].mean()
    return html.Div([
        html.P(f'Average Quality Rating: {avg_quality_rating:.2f}'),
        html.P(f'Average Improvement Actions: {avg_improvement_actions:.2f}')
    ])

# Update quality graph based on project selection
@app.callback(
    Output('quality-graph', 'figure'),
    [Input('project-dropdown', 'value')]
)
def update_quality_graph(project):
    filtered_df = df[df['Project'] == project]
    if filtered_df.empty:
        raise PreventUpdate
    fig = px.bar(filtered_df, x='Phase', y='Quality Rating', title='Quality Ratings by Phase')
    return fig

# Update improvement graph based on project selection
@app.callback(
    Output('improvement-graph', 'figure'),
    [Input('project-dropdown', 'value')]
)
def update_improvement_graph(project):
    filtered_df = df[df['Project'] == project]
    if filtered_df.empty:
        raise PreventUpdate
    fig = px.bar(filtered_df, x='Phase', y='Improvement Actions', title='Improvement Actions by Phase')
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```
