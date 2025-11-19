"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcoins.net
Prompt: Create a simple web application that allows users to register and log in to Claimcoins, utilizing their payment proof system.
Generated: DETERMINISTIC_fd80eb24586df315
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a simple web application using Flask that allows users to register and log in to Claimcoins. The application includes a payment proof system for registration validation:

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session

# Database file
DATABASE = "claimcoins.db"

# Create database and tables if they don't exist
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            payment_proof TEXT NOT NULL
        );
        """)
        conn.commit()

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        payment_proof = request.form['payment_proof']

        # Validate form inputs
        if not username or not password or not payment_proof:
            flash("All fields are required!", "error")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        try:
            # Insert user into database
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO users (username, password, payment_proof)
                VALUES (?, ?, ?);
                """, (username, hashed_password, payment_proof))
                conn.commit()
            flash("Registration successful! You can now log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Choose a different username.", "error")
            return redirect(url_for('register'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("All fields are required!", "error")
            return redirect(url_for('login'))

        try:
            # Retrieve user from database
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username = ?;", (username,))
                user = cursor.fetchone()

            if user and check_password_hash(user[2], password):
                # Successful login
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash("Login successful!", "success")
                return redirect(url_for('dashboard'))
            else:
                # Invalid credentials
                flash("Invalid username or password.", "error")
                return redirect(url_for('login'))

        except sqlite3.Error as e:
            flash("An error occurred: " + str(e), "error")
            return redirect(url_for('login'))

    return render_template('login.html')

# Dashboard route (requires login)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        flash("You must be logged in to access the dashboard.", "error")
        return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))

# Start the web application
if __name__ == "__main__":
    init_db()  # Ensure the database is initialized
    app.run(debug=True)
```

### Required HTML Files:
Save the following HTML files in a `templates/` directory:

#### `register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Register - Claimcoins</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <label>Payment Proof:</label>
        <input type="text" name="payment_proof" required><br>
        <button type="submit">Register</button>
    </form>
    <a href="/login">Already have an account? Log in here.</a>
</body>
</html>
```

#### `login.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login - Claimcoins</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    <a href="/register">Don't have an account? Register here.</a>
</body>
</html>
```

#### `dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dashboard - Claimcoins</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
    <p>This is your dashboard.</p>
    <a href="/logout">Logout</a>
</body>
</html>
```
