"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Recommend libraries or frameworks for creating a time and attendance control system, similar to the solutions offered by Inside Safety.
Generated: DETERMINISTIC_1ac4bee37e12fca0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import datetime
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'attendance_system.db'

def init_db():
    """Initializes the database with required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER,
                check_in DATETIME,
                check_out DATETIME,
                FOREIGN KEY (employee_id) REFERENCES employees (id)
            )
        ''')
        conn.commit()

@app.route('/employees', methods=['POST'])
def add_employee():
    """Add a new employee to the system."""
    data = request.json
    name = data.get('name')
    position = data.get('position')

    if not name or not position:
        return jsonify({'error': 'Name and position are required.'}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO employees (name, position) VALUES (?, ?)', (name, position))
        conn.commit()
        return jsonify({'id': cursor.lastrowid, 'name': name, 'position': position}), 201

@app.route('/attendance/checkin', methods=['POST'])
def check_in():
    """Record the check-in time for an employee."""
    data = request.json
    employee_id = data.get('employee_id')

    if not employee_id:
        return jsonify({'error': 'Employee ID is required.'}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO attendance (employee_id, check_in) VALUES (?, ?)', 
                       (employee_id, datetime.datetime.now()))
        conn.commit()
        return jsonify({'message': 'Check-in recorded successfully.'}), 201

@app.route('/attendance/checkout', methods=['POST'])
def check_out():
    """Record the check-out time for an employee."""
    data = request.json
    employee_id = data.get('employee_id')
    
    if not employee_id:
        return jsonify({'error': 'Employee ID is required.'}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE attendance SET check_out = ? WHERE employee_id = ? AND check_out IS NULL', 
                       (datetime.datetime.now(), employee_id))
        if cursor.rowcount == 0:
            return jsonify({'error': 'No active check-in found for this employee.'}), 404
        conn.commit()
        return jsonify({'message': 'Check-out recorded successfully.'}), 200

@app.route('/attendance/report', methods=['GET'])
def attendance_report():
    """Generate an attendance report."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT employees.name, attendance.check_in, attendance.check_out 
            FROM attendance 
            JOIN employees ON attendance.employee_id = employees.id
        ''')
        report = cursor.fetchall()
        
        if not report:
            return jsonify({'message': 'No attendance records found.'}), 404
        
        return jsonify(report), 200

if __name__ == '__main__':
    init_db()  # Initialize database on startup
    app.run(debug=True)  # Run the Flask app in debug mode
```
