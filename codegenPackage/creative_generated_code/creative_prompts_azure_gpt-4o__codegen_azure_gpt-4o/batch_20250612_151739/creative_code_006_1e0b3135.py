"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Generate code for a searchable database of aviation training courses, including filters for course types like "Avsec Supervisor Course" and "Avsec Management Course," inspired by the Welwitschia Aviation offerings.
Generated: DETERMINISTIC_1e0b3135992cabae
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
DATABASE = 'aviation_courses.db'

def initialize_database():
    """Initialize the database with aviation courses."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Create courses table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            course_type TEXT NOT NULL
        )
    ''')

    # Insert sample data (Inspired by Welwitschia Aviation)
    sample_courses = [
        ("Avsec Supervisor Course", "Training for aviation security supervisors.", "Avsec Supervisor"),
        ("Avsec Management Course", "Advanced training for aviation security managers.", "Avsec Management"),
        ("Flight Operations Course", "Training for flight operations personnel.", "Flight Operations"),
        ("Aircraft Maintenance Course", "Training for aircraft maintenance technicians.", "Maintenance"),
    ]

    cursor.executemany('''
        INSERT INTO courses (name, description, course_type)
        VALUES (?, ?, ?)
    ''', sample_courses)

    connection.commit()
    connection.close()

# Initialize the database
initialize_database()

# API routes
@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Fetch courses from the database, with optional filters for course type.
    Example query: /courses?course_type=Avsec Supervisor
    """
    try:
        # Connect to the database
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        # Parse query parameters
        course_type = request.args.get('course_type')

        # Build SQL query with optional filtering
        if course_type:
            cursor.execute('''
                SELECT id, name, description, course_type
                FROM courses
                WHERE course_type = ?
            ''', (course_type,))
        else:
            cursor.execute('''
                SELECT id, name, description, course_type
                FROM courses
            ''')

        # Fetch results and format them as a list of dictionaries
        rows = cursor.fetchall()
        courses = [
            {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "course_type": row[3]
            }
            for row in rows
        ]

        connection.close()
        return jsonify(courses), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/courses', methods=['POST'])
def add_course():
    """
    Add a new course to the database. Expects JSON data:
    {
        "name": "Course Name",
        "description": "Course Description",
        "course_type": "Course Type"
    }
    """
    try:
        # Parse input data
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        course_type = data.get('course_type')

        # Validate input
        if not name or not description or not course_type:
            return jsonify({"error": "Missing required fields"}), 400

        # Connect to the database
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        # Insert new course into the database
        cursor.execute('''
            INSERT INTO courses (name, description, course_type)
            VALUES (?, ?, ?)
        ''', (name, description, course_type))

        connection.commit()
        connection.close()

        return jsonify({"message": "Course added successfully"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
