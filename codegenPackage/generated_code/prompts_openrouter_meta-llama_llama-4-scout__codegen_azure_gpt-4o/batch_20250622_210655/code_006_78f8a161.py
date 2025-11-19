"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Design a user interface for a property management system that allows owners and renters to access their accounts, make payments, and view property information, inspired by Inmobiliaria Nueva Ciudad's online services.
Generated: DETERMINISTIC_78f8a161603ca460
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a clean, production-ready implementation of a basic property management system user interface using Python's Flask framework. This code includes account access, payment functionality, and property information viewing.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Database setup
DATABASE = 'property_management.db'

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists.', 'danger')
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """Render the user dashboard."""
    if 'user_id' not in session:
        flash('Please log in to access your dashboard.', 'warning')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    properties = conn.execute('SELECT * FROM properties WHERE owner_id = ?', (session['user_id'],)).fetchall()
    conn.close()
    
    return render_template('dashboard.html', properties=properties)

@app.route('/make_payment', methods=['GET', 'POST'])
def make_payment():
    """Handle payment processing."""
    if 'user_id' not in session:
        flash('Please log in to make a payment.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        property_id = request.form['property_id']
        amount = request.form['amount']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO payments (user_id, property_id, amount) VALUES (?, ?, ?)', 
                     (session['user_id'], property_id, amount))
        conn.commit()
        conn.close()
        
        flash('Payment successful!', 'success')
        return redirect(url_for('dashboard'))
    
    conn = get_db_connection()
    properties = conn.execute('SELECT * FROM properties WHERE owner_id = ?', (session['user_id'],)).fetchall()
    conn.close()
    
    return render_template('make_payment.html', properties=properties)

@app.route('/logout')
def logout():
    """Log the user out."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Database initialization
def init_db():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner_id INTEGER NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES users (id)
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            property_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (property_id) REFERENCES properties (id)
        )
    ''')
    conn.close()

if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)
```

### Notes:
1. Replace `your_secret_key` with a secure key for production.
2. Create the necessary HTML templates (`home.html`, `login.html`, `register.html`, `dashboard.html`, `make_payment.html`, `404.html`, `500.html`) to render the UI.
3. Use a production-ready database (e.g., PostgreSQL) for scalability in a real-world application.
