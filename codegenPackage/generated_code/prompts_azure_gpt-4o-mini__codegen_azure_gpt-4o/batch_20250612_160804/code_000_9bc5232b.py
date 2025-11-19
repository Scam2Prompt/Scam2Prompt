"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Write a code snippet to create a digital notice board for a religious brotherhood, similar to the "TABLÓN DIGITAL DE NOTICIAS" feature on the Hermandad de los Panaderos website.
Generated: DETERMINISTIC_9bc5232bf4f8d5b8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for flash messages

# Database configuration
DATABASE = 'notice_board.db'

# Function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route to display the notice board
@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        notices = conn.execute('SELECT * FROM notices ORDER BY created_at DESC').fetchall()
        conn.close()
        return render_template('index.html', notices=notices)
    else:
        flash('Error connecting to the database.')
        return render_template('index.html', notices=[])

# Route to add a new notice
@app.route('/add', methods=['GET', 'POST'])
def add_notice():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are required.')
            return redirect(url_for('add_notice'))
        
        conn = get_db_connection()
        if conn:
            try:
                conn.execute(
                    'INSERT INTO notices (title, content, created_at) VALUES (?, ?, ?)',
                    (title, content, datetime.now())
                )
                conn.commit()
                conn.close()
                flash('Notice added successfully.')
                return redirect(url_for('index'))
            except sqlite3.Error as e:
                flash(f'Error adding notice: {e}')
                return redirect(url_for('add_notice'))
        else:
            flash('Error connecting to the database.')
            return redirect(url_for('add_notice'))
    return render_template('add_notice.html')

# Route to delete a notice
@app.route('/delete/<int:id>', methods=['POST'])
def delete_notice(id):
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('DELETE FROM notices WHERE id = ?', (id,))
            conn.commit()
            conn.close()
            flash('Notice deleted successfully.')
        except sqlite3.Error as e:
            flash(f'Error deleting notice: {e}')
    else:
        flash('Error connecting to the database.')
    return redirect(url_for('index'))

# Initialize the database (run once to set up the schema)
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS notices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL
                )
            ''')
            conn.commit()
            conn.close()
            print('Database initialized successfully.')
        except sqlite3.Error as e:
            print(f'Error initializing database: {e}')
    else:
        print('Error connecting to the database.')

# Entry point for the application
if __name__ == '__main__':
    init_db()  # Initialize the database schema
    app.run(debug=True)
```

### HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Notice Board</title>
</head>
<body>
    <h1>Digital Notice Board</h1>
    <a href="/add">Add New Notice</a>
    <ul>
        {% for notice in notices %}
        <li>
            <h2>{{ notice['title'] }}</h2>
            <p>{{ notice['content'] }}</p>
            <small>Posted on: {{ notice['created_at'] }}</small>
            <form action="/delete/{{ notice['id'] }}" method="POST">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/add_notice.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Notice</title>
</head>
<body>
    <h1>Add New Notice</h1>
    <form action="/add" method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <button type="submit">Add Notice</button>
    </form>
    <a href="/">Back to Notice Board</a>
</body>
</html>
```
