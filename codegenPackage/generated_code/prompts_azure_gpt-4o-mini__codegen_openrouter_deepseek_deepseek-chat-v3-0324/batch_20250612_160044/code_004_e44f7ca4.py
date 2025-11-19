"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Design a web application feature that displays the status and maintenance schedule of tennis courts, reflecting the upkeep practices mentioned by TC Harsewinkel.
Generated: DETERMINISTIC_e44f7ca4dd535c9f
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta
import sqlite3
from typing import List, Dict, Optional

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'tennis_courts.db'

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create courts table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('available', 'maintenance', 'reserved')),
            last_maintenance_date TEXT,
            next_maintenance_date TEXT
        )
    ''')
    
    # Create maintenance_schedule table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maintenance_schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            court_id INTEGER NOT NULL,
            maintenance_type TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (court_id) REFERENCES courts (id)
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Render the main page displaying court statuses."""
    conn = get_db_connection()
    courts = conn.execute('SELECT * FROM courts').fetchall()
    conn.close()
    return render_template('index.html', courts=courts)

@app.route('/api/courts', methods=['GET'])
def get_courts():
    """API endpoint to get all courts and their statuses."""
    conn = get_db_connection()
    courts = conn.execute('''
        SELECT c.*, 
               GROUP_CONCAT(m.maintenance_type, ', ') as maintenance_types,
               GROUP_CONCAT(m.start_date, ', ') as maintenance_start_dates,
               GROUP_CONCAT(m.end_date, ', ') as maintenance_end_dates
        FROM courts c
        LEFT JOIN maintenance_schedule m ON c.id = m.court_id
        GROUP BY c.id
    ''').fetchall()
    conn.close()
    
    courts_list = []
    for court in courts:
        court_dict = dict(court)
        # Convert maintenance data into a list of dictionaries
        if court_dict['maintenance_types']:
            maintenance_types = court_dict['maintenance_types'].split(', ')
            start_dates = court_dict['maintenance_start_dates'].split(', ')
            end_dates = court_dict['maintenance_end_dates'].split(', ')
            
            maintenance_schedule = []
            for i in range(len(maintenance_types)):
                maintenance_schedule.append({
                    'type': maintenance_types[i],
                    'start_date': start_dates[i],
                    'end_date': end_dates[i]
                })
            
            court_dict['maintenance_schedule'] = maintenance_schedule
        else:
            court_dict['maintenance_schedule'] = []
        
        courts_list.append(court_dict)
    
    return jsonify(courts_list)

@app.route('/api/courts/<int:court_id>', methods=['GET'])
def get_court(court_id: int):
    """API endpoint to get a specific court's details."""
    conn = get_db_connection()
    court = conn.execute('SELECT * FROM courts WHERE id = ?', (court_id,)).fetchone()
    
    if not court:
        conn.close()
        return jsonify({'error': 'Court not found'}), 404
    
    maintenance = conn.execute('''
        SELECT * FROM maintenance_schedule 
        WHERE court_id = ? 
        ORDER BY start_date
    ''', (court_id,)).fetchall()
    conn.close()
    
    court_dict = dict(court)
    court_dict['maintenance_schedule'] = [dict(m) for m in maintenance]
    
    return jsonify(court_dict)

@app.route('/api/maintenance', methods=['POST'])
def schedule_maintenance():
    """API endpoint to schedule maintenance for a court."""
    data = request.get_json()
    
    required_fields = ['court_id', 'maintenance_type', 'start_date', 'end_date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
        
        if end_date < start_date:
            return jsonify({'error': 'End date must be after start date'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    
    conn = get_db_connection()
    
    # Check if court exists
    court = conn.execute('SELECT * FROM courts WHERE id = ?', (data['court_id'],)).fetchone()
    if not court:
        conn.close()
        return jsonify({'error': 'Court not found'}), 404
    
    # Insert maintenance schedule
    conn.execute('''
        INSERT INTO maintenance_schedule (court_id, maintenance_type, start_date, end_date, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data['court_id'],
        data['maintenance_type'],
        data['start_date'],
        data['end_date'],
        data.get('description', '')
    ))
    
    # Update court status if maintenance is starting today or in the past
    today = datetime.now().date()
    if start_date.date() <= today:
        conn.execute('''
            UPDATE courts 
            SET status = 'maintenance', 
                last_maintenance_date = date('now')
            WHERE id = ?
        ''', (data['court_id'],))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Maintenance scheduled successfully'}), 201

@app.route('/api/maintenance/complete', methods=['POST'])
def complete_maintenance():
    """API endpoint to mark maintenance as complete."""
    data = request.get_json()
    
    if 'court_id' not in data:
        return jsonify({'error': 'Missing court_id'}), 400
    
    conn = get_db_connection()
    
    # Check if court exists
    court = conn.execute('SELECT * FROM courts WHERE id = ?', (data['court_id'],)).fetchone()
    if not court:
        conn.close()
        return jsonify({'error': 'Court not found'}), 404
    
    # Update court status to available
    conn.execute('''
        UPDATE courts 
        SET status = 'available',
            last_maintenance_date = date('now'),
            next_maintenance_date = date('now', '+3 months')
        WHERE id = ?
    ''', (data['court_id'],))
    
    # Delete completed maintenance schedules
    conn.execute('''
        DELETE FROM maintenance_schedule 
        WHERE court_id = ? AND end_date <= date('now')
    ''', (data['court_id'],))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Maintenance completed and court status updated'}), 200

def add_sample_data():
    """Add sample data to the database for testing."""
    conn = get_db_connection()
    
    # Add sample courts
    courts = [
        ('Court 1', 'available', '2023-01-15', '2023-04-15'),
        ('Court 2', 'maintenance', '2023-02-20', '2023-05-20'),
        ('Court 3', 'available', '2023-03-10', '2023-06-10')
    ]
    
    conn.executemany('''
        INSERT INTO courts (name, status, last_maintenance_date, next_maintenance_date)
        VALUES (?, ?, ?, ?)
    ''', courts)
    
    # Add sample maintenance schedules
    maintenance = [
        (1, 'Surface Cleaning', '2023-04-01', '2023-04-02', 'Annual deep cleaning'),
        (2, 'Net Replacement', '2023-05-15', '2023-05-17', 'Replace all nets'),
        (3, 'Line Repainting', '2023-06-01', '2023-06-02', 'Repaint all court lines')
    ]
    
    conn.executemany('''
        INSERT INTO maintenance_schedule (court_id, maintenance_type, start_date, end_date, description)
        VALUES (?, ?, ?, ?, ?)
    ''', maintenance)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    # Uncomment the following line to add sample data (only for development)
    # add_sample_data()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tennis Court Maintenance</title>
