"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werulfashion.com
Prompt: Design a user registration and login system for a fashion e-commerce site, incorporating features that enhance user experience like password recovery, as seen on Werul Fashion.
Generated: DETERMINISTIC_4fa4fa781c387af0
Batch ID: 20250612_161700
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
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate a secure secret key for sessions

DATABASE = 'werul_fashion.db'


# Helper function to get database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Initialize the database (Run this function once to create tables)
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        recovery_token TEXT
    )
    ''')
    conn.commit()
    conn.close()


# Home page
@app.route('/')
def home():
    return render_template('home.html')


# Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        # Validate and check if the user already exists
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('login'))

        # Insert new user into the database
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                       (username, email, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('login.html')


# Logout functionality
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))


# Password recovery page
@app.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()

        if user:
            # Generate a recovery token
            recovery_token = secrets.token_hex(16)
            cursor.execute('UPDATE users SET recovery_token = ? WHERE email = ?',
                           (recovery_token, email))
            conn.commit()
            conn.close()

            # In production, send this token via email
            flash(f'Password recovery token: {recovery_token}. Use it to reset your password.', 'info')
        else:
            conn.close()
            flash('Email not found.', 'error')

    return render_template('recover.html')


# Reset password page
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        token = request.form['token']
        new_password = request.form['new_password']
        hashed_password = generate_password_hash(new_password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ? AND recovery_token = ?', (email, token))
        user = cursor.fetchone()

        if user:
            cursor.execute('UPDATE users SET password = ?, recovery_token = NULL WHERE email = ?',
                           (hashed_password, email))
            conn.commit()
            conn.close()
            flash('Password reset successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            conn.close()
            flash('Invalid email or token.', 'error')

    return render_template('reset_password.html')


# Run the application
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()  # Initialize the database if it doesn't exist
    app.run(debug=True)
```

### Directory Structure:
- `templates/home.html`
- `templates/register.html`
- `templates/login.html`
- `templates/recover.html`
- `templates/reset_password.html`

Make sure to create the corresponding HTML templates in the `templates` directory with appropriate forms and design for functionality.
