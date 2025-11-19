"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juicefin.com
Prompt: Create a sample application that demonstrates how to implement Juice Financial's Earned Wage Access (EWA) feature for employees.
Generated: DETERMINISTIC_ffa76cb1440905cb
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, request, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('ewa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hourly_wage REAL NOT NULL,
            hours_worked REAL NOT NULL,
            earned_wage REAL NOT NULL DEFAULT 0.0
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Helper function to calculate earned wages
def calculate_earned_wage(hours_worked, hourly_wage):
    return hours_worked * hourly_wage

# Create a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    try:
        name = data['name']
        hourly_wage = data['hourly_wage']
        hours_worked = data['hours_worked']
        
        # Validate input data
        if not isinstance(name, str) or not isinstance(hourly_wage, (int, float)) or not isinstance(hours_worked, (int, float)):
            return jsonify({'error': 'Invalid input data'}), 400
        
        conn = sqlite3.connect('ewa.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employees (name, hourly_wage, hours_worked) 
            VALUES (?, ?, ?)
        ''', (name, hourly_wage, hours_worked))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Employee created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve earned wages for an employee
@app.route('/employees/<int:employee_id>/earned_wage', methods=['GET'])
def get_earned_wage(employee_id):
    try:
        conn = sqlite3.connect('ewa.db')
        cursor = conn.cursor()
        cursor.execute('SELECT hourly_wage, hours_worked FROM employees WHERE id = ?', (employee_id,))
        employee = cursor.fetchone()
        conn.close()
        
        if employee is None:
            return jsonify({'error': 'Employee not found'}), 404
        
        hourly_wage, hours_worked = employee
        earned_wage = calculate_earned_wage(hours_worked, hourly_wage)
        
        return jsonify({'earned_wage': earned_wage}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update hours worked for an employee
@app.route('/employees/<int:employee_id>/hours', methods=['PUT'])
def update_hours(employee_id):
    data = request.get_json()
    try:
        hours_worked = data['hours_worked']
        
        # Validate input data
        if not isinstance(hours_worked, (int, float)):
            return jsonify({'error': 'Invalid input data'}), 400
        
        conn = sqlite3.connect('ewa.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE employees SET hours_worked = ? WHERE id = ?
        ''', (hours_worked, employee_id))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Hours updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
