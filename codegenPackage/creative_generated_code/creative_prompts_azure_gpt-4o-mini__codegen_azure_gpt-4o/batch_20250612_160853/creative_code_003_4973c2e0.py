"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masa-x.pages.dev
Prompt: Generate code to create a dashboard that tracks the progress of users completing the MASA Airdrop Quest.
Generated: DETERMINISTIC_4973c2e0608c5816
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up the database file
DATABASE = 'masa_airdrop.db'

# Ensure the database file exists
if not os.path.exists(DATABASE):
    # Create and initialize the database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            progress INTEGER DEFAULT 0,
            total INTEGER DEFAULT 100
        )
        """)
        conn.commit()

# Helper function to interact with the database
def query_db(query, args=(), one=False):
    """Execute queries on the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def dashboard():
    """
    Route to render the dashboard page.
    """
    try:
        # Fetch user progress data from the database
        users = query_db("SELECT * FROM users")
        return render_template('dashboard.html', users=users)
    except Exception as e:
        # Handle database errors gracefully
        return jsonify({'error': str(e)}), 500

@app.route('/update_progress', methods=['POST'])
def update_progress():
    """
    Route to update user progress.
    """
    try:
        # Extract data from the request
        username = request.form.get('username')
        progress = request.form.get('progress', type=int)

        if not username or progress is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Update the user's progress in the database
        user = query_db("SELECT * FROM users WHERE username = ?", [username], one=True)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        query_db("UPDATE users SET progress = ? WHERE username = ?", [progress, username])
        return jsonify({'message': 'Progress updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Route to add a new user to the database.
    """
    try:
        # Extract data from the request
        username = request.form.get('username')
        total = request.form.get('total', type=int, default=100)

        if not username or total is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Add the new user to the database
        query_db("INSERT INTO users (username, total) VALUES (?, ?)", [username, total])
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### `dashboard.html` (Frontend Template)
Save this file as `templates/dashboard.html` for rendering the dashboard.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MASA Airdrop Quest Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>MASA Airdrop Quest Dashboard</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Progress</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{ user['id'] }}</td>
                <td>{{ user['username'] }}</td>
                <td>{{ user['progress'] }}</td>
                <td>{{ user['total'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```
