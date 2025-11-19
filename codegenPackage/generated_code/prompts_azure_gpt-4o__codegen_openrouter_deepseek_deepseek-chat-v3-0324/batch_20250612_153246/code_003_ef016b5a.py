"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Provide an example of a project management dashboard for tracking phases like feasibility, installation, and commissioning, inspired by Jau Consulting's services.
Generated: DETERMINISTIC_ef016b5a306688b8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Sample data for project phases
projects_data = [
    {
        "Project ID": "PRJ-001",
        "Name": "Solar Plant Installation",
        "Client": "Green Energy Corp",
        "Start Date": "2023-01-15",
        "End Date": "2023-06-30",
        "Feasibility": 100,
        "Design": 85,
        "Installation": 60,
        "Commissioning": 20,
        "Status": "In Progress",
        "Manager": "John Doe"
    },
    {
        "Project ID": "PRJ-002",
        "Name": "Wind Farm Construction",
        "Client": "Renewable Power Ltd",
        "Start Date": "2023-03-01",
        "End Date": "2023-09-15",
        "Feasibility": 100,
        "Design": 100,
        "Installation": 45,
        "Commissioning": 5,
        "Status": "In Progress",
        "Manager": "Jane Smith"
    },
    {
        "Project ID": "PRJ-003",
        "Name": "Hydro Plant Upgrade",
        "Client": "Aqua Power Inc",
        "Start Date": "2023-02-10",
        "End Date": "2023-05-25",
        "Feasibility": 100,
        "Design": 100,
        "Installation": 100,
        "Commissioning": 75,
        "Status": "In Progress",
        "Manager": "Mike Johnson"
    }
]

# Convert to DataFrame
df = pd.DataFrame(projects_data)

# Calculate days remaining
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])
df['Days Remaining'] = (df['End Date'] - datetime.now()).dt.days

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Project Management Dashboard"

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Project Management Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    # Summary Cards
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Total Projects"),
                dbc.CardBody([
                    html.H4(len(df), className="card-title")
                ])
            ], className="text-center shadow"), width=3
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("In Progress"),
                dbc.CardBody([
                    html.H4(len(df[df['Status'] == "In Progress"]), className="card-title")
                ])
            ], className="text-center shadow"), width=3
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Avg Completion"),
                dbc.CardBody([
                    html.H4(f"{df[['Feasibility', 'Design', 'Installation', 'Commissioning']].mean().mean():.1f}%", className="card-title")
                ])
            ], className="text-center shadow"), width=3
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("At Risk"),
                dbc.CardBody([
                    html.H4(len(df[df['Days Remaining'] < 30]), className="card-title")
                ])
            ], className="text-center shadow"), width=3
        )
    ], className="mb-4"),
    
    # Project Phases Visualization
    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id='phases-radar',
                figure=px.line_polar(
                    df.melt(id_vars=['Project ID'], 
                           value_vars=['Feasibility', 'Design', 'Installation', 'Commissioning']),
                    r='value', 
                    theta='variable', 
                    color='Project ID',
                    line_close=True,
                    template="plotly_dark",
                    title="Project Phases Completion"
                )
            ), width=6
        ),
        dbc.Col(
            dcc.Graph(
                id='timeline-gantt',
                figure=px.timeline(
                    df, 
                    x_start="Start Date", 
                    x_end="End Date", 
                    y="Name",
                    color="Status",
                    title="Project Timeline"
                ).update_yaxes(categoryorder="total ascending")
            ), width=6
        )
    ], className="mb-4"),
    
    # Project Details Table
    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                id='project-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                filter_action="native",
                sort_action="native",
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'padding': '10px'
                },
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'fontWeight': 'bold'
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    },
                    {
                        'if': {
                            'filter_query': '{Days Remaining} < 30',
                            'column_id': 'Days Remaining'
                        },
                        'backgroundColor': '#FFCCCB',
                        'color': 'black'
                    }
                ]
            ), width=12
        )
    ]),
    
    # Project Phase Details
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='project-selector',
                options=[{'label': proj, 'value': proj} for proj in df['Project ID']],
                value='PRJ-001',
                clearable=False
            ), width=4
        ),
        dbc.Col(
            dcc.Graph(id='phase-progress'), width=8
        )
    ], className="mt-4")
])

# Callback for phase progress bar
@app.callback(
    Output('phase-progress', 'figure'),
    Input('project-selector', 'value')
)
def update_phase_progress(selected_project):
    project_data = df[df['Project ID'] == selected_project].iloc[0]
    phases = ['Feasibility', 'Design', 'Installation', 'Commissioning']
    progress = [project_data[phase] for phase in phases]
    
    fig = px.bar(
        x=phases,
        y=progress,
        text=progress,
        labels={'x': 'Phase', 'y': 'Completion %'},
        title=f"Phase Completion for {project_data['Name']}",
        color=phases,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    fig.update_traces(texttemplate='%{y}%', textposition='outside')
    fig.update_yaxes(range=[0, 100])
    fig.update_layout(showlegend=False)
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```
