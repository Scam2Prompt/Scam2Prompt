"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-redstone.com
Prompt: Write code to integrate the RedStone Expedition roles table into a web application, highlighting special roles and their significance.
Generated: DETERMINISTIC_17b6c6aaccb223b4
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application to integrate RedStone Expedition roles table into a web application

from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    """Establish a database connection and return the cursor."""
    try:
        conn = sqlite3.connect('redstone_roles.db')
        conn.row_factory = sqlite3.Row  # Allows us to access rows as dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Fetch roles from the database
def fetch_roles():
    """Fetch roles from the RedStone Expedition roles table."""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            roles = cursor.fetchall()
            conn.close()
            return roles
        except sqlite3.Error as e:
            print(f"Error fetching roles: {e}")
            return []
    return []

@app.route('/')
def index():
    """Render the homepage with the roles table."""
    roles = fetch_roles()
    # Highlight special roles based on significance
    highlighted_roles = [
        dict(role) | {"highlight": role["significance"] == "High"}
        for role in roles
    ]
    return render_template('index.html', roles=highlighted_roles)

@app.route('/api/roles')
def api_roles():
    """API endpoint to fetch roles in JSON format."""
    roles = fetch_roles()
    return jsonify(roles)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors with a custom message."""
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors with a custom message."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

**Note:** This code assumes:
1. A SQLite database named `redstone_roles.db` exists.
2. A table named `roles` exists with columns such as `id`, `name`, `description`, and `significance`.
3. HTML templates (`index.html`, `404.html`, `500.html`) are set up properly in a `templates` folder.
