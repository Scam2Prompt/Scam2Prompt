"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emirates.dev.get-myesim.com
Prompt: How can I implement password protection for a partner login page similar to the one on Emirates MyESIM?
Generated: DETERMINISTIC_dbd3c8a0f775e357
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation in Python using Flask for a password-protected partner login page:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Simulating a database with one partner login for demonstration purposes
# In a production environment, use a secure database
PARTNER_DB = {
    "partner_username": {
        "password": generate_password_hash("secure_password")  # Replace with a secure password
    }
}

@app.route('/')
def home():
    """
    Home page route. Redirects to login page.
    """
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login page route. Handles GET for the login form and POST for login submissions.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate user input
        if not username or not password:
            flash("Username and password are required!", "error")
            return render_template('login.html')

        # Check if the user exists and the password is correct
        partner_data = PARTNER_DB.get(username)
        if partner_data and check_password_hash(partner_data['password'], password):
            session['username'] = username  # Store the username in session for authentication
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password.", "error")
            return render_template('login.html')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Dashboard route. Only accessible to authenticated users.
    """
    if 'username' not in session:  # Check if the user is logged in
        flash("You must be logged in to access the dashboard.", "error")
        return redirect(url_for('login'))

    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    """
    Logout route. Clears the session and redirects to the login page.
    """
    session.pop('username', None)  # Remove the username from session
    flash("Logged out successfully.", "info")
    return redirect(url_for('login'))

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

### Directory Structure
```
- app.py
- templates/
    - login.html
    - dashboard.html
    - 404.html
```

### Example `login.html` Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Partner Login</title>
</head>
<body>
    <h1>Partner Login</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                <li><strong>{{ category }}</strong>: {{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Example `dashboard.html` Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
    <p>This is the partner dashboard.</p>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

### Example `404.html` Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{{ url_for('login') }}">Go to Login</a>
</body>
</html>
```

### Notes
1. Replace `your_secret_key_here` with a secure key (e.g., generated using `secrets.token_hex()` in Python).
2. Replace `secure_password` with a strong password for demonstration purposes.
3. For production:
   - Use HTTPS to secure communication.
   - Implement a proper database for storing partner credentials.
   - Consider rate-limiting, CAPTCHA, or other measures to prevent brute-force attacks.
   - Use environment variables for sensitive configurations like the secret key.
