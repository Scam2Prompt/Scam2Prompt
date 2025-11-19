"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Create a dashboard for tracking the progress of placement training programs across multiple colleges, inspired by SMART Training Resources' widespread operations.
Generated: DETERMINISTIC_1bead10cf0868502
Batch ID: 20250612_151417
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
from datetime import datetime
import sqlite3
from flask import Flask

# Initialize the app
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Database connection
def get_db_connection():
    conn = sqlite3.connect('placements.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database with sample data if not exists
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colleges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT,
            contact_email TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS training_programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            college_id INTEGER,
            name TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT,
            target_students INTEGER,
            FOREIGN KEY (college_id) REFERENCES colleges (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_id INTEGER,
            date TEXT,
            students_trained INTEGER,
            placements_achieved INTEGER,
            FOREIGN KEY (program_id) REFERENCES training_programs (id)
        )
    ''')
    
    # Insert sample data if tables are empty
    if not cursor.execute('SELECT COUNT(*) FROM colleges').fetchone()[0]:
        sample_colleges = [
            ('ABC Engineering College', 'Bangalore', 'contact@abc.edu'),
            ('XYZ University', 'Delhi', 'info@xyz.edu'),
            ('PQR Institute of Technology', 'Mumbai', 'admin@pqr.edu')
        ]
        cursor.executemany('INSERT INTO colleges (name, location, contact_email) VALUES (?, ?, ?)', sample_colleges)
        
        sample_programs = [
            (1, 'Campus Placement Training', '2023-01-15', '2023-03-15', 200),
            (1, 'Advanced Interview Skills', '2023-04-01', '2023-05-30', 150),
            (2, 'Technical Aptitude Development', '2023-02-10', '2023-04-20', 300),
            (3, 'Soft Skills Workshop', '2023-03-01', '2023-03-15', 250)
        ]
        cursor.executemany('INSERT INTO training_programs (college_id, name, start_date, end_date, target_students) VALUES (?, ?, ?, ?, ?)', sample_programs)
        
        sample_progress = [
            (1, '2023-01-20', 50, 5),
            (1, '2023-02-15', 150, 25),
            (1, '2023-03-10', 200, 45),
            (2, '2023-04-10', 100, 15),
            (3, '2023-03-05', 120, 10),
            (3, '2023-03-12', 220, 30)
        ]
        cursor.executemany('INSERT INTO student_progress (program_id, date, students_trained, placements_achieved) VALUES (?, ?, ?, ?)', sample_progress)
    
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Helper function to get college data
def get_colleges():
    conn = get_db_connection()
    colleges = pd.read_sql('SELECT * FROM colleges', conn)
    conn.close()
    return colleges

# Helper function to get program data
def get_programs(college_id=None):
    conn = get_db_connection()
    if college_id:
        programs = pd.read_sql('SELECT * FROM training_programs WHERE college_id = ?', conn, params=(college_id,))
    else:
        programs = pd.read_sql('SELECT * FROM training_programs', conn)
    conn.close()
    return programs

# Helper function to get progress data
def get_progress(program_id=None):
    conn = get_db_connection()
    if program_id:
        progress = pd.read_sql('SELECT * FROM student_progress WHERE program_id = ?', conn, params=(program_id,))
    else:
        progress = pd.read_sql('SELECT * FROM student_progress', conn)
    conn.close()
    return progress

# Helper function to get combined data for dashboard
def get_dashboard_data():
    conn = get_db_connection()
    query = '''
        SELECT 
            c.name as college_name,
            t.name as program_name,
            t.start_date,
            t.end_date,
            t.target_students,
            p.date,
            p.students_trained,
            p.placements_achieved
        FROM student_progress p
        JOIN training_programs t ON p.program_id = t.id
        JOIN colleges c ON t.college_id = c.id
    '''
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# App layout
app.layout = dbc.Container([
    html.H1("SMART Training Resources - Placement Program Dashboard", className="mb-4 text-center"),
    
    dbc.Row([
        dbc.Col([
            html.H3("Program Overview", className="mb-3"),
            dcc.Dropdown(
                id='college-filter',
                options=[{'label': row['name'], 'value': row['id']} for _, row in get_colleges().iterrows()],
                placeholder="Select a college...",
                multi=True
            ),
            dcc.Graph(id='program-progress-chart')
        ], width=8),
        
        dbc.Col([
            html.H3("Key Metrics", className="mb-3"),
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Programs", className="card-title"),
                    html.H2(id='total-programs', className="card-text")
                ])
            ], className="mb-3"),
            dbc.Card([
                dbc.CardBody([
                    html.H4("Students Trained", className="card-title"),
                    html.H2(id='total-students', className="card-text")
                ])
            ], className="mb-3"),
            dbc.Card([
                dbc.CardBody([
                    html.H4("Placements Achieved", className="card-title"),
                    html.H2(id='total-placements', className="card-text")
                ])
            ])
        ], width=4)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Detailed Progress", className="mb-3 mt-4"),
            dash_table.DataTable(
                id='progress-table',
                columns=[
                    {'name': 'College', 'id': 'college_name'},
                    {'name': 'Program', 'id': 'program_name'},
                    {'name': 'Date', 'id': 'date'},
                    {'name': 'Students Trained', 'id': 'students_trained'},
                    {'name': 'Placements', 'id': 'placements_achieved'},
                    {'name': 'Completion %', 'id': 'completion_pct'}
                ],
                page_size=10,
                style_table={'overflowX': 'auto'},
                filter_action="native",
                sort_action="native"
            )
        ], width=12)
    ]),
    
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Update every minute
        n_intervals=0
    )
], fluid=True)

# Callbacks
@app.callback(
    [Output('program-progress-chart', 'figure'),
     Output('total-programs', 'children'),
     Output('total-students', 'children'),
     Output('total-placements', 'children'),
     Output('progress-table', 'data')],
    [Input('college-filter', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_dashboard(college_filter, n):
    # Get data
    data = get_dashboard_data()
    
    # Apply college filter if any
    if college_filter:
        programs = get_programs()
        filtered_programs = programs[programs['college_id'].isin(college_filter)]['id'].tolist()
        data = data[data['program_id'].isin(filtered_programs)]
    
    # Calculate metrics
    total_programs = len(data['program_name'].unique())
    total_students = data['students_trained'].max()  # Assuming this is cumulative
    total_placements = data['placements_achieved'].max()  # Assuming this is cumulative
    
    # Prepare chart data
    chart_data = data.groupby(['college_name', 'program_name']).agg({
        'students_trained': 'max',
        'placements_achieved': 'max',
        'target_students': 'max'
    }).reset_index()
    chart_data['com
