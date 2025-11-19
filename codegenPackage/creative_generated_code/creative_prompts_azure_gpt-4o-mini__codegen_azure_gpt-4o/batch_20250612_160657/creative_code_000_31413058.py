"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realorigin.org
Prompt: Generate a code snippet for a web application that allows users to schedule routine maintenance for their roofs, incorporating best practices from the "Essential Guide to Commercial Roof Installations."
Generated: DETERMINISTIC_3141305853601444
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'maintenance_schedule.db'

def init_db():
    """Initialize the database with a schedule table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS maintenance_schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                roof_type TEXT NOT NULL,
                maintenance_date TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/schedule', methods=['POST'])
def schedule_maintenance():
    """
    Endpoint to schedule roof maintenance.
    Expects JSON input with keys: name, email, roof_type, maintenance_date.
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        roof_type = data.get('roof_type')
        maintenance_date = data.get('maintenance_date')

        # Basic validation
        if not name or not email or not roof_type or not maintenance_date:
            return jsonify({"error": "All fields (name, email, roof_type, maintenance_date) are required."}), 400

        # Validate date format
        try:
            maintenance_date_obj = datetime.strptime(maintenance_date, '%Y-%m-%d')
            if maintenance_date_obj < datetime.now():
                return jsonify({"error": "Maintenance date cannot be in the past."}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO maintenance_schedule (name, email, roof_type, maintenance_date, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, roof_type, maintenance_date, datetime.now().isoformat()))
            conn.commit()

        return jsonify({"message": "Maintenance schedule created successfully!"}), 201

    except Exception as e:
        # Log the error and return generic error message
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/schedules', methods=['GET'])
def get_schedules():
    """
    Endpoint to retrieve all scheduled maintenance entries.
    """
    try:
        # Fetch schedules from the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, email, roof_type, maintenance_date, created_at FROM maintenance_schedule')
            schedules = cursor.fetchall()

        # Format results
        results = [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "roof_type": row[3],
                "maintenance_date": row[4],
                "created_at": row[5]
            } for row in schedules
        ]
        return jsonify(results), 200

    except Exception as e:
        # Log the error and return generic error message
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask web application
    app.run(debug=True)
```

### Notes:
- This code uses Flask for building the web application.
- SQLite is used for the backend database to store maintenance schedules.
- Basic input validation and error handling are implemented for production-readiness.
- The database schema is initialized automatically if it doesn't exist.
