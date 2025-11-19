"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: Generate a sample code snippet for a login form in a POS system.
Generated: DETERMINISTIC_c05d80b4fbfd5ed5
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management and flash messages. Replace with a strong key.

# Mock database for demonstration purposes
mock_users_db = {
    "admin": {
        "username": "admin",
        "password_hash": "pbkdf2:sha256:150000$example$e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # Replace with hashed password
    }
}

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle login form submission.
    If GET: Render the login page.
    If POST: Validate user credentials and log them in.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate input
        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for('login'))

        # Fetch user from the mock database
        user = mock_users_db.get(username)

        # Check if user exists and password is correct
        if user and check_password_hash(user['password_hash'], password):
            session['user'] = username
            flash(f"Welcome, {username}!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    """Log the user out and redirect to the login page."""
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes on `login.html` and `home.html` (HTML templates):
Below is an example structure for the `login.html` template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>POS Login</title>
</head>
<body>
    <h1>Login Form</h1>
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
    <p>{{ get_flashed_messages() }}</p>
</body>
</html>
```

And an example structure for `home.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>POS Home</title>
</head>
<body>
    <h1>Welcome to the POS System</h1>
    {% if 'user' in session %}
        <p>Logged in as: {{ session['user'] }}</p>
        <a href="/logout">Logout</a>
    {% else %}
        <p>You are not logged in.</p>
        <a href="/login">Login</a>
    {% endif %}
</body>
</html>
```
