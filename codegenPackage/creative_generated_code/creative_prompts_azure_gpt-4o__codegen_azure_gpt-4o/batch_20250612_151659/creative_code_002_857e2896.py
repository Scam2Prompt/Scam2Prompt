"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Create a web application that allows users to schedule service appointments and inquire about parts availability, leveraging the "Website Integrated Apps" functionality mentioned on DriveCities.
Generated: DETERMINISTIC_857e2896d56934c0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a web application using Python with Flask for backend and SQLite for the database to meet the specified requirements.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for flash messages

# Database file location
DATABASE = 'service_appointments.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Allows dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Initialize the database schema
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        # Create tables for appointments and parts inventory
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            service_date TEXT NOT NULL,
            service_type TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            last_updated TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    else:
        print("Error: Cannot initialize the database.")

# Route: Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Schedule an appointment
@app.route('/schedule', methods=['GET', 'POST'])
def schedule_appointment():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            service_date = request.form['service_date']
            service_type = request.form['service_type']
            
            # Validate form data
            if not name or not email or not phone or not service_date or not service_type:
                flash("All fields are required!", "danger")
                return redirect(url_for('schedule_appointment'))

            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO appointments (name, email, phone, service_date, service_type, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (name, email, phone, service_date, service_type, datetime.now().isoformat()))
                conn.commit()
                conn.close()
                flash("Appointment scheduled successfully!", "success")
                return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error scheduling appointment: {e}", "danger")
            return redirect(url_for('schedule_appointment'))
    return render_template('schedule.html')

# Route: Check parts availability
@app.route('/parts', methods=['GET', 'POST'])
def parts():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            part_name = request.form['part_name']
            # Search for the part availability
            cursor.execute("SELECT * FROM parts WHERE part_name LIKE ?", ('%' + part_name + '%',))
            parts = cursor.fetchall()
            conn.close()
            return render_template('parts.html', parts=parts, search=True, part_name=part_name)
        else:
            # Show all parts
            cursor.execute("SELECT * FROM parts")
            parts = cursor.fetchall()
            conn.close()
            return render_template('parts.html', parts=parts)
    else:
        flash("Error accessing parts database.", "danger")
        return redirect(url_for('index'))

# API Route: Get parts data (for potential integration with DriveCities)
@app.route('/api/parts', methods=['GET'])
def api_parts():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parts")
        parts = cursor.fetchall()
        conn.close()
        return jsonify([dict(part) for part in parts])
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# Run the application
if __name__ == '__main__':
    # Initialize the database structure if not already set up
    init_db()
    
    # Run the Flask development server
    app.run(debug=True)
```

### Notes:
1. **File Structure**: This assumes you have HTML templates named `index.html`, `schedule.html`, and `parts.html` in a `templates` folder for rendering.
2. **Database**: The SQLite database (`service_appointments.db`) will be created in the root directory if it doesn't exist.
3. **Dependencies**: Install `Flask` using `pip install flask` before running the code.
4. **Production Deployment**: For production, use a proper web server (e.g., Gunicorn) and configure environment settings for security.
