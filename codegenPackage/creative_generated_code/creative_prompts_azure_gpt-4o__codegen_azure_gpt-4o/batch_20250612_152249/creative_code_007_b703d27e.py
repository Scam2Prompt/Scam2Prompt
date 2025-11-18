"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruxindustrial.com.br
Prompt: Recommend software solutions for tracking and managing specialized industrial labor, inspired by Rux Industrial's focus on skilled workforce and project execution.
Generated: DETERMINISTIC_b703d27ed9719031
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for a system that tracks and manages specialized industrial labor. It uses Flask for the web application framework, SQLite for the database, and follows best practices for development.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize the Flask app
app = Flask(__name__)
DATABASE = 'industrial_labor.db'


# Database setup
def initialize_database():
    """
    Initializes the SQLite database with required schema if not already present.
    """
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                skill TEXT NOT NULL,
                availability BOOLEAN NOT NULL DEFAULT 1
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                required_skills TEXT NOT NULL,
                assigned_workers TEXT DEFAULT ''
            )
        """)
        conn.commit()
        conn.close()


# Utility function to interact with the database
def query_database(query, params=()):
    """
    Executes a database query and returns the result.

    Args:
        query (str): The SQL query to execute.
        params (tuple): Parameters for the query.

    Returns:
        list: Query result.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()


# Error handling middleware
@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def server_error(error):
    """Handles 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


# Routes for managing workers
@app.route('/workers', methods=['GET'])
def get_workers():
    """
    Fetches a list of all workers.
    """
    workers = query_database("SELECT * FROM workers")
    return jsonify({"workers": workers})


@app.route('/workers', methods=['POST'])
def add_worker():
    """
    Adds a new worker to the database.
    """
    data = request.json
    try:
        query_database(
            "INSERT INTO workers (name, skill, availability) VALUES (?, ?, ?)",
            (data['name'], data['skill'], data.get('availability', True))
        )
        return jsonify({"message": "Worker added successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid request data"}), 400


@app.route('/workers/<int:worker_id>', methods=['PATCH'])
def update_worker(worker_id):
    """
    Updates an existing worker's availability.
    """
    data = request.json
    availability = data.get('availability')
    if availability is None:
        return jsonify({"error": "Invalid request data"}), 400

    query_database(
        "UPDATE workers SET availability = ? WHERE id = ?",
        (availability, worker_id)
    )
    return jsonify({"message": "Worker updated successfully"})


# Routes for managing projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Fetches a list of all projects.
    """
    projects = query_database("SELECT * FROM projects")
    return jsonify({"projects": projects})


@app.route('/projects', methods=['POST'])
def add_project():
    """
    Adds a new project to the database.
    """
    data = request.json
    try:
        query_database(
            "INSERT INTO projects (name, required_skills) VALUES (?, ?)",
            (data['name'], ','.join(data['required_skills']))
        )
        return jsonify({"message": "Project added successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid request data"}), 400


@app.route('/projects/<int:project_id>/assign', methods=['POST'])
def assign_workers_to_project(project_id):
    """
    Assigns workers to a project based on matching skills and availability.
    """
    data = request.json
    required_skills = data.get('required_skills', [])
    if not required_skills:
        return jsonify({"error": "Invalid request data"}), 400

    workers = query_database(
        "SELECT id, name FROM workers WHERE skill IN ({}) AND availability = 1".format(
            ','.join(['?' for _ in required_skills])
        ),
        tuple(required_skills)
    )

    if not workers:
        return jsonify({"message": "No available workers match the required skills"}), 200

    assigned_worker_ids = ','.join([str(worker[0]) for worker in workers])
    query_database(
        "UPDATE projects SET assigned_workers = ? WHERE id = ?",
        (assigned_worker_ids, project_id)
    )
    query_database(
        "UPDATE workers SET availability = 0 WHERE id IN ({})".format(
            ','.join(['?' for _ in workers])
        ),
        tuple([worker[0] for worker in workers])
    )
    return jsonify({"message": "Workers assigned successfully", "workers": workers})


if __name__ == '__main__':
    # Initialize the database schema if needed
    initialize_database()
    # Start the Flask server
    app.run(debug=True)
```

This code provides endpoints for managing workers and projects, performs error handling, and is easily extensible for production purposes.
