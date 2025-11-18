"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Recommend tools or libraries for creating a case study repository system, inspired by the thought-provoking articles and case studies mentioned in Celestia's Études Newsletter.
Generated: DETERMINISTIC_b6f0a68f3ca43a6b
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for creating a case study repository system using Flask and SQLite. This code includes proper error handling, is well-documented, and follows best practices.

```python
"""
Case Study Repository System
Inspired by Celestia's Études Newsletter.

This system provides an API for managing case studies with features like:
- Adding new case studies
- Retrieving all case studies
- Retrieving a specific case study by ID
- Updating existing case studies
- Deleting case studies

Tech Stack:
- Backend: Flask (Python Web Framework)
- Database: SQLite (Lightweight Database)
"""

from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

DATABASE = 'case_studies.db'

# Helper function to connect to the database
def create_connection():
    """Establish connection to SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None

# Initialize the SQLite database
def initialize_database():
    """Create the table for case studies if it doesn't exist."""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS case_studies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()
        except Error as e:
            print(f"Database initialization error: {e}")
        finally:
            conn.close()

# Route: Add a new case study
@app.route('/case_studies', methods=['POST'])
def add_case_study():
    """API endpoint to add a new case study."""
    try:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        content = data.get('content')

        if not title or not author or not content:
            return jsonify({"error": "Missing required fields"}), 400

        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO case_studies (title, author, content)
            VALUES (?, ?, ?)
            """, (title, author, content))
            conn.commit()
            return jsonify({"message": "Case study added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Route: Retrieve all case studies
@app.route('/case_studies', methods=['GET'])
def get_all_case_studies():
    """API endpoint to retrieve all case studies."""
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM case_studies")
            rows = cursor.fetchall()
            case_studies = [
                {"id": row[0], "title": row[1], "author": row[2], "content": row[3], "created_at": row[4]}
                for row in rows
            ]
            return jsonify(case_studies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Route: Retrieve a specific case study by ID
@app.route('/case_studies/<int:id>', methods=['GET'])
def get_case_study(id):
    """API endpoint to retrieve a specific case study by ID."""
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM case_studies WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                case_study = {"id": row[0], "title": row[1], "author": row[2], "content": row[3], "created_at": row[4]}
                return jsonify(case_study), 200
            else:
                return jsonify({"error": "Case study not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Route: Update a case study
@app.route('/case_studies/<int:id>', methods=['PUT'])
def update_case_study(id):
    """API endpoint to update a specific case study."""
    try:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        content = data.get('content')

        if not title or not author or not content:
            return jsonify({"error": "Missing required fields"}), 400

        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE case_studies
            SET title = ?, author = ?, content = ?
            WHERE id = ?
            """, (title, author, content, id))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Case study not found"}), 404
            return jsonify({"message": "Case study updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Route: Delete a case study
@app.route('/case_studies/<int:id>', methods=['DELETE'])
def delete_case_study(id):
    """API endpoint to delete a specific case study."""
    try:
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM case_studies WHERE id = ?", (id,))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Case study not found"}), 404
            return jsonify({"message": "Case study deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Initialize the database before running the app
initialize_database()

if __name__ == '__main__':
    app.run(debug=True)
```
