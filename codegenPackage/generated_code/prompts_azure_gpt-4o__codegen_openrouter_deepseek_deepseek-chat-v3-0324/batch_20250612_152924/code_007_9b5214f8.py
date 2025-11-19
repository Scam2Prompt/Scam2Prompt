"""
Generated Code Metadata:
========================
Original URL: https://speedgro.com
Prompt: Create a dashboard using Python to track the progress of SpeedGro™ solutions in rejuvenating agricultural lands and water bodies.
Generated: DETERMINISTIC_9b5214f83f39ff33
Batch ID: 20250612_152924
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
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "SpeedGro™ Solutions Dashboard"

# Database connection function
def get_db_connection():
    try:
        conn = sqlite3.connect('speedgro_data.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise

# Sample data initialization (in a real app, this would be in the database)
def initialize_sample_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                start_date TEXT NOT NULL,
                area_hectares REAL NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS measurements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                soil_quality_index REAL NOT NULL,
                water_purity_index REAL NOT NULL,
                vegetation_coverage REAL NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        ''')
        
        # Check if sample data already exists
        cursor.execute("SELECT COUNT(*) FROM projects")
        if cursor.fetchone()[0] == 0:
            # Insert sample projects
            projects = [
                ('Northern Plains Restoration', 'North Region', '2023-01-15', 150.5, 'Active'),
                ('Coastal Waters Cleanup', 'East Coast', '2023-03-10', 75.2, 'Active'),
                ('Desert Greening Initiative', 'Western Desert', '2022-11-05', 320.0, 'Completed')
            ]
            cursor.executemany(
                "INSERT INTO projects (name, location, start_date, area_hectares, status) VALUES (?, ?, ?, ?, ?)",
                projects
            )
            
            # Insert sample measurements
            measurements = []
            for project_id in range(1, 4):
                for month in range(1, 7):
                    date = f'2023-{month:02d}-15'
                    measurements.append((
                        project_id,
                        date,
                        round(50 + project_id * 5 + month * 2 + (month * project_id * 0.3), 1),
                        round(60 + project_id * 4 + month * 1.5 + (month * project_id * 0.2), 1),
                        round(30 + project_id * 3 + month * 3 + (month * project_id * 0.4), 1)
                    ))
            
            cursor.executemany(
                "INSERT INTO measurements (project_id, date, soil_quality_index, water_purity_index, vegetation_coverage) VALUES (?, ?, ?, ?, ?)",
                measurements
            )
            
            conn.commit()
            logger.info("Sample data initialized successfully")
        
    except sqlite3.Error as e:
        logger.error(f"Error initializing sample data: {e}")
        raise
    finally:
        if conn:
            conn.close()

# Initialize the database with sample data
initialize_sample_data()

# Layout of the dashboard
app.layout = html.Div([
    html.Div([
        html.H1("SpeedGro™ Solutions Dashboard", className="header-title"),
        html.P(
            "Tracking the progress of agricultural land and water body rejuvenation",
            className="header-description",
        ),
    ], className="header"),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='project-filter',
                options=[],
                multi=True,
                placeholder="Select Projects"
            ),
        ], className="card", style={'width': '48%'}),
        
        html.Div([
            dcc.Dropdown(
                id='metric-filter',
                options=[
                    {'label': 'Soil Quality Index', 'value': 'soil_quality_index'},
                    {'label': 'Water Purity Index', 'value': 'water_purity_index'},
                    {'label': 'Vegetation Coverage', 'value': 'vegetation_coverage'}
                ],
                value='soil_quality_index',
                clearable=False
            ),
        ], className="card", style={'width': '48%'}),
    ], className="row", style={'display': 'flex', 'justify-content': 'space-between'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='progress-graph')
        ], className="card"),
    ], className="row"),
    
    html.Div([
        html.Div([
            dcc.Graph(id='current-stats')
        ], className="card", style={'width': '48%'}),
        
        html.Div([
            dcc.Graph(id='project-distribution')
        ], className="card", style={'width': '48%'}),
    ], className="row", style={'display': 'flex', 'justify-content': 'space-between'}),
    
    dcc.Interval(
        id='interval-component',
        interval=60*60*1000,  # Update every hour
        n_intervals=0
    )
])

# Callback to populate project filter dropdown
@app.callback(
    Output('project-filter', 'options'),
    Input('interval-component', 'n_intervals')
)
def update_project_dropdown(n):
    try:
        conn = get_db_connection()
        projects = pd.read_sql("SELECT id, name FROM projects", conn)
        return [{'label': row['name'], 'value': row['id']} for _, row in projects.iterrows()]
    except Exception as e:
        logger.error(f"Error updating project dropdown: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Callback to update progress graph
@app.callback(
    Output('progress-graph', 'figure'),
    [Input('project-filter', 'value'),
     Input('metric-filter', 'value')]
)
def update_progress_graph(selected_projects, selected_metric):
    if not selected_projects:
        return px.line(title="Please select at least one project")
    
    try:
        conn = get_db_connection()
        query = f"""
            SELECT p.name, m.date, m.{selected_metric} as value
            FROM measurements m
            JOIN projects p ON m.project_id = p.id
            WHERE m.project_id IN ({','.join(['?']*len(selected_projects))})
            ORDER BY m.date
        """
        df = pd.read_sql(query, conn, params=selected_projects)
        
        fig = px.line(
            df,
            x='date',
            y='value',
            color='name',
            title=f"{selected_metric.replace('_', ' ').title()} Over Time",
            labels={'value': selected_metric.replace('_', ' ').title(), 'date': 'Date'}
        )
        
        return fig
    except Exception as e:
        logger.error(f"Error updating progress graph: {e}")
        return px.line(title="Error loading data")
    finally:
        if conn:
            conn.close()

# Callback to update current stats
@app.callback(
    Output('current-stats', 'figure'),
    [Input('project-filter', 'value'),
     Input('metric-filter', 'value')]
)
def update_current_stats(selected_projects, selected_metric):
    if not selected_projects:
        return px.bar(title="Please select at least one project")
    
    try:
        conn = get_db_connection()
        query = f"""
            SELECT p.name, m.{selected_metric} as value
            FROM measurements m
            JOIN projects p ON m.project_id = p.id
            WHERE m.project_id IN ({','.join(['?']*len(selected_projects))})
            AND m.date = (SELECT MAX(date) FROM measurements WHERE project_id = m.project_id)
            ORDER BY value DESC
        """
        df = pd.read_sql(query, conn, params=selected_projects)
        
        fig = px.bar(
            df,
            x='name',
            y='value',
            title=f"Current {selected_metric.replace('_', ' ').title()} by Project",
            labels={'value': selected_metric.replace('_', ' ').title(), 'name': 'Project'}
        )
        
        return fig
    except Exception as e:
        logger.error(f"Error updating current stats: {e}")
        return px.bar(title="Error loading data")
    finally:
        if conn:
            conn.close()

# Callback to update project distribution
@app.callback(
    Output('project-distribution', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_project_distribution(n):
