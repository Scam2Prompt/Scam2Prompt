"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-shop-dev.myshopify.com
Prompt: How can I implement password protection for an e-commerce store like the Coinbase Shop Dev?
Generated: DETERMINISTIC_3256b3581ada84c7
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a production-ready Python implementation of password protection using Flask for an e-commerce store. This example demonstrates user authentication (registration and login) and password hashing using `werkzeug.security`. It stores user credentials in an SQLite database.

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace this with a strong secret key for session management

DATABASE = 'ecommerce_store.db'

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries for easier access
    return conn

# Create the database schema if it doesn't exist
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Route for the home page
@app.route('/')
def home():
    # Render the home page
    return render_template('home.html', username=session.get('username'))

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Username and password are required!', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')

        try:
            conn = get_db_connection()
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

# Initialize the database schema
init_db()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
The `templates` directory should contain the following HTML files:

#### **home.html**
```html
<!doctype html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    {% if username %}
        <h1>Welcome, {{ username }}!</h1>
        <a href="{{ url_for('logout') }}">Logout</a>
    {% else %}
        <h1>Welcome to the E-commerce Store!</h1>
        <a href="{{ url_for('login') }}">Login</a> |
        <a href="{{ url_for('register') }}">Register</a>
    {% endif %}
</body>
</html>
```

#### **register.html**
```html
<!doctype html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
    <a href="{{ url_for('login') }}">Already have an account? Login here.</a>
</body>
</html>
```

#### **login.html**
```html
<!doctype html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
    <a href="{{ url_for('register') }}">Don't have an account? Register here.</a>
</body>
</html>
```

Ensure you have Flask installed (`pip install flask`) and set up a proper production environment if deploying this code.
