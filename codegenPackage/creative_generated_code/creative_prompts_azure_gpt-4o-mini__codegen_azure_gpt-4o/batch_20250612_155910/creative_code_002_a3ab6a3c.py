"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiohuitakafusa.com
Prompt: Create an API endpoint that allows students to enroll in "Auxiliar en Preescolar" courses at Colegio Huitaka Fusagasugá.
Generated: DETERMINISTIC_a3ab6a3c6803ebfe
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup (production may use a more robust database like PostgreSQL or MySQL)
DATABASE = 'college.db'

def init_db():
    """Initializes the database if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_email TEXT NOT NULL UNIQUE,
            course_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/api/enroll', methods=['POST'])
def enroll_student():
    """
    Endpoint to enroll a student in 'Auxiliar en Preescolar' course.
    Expects a JSON payload with 'student_name' and 'student_email'.
    """
    try:
        # Parse JSON request payload
        data = request.get_json()
        student_name = data.get('student_name')
        student_email = data.get('student_email')
        course_name = "Auxiliar en Preescolar"

        # Validate required fields
        if not student_name or not student_email:
            return jsonify({"error": "Missing required fields 'student_name' or 'student_email'."}), 400

        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert enrollment record
        cursor.execute('''
            INSERT INTO enrollments (student_name, student_email, course_name)
            VALUES (?, ?, ?)
        ''', (student_name, student_email, course_name))
        conn.commit()

        return jsonify({
            "message": f"Student {student_name} successfully enrolled in '{course_name}' course."
        }), 201

    except sqlite3.IntegrityError:
        # Handle duplicate email error
        return jsonify({"error": "Student with this email is already enrolled."}), 409

    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    finally:
        # Ensure database connection is closed
        if 'conn' in locals():
            conn.close()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
