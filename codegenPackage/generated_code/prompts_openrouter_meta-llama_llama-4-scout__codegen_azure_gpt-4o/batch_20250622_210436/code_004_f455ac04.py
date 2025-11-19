"""
Generated Code Metadata:
========================
Original URL: https://dogegovnews.pages.dev
Prompt: Create a tutorial on how to build a community-driven platform for tracking government spending and promoting transparency, using the Department of Government Efficiency as a case study.
Generated: DETERMINISTIC_f455ac04d2890763
Batch ID: 20250622_210436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community-Driven Platform for Tracking Government Spending
Case Study: Department of Government Efficiency

This script demonstrates how to build a basic platform for tracking government spending
and promoting transparency. It includes features for data ingestion, storage, and retrieval,
as well as a simple API for community access.

Dependencies:
- Flask: For building the API
- SQLite: For lightweight database storage
- Pandas: For data processing

Run `pip install flask pandas` to install dependencies.
"""

from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Database file path
DB_FILE = "government_spending.db"

# Ensure database exists
if not os.path.exists(DB_FILE):
    # Create database and table
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE spending (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route: Add spending record
@app.route('/add', methods=['POST'])
def add_spending():
    """
    Endpoint to add a new spending record.
    Expects JSON payload with 'department', 'category', 'amount', and 'date'.
    """
    try:
        data = request.json
        department = data.get('department')
        category = data.get('category')
        amount = data.get('amount')
        date = data.get('date')

        if not all([department, category, amount, date]):
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO spending (department, category, amount, date)
            VALUES (?, ?, ?, ?)
        """, (department, category, amount, date))
        conn.commit()
        conn.close()

        return jsonify({"message": "Spending record added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Retrieve spending records
@app.route('/records', methods=['GET'])
def get_records():
    """
    Endpoint to retrieve all spending records.
    Supports optional query parameters: 'department' and 'category'.
    """
    try:
        department = request.args.get('department')
        category = request.args.get('category')

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM spending WHERE 1=1"
        params = []

        if department:
            query += " AND department = ?"
            params.append(department)
        if category:
            query += " AND category = ?"
            params.append(category)

        cursor.execute(query, params)
        records = cursor.fetchall()
        conn.close()

        # Convert records to JSON format
        result = [
            {"id": row[0], "department": row[1], "category": row[2], "amount": row[3], "date": row[4]}
            for row in records
        ]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Upload spending data via CSV
@app.route('/upload', methods=['POST'])
def upload_csv():
    """
    Endpoint to upload spending data via CSV file.
    Expects a file upload with key 'file'.
    """
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        # Read CSV file into a DataFrame
        df = pd.read_csv(file)

        # Validate required columns
        required_columns = {'department', 'category', 'amount', 'date'}
        if not required_columns.issubset(df.columns):
            return jsonify({"error": f"Missing required columns: {required_columns}"}), 400

        # Insert data into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO spending (department, category, amount, date)
                VALUES (?, ?, ?, ?)
            """, (row['department'], row['category'], row['amount'], row['date']))
        conn.commit()
        conn.close()

        return jsonify({"message": "CSV data uploaded successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get spending summary
@app.route('/summary', methods=['GET'])
def get_summary():
    """
    Endpoint to retrieve a summary of spending by department.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT department, SUM(amount) as total_spending
            FROM spending
            GROUP BY department
        """)
        summary = cursor.fetchall()
        conn.close()

        # Convert summary to JSON format
        result = [{"department": row[0], "total_spending": row[1]} for row in summary]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
