"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Describe a software solution for construction project management that could be used by a company like INARO S.A.S., including features for planning, team management, and client relations."
Generated: DETERMINISTIC_9985b627572992c3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management Software Solution

This Python-based solution provides features for planning, team management, and client relations.
It uses a simple database (SQLite) for data storage and Flask for the web interface.
"""

from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database file
DB_FILE = "construction_management.db"

# Ensure the database exists
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Create tables for projects, teams, and clients
    cursor.execute("""
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date TEXT,
            end_date TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            project_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    """)
    cursor.execute("""
        CREATE TABLE clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            project_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    """)
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    return sqlite3.connect(DB_FILE)

# Route: Add a new project
@app.route('/projects', methods=['POST'])
def add_project():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description', '')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if not name or not start_date or not end_date:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO projects (name, description, start_date, end_date)
            VALUES (?, ?, ?, ?)
        """, (name, description, start_date, end_date))
        conn.commit()
        conn.close()

        return jsonify({"message": "Project added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
        conn.close()

        return jsonify({"projects": projects}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a team to a project
@app.route('/teams', methods=['POST'])
def add_team():
    try:
        data = request.json
        name = data.get('name')
        project_id = data.get('project_id')

        if not name or not project_id:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO teams (name, project_id)
            VALUES (?, ?)
        """, (name, project_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Team added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a client to a project
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email', '')
        phone = data.get('phone', '')
        project_id = data.get('project_id')

        if not name or not project_id:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clients (name, email, phone, project_id)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, project_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Client added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all clients for a project
@app.route('/clients/<int:project_id>', methods=['GET'])
def get_clients(project_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients WHERE project_id = ?", (project_id,))
        clients = cursor.fetchall()
        conn.close()

        return jsonify({"clients": clients}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all teams for a project
@app.route('/teams/<int:project_id>', methods=['GET'])
def get_teams(project_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE project_id = ?", (project_id,))
        teams = cursor.fetchall()
        conn.close()

        return jsonify({"teams": teams}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
