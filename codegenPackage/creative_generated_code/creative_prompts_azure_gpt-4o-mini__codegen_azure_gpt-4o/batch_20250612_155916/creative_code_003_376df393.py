"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Describe how to use a specific library to develop an application that showcases innovative construction and remodeling solutions, as highlighted by Fullteco Spa.
Generated: DETERMINISTIC_376df39329f3a3d2
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the Flask framework to showcase innovative construction and remodeling solutions. The code leverages SQLite for data storage and highlights Fullteco Spa's solutions.

```python
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'construction_solutions.db'

# Ensure the database file exists
if not os.path.exists(DATABASE):
    # Create the database and initialize tables
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE solutions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT
        )
    ''')
    conn.commit()
    conn.close()


def get_db_connection():
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None


@app.route('/')
def index():
    """
    Home page route.
    Displays a list of construction and remodeling solutions.
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM solutions')
        solutions = cursor.fetchall()
        conn.close()
        return render_template('index.html', solutions=solutions)
    else:
        return "Error connecting to the database.", 500


@app.route('/add', methods=['GET', 'POST'])
def add_solution():
    """
    Route to add a new construction or remodeling solution.
    Handles both GET (form display) and POST (form submission) requests.
    """
    if request.method == 'POST':
        # Retrieve form data
        title = request.form.get('title')
        description = request.form.get('description')
        image_url = request.form.get('image_url', None)

        # Validate form data
        if not title or not description:
            return "Title and description are required.", 400

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO solutions (title, description, image_url)
                VALUES (?, ?, ?)
            ''', (title, description, image_url))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        else:
            return "Error connecting to the database.", 500

    # For GET requests, render the solution addition form
    return render_template('add.html')


@app.route('/api/solutions', methods=['GET'])
def api_solutions():
    """
    API endpoint to retrieve all solutions in JSON format.
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM solutions')
        solutions = cursor.fetchall()
        conn.close()
        solutions_list = [
            {
                'id': solution[0],
                'title': solution[1],
                'description': solution[2],
                'image_url': solution[3]
            } for solution in solutions
        ]
        return jsonify(solutions_list)
    else:
        return jsonify({'error': 'Error connecting to the database.'}), 500


@app.errorhandler(404)
def page_not_found(error):
    """
    Custom 404 error handler.
    """
    return render_template('404.html'), 404


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Explanation of Code Structure in Comments:
- **Database Setup:** The SQLite database is initialized on the first run to store construction solutions.
- **Flask Application:** Routes include:
  - `/`: Displays a list of solutions.
  - `/add`: Allows users to add new solutions via a form.
  - `/api/solutions`: Provides a JSON API for solutions.
- **Error Handling:** Handles database connection errors and includes a custom 404 page.
- **Best Practices:** Includes validation for form inputs and uses parameterized SQL queries to prevent SQL injection.

### Notes:
- Create accompanying HTML templates (`index.html`, `add.html`, and `404.html`) for the web interface.
- To test the application, install required packages (`flask`) using `pip install flask`.
