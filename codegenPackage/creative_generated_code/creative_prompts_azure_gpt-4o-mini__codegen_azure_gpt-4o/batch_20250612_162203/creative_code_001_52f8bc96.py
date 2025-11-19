"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: What are the best practices for creating a secure admin login system like the one on EDealKart?
Generated: DETERMINISTIC_52f8bc96d0d1d956
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the secure admin login system code implemented in Python using Flask and SQLite for demonstration purposes. It follows best practices for security and design.

```python
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session encryption

# Path for SQLite database
DATABASE = 'edealkart_admin.db'


# Function to initialize the database
def init_db():
    """Initialize the SQLite database with an admin_users table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)
        conn.commit()


# Route: Admin login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle admin login functionality."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate user input
        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for('login'))
        
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                # Fetch user from database
                cursor.execute("SELECT * FROM admin_users WHERE username = ?", (username,))
                user = cursor.fetchone()
                
                if user and check_password_hash(user[2], password):  # Check hashed password
                    # Valid login
                    session['admin'] = user[1]  # Store username in session
                    flash("Login successful!", "success")
                    return redirect(url_for('dashboard'))
                else:
                    # Invalid login
                    flash("Invalid username or password.", "error")
                    return redirect(url_for('login'))
        except sqlite3.Error as e:
            flash("Database error occurred. Please try again.", "error")
            return redirect(url_for('login'))
    
    return render_template('login.html')  # Render login page template


# Route: Admin dashboard (protected)
@app.route('/dashboard')
def dashboard():
    """Render the admin dashboard."""
    if 'admin' not in session:  # Check if admin is logged in
        flash("Unauthorized access. Please log in.", "error")
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', admin=session['admin'])  # Pass admin username to template


# Route: Admin logout
@app.route('/logout')
def logout():
    """Handle admin logout functionality."""
    session.pop('admin', None)  # Remove admin session
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))


# Route: Create admin user (example only, should be restricted in production)
@app.route('/create-admin', methods=['POST'])
def create_admin():
    """Create a new admin user (for demonstration purposes only)."""
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Validate user input
    if not username or not password:
        flash("Username and password are required.", "error")
        return redirect(url_for('dashboard'))
    
    hashed_password = generate_password_hash(password, method='sha256')  # Hash password securely
    
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO admin_users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            flash("Admin user created successfully!", "success")
    except sqlite3.IntegrityError:
        flash("Username already exists. Please choose a different username.", "error")
    except sqlite3.Error as e:
        flash("Database error occurred. Please try again.", "error")
    
    return redirect(url_for('dashboard'))


# Main entry point
if __name__ == '__main__':
    # Ensure database is initialized
    init_db()
    # Run the Flask app
    app.run(debug=True)
```

### Note:
1. Templates `login.html` and `dashboard.html` should be created in the `templates` directory for proper rendering.
2. Remove the `/create-admin` route or protect it in production to prevent unauthorized user creation.
3. Use HTTPS in production to ensure secure communication.
4. Ensure proper rate-limiting and monitoring of login attempts to prevent brute-force attacks.
