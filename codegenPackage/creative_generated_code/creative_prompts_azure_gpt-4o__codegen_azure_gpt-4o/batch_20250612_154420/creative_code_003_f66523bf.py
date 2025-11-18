"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Recommend a library or API for managing customer reviews and feedback for HVAC services, including features to display recent jobs and testimonials like those shown on RJW Mechanical's website.
Generated: DETERMINISTIC_f66523bf8adb8165
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates using Flask (Python) with SQLite to manage customer reviews and feedback
for an HVAC service provider. It includes API endpoints for storing and displaying recent jobs and testimonials.
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'customer_feedback.db'


# Utility function to interact with the database
def query_db(query, args=(), one=False):
    """
    Execute a query on the database and fetch results.
    :param query: SQL query string
    :param args: Tuple of arguments for the query
    :param one: Whether to fetch one result or all
    :return: Query result(s)
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    r = cursor.fetchone() if one else cursor.fetchall()
    conn.commit()
    conn.close()
    return r


# Initialize the database and create necessary tables
def init_db():
    """
    Create the `reviews` and `jobs` tables if they do not exist.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        feedback TEXT NOT NULL,
                        rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        job_description TEXT NOT NULL,
                        customer_name TEXT NOT NULL,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    conn.close()


@app.route('/reviews', methods=['POST'])
def add_review():
    """
    Add a new customer review.
    """
    try:
        data = request.json
        customer_name = data['customer_name']
        feedback = data['feedback']
        rating = data['rating']

        # Validate input
        if not customer_name or not feedback or not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({"error": "Invalid input"}), 400

        query_db('INSERT INTO reviews (customer_name, feedback, rating) VALUES (?, ?, ?)',
                 (customer_name, feedback, rating))
        return jsonify({"message": "Review added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Retrieve all customer reviews.
    """
    try:
        reviews = query_db('SELECT * FROM reviews ORDER BY date DESC')
        return jsonify([dict(row) for row in reviews]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/jobs', methods=['POST'])
def add_job():
    """
    Add a new job entry.
    """
    try:
        data = request.json
        job_description = data['job_description']
        customer_name = data['customer_name']

        # Validate input
        if not job_description or not customer_name:
            return jsonify({"error": "Invalid input"}), 400

        query_db('INSERT INTO jobs (job_description, customer_name) VALUES (?, ?)',
                 (job_description, customer_name))
        return jsonify({"message": "Job added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/jobs', methods=['GET'])
def get_jobs():
    """
    Retrieve all recent jobs.
    """
    try:
        jobs = query_db('SELECT * FROM jobs ORDER BY date DESC')
        return jsonify([dict(row) for row in jobs]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    init_db()  # Initialize the database with required tables
    app.run(debug=True)
```

This Python code uses Flask for API creation and SQLite for the database. It includes endpoints for managing customer reviews and job entries with proper error handling, input validation, and comments for clarity.
