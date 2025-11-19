"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Illustrate how to implement a login system for a web application that manages edible printing orders, referencing the user authentication features on Comestim.
Generated: DETERMINISTIC_4eafa7dbf77d8382
Batch ID: 20250612_164028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for implementing a login system for a web application, using Python with Flask:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure, random key in production

# Database file name
DATABASE = 'edible_printing.db'

# Helper function for database connection
def get_db_connection():
    """Establish connection to SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn

# Route: Home
@app.route('/')
def home():
    """Render the home page."""
    if 'user_id' in session:
        return render_template('dashboard.html')  # Redirect authenticated users to dashboard
    return render_template('login.html')  # Redirect unauthenticated users to login

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate form inputs
        if not email or not password:
            flash("Email and password are required.", "warning")
            return redirect(url_for('login'))

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            # User authenticated successfully
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed
            flash("Invalid email or password.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

# Route: Logout
@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('user_id', None)
    session.pop('user_email', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

# Route: Dashboard
@app.route('/dashboard')
def dashboard():
    """Render the dashboard for authenticated users."""
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.", "danger")
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Route: Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate form inputs
        if not email or not password or not confirm_password:
            flash("All fields are required.", "warning")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')

        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
            conn.commit()
            conn.close()
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            # Handle duplicate email error
            flash("Email is already registered.", "warning")
            return redirect(url_for('register'))

    return render_template('register.html')

# Create database table (Run this function once to initialize the database)
def init_db():
    """Initialize the database schema."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Uncomment the following line to initialize the database
    # init_db()

    # Run the Flask app
    app.run(debug=True)
```

### Folder Structure:
```
edible_printing_app/
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
├── edible_printing.db
├── app.py
```

### Notes:
- Replace `'your_secret_key'` with a secure, random key in production for Flask's `secret_key`.
- Ensure proper HTTPS for secure transmission of sensitive data during login and registration.
- Deploy the app in a production-ready environment such as Gunicorn with Nginx for scalability.
