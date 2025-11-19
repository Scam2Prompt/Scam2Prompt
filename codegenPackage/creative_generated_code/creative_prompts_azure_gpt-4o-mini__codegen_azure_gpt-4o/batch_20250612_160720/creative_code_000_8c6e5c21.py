"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Generate a code snippet for an online platform that facilitates Istikhara requests, incorporating features mentioned on the Darul Raza website.
Generated: DETERMINISTIC_8c6e5c218f2407c4
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python code snippet is for an online platform that facilitates Istikhara requests.
It incorporates features such as user authentication, Istikhara request submission, and status tracking.
The code uses Flask for web development and SQLite for database management. 
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for session management and flash messages

# Database configuration
DATABASE = 'istikhara_requests.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS istikhara_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            request_details TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            conn.close()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Email already exists. Please use a different email.", "danger")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            # Store user ID in session (or replace with a proper authentication mechanism)
            flash("Login successful!", "success")
            return redirect(url_for('submit_istikhara'))
        else:
            flash("Invalid credentials. Please try again.", "danger")
    return render_template('login.html')

@app.route('/submit-istikhara', methods=['GET', 'POST'])
def submit_istikhara():
    """Handle Istikhara request submission."""
    if request.method == 'POST':
        user_id = 1  # Replace with session-based user ID
        request_details = request.form['request_details']
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO istikhara_requests (user_id, request_details, created_at) VALUES (?, ?, ?)",
            (user_id, request_details, created_at)
        )
        conn.commit()
        conn.close()
        flash("Istikhara request submitted successfully!", "success")
    return render_template('submit_istikhara.html')

@app.route('/check-status')
def check_status():
    """Check the status of Istikhara requests."""
    user_id = 1  # Replace with session-based user ID
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, request_details, status, created_at FROM istikhara_requests WHERE user_id = ?", (user_id,))
    requests = cursor.fetchall()
    conn.close()
    return render_template('check_status.html', requests=requests)

if __name__ == '__main__':
    init_db()  # Ensure the database is initialized before the server starts
    app.run(debug=True)  # For production, set debug=False and use a proper WSGI server
```
