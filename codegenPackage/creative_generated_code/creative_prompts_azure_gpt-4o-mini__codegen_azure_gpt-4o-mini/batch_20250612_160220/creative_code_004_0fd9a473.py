"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farming-carv.app
Prompt: What are the best practices for securing a website against phishing attacks, and how can I implement them using available libraries?
Generated: DETERMINISTIC_0fd9a473a332c768
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, redirect, url_for, session, flash, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Use a strong secret key in production

# Sample user database
users_db = {}

def is_phishing_attempt(url):
    """
    Check if a given URL is a potential phishing attempt based on known patterns.
    """
    # Define a list of common phishing keywords
    phishing_keywords = ["login", "verify", "account", "update"]
    return any(keyword in url for keyword in phishing_keywords)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate email
        try:
            valid = validate_email(email)
            email = valid.email  # Get the normalized email
        except EmailNotValidError as e:
            flash(f'Invalid email address: {str(e)}', 'error')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Store user data securely
        users_db[email] = hashed_password
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists and password is correct
        if email in users_db and check_password_hash(users_db[email], password):
            session['user_email'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    User dashboard that is accessible after successful login.
    """
    if 'user_email' not in session:
        flash('You need to log in first', 'error')
        return redirect(url_for('login'))
    
    return f"Welcome {session['user_email']}!"

@app.route('/report', methods=['POST'])
def report_phishing():
    """
    Endpoint to report a potential phishing URL submitted by the user.
    """
    url = request.form['url']

    if is_phishing_attempt(url):
        # Here we would handle the reporting logic, e.g., log it or notify admins
        flash('Phishing attempt reported successfully!', 'success')
    else:
        flash('URL looks safe, no action taken.', 'info')

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Note:
- This code uses Flask, a popular web framework for Python.
- Remember to add error handling, logging, and other security measures as necessary for your production environment.
- Ensure to adjust the `secret_key` and consider using a database for user management in a real application.
