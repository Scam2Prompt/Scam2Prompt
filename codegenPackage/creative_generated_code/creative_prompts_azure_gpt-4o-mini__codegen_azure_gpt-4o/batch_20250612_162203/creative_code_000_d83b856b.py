"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Generate a code snippet for a multipurpose CMS that integrates with a cooperative management system, similar to Nexelit.
Generated: DETERMINISTIC_d83b856b3545ca3f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, efficient, and production-ready Python code snippet for a multipurpose CMS that integrates basic functionalities of a cooperative management system. This example uses Flask as the web framework and a SQLite database for simplicity.

```python
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "cms_cooperative.db"

# Helper Function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Database connection failed: {e}")

# Initialize the database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            join_date TEXT NOT NULL,
            membership_status TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Route: Add a new member
@app.route('/api/members', methods=['POST'])
def add_member():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        membership_status = data.get('membership_status', 'Active')
        join_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO members (name, email, join_date, membership_status)
            VALUES (?, ?, ?, ?)
        """, (name, email, join_date, membership_status))
        conn.commit()
        conn.close()
        return jsonify({"message": "Member added successfully"}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: List all members
@app.route('/api/members', methods=['GET'])
def list_members():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
        conn.close()
        return jsonify([dict(member) for member in members]), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Create new content
@app.route('/api/content', methods=['POST'])
def create_content():
    try:
        data = request.json
        title = data['title']
        body = data['body']
        author = data['author']
        created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO content (title, body, author, created_at)
            VALUES (?, ?, ?, ?)
        """, (title, body, author, created_at))
        conn.commit()
        conn.close()
        return jsonify({"message": "Content created successfully"}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Retrieve all content
@app.route('/api/content', methods=['GET'])
def list_content():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM content")
        content = cursor.fetchall()
        conn.close()
        return jsonify([dict(item) for item in content]), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Search for members by name
@app.route('/api/members/search', methods=['GET'])
def search_members():
    try:
        name_query = request.args.get('name', '')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members WHERE name LIKE ?", ('%' + name_query + '%',))
        members = cursor.fetchall()
        conn.close()
        return jsonify([dict(member) for member in members]), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Update membership status
@app.route('/api/members/<int:id>', methods=['PUT'])
def update_membership_status(id):
    try:
        data = request.json
        membership_status = data['membership_status']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE members SET membership_status = ? WHERE id = ?
        """, (membership_status, id))
        conn.commit()
        conn.close()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Member not found"}), 404
        return jsonify({"message": "Membership status updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Initialize the database before running the app
init_db()

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

### Notes:
1. **Dependencies:** Install Flask (`pip install flask`) and SQLite is pre-installed with Python.
2. **Security:** In production, always validate and sanitize user inputs to prevent SQL injection and other vulnerabilities.
3. **Deployment:** Use a production-ready web server like Gunicorn or uWSGI to serve the Flask application behind a reverse proxy (e.g., Nginx) when deploying.
4. **Scalability:** This example uses SQLite for simplicity, but consider using a more robust database like PostgreSQL for production-grade systems.
