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
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import datetime
from flask import Flask

# Initialize the Flask server and Dash app
server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/')

# Sample data for demonstration (in production, this would come from a database)
projects_data = {
    'ProjectID': ['P001', 'P002', 'P003', 'P004'],
    'ProjectName': ['Bridge Construction', 'Software Development', 'Power Plant', 'Water Treatment'],
    'StartDate': ['2023-01-01', '2023-02-15', '2023-03-10', '2023-04-05'],
    'EndDate': ['2023-06-30', '2023-08-20', '2023-11-15', '2023-09-10'],
    'Progress': [75, 50, 30, 90],
    'QualityScore': [88, 92, 85, 95],
    'ContinuousImprovement': [4.2, 4.5, 3.8, 4.7],
    'Status': ['On Track', 'Delayed', 'At Risk', 'Completed']
}

df = pd.DataFrame(projects_data)
df['StartDate'] = pd.to_datetime(df['StartDate'])
df['EndDate'] = pd.to_datetime(df['EndDate'])

# Calculate days remaining for each project
today = datetime.datetime.now()
df['DaysRemaining'] = (df['EndDate'] - today).dt.days

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('SET Ingeniería - Engineering Projects Dashboard', style={'textAlign': 'center'}),
    
    # Project Overview Section
    html.Div([
        html.H2('Project Overview'),
        dcc.Dropdown(
            id='project-filter',
            options=[{'label': project, 'value': project} for project in df['ProjectName']],
            value=df['ProjectName'][0],
            clearable=False
        ),
        html.Div(id='project-details')
    ], style={'padding': '20px', 'margin': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'}),
    
    # Quality and Improvement Metrics
    html.Div([
        html.H2('Quality and Continuous Improvement Metrics'),
        dcc.Graph(id='quality-graph'),
        dcc.Graph(id='improvement-graph')
    ], style={'padding': '20px', 'margin': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'}),
    
    # Progress Tracking
    html.Div([
        html.H2('Progress Tracking'),
        dcc.Graph(
            id='progress-graph',
            figure=px.bar(df, x='ProjectName', y='Progress', title='Project Progress (%)')
        )
    ], style={'padding': '20px', 'margin': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'}),
    
    # Timeline View
    html.Div([
        html.H2('Project Timeline'),
        dcc.Graph(
            id='timeline-graph',
            figure=px.timeline(df, x_start='StartDate', x_end='EndDate', y='ProjectName', color='Status',
                              title='Project Timeline')
        )
    ], style={'padding': '20px', 'margin': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px'}),
    
    # Refresh interval
    dcc.Interval(
        id='interval-component',
        interval=60*60*1000,  # 1 hour in milliseconds
        n_intervals=0
    )
])

# Callback for project details
@app.callback(
    Output('project-details', 'children'),
    [Input('project-filter', 'value')]
)
def update_project_details(selected_project):
    try:
        project = df[df['ProjectName'] == selected_project].iloc[0]
        return html.Div([
            html.H3(f"{project['ProjectName']} (ID: {project['ProjectID']})"),
            html.P(f"Status: {project['Status']}"),
            html.P(f"Progress: {project['Progress']}%"),
            html.P(f"Quality Score: {project['QualityScore']}/100"),
            html.P(f"Continuous Improvement Rating: {project['ContinuousImprovement']}/5"),
            html.P(f"Days Remaining: {project['DaysRemaining']}"),
            html.P(f"Start Date: {project['StartDate'].strftime('%Y-%m-%d')}"),
            html.P(f"End Date: {project['EndDate'].strftime('%Y-%m-%d')}")
        ])
    except Exception as e:
        return html.Div(f"Error loading project details: {str(e)}")

# Callback for quality graph
@app.callback(
    Output('quality-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_quality_graph(n):
    try:
        fig = px.bar(df, x='ProjectName', y='QualityScore', title='Quality Scores by Project')
        fig.update_layout(yaxis_range=[0, 100])
        return fig
    except Exception as e:
        return px.bar(title=f"Error: {str(e)}")

# Callback for improvement graph
@app.callback(
    Output('improvement-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_improvement_graph(n):
    try:
        fig = px.bar(df, x='ProjectName', y='ContinuousImprovement', title='Continuous Improvement Ratings')
        fig.update_layout(yaxis_range=[0, 5])
        return fig
    except Exception as e:
        return px.bar(title=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
