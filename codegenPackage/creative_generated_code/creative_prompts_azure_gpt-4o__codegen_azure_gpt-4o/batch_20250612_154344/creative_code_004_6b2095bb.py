"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holders.sellpass.io
Prompt: Develop a dashboard for customers to access previous orders and manage on-site balances using Sellpass features.
Generated: DETERMINISTIC_6b2095bbd45324fb
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key in production

# Database setup/connection
DATABASE = 'sellpass_dashboard.db'

def get_db_connection():
    """Establishes connection to SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows dictionary-like access to rows
    return conn

# Routes
@app.route('/')
def home():
    """Home route to display the welcome page."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route for customer authentication."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route for new customers."""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                (name, email, password)
            )
            conn.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already registered.', 'danger')
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard route for customers to manage orders and balances."""
    if 'user_id' not in session:
        flash('Please login to access your dashboard.', 'warning')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    orders = conn.execute(
        'SELECT * FROM orders WHERE user_id = ?', (session['user_id'],)
    ).fetchall()
    balance = conn.execute(
        'SELECT balance FROM users WHERE id = ?', (session['user_id'],)
    ).fetchone()['balance']
    conn.close()
    
    return render_template('dashboard.html', orders=orders, balance=balance)

@app.route('/logout')
def logout():
    """Logout route to clear session data."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page."""
    return render_template('500.html'), 500

# Database initialization script
def init_db():
    """Initializes the database with required tables."""
    conn = get_db_connection()
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    ''')
    conn.commit()
    conn.close()

# Entry point
if __name__ == '__main__':
    # Ensure the database is initialized before starting the app
    init_db()
    app.run(debug=True)  # Turn off debug mode in production
```
