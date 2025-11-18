"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puroworldclub.com
Prompt: Provide code to implement a secure membership login system for the Puro World Club website, integrating features for private member access to exclusive cigar offerings.
Generated: DETERMINISTIC_807ac0f83a9d785d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure Membership Login System for Puro World Club Website

This script implements a membership login system with private access to exclusive member offerings. 
It includes secure password hashing, session management, and access control mechanisms.
"""

import bcrypt
import sqlite3
from flask import Flask, request, session, redirect, url_for, render_template
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_super_secret_key'  # Use a strong secret key for session encryption

# Database setup
DB_FILE = 'membership.db'

def init_db():
    """Initializes the database with a members table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()  # Ensure the database is initialized

# Helper functions
def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, password_hash):
    """Checks if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def get_member_by_username(username):
    """Fetches a member record by username."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members WHERE username = ?", (username,))
    member = cursor.fetchone()
    conn.close()
    return member

# Routes
@app.route('/')
def home():
    """Homepage route, provides login/register option."""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Member registration route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            raise BadRequest("Both username and password are required.")
        
        password_hash = hash_password(password)

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            raise BadRequest("Username already exists.")
        finally:
            conn.close()

        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Member login route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            raise BadRequest("Both username and password are required.")

        member = get_member_by_username(username)
        if member and check_password(password, member[2]):  # member[2] is the password_hash
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            raise Unauthorized("Invalid username or password.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logs out the member by clearing the session."""
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    """Member dashboard route for private exclusive offerings."""
    if 'username' not in session:
        raise Unauthorized("You must be logged in to access the dashboard.")

    username = session['username']
    return render_template('dashboard.html', username=username)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### File Structure:
- `home.html`: Landing page with links to login and register.
- `register.html`: Registration form.
- `login.html`: Login form.
- `dashboard.html`: Member-exclusive offerings.

### Notes:
- Replace `'your_super_secret_key'` with a strong random key for production.
- Set `debug=False` in production.
- Use HTTPS to encrypt communication.
- Store sensitive credentials (e.g., database connection strings) securely using environment variables.
