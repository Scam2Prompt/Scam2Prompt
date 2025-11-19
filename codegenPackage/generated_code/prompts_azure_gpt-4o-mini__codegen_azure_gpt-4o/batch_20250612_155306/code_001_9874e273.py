"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Write a code snippet that integrates a digital platform for tracking student progress and communication with parents, similar to the services offered by Del Sol Montessori.
Generated: DETERMINISTIC_9874e273d1153223
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE = 'student_progress.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS communication (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Routes for managing students
@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student to the database."""
    try:
        data = request.json
        name = data['name']
        grade = data['grade']
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Student added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students from the database."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        conn.close()
        
        return jsonify({'students': students}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Routes for tracking student progress
@app.route('/progress', methods=['POST'])
def add_progress():
    """Add progress data for a student."""
    try:
        data = request.json
        student_id = data['student_id']
        subject = data['subject']
        score = data['score']
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO progress (student_id, subject, score) VALUES (?, ?, ?)', (student_id, subject, score))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Progress added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/progress/<int:student_id>', methods=['GET'])
def get_progress(student_id):
    """Retrieve progress data for a specific student."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM progress WHERE student_id = ?', (student_id,))
        progress = cursor.fetchall()
        conn.close()
        
        return jsonify({'progress': progress}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Routes for parent communication
@app.route('/communication', methods=['POST'])
def add_communication():
    """Add a communication message for a student."""
    try:
        data = request.json
        student_id = data['student_id']
        message = data['message']
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO communication (student_id, message) VALUES (?, ?)', (student_id, message))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Communication added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/communication/<int:student_id>', methods=['GET'])
def get_communication(student_id):
    """Retrieve communication messages for a specific student."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM communication WHERE student_id = ?', (student_id,))
        communication = cursor.fetchall()
        conn.close()
        
        return jsonify({'communication': communication}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
