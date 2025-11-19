"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Write code to create a dashboard that tracks job application progress, including resume reviews, interview prep sessions, and networking events, as described in Bridges to Professions' career coaching services.
Generated: DETERMINISTIC_ec5d780f6973ca81
Batch ID: 20250612_145444
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
import pandas as pd
import plotly.express as px
from datetime import datetime
import sqlite3
from flask import Flask

# Initialize the app
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Database setup
def init_db():
    conn = sqlite3.connect('job_applications.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        application_date TEXT NOT NULL,
        status TEXT NOT NULL,
        notes TEXT,
        last_updated TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        application_id INTEGER,
        activity_type TEXT NOT NULL,
        activity_date TEXT NOT NULL,
        duration_minutes INTEGER,
        notes TEXT,
        FOREIGN KEY (application_id) REFERENCES applications (id)
    )
    ''')
    
    conn.commit()
    conn.close()

init_db()

# Sample data insertion (for demo purposes)
def insert_sample_data():
    conn = sqlite3.connect('job_applications.db')
    cursor = conn.cursor()
    
    # Check if sample data already exists
    cursor.execute("SELECT COUNT(*) FROM applications")
    if cursor.fetchone()[0] == 0:
        # Insert sample applications
        applications = [
            ("TechCorp", "Software Engineer", "2023-01-15", "Applied", "Waiting for response", datetime.now().isoformat()),
            ("DataSystems", "Data Analyst", "2023-02-01", "Interview Scheduled", "Technical interview next week", datetime.now().isoformat()),
            ("WebSolutions", "Frontend Developer", "2023-01-20", "Offer Received", "Negotiating salary", datetime.now().isoformat())
        ]
        cursor.executemany("INSERT INTO applications (company, position, application_date, status, notes, last_updated) VALUES (?, ?, ?, ?, ?, ?)", applications)
        
        # Insert sample activities
        activities = [
            (1, "Resume Review", "2023-01-10", 60, "Reviewed with career coach"),
            (1, "Networking Event", "2023-01-12", 120, "Met with TechCorp employees"),
            (2, "Interview Prep", "2023-02-05", 90, "Mock technical interview"),
            (3, "Resume Review", "2023-01-18", 45, "Tailored for WebSolutions")
        ]
        cursor.executemany("INSERT INTO activities (application_id, activity_type, activity_date, duration_minutes, notes) VALUES (?, ?, ?, ?, ?)", activities)
        
        conn.commit()
    conn.close()

insert_sample_data()

# Helper functions
def get_applications():
    conn = sqlite3.connect('job_applications.db')
    df = pd.read_sql_query("SELECT * FROM applications", conn)
    conn.close()
    return df

def get_activities():
    conn = sqlite3.connect('job_applications.db')
    df = pd.read_sql_query("SELECT * FROM activities", conn)
    conn.close()
    return df

def get_combined_data():
    applications = get_applications()
    activities = get_activities()
    
    if not applications.empty and not activities.empty:
        combined = pd.merge(activities, applications, left_on='application_id', right_on='id', how='left')
        combined['activity_date'] = pd.to_datetime(combined['activity_date'])
        combined['application_date'] = pd.to_datetime(combined['application_date'])
        return combined
    return pd.DataFrame()

# Layout components
def create_status_pie_chart():
    df = get_applications()
    if not df.empty:
        fig = px.pie(df, names='status', title='Application Status Distribution')
        return dcc.Graph(figure=fig)
    return html.Div("No application data available")

def create_activity_timeline():
    combined = get_combined_data()
    if not combined.empty:
        fig = px.timeline(
            combined,
            x_start="activity_date",
            x_end="activity_date",
            y="company",
            color="activity_type",
            title="Activity Timeline",
            hover_data=["position", "notes"]
        )
        return dcc.Graph(figure=fig)
    return html.Div("No activity data available")

def create_activity_bar_chart():
    combined = get_combined_data()
    if not combined.empty:
        fig = px.bar(
            combined,
            x="activity_type",
            y="duration_minutes",
            color="status",
            title="Time Spent on Activities by Status",
            barmode="group"
        )
        return dcc.Graph(figure=fig)
    return html.Div("No activity data available")

def create_application_table():
    df = get_applications()
    if not df.empty:
        return dash_table.DataTable(
            id='application-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            filter_action="native",
            sort_action="native",
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={
                'textAlign': 'left',
                'minWidth': '100px',
                'width': '150px',
                'maxWidth': '300px',
                'whiteSpace': 'normal'
            }
        )
    return html.Div("No application data available")

# Form components
application_form = dbc.Card(
    dbc.CardBody([
        html.H4("Add New Application", className="card-title"),
        dbc.Form([
            dbc.Row([
                dbc.Col(
                    dbc.Input(id="company-input", placeholder="Company", type="text"),
                    md=6
                ),
                dbc.Col(
                    dbc.Input(id="position-input", placeholder="Position", type="text"),
                    md=6
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dcc.DatePickerSingle(
                        id='application-date-input',
                        date=datetime.now().date(),
                        display_format='YYYY-MM-DD'
                    ),
                    md=6
                ),
                dbc.Col(
                    dbc.Select(
                        id="status-input",
                        options=[
                            {"label": "Researching", "value": "Researching"},
                            {"label": "Applied", "value": "Applied"},
                            {"label": "Interview Scheduled", "value": "Interview Scheduled"},
                            {"label": "Offer Received", "value": "Offer Received"},
                            {"label": "Rejected", "value": "Rejected"}
                        ],
                        value="Applied"
                    ),
                    md=6
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Textarea(id="notes-input", placeholder="Notes"),
                    md=12
                )
            ]),
            dbc.Button("Submit", id="submit-application", color="primary", className="mt-2")
        ])
    ])
)

activity_form = dbc.Card(
    dbc.CardBody([
        html.H4("Log Activity", className="card-title"),
        dbc.Form([
            dbc.Row([
                dbc.Col(
                    dbc.Select(
                        id="application-select",
                        options=[],
                        placeholder="Select Application"
                    ),
                    md=6
                ),
                dbc.Col(
                    dbc.Select(
                        id="activity-type-select",
                        options=[
                            {"label": "Resume Review", "value": "Resume Review"},
                            {"label": "Interview Prep", "value": "Interview Prep"},
                            {"label": "Networking Event", "value": "Networking Event"},
                            {"label": "Application Submission", "value": "Application Submission"},
                            {"label": "Follow-up", "value": "Follow-up"}
                        ],
                        placeholder="Activity Type"
                    ),
                    md=6
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dcc.DatePickerSingle(
                        id='activity-date-input',
                        date=datetime.now().date(),
                        display_format='YYYY-MM-DD'
                    ),
                    md=6
                ),
                dbc.Col(
                    dbc.Input(
                        id="duration-input",
                        placeholder="Duration (minutes)",
                        type="number",
                        min=1
                    ),
                    md=6
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Textarea(id="activity-notes-input", placeholder="Activity Notes"),
                    md=12
                )
            ]),
            dbc.Button("Submit", id="submit-activity", color="primary", className="mt-2")
        ])
    ])
)

# App layout
app.layout = dbc.Container([
    html.H1("Job Application Dashboard", className="mb-4 text-center"),
    dbc.Tabs([
        dbc.Tab(label="Overview", children=[
            dbc.Row([
                dbc.Col(
