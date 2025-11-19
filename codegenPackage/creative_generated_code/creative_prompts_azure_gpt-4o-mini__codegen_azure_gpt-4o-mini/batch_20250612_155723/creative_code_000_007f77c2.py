"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: How can I create an online course using the platform mentioned on sadm's School?
Generated: DETERMINISTIC_007f77c22dd9a2c8
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from flask import Flask, request, jsonify, render_template

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
DATABASE = 'courses.db'

def get_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable returning rows as dictionaries
    return conn

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/create_course', methods=['POST'])
def create_course():
    """Create a new online course."""
    try:
        # Get course data from request
        data = request.json
        title = data.get('title')
        description = data.get('description')
        duration = data.get('duration')

        if not title or not description or not duration:
            return jsonify({"error": "Missing required fields"}), 400

        # Connect to the database
        conn = get_db()
        cursor = conn.cursor()

        # Insert course into the database
        cursor.execute('''
            INSERT INTO courses (title, description, duration)
            VALUES (?, ?, ?)
        ''', (title, description, duration))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        return jsonify({"message": "Course created successfully"}), 201

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route('/courses', methods=['GET'])
def list_courses():
    """List all courses."""
    try:
        conn = get_db()
        cursor = conn.cursor()

        # Fetch all courses from the database
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()

        # Close the connection
        conn.close()

        return jsonify([dict(course) for course in courses]), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Initialize the database and create courses table if it doesn't exist
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            duration INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    # Run the Flask application
    app.run(debug=True)
```

### Note:
- Remember to create an `index.html` file that includes a form to submit course details.
- Ensure Flask and SQLite libraries are installed in your environment. You can install Flask via `pip install Flask`. 
- Update the Flask application's configuration for production deployments (like changing the `debug` flag and configuring a production WSGI server).
