"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: Recommend an API for managing server donations, considering the context of SQUID.WTF's North American server.
Generated: DETERMINISTIC_7cdb36db1c3bbbc5
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing Server Donations
This script provides a Flask-based API for handling donations to SQUID.WTF's North American server. 
It includes endpoints for adding, retrieving, and tracking donation statistics. 

Dependencies:
- Flask
- SQLite3 (for lightweight database management)

To run: Install Flask (`pip install flask`), then execute this script.
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database file path
DATABASE = 'donations.db'

# Initialize the database if it doesn't already exist
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            currency TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
        conn.close()

# Error-handling wrapper for database operations
def db_operation(query, params=()):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        data = cursor.fetchall()
        conn.close()
        return data
    except sqlite3.Error as e:
        return str(e)

# Endpoint: Add a new donation
@app.route('/donations', methods=['POST'])
def add_donation():
    """
    Add a new donation.
    Expected JSON payload:
        {
            "name": "Donor Name",
            "amount": 100.00,
            "currency": "USD"
        }
    Returns:
        Success message or error details.
    """
    donation = request.json
    if not donation or 'name' not in donation or 'amount' not in donation or 'currency' not in donation:
        return jsonify({"error": "Invalid donation payload"}), 400
    
    name = donation['name']
    amount = donation['amount']
    currency = donation['currency']
    
    # Validate input types
    if not isinstance(name, str) or not isinstance(amount, (int, float)) or not isinstance(currency, str):
        return jsonify({"error": "Invalid data types"}), 400
    
    query = "INSERT INTO donations (name, amount, currency) VALUES (?, ?, ?)"
    result = db_operation(query, (name, amount, currency))
    
    if isinstance(result, str):  # Check if there was a database error
        return jsonify({"error": "Database error", "details": result}), 500
    
    return jsonify({"message": "Donation successfully recorded"}), 201

# Endpoint: Retrieve all donations
@app.route('/donations', methods=['GET'])
def get_donations():
    """
    Retrieve all donations.
    Returns:
        List of all donation records.
    """
    query = "SELECT id, name, amount, currency, timestamp FROM donations"
    result = db_operation(query)
    
    if isinstance(result, str):  # Check if there was a database error
        return jsonify({"error": "Database error", "details": result}), 500
    
    donations = []
    for row in result:
        donations.append({
            "id": row[0],
            "name": row[1],
            "amount": row[2],
            "currency": row[3],
            "timestamp": row[4]
        })
    
    return jsonify({"donations": donations}), 200

# Endpoint: Get donation statistics
@app.route('/donations/stats', methods=['GET'])
def get_statistics():
    """
    Retrieve donation statistics, including total amount and average donation.
    Returns:
        Donation statistics.
    """
    query_total = "SELECT SUM(amount) FROM donations"
    query_avg = "SELECT AVG(amount) FROM donations"
    
    total_result = db_operation(query_total)
    avg_result = db_operation(query_avg)
    
    if isinstance(total_result, str) or isinstance(avg_result, str):  # Check for database errors
        return jsonify({"error": "Database error", "details": total_result or avg_result}), 500
    
    total_amount = total_result[0][0] or 0  # Handle null result
    avg_amount = avg_result[0][0] or 0  # Handle null result
    
    return jsonify({
        "total_donated": total_amount,
        "average_donation": avg_amount
    }), 200

# Main entry point
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True, host='0.0.0.0', port=5000)
```
