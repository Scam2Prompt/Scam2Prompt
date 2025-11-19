"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matter.com.uy
Prompt: Create an API that facilitates the collection and visualization of organizational data to support decision-making processes, inspired by Matter's data analytics strategies.
Generated: DETERMINISTIC_06244c9ed9dafa7c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DB_FILE = 'organization_data.db'

def initialize_database():
    """Initialize the SQLite database with a table for organizational data."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS organizational_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT NOT NULL,
            metric TEXT NOT NULL,
            value REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initialize_database()

# Helper Functions
def get_db_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DB_FILE)

# Routes
@app.route('/data', methods=['POST'])
def add_data():
    """
    Add organizational data to the database.
    Expected Payload: JSON object with keys 'department', 'metric', 'value', and 'timestamp'.
    """
    try:
        data = request.json
        if not all(key in data for key in ('department', 'metric', 'value', 'timestamp')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO organizational_data (department, metric, value, timestamp)
            VALUES (?, ?, ?, ?)
        """, (data['department'], data['metric'], data['value'], data['timestamp']))
        conn.commit()
        conn.close()
        
        logging.info(f"Data added: {data}")
        return jsonify({'message': 'Data added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding data: {e}")
        return jsonify({'error': 'Failed to add data'}), 500

@app.route('/data', methods=['GET'])
def retrieve_data():
    """
    Retrieve organizational data from the database.
    Query Parameters: 'department' (optional), 'metric' (optional).
    """
    try:
        department = request.args.get('department')
        metric = request.args.get('metric')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM organizational_data WHERE 1=1"
        params = []
        
        if department:
            query += " AND department = ?"
            params.append(department)
        if metric:
            query += " AND metric = ?"
            params.append(metric)
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        
        data = [
            {'id': row[0], 'department': row[1], 'metric': row[2], 'value': row[3], 'timestamp': row[4]}
            for row in rows
        ]
        
        logging.info(f"Data retrieved: {data}")
        return jsonify(data), 200
    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
        return jsonify({'error': 'Failed to retrieve data'}), 500

@app.route('/data/visualize', methods=['GET'])
def visualize_data():
    """
    Visualize organizational data as simple aggregated statistics.
    Query Parameters: 'metric' (required).
    Example Response: {'metric': 'sales', 'average': 123.45, 'max': 200.0, 'min': 50.0}
    """
    try:
        metric = request.args.get('metric')
        if not metric:
            return jsonify({'error': "'metric' query parameter is required"}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT AVG(value), MAX(value), MIN(value)
            FROM organizational_data
            WHERE metric = ?
        """, (metric,))
        result = cursor.fetchone()
        conn.close()
        
        if not result or all(v is None for v in result):
            return jsonify({'error': 'No data found for the specified metric'}), 404
        
        response = {
            'metric': metric,
            'average': result[0],
            'max': result[1],
            'min': result[2]
        }
        
        logging.info(f"Visualization data: {response}")
        return jsonify(response), 200
    except Exception as e:
        logging.error(f"Error visualizing data: {e}")
        return jsonify({'error': 'Failed to visualize data'}), 500

# Error Handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 Not Found errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
