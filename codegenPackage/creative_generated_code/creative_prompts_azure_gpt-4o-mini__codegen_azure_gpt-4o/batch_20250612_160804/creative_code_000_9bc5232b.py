"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hdadpanaderos.es
Prompt: Write a code snippet to create a digital notice board for a religious brotherhood, similar to the "TABLÓN DIGITAL DE NOTICIAS" feature on the Hermandad de los Panaderos website.
Generated: DETERMINISTIC_9bc5232bf4f8d5b8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException
import sqlite3
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a secure random key in production

# Database configuration
DATABASE = 'notice_board.db'

# Function to connect to the database
def connect_db():
    """Establish connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries for easy access
    return conn

# Function to initialize the database
def initialize_db():
    """Create the notices table if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Route: Display notices on the digital notice board
@app.route('/')
def index():
    """Render the notice board with all notices."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notices ORDER BY created_at DESC")
    notices = cursor.fetchall()
    conn.close()
    return render_template('index.html', notices=notices)

# Route: Add a new notice
@app.route('/add', methods=['GET', 'POST'])
def add_notice():
    """Add a new notice to the notice board."""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash("Title and content are required.", "error")
            return redirect(url_for('add_notice'))
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO notices (title, content, created_at)
            VALUES (?, ?, ?)
        """, (title, content, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        
        flash("Notice added successfully!", "success")
        return redirect(url_for('index'))
    
    return render_template('add_notice.html')

# Route: Delete a notice
@app.route('/delete/<int:notice_id>', methods=['POST'])
def delete_notice(notice_id):
    """Delete a specific notice from the notice board."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notices WHERE id = ?", (notice_id,))
        conn.commit()
        conn.close()
        
        flash("Notice deleted successfully!", "success")
    except sqlite3.Error as e:
        flash("An error occurred while deleting the notice.", "error")
    
    return redirect(url_for('index'))

# Error handling
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors by displaying a custom message."""
    return render_template('error.html', error=e), e.code

# Initialize the database
initialize_db()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Directory Structure:
```
project/
├── app.py             # The main Python script
├── notice_board.db    # SQLite database (auto-generated after running the app)
├── templates/
│   ├── index.html     # Template for displaying notices
│   ├── add_notice.html # Template for adding a notice
│   └── error.html     # Template for error handling
├── static/            # Static assets like CSS, images, etc.
```

### Sample Templates
**index.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Notice Board</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Digital Notice Board</h1>
    <a href="/add">Add New Notice</a>
    <ul>
        {% for notice in notices %}
        <li>
            <h3>{{ notice.title }}</h3>
            <p>{{ notice.content }}</p>
            <small>Posted on: {{ notice.created_at }}</small>
            <form action="/delete/{{ notice.id }}" method="POST">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_notice.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Notice</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Add a New Notice</h1>
    <form action="/add" method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Back to Notice Board</a>
</body>
</html>
```

**error.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>{{ error.name }}: {{ error.description }}</p>
    <a href="/">Back to Notice Board</a>
</body>
</html>
```
