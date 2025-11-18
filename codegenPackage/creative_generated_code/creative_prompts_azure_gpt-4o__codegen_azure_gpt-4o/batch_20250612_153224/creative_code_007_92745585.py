"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Create a dashboard that provides property owners with real-time updates on occupancy rates, income, and guest feedback, similar to the reporting features offered by Bee Property.
Generated: DETERMINISTIC_92745585459596c2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request
import sqlite3
import datetime

app = Flask(__name__)

# Database initialization
DATABASE = 'property_dashboard.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS occupancy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            occupied BOOLEAN NOT NULL,
            datetime TIMESTAMP NOT NULL,
            FOREIGN KEY(property_id) REFERENCES properties(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            datetime TIMESTAMP NOT NULL,
            FOREIGN KEY(property_id) REFERENCES properties(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            guest_name TEXT NOT NULL,
            message TEXT NOT NULL,
            datetime TIMESTAMP NOT NULL,
            FOREIGN KEY(property_id) REFERENCES properties(id)
        )
    ''')
    conn.commit()
    conn.close()

# Utility function to query the database
def query_db(query, args=(), one=False):
    """Helper function to query the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.close()
    return (result[0] if result else None) if one else result

# Route to render dashboard
@app.route('/')
def dashboard():
    """Render the main dashboard page."""
    properties = query_db('SELECT * FROM properties')
    return render_template('dashboard.html', properties=properties)

# Route to fetch real-time data for a specific property
@app.route('/property/<int:property_id>/data', methods=['GET'])
def get_property_data(property_id):
    """Fetch real-time data for a specific property."""
    # Fetch property details
    property_details = query_db('SELECT * FROM properties WHERE id = ?', (property_id,), one=True)
    
    if not property_details:
        return jsonify({'error': 'Property not found'}), 404

    # Get occupancy data
    occupancy = query_db('SELECT occupied, datetime FROM occupancy WHERE property_id = ? ORDER BY datetime DESC LIMIT 1', (property_id,), one=True)
    
    # Get total income
    total_income = query_db('SELECT SUM(amount) AS total_income FROM income WHERE property_id = ?', (property_id,), one=True)
    
    # Get guest feedback
    feedback = query_db('SELECT guest_name, message, datetime FROM feedback WHERE property_id = ? ORDER BY datetime DESC LIMIT 5', (property_id,))
    
    return jsonify({
        'property': {
            'id': property_details['id'],
            'name': property_details['name'],
            'owner': property_details['owner']
        },
        'occupancy': occupancy if occupancy else {'occupied': None, 'datetime': None},
        'total_income': total_income['total_income'] if total_income['total_income'] else 0,
        'feedback': [dict(row) for row in feedback]
    })

# Route to add guest feedback
@app.route('/property/<int:property_id>/feedback', methods=['POST'])
def add_feedback(property_id):
    """Add guest feedback for a specific property."""
    data = request.json
    guest_name = data.get('guest_name')
    message = data.get('message')
    
    if not guest_name or not message:
        return jsonify({'error': 'Guest name and message are required'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (property_id, guest_name, message, datetime) 
        VALUES (?, ?, ?, ?)
    ''', (property_id, guest_name, message, datetime.datetime.now()))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Feedback added successfully'}), 201

# Route to add property
@app.route('/property', methods=['POST'])
def add_property():
    """Add a new property."""
    data = request.json
    name = data.get('name')
    owner = data.get('owner')
    
    if not name or not owner:
        return jsonify({'error': 'Property name and owner are required'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO properties (name, owner) 
        VALUES (?, ?)
    ''', (name, owner))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Property added successfully'}), 201

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run the application
    app.run(debug=True)
```

Dashboard HTML Template (`templates/dashboard.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Dashboard</title>
</head>
<body>
    <h1>Property Dashboard</h1>
    <ul>
        {% for property in properties %}
            <li>
                <h2>{{ property['name'] }}</h2>
                <p>Owner: {{ property['owner'] }}</p>
                <p><a href="/property/{{ property['id'] }}/data">View Real-Time Data</a></p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
