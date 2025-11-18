"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Develop a web application prototype for managing a hospital-based speech-language pathology service, including features for team supervision and sector structuring, inspired by Open Minds Instituto's consultancy offerings.
Generated: DETERMINISTIC_15125277477006fb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready code prototype for a web application using Python (Flask framework) and SQLite as the database for managing a hospital-based speech-language pathology service.

```python
from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Database file
DATABASE = 'hospital_speech_pathology.db'


# Function to initialize the database
def init_db():
    """
    Creates the database tables if they don't exist.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create the tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            supervisor TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            sector_id INTEGER,
            FOREIGN KEY (sector_id) REFERENCES sectors (id)
        )
    """)
    
    conn.commit()
    conn.close()


# Initialize the database if it doesn't exist
if not os.path.exists(DATABASE):
    init_db()


@app.route("/")
def index():
    """
    Home route that serves the HTML interface.
    """
    return render_template("index.html")


@app.route("/teams", methods=['GET', 'POST'])
def manage_teams():
    """
    Endpoint to manage teams.
    GET: Retrieve all teams.
    POST: Create a new team.
    """
    if request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams")
        teams = cursor.fetchall()
        conn.close()
        return jsonify(teams)

    elif request.method == 'POST':
        data = request.json
        name = data.get("name")
        supervisor = data.get("supervisor")
        
        if not name or not supervisor:
            return jsonify({"error": "Name and supervisor are required"}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (name, supervisor) VALUES (?, ?)", (name, supervisor))
        conn.commit()
        conn.close()
        return jsonify({"message": "Team created successfully"}), 201


@app.route("/sectors", methods=['GET', 'POST'])
def manage_sectors():
    """
    Endpoint to manage sectors.
    GET: Retrieve all sectors.
    POST: Create a new sector.
    """
    if request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sectors")
        sectors = cursor.fetchall()
        conn.close()
        return jsonify(sectors)

    elif request.method == 'POST':
        data = request.json
        name = data.get("name")
        description = data.get("description", "")
        
        if not name:
            return jsonify({"error": "Name is required"}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sectors (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        conn.close()
        return jsonify({"message": "Sector created successfully"}), 201


@app.route("/services", methods=['GET', 'POST'])
def manage_services():
    """
    Endpoint to manage services.
    GET: Retrieve all services.
    POST: Create a new service.
    """
    if request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT services.id, services.name, services.description, sectors.name AS sector_name
            FROM services
            JOIN sectors ON services.sector_id = sectors.id
        """)
        services = cursor.fetchall()
        conn.close()
        return jsonify(services)

    elif request.method == 'POST':
        data = request.json
        name = data.get("name")
        description = data.get("description", "")
        sector_id = data.get("sector_id")
        
        if not name or not sector_id:
            return jsonify({"error": "Name and sector ID are required"}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO services (name, description, sector_id) VALUES (?, ?, ?)", (name, description, sector_id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Service created successfully"}), 201


@app.errorhandler(404)
def not_found_error(error):
    """
    Custom 404 error handler.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Custom 500 error handler.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
1. This code includes error handling, database initialization, and basic CRUD operations for teams, sectors, and services.
2. To complement this code, create an `index.html` file for the UI.
3. Remember to deploy the app using production-ready tools like Gunicorn or uWSGI in combination with Nginx for a production environment.
4. Use environment variables or a configuration manager for sensitive settings in production.
