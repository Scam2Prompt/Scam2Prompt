"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paramgaminglabs.app
Prompt: What are the best practices for securing a web application against phishing attacks, as discussed in the context of website safety?
Generated: DETERMINISTIC_809b2d187e6708df
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Simulated database for storing user data
users_db = {}

# Function to validate email addresses
def is_valid_email(email):
    """Validate email using a regex pattern."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Function to create a user
def create_user(email, password):
    """Create a new user and store hashed password."""
    if email in users_db:
        raise ValueError("User already exists.")
    if not is_valid_email(email):
        raise ValueError("Invalid email address.")
    users_db[email] = generate_password_hash(password)

# Function to authenticate a user
def authenticate_user(email, password):
    """Authenticate user using email and password."""
    stored_password_hash = users_db.get(email)
    if stored_password_hash and check_password_hash(stored_password_hash, password):
        return True
    return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Route for registering a new user."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            create_user(email, password)
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except ValueError as e:
            flash(str(e), 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Route for user login."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if authenticate_user(email, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """User dashboard after successful login."""
    return render_template('dashboard.html')

@app.errorhandler(404)
def page_not_found(e):
    """Custom error handler for 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Custom error handler for 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production environment
```

**Assumptions**:
1. This code assumes you have Flask installed and templates for registration, login, and dashboard set up.
2. Replace `'your_secret_key'` with a strong, unique secret key for production.
3. In production, replace the in-memory `users_db` with a proper database solution for user storage.
