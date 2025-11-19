"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: How can I implement a secure login feature for an employee portal similar to the Socrates GM portal, including username and password requirements?
Generated: DETERMINISTIC_2df146841443401d
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, secure, and production-ready implementation of a secure login feature for an employee portal. It uses Python with Flask for the web framework and includes username/password validation, hashed password storage, and proper error handling. It assumes you have a database set up (e.g., SQLite) and Flask installed.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for session management

DATABASE = 'employee_portal.db'

# Helper function to interact with the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

# Username and password validation requirements
USERNAME_REGEX = r"^[a-zA-Z0-9_.-]{5,20}$"  # 5-20 characters, alphanumeric with _.- allowed
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # Minimum 8 characters, 1 letter, 1 number, 1 special character

@app.route('/')
def index():
    # Check if the user is logged in
    if 'user_id' in session:
        return f"Welcome to the Employee Portal, User ID: {session['user_id']}!"
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate inputs
        if not username or not password:
            flash('Username and password are required.', 'error')
            return redirect(url_for('login'))

        # Fetch user from the database
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            # Successful login
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate username
        if not re.match(USERNAME_REGEX, username):
            flash('Username must be 5-20 characters long and can contain letters, numbers, and _.-.', 'error')
            return redirect(url_for('register'))

        # Validate password
        if not re.match(PASSWORD_REGEX, password):
            flash('Password must be at least 8 characters long and include 1 letter, 1 number, and 1 special character.', 'error')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Save user to the database
        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            conn.close()

            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            # Handle duplicate username error
            flash('Username already exists.', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    # Remove the user ID from the session
    session.pop('user_id', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

# Initialize the database (run this once to create the schema)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Uncomment the line below to initialize the database for the first time
    # init_db()
    app.run(debug=True)
```

### Notes:
1. The `init_db()` function should be called once to set up the database schema.
2. Replace `your_secret_key` with a strong, unique secret key.
3. Templates `login.html` and `register.html` need to be created with the appropriate forms for login and registration.
4. This code uses SQLite for simplicity. Replace it with a more robust database in production if necessary.
5. The password hashing uses the `werkzeug.security` library, which is considered secure and best practice.
