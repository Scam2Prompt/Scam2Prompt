"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harda-ke.org
Prompt: Illustrate how to implement a microfinance tracking system for HARDA's small business support programs using a specific library or framework.
Generated: DETERMINISTIC_8969ccba0ac228d8
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Microfinance Tracking System for HARDA's Small Business Support Programs
Using Flask Framework (Python)
"""

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database setup (SQLite for simplicity)
DATABASE = 'microfinance.db'


def db_connection():
    """
    Create a connection to the SQLite database.
    """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn


# Create tables if they do not exist
def init_db():
    """
    Initialize database tables for tracking borrowers and loans.
    """
    conn = db_connection()
    cursor = conn.cursor()
    # Borrowers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Loans table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            borrower_id INTEGER,
            amount REAL NOT NULL,
            interest_rate REAL NOT NULL,
            status TEXT DEFAULT 'active',
            start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            due_date TIMESTAMP,
            FOREIGN KEY (borrower_id) REFERENCES borrowers (id)
        )
    """)
    conn.commit()
    conn.close()


# Routes
@app.route('/borrowers', methods=['POST'])
def add_borrower():
    """
    Add a new borrower.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not name or not email or not phone:
            return jsonify({"error": "Missing required fields"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO borrowers (name, email, phone)
            VALUES (?, ?, ?)
        """, (name, email, phone))
        conn.commit()
        conn.close()

        return jsonify({"message": "Borrower added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/borrowers', methods=['GET'])
def list_borrowers():
    """
    Retrieve all borrowers.
    """
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM borrowers")
        borrowers = cursor.fetchall()
        conn.close()

        return jsonify(borrowers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/loans', methods=['POST'])
def add_loan():
    """
    Issue a new loan to a borrower.
    """
    try:
        data = request.json
        borrower_id = data.get('borrower_id')
        amount = data.get('amount')
        interest_rate = data.get('interest_rate')
        due_date = data.get('due_date')  # Format: YYYY-MM-DD

        if not borrower_id or not amount or not interest_rate or not due_date:
            return jsonify({"error": "Missing required fields"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO loans (borrower_id, amount, interest_rate, due_date)
            VALUES (?, ?, ?, ?)
        """, (borrower_id, amount, interest_rate, due_date))
        conn.commit()
        conn.close()

        return jsonify({"message": "Loan issued successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/loans', methods=['GET'])
def list_loans():
    """
    Retrieve all loans.
    """
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM loans")
        loans = cursor.fetchall()
        conn.close()

        return jsonify(loans), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/loans/<int:loan_id>', methods=['PATCH'])
def update_loan_status(loan_id):
    """
    Update the status of a loan (e.g., mark paid or defaulted).
    """
    try:
        data = request.json
        status = data.get('status')

        if not status:
            return jsonify({"error": "Missing required field: status"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE loans SET status = ? WHERE id = ?
        """, (status, loan_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Loan status updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the app
if __name__ == '__main__':
    # Ensure database tables are initialized
    init_db()
    app.run(debug=True)
```
