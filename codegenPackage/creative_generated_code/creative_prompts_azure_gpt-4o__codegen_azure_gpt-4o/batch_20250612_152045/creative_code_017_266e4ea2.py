"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Develop a web application for society management, using the features described in MDA Tech Sys's society software offerings.
Generated: DETERMINISTIC_266e4ea2104773f0
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: A web application for society management using Flask framework.

from flask import Flask, jsonify, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Database file name
DATABASE = 'society_management.db'


def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file.
    :param db_file: Database file path
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error while connecting to database: {e}")
        return None


def create_tables():
    """
    Create necessary tables in the database for society management.
    """
    conn = create_connection(DATABASE)
    if conn is None:
        print("Error! Cannot create tables in database.")
        return

    try:
        # Create tables for Members, Complaints, Payments
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    flat_number TEXT NOT NULL UNIQUE,
                    contact TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending',
                    FOREIGN KEY (member_id) REFERENCES Members (id)
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    payment_date TEXT NOT NULL,
                    FOREIGN KEY (member_id) REFERENCES Members (id)
                )
            """)
        print("Tables created successfully.")
    except Error as e:
        print(f"Error while creating tables: {e}")
    finally:
        conn.close()


@app.route('/members', methods=['POST'])
def add_member():
    """
    Add a new member to the society.
    """
    data = request.json
    name = data.get('name')
    flat_number = data.get('flat_number')
    contact = data.get('contact')

    if not name or not flat_number or not contact:
        return jsonify({"error": "Missing required fields"}), 400

    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn:
            conn.execute("""
                INSERT INTO Members (name, flat_number, contact)
                VALUES (?, ?, ?)
            """, (name, flat_number, contact))
        return jsonify({"message": "Member added successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Flat number already exists"}), 409
    except Error as e:
        print(f"Error while adding member: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()


@app.route('/members', methods=['GET'])
def get_members():
    """
    Retrieve all members of the society.
    """
    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn:
            cursor = conn.execute("SELECT * FROM Members")
            members = [
                {"id": row[0], "name": row[1], "flat_number": row[2], "contact": row[3]}
                for row in cursor.fetchall()
            ]
        return jsonify(members), 200
    except Error as e:
        print(f"Error while retrieving members: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()


@app.route('/complaints', methods=['POST'])
def add_complaint():
    """
    Add a new complaint for a member.
    """
    data = request.json
    member_id = data.get('member_id')
    description = data.get('description')

    if not member_id or not description:
        return jsonify({"error": "Missing required fields"}), 400

    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn:
            conn.execute("""
                INSERT INTO Complaints (member_id, description)
                VALUES (?, ?)
            """, (member_id, description))
        return jsonify({"message": "Complaint added successfully"}), 201
    except Error as e:
        print(f"Error while adding complaint: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()


@app.route('/complaints', methods=['GET'])
def get_complaints():
    """
    Retrieve all complaints.
    """
    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn:
            cursor = conn.execute("SELECT * FROM Complaints")
            complaints = [
                {"id": row[0], "member_id": row[1], "description": row[2], "status": row[3]}
                for row in cursor.fetchall()
            ]
        return jsonify(complaints), 200
    except Error as e:
        print(f"Error while retrieving complaints: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()


@app.route('/payments', methods=['POST'])
def add_payment():
    """
    Add a payment record for a member.
    """
    data = request.json
    member_id = data.get('member_id')
    amount = data.get('amount')
    payment_date = data.get('payment_date')

    if not member_id or not amount or not payment_date:
        return jsonify({"error": "Missing required fields"}), 400

    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn:
            conn.execute("""
                INSERT INTO Payments (member_id, amount, payment_date)
                VALUES (?, ?, ?)
            """, (member_id, amount, payment_date))
        return jsonify({"message": "Payment added successfully"}), 201
    except Error as e:
        print(f"Error while adding payment: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()


@app.route('/payments', methods=['GET'])
def get_payments():
    """
    Retrieve all payment records.
    """
    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        with conn:
            cursor = conn.execute("SELECT * FROM Payments")
            payments = [
                {"id": row[0], "member_id": row[1], "amount": row[2], "payment_date": row[3]}
                for row in cursor.fetchall()
            ]
        return jsonify(payments), 200
    except Error as e:
        print(f"Error while retrieving payments: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()


if __name__ == '__main__':
    # Create database tables if they don't exist
    create_tables()
    
    # Start the Flask application
    app.run(debug=True)
```
