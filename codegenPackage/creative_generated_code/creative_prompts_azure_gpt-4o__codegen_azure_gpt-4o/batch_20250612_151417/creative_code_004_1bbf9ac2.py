"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Suggest APIs or tools to implement a seamless online test support system for employability skill assessment, inspired by SMART Training Resources' methodology.
Generated: DETERMINISTIC_1bbf9ac2b16a6a24
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Online Test Support System for Employability Skill Assessment
This Python script provides a skeleton implementation using Flask for the backend API. 
The APIs handle user registration, test management, and skill assessment.
You can extend this based on SMART Training Resources' methodology.

Requirements:
- Install Flask: `pip install flask`
- Install SQLite for lightweight database management.
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
DB_FILE = 'online_test_system.db'

def initialize_database():
    """Initialize the database with required tables."""
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            max_score INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_tests (
            user_id INTEGER,
            test_id INTEGER,
            score INTEGER,
            PRIMARY KEY (user_id, test_id),
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (test_id) REFERENCES tests (id)
        )
    ''')
    connection.commit()
    connection.close()

# Initialize the database at startup
initialize_database()

# API Endpoints

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    Payload: { "name": "<name>", "email": "<email>", "password": "<password>" }
    """
    data = request.json
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', 
                       (data['name'], data['email'], data['password']))
        connection.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/create-test', methods=['POST'])
def create_test():
    """
    Create a new test.
    Payload: { "name": "<test_name>", "description": "<description>", "max_score": <max_score> }
    """
    data = request.json
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO tests (name, description, max_score) VALUES (?, ?, ?)', 
                       (data['name'], data.get('description', ''), data['max_score']))
        connection.commit()
        return jsonify({"message": "Test created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/assign-test', methods=['POST'])
def assign_test():
    """
    Assign a test to a user.
    Payload: { "user_id": <user_id>, "test_id": <test_id>, "score": <score> }
    """
    data = request.json
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user_tests (user_id, test_id, score) VALUES (?, ?, ?)', 
                       (data['user_id'], data['test_id'], data.get('score', 0)))
        connection.commit()
        return jsonify({"message": "Test assigned to user successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User or Test ID does not exist!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/results/<int:user_id>', methods=['GET'])
def get_results(user_id):
    """
    Get test results for a specific user.
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            SELECT t.name, ut.score 
            FROM user_tests ut
            JOIN tests t ON ut.test_id = t.id
            WHERE ut.user_id = ?
        ''', (user_id,))
        results = cursor.fetchall()
        return jsonify({"results": [{"test_name": row[0], "score": row[1]} for row in results]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/all-tests', methods=['GET'])
def get_all_tests():
    """
    Get a list of all available tests.
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, description, max_score FROM tests')
        tests = cursor.fetchall()
        return jsonify({"tests": [{"id": row[0], "name": row[1], "description": row[2], "max_score": row[3]} for row in tests]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# Error handling for invalid routes
@app.errorhandler(404)
def route_not_found(e):
    return jsonify({"error": "Route not found!"}), 404

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
```
