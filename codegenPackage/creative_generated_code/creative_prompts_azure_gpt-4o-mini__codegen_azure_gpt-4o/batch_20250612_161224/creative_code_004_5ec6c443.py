"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zushi.shop
Prompt: How can I create a login interface for store owners that integrates with a member management system, similar to the one used by ZUSHI WAVE SHOP?
Generated: DETERMINISTIC_5ec6c443a2ccc51d
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is production-ready Python code using the Flask framework for building a login interface for store owners that integrates with a member management system. This example assumes a database connection (SQLite for this demo) and uses hashed passwords for security.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Database file name
DATABASE = 'store_owners.db'

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows dictionary-like access to rows
    return conn

# Route: Homepage (Login Page)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate input
        if not username or not password:
            flash('Username and password are required!', 'error')
            return redirect(url_for('login'))

        # Database query to find the user
        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM store_owners WHERE username = ?', (username,)
        ).fetchone()
        conn.close()

        # Check if user exists and password matches
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

# Route: Dashboard (After Login)
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))

    return render_template('dashboard.html', username=session['username'])

# Route: Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

# Route: For initial setup - Add store owners (Admin-only functionality)
@app.route('/add_store_owner', methods=['POST'])
def add_store_owner():
    # This route is for demonstration purposes. Ideally, it should be protected (e.g., admin access only)
    username = request.form['username']
    password = request.form['password']
    
    # Validate input
    if not username or not password:
        flash('Username and password are required!', 'error')
        return redirect(url_for('add_store_owner'))

    hashed_password = generate_password_hash(password, method='sha256')

    # Insert new store owner into the database
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO store_owners (username, password) VALUES (?, ?)',
        (username, hashed_password)
    )
    conn.commit()
    conn.close()

    flash('Store owner added successfully!', 'success')
    return redirect(url_for('login'))

# Create the database schema (Run this once for setup)
def setup_database():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS store_owners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Main entry point
if __name__ == '__main__':
    setup_database()  # Ensure the database schema exists
    app.run(debug=True)
```

### Directory Structure
Ensure you have the following files in place:
- `templates/login.html` (Login Page HTML)
- `templates/dashboard.html` (Dashboard Page HTML)

### Example HTML (`login.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
</head>
<body>
    <h1>Store Owner Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

### Example HTML (`dashboard.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
    <p>This is your dashboard.</p>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

Make sure to install Flask and Werkzeug before running the code:
```bash
pip install flask werkzeug
```
