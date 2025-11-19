"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: "Write a Python code snippet to create a financial advisory platform for corporates and entrepreneurs in Africa, including fundraising and investment management features."
Generated: DETERMINISTIC_2431c157fc7918af
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'financial_advisory.db'

def init_db():
    """Initialize the database with required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                role TEXT CHECK(role IN ('corporate', 'entrepreneur')) NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS investments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL NOT NULL,
                investment_type TEXT NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user (corporate or entrepreneur)."""
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'role' not in data:
        raise BadRequest("Missing required fields: name, email, role")

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, email, role) VALUES (?, ?, ?)
            ''', (data['name'], data['email'], data['role']))
            conn.commit()
            return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400

@app.route('/invest', methods=['POST'])
def make_investment():
    """Record a new investment made by a user."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'amount' not in data or 'investment_type' not in data:
        raise BadRequest("Missing required fields: user_id, amount, investment_type")

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO investments (user_id, amount, investment_type) VALUES (?, ?, ?)
            ''', (data['user_id'], data['amount'], data['investment_type']))
            conn.commit()
            return jsonify({"message": "Investment recorded successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 400

@app.route('/investments/<int:user_id>', methods=['GET'])
def get_investments(user_id):
    """Retrieve all investments made by a specific user."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM investments WHERE user_id = ?
            ''', (user_id,))
            investments = cursor.fetchall()
            return jsonify(investments), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```
