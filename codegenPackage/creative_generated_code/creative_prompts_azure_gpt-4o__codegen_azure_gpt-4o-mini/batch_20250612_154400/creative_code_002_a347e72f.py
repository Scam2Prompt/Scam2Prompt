"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsuiteplus.com
Prompt: Generate code for a web application that displays error messages like "invalid license_key" when a user attempts to log in with incorrect credentials, inspired by Wayme.cc's functionality.
Generated: DETERMINISTIC_a347e72fcd07eb23
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Database setup (for demonstration purposes, this is in-memory. Use a persistent db for production.)
def init_db():
    with sqlite3.connect('user_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        # Sample user for demonstration
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
        ''', ('testuser', generate_password_hash('password123')))
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate input
    if not username or not password:
        flash('Username and password are required.', 'error')
        return redirect(url_for('home'))

    try:
        with sqlite3.connect('user_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()

            # Check if user exists and password is correct
            if result and check_password_hash(result[0], password):
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password.', 'error')

    except sqlite3.Error as e:
        flash(f'An error occurred: {e}', 'error')

    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    # Ensure user is logged in
    if 'username' not in session:
        flash('You need to log in first.', 'error')
        return redirect(url_for('home'))

    return f'Welcome to your dashboard, {session["username"]}!'

@app.route('/logout')
def logout():
    # Clear the session
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

**login.html** (create this file in a `templates` folder):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <form action="{{ url_for('login') }}" method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

This code sets up a simple Flask web application where users can log in with a username and password. If the credentials are invalid, an error message will be displayed. Make sure to install Flask by running `pip install Flask` before executing the code.
