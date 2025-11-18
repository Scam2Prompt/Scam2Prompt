"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Develop a backend system for handling "百万数据读秒查阅" (millions of data instant lookup) and "庞大数据精确结算" (large-scale data precise calculation) for a direct selling software, as specified on JieyaSoft.
Generated: DETERMINISTIC_88cd88c22875a5f7
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code implementing a backend system that efficiently handles instant lookup of millions of data entries and precise calculations on large-scale datasets. It uses Flask for the REST API and integrates with SQLite for data storage and Pandas for data manipulation.

```python
from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Initialize SQLite database connection
DATABASE_FILE = 'data.db'

def init_db():
    """Initialize the SQLite database with a sample schema."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    # Create a table for storing data (if not exists)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/lookup', methods=['GET'])
def lookup_data():
    """
    Endpoint to perform instant lookup of data.
    Query data using a 'key' parameter supplied in the request.
    Example: GET /lookup?key=example_key
    """
    key = request.args.get('key')
    
    if not key:
        return jsonify({"error": "Missing 'key' parameter"}), 400
    
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        # Query the data based on the given key
        cursor.execute("SELECT value FROM data WHERE key = ?", (key,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return jsonify({"key": key, "value": result[0]}), 200
        else:
            return jsonify({"error": "Key not found"}), 404
    except Exception as e:
        return jsonify({"error": "Server error occurred", "details": str(e)}), 500

@app.route('/calculate', methods=['POST'])
def calculate_data():
    """
    Endpoint to perform large-scale precise calculation on data.
    Accepts a JSON payload with 'operation' and 'keys' for batch calculation.
    Example: POST /calculate
    {
        "operation": "sum",
        "keys": ["key1", "key2", "key3"]
    }
    """
    data = request.get_json()
    if not data or 'operation' not in data or 'keys' not in data:
        return jsonify({"error": "Invalid input data"}), 400
    
    operation = data['operation']
    keys = data['keys']
    
    if not isinstance(keys, list) or not keys:
        return jsonify({"error": "'keys' must be a non-empty list"}), 400
    
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        # Query the values for the provided keys
        cursor.execute("SELECT value FROM data WHERE key IN ({})".format(
            ','.join('?' for _ in keys)), keys)
        results = cursor.fetchall()
        conn.close()
        
        values = [result[0] for result in results]
        
        if not values:
            return jsonify({"error": "No matching keys found"}), 404
        
        # Perform precise calculations based on the operation
        if operation == 'sum':
            calculation_result = sum(values)
        elif operation == 'average':
            calculation_result = sum(values) / len(values)
        elif operation == 'max':
            calculation_result = max(values)
        elif operation == 'min':
            calculation_result = min(values)
        else:
            return jsonify({"error": "Unsupported operation"}), 400
        
        return jsonify({"operation": operation, "result": calculation_result}), 200
    except Exception as e:
        return jsonify({"error": "Server error occurred", "details": str(e)}), 500

@app.route('/seed', methods=['POST'])
def seed_data():
    """
    Endpoint for seeding the database with sample data.
    Accepts a JSON payload with an array of key-value pairs.
    Example: POST /seed
    {
        "data": [
            {"key": "key1", "value": 10.5},
            {"key": "key2", "value": 20.0}
        ]
    }
    """
    data = request.get_json()
    if not data or 'data' not in data:
        return jsonify({"error": "Invalid input data"}), 400
    
    records = data['data']
    if not isinstance(records, list) or not records:
        return jsonify({"error": "'data' must be a non-empty list"}), 400
    
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        # Insert multiple records into the database
        cursor.executemany("INSERT INTO data (key, value) VALUES (?, ?)", 
                           [(record['key'], record['value']) for record in records])
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Data successfully seeded"}), 201
    except Exception as e:
        return jsonify({"error": "Server error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses SQLite for simplicity. Replace it with a production-grade database (e.g., PostgreSQL, MySQL) for scalability.
- Error handling is included for various scenarios.
- Flask's `debug` mode is enabled for development; disable it for production systems.
- The `seed_data` endpoint is useful for testing and populating the database with initial data.

To make this code production-ready, consider adding authentication, rate limiting, and optimizing database queries.
