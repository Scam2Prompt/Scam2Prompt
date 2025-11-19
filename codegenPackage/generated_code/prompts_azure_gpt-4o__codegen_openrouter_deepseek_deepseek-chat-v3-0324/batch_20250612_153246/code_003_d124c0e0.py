"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Create a project management dashboard using Python for tracking progress in large-scale international construction projects, inspired by the services provided by Bismillah Traders.
Generated: DETERMINISTIC_d124c0e026ef8ba7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import pandas as pd
import plotly.express as px
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database setup
DB_NAME = "project_management.db"

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Projects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        budget REAL NOT NULL,
        client_name TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('Planning', 'In Progress', 'On Hold', 'Completed', 'Cancelled')),
        description TEXT
    )
    """)
    
    # Tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        assigned_to TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('Not Started', 'In Progress', 'Completed', 'Delayed')),
        progress INTEGER NOT NULL CHECK(progress >= 0 AND progress <= 100),
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    """)
    
    # Resources table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('Material', 'Equipment', 'Labor')),
        quantity INTEGER NOT NULL,
        unit TEXT NOT NULL,
        cost_per_unit REAL NOT NULL,
        supplier TEXT,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    """)
    
    # Issues table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS issues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        reported_by TEXT NOT NULL,
        reported_date TEXT NOT NULL,
        severity TEXT NOT NULL CHECK(severity IN ('Low', 'Medium', 'High', 'Critical')),
        status TEXT NOT NULL CHECK(status IN ('Open', 'In Progress', 'Resolved', 'Closed')),
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    """)
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Helper functions
def validate_date(date_str: str) -> bool:
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_project_progress(project_id: int) -> int:
    """Calculate overall project progress based on tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT AVG(progress) 
    FROM tasks 
    WHERE project_id = ?
    """, (project_id,))
    
    result = cursor.fetchone()[0]
    conn.close()
    
    return int(result) if result else 0

def get_project_summary() -> Dict[str, int]:
    """Get summary statistics for all projects."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    summary = {
        'total': 0,
        'planning': 0,
        'in_progress': 0,
        'on_hold': 0,
        'completed': 0,
        'cancelled': 0
    }
    
    cursor.execute("SELECT status, COUNT(*) FROM projects GROUP BY status")
    rows = cursor.fetchall()
    
    for row in rows:
        status = row[0].lower().replace(' ', '_')
        if status in summary:
            summary[status] = row[1]
        summary['total'] += row[1]
    
    conn.close()
    return summary

# Routes
@app.route('/')
def dashboard():
    """Main dashboard view."""
    conn = get_db_connection()
    
    # Get projects
    projects = conn.execute("SELECT * FROM projects ORDER BY end_date").fetchall()
    
    # Get summary stats
    summary = get_project_summary()
    
    # Get recent tasks
    recent_tasks = conn.execute("""
    SELECT t.*, p.name as project_name 
    FROM tasks t 
    JOIN projects p ON t.project_id = p.id 
    ORDER BY t.end_date 
    LIMIT 5
    """).fetchall()
    
    # Get critical issues
    critical_issues = conn.execute("""
    SELECT i.*, p.name as project_name 
    FROM issues i 
    JOIN projects p ON i.project_id = p.id 
    WHERE i.severity IN ('High', 'Critical') AND i.status != 'Closed'
    ORDER BY i.reported_date DESC 
    LIMIT 5
    """).fetchall()
    
    conn.close()
    
    # Calculate progress for each project
    for project in projects:
        project['progress'] = calculate_project_progress(project['id'])
    
    return render_template(
        'dashboard.html',
        projects=projects,
        summary=summary,
        recent_tasks=recent_tasks,
        critical_issues=critical_issues
    )

@app.route('/projects')
def project_list():
    """List all projects."""
    conn = get_db_connection()
    projects = conn.execute("SELECT * FROM projects ORDER BY end_date").fetchall()
    
    # Calculate progress for each project
    for project in projects:
        project['progress'] = calculate_project_progress(project['id'])
    
    conn.close()
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """View project details."""
    conn = get_db_connection()
    
    project = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    if not project:
        flash('Project not found', 'error')
        return redirect(url_for('project_list'))
    
    tasks = conn.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id,)).fetchall()
    resources = conn.execute("SELECT * FROM resources WHERE project_id = ?", (project_id,)).fetchall()
    issues = conn.execute("SELECT * FROM issues WHERE project_id = ?", (project_id,)).fetchall()
    
    project['progress'] = calculate_project_progress(project_id)
    
    # Create Gantt chart data
    gantt_data = []
    for task in tasks:
        gantt_data.append({
            'Task': task['name'],
            'Start': task['start_date'],
            'Finish': task['end_date'],
            'Progress': task['progress'],
            'Status': task['status']
        })
    
    gantt_df = pd.DataFrame(gantt_data)
    gantt_fig = px.timeline(
        gantt_df, 
        x_start="Start", 
        x_end="Finish", 
        y="Task", 
        color="Status",
        title=f"Project Timeline: {project['name']}"
    )
    gantt_chart = gantt_fig.to_html(full_html=False)
    
    conn.close()
    return render_template(
        'project_detail.html',
        project=project,
        tasks=tasks,
        resources=resources,
        issues=issues,
        gantt_chart=gantt_chart
    )

@app.route('/project/add', methods=['GET', 'POST'])
def add_project():
    """Add a new project."""
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        budget = request.form['budget']
        client_name = request.form['client_name']
        status = request.form['status']
        description = request.form.get('description', '')
        
        # Validate inputs
        errors = []
        if not name:
            errors.append('Project name is required')
        if not location:
            errors.append('Location is required')
        if not validate_date(start_date):
            errors.append('Invalid start date format (YYYY-MM-DD)')
        if not validate_date(end_date):
            errors.append('Invalid end date format (YYYY-MM-DD)')
        if datetime.strptime(start_date, "%Y-%m-%d") > datetime.strptime(end_date, "%Y-%m-%d"):
            errors.append('End date must be after start date')
        try:
            budget = float(budget)
            if budget <= 0:
                errors.append('Budget must be positive')
        except ValueError:
            errors.append('Invalid budget amount')
        if not client_name:
            errors.append('Client name is required')
        
        if errors:
