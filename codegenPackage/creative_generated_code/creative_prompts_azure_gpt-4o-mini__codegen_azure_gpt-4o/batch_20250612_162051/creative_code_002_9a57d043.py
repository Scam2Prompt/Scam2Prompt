"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grenoble-boxe.fr
Prompt: What are the best practices for implementing a membership management system for GRENOBLE BOXE on TEAMMHIYAOUI.COM?
Generated: DETERMINISTIC_9a57d0434a4978c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import datetime
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Database setup: SQLite connection
DATABASE = 'grenoble_boxe.db'

def init_db():
    """
    Initialize the database with necessary tables.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create members table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            membership_status TEXT NOT NULL, -- active, expired, etc.
            join_date DATE NOT NULL,
            expiry_date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.before_first_request
def setup():
    """
    Ensure the database is initialized before the first request.
    """
    init_db()

# Helper function to connect to the database
def db_connection():
    """
    Create a database connection.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

# Route: Add a new member to the system
@app.route('/members', methods=['POST'])
def add_member():
    """
    Endpoint to add a new member.
    Expects JSON payload with first_name, last_name, email, phone, and membership duration (in months).
    """
    try:
        data = request.json
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone = data.get('phone', None)
        membership_duration = int(data['membership_duration'])  # in months

        join_date = datetime.date.today()
        expiry_date = join_date + datetime.timedelta(days=membership_duration * 30)

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO members (first_name, last_name, email, phone, membership_status, join_date, expiry_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, phone, 'active', join_date, expiry_date))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Member added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route: Get all members
@app.route('/members', methods=['GET'])
def get_members():
    """
    Endpoint to fetch all members.
    """
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM members')
        members = cursor.fetchall()
        conn.close()

        # Format data into JSON
        member_list = []
        for member in members:
            member_list.append({
                'id': member[0],
                'first_name': member[1],
                'last_name': member[2],
                'email': member[3],
                'phone': member[4],
                'membership_status': member[5],
                'join_date': member[6],
                'expiry_date': member[7],
            })

        return jsonify(member_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route: Update member's membership status
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """
    Endpoint to update a member's information or membership status.
    Expects JSON payload with fields to update.
    """
    try:
        data = request.json
        conn = db_connection()
        cursor = conn.cursor()

        updates = []
        for key, value in data.items():
            updates.append(f"{key} = '{value}'")

        if updates:
            update_query = f"UPDATE members SET {', '.join(updates)} WHERE id = {member_id}"
            cursor.execute(update_query)
            conn.commit()

        conn.close()

        return jsonify({'message': 'Member updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route: Delete a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """
    Endpoint to remove a member from the database.
    """
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Member deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
