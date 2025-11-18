"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Suggest an open-source tool or library for managing bilingual education programs, similar to the Greenwich platform used by the Politécnico Municipal de Cali, and provide an example of how to integrate it into a school's system.
Generated: DETERMINISTIC_4d63ccfdf88d4210
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This example demonstrates using an open-source library called "Flask" to build a simple API for managing bilingual education programs.
Flask is a lightweight Python web framework that can be used to integrate a system for managing bilingual education programs into a school's system.

The API allows the creation and querying of programs, students, and courses.
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'school_system.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Initialize the database with tables for bilingual programs
def init_db():
    conn = get_db_connection()
    if conn:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS programs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    program_id INTEGER,
                    FOREIGN KEY(program_id) REFERENCES programs(id)
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    program_id INTEGER,
                    FOREIGN KEY(program_id) REFERENCES programs(id)
                )
            ''')
            print("Database initialized successfully.")
    else:
        print("Failed to initialize the database.")

# Endpoint to create a new bilingual program
@app.route('/programs', methods=['POST'])
def create_program():
    data = request.json
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({"error": "Program name is required"}), 400

    conn = get_db_connection()
    if conn:
        try:
            with conn:
                conn.execute(
                    'INSERT INTO programs (name, description) VALUES (?, ?)',
                    (name, description)
                )
            return jsonify({"message": "Program created successfully"}), 201
        except sqlite3.Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

# Endpoint to retrieve all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    conn = get_db_connection()
    if conn:
        try:
            programs = conn.execute('SELECT * FROM programs').fetchall()
            return jsonify([dict(program) for program in programs]), 200
        except sqlite3.Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

# Endpoint to add a student to a program
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    name = data.get('name')
    program_id = data.get('program_id')

    if not name or not program_id:
        return jsonify({"error": "Student name and program ID are required"}), 400

    conn = get_db_connection()
    if conn:
        try:
            with conn:
                conn.execute(
                    'INSERT INTO students (name, program_id) VALUES (?, ?)',
                    (name, program_id)
                )
            return jsonify({"message": "Student added successfully"}), 201
        except sqlite3.Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

# Endpoint to retrieve all students in a program
@app.route('/programs/<int:program_id>/students', methods=['GET'])
def get_students_in_program(program_id):
    conn = get_db_connection()
    if conn:
        try:
            students = conn.execute(
                'SELECT * FROM students WHERE program_id = ?',
                (program_id,)
            ).fetchall()
            return jsonify([dict(student) for student in students]), 200
        except sqlite3.Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

# Initialize database before starting the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

This code sets up a basic API using Flask to manage bilingual education programs. It includes endpoints for creating programs, adding students, and retrieving information. It uses SQLite as the database, provides error handling, and follows Python best practices.
