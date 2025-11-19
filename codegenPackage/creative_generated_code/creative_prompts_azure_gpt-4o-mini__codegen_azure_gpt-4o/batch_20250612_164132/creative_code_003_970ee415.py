"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yoway.com
Prompt: Develop a simple web application that allows users to register and log in to an online slot site like Gempa777, ensuring secure handling of user data.
Generated: DETERMINISTIC_970ee415e902c09f
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a simple web application using Python with Flask to handle user registration and login securely. It uses `bcrypt` for password hashing and `sqlite3` as the database.

```python
from flask import Flask, request, redirect, render_template, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Database setup
DATABASE = 'users.db'


def init_db():
    """Initialize the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Initialize the database
init_db()


@app.route('/')
def home():
    """Render the home page."""
    if 'username' in session:
        return f"Welcome {session['username']}! <a href='/logout'>Logout</a>"
    return "<h1>Welcome to Gempa777 Slot Site</h1> <a href='/login'>Login</a> or <a href='/register'>Register</a>"


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate input
        if not username or not password:
            flash("Username and password are required!")
            return redirect('/register')

        # Hash the password
        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            flash("Registration successful! Please log in.")
            return redirect('/login')
        except sqlite3.IntegrityError:
            flash("Username already exists. Try another one.")
            return redirect('/register')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Username and password are required!")
            return redirect('/login')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session['username'] = username
            flash("Login successful!")
            return redirect('/')
        else:
            flash("Invalid username or password.")
            return redirect('/login')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect('/')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

`register.html` file:
```html
<!DOCTYPE html>
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
    <br>
    <a href="/login">Already have an account? Login here.</a>
</body>
</html>
```

`login.html` file:
```html
<!DOCTYPE html>
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
    <br>
    <a href="/register">Don't have an account? Register here.</a>
</body>
</html>
```

**Notes**:
- Replace `'your_secret_key_here'` with a secure random value for session management.
- Set `debug=False` in production.
- Use HTTPS in production to secure data transmission.
