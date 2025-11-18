"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-wiederherstellung.com
Prompt: Write code to create a privacy-friendly login system that includes an option to use a private browsing window, similar to the feature highlighted on the Coinbase login page.
Generated: DETERMINISTIC_d581a57792364f85
Batch ID: 20250612_153848
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
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Securely generate a secret key for session management

# Dummy database for demonstration
users_db = {}

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate user credentials
        user = users_db.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Render the user dashboard."""
    if 'username' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('username', None)  # Clear the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        if username in users_db:
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))

        # Hash the password and store user info
        users_db[username] = {
            'password': generate_password_hash(password)
        }
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/private-browsing')
def private_browsing():
    """Render the private browsing information page."""
    return render_template('private_browsing.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates (Assumed Structure)
- `index.html`: Welcome page with links to login and register.
- `login.html`: Form for user login.
- `dashboard.html`: User dashboard displaying user information.
- `register.html`: Form for user registration.
- `private_browsing.html`: Information page about private browsing.
- `404.html`: Custom 404 error page.
- `500.html`: Custom 500 error page.

### Note
Please ensure that you have Flask installed in your Python environment to run this code:
```bash
pip install Flask
```
