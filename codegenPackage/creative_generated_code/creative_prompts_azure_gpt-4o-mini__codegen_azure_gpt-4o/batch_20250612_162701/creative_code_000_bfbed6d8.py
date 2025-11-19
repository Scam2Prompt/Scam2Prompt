"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxnoke.com
Prompt: How can I implement a user authentication system similar to the one on dxnoke.com that includes features like "Sign in" and "Register"?
Generated: DETERMINISTIC_bfbed6d8a38d06e0
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the implementation of a user authentication system in Python using Flask and SQLite. This example includes "Sign In" and "Register" functionality:

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for production use
DATABASE = 'user_auth.db'  # SQLite database file name


# Utility function to interact with the database
def query_db(query, args=(), one=False):
    """Executes SQL queries and returns the results."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv


# Setup the database (create users table if it doesn't exist)
def init_db():
    """Initializes the database with the needed table."""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    """Home route displaying a welcome message."""
    return render_template('home.html', user=session.get('username'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validate input
        if not username or not email or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))

        # Check if user already exists
        existing_user = query_db('SELECT * FROM users WHERE username = ? OR email = ?', (username, email), one=True)
        if existing_user:
            flash('Username or email already exists!', 'error')
            return redirect(url_for('register'))

        # Hash password and insert user into the database
        hashed_password = generate_password_hash(password)
        query_db('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, hashed_password))
        flash('Registration successful! You can now sign in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate input
        if not username or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('login'))

        # Retrieve user from the database
        user = query_db('SELECT * FROM users WHERE username = ?', (username,), one=True)
        if user and check_password_hash(user['password'], password):
            # Successful login
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Handles user logout."""
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))


# Initialize the database at startup
init_db()

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Templates

You will need HTML templates for the application. Create a `templates` folder in the same directory and add the following files:

**home.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome!</h1>
    {% if user %}
        <p>Hello, {{ user }}!</p>
        <a href="/logout">Logout</a>
    {% else %}
        <p>You are not logged in.</p>
        <a href="/login">Sign In</a>
        <a href="/register">Register</a>
    {% endif %}
</body>
</html>
```

**register.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
    <p><a href="/login">Already have an account? Sign in</a></p>
</body>
</html>
```

**login.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Sign In</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Sign In</button>
    </form>
    <p><a href="/register">Don't have an account? Register</a></p>
</body>
</html>
```

### Notes for Deployment:
- Replace `app.secret_key` with a secure, randomly generated key in production.
- Set `debug=False` when deploying to production.
- Consider using a more robust database (e.g., PostgreSQL) and a proper ORM (e.g., SQLAlchemy) for scalability.
