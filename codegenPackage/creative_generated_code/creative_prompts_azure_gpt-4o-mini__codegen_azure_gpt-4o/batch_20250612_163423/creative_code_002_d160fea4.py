"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorcommunity.com
Prompt: Can you provide a code snippet for creating a login form that restricts access to a specific section of a website?
Generated: DETERMINISTIC_d160fea4559b7566
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Mock user database (for demonstration purposes only)
# In a production environment, use a proper database to store user credentials.
users = {
    "testuser": generate_password_hash("password123")  # Example user with hashed password
}

@app.route('/')
def home():
    """
    Home route showing the public content.
    """
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route for user authentication.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate user credentials
        if username in users and check_password_hash(users[username], password):
            session['user'] = username  # Store username in session
            flash('Login successful!', 'success')
            return redirect(url_for('restricted'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Logout route to clear session data.
    """
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/restricted')
def restricted():
    """
    Restricted route accessible only to logged-in users.
    """
    if 'user' in session:
        return render_template('restricted.html', user=session['user'])
    else:
        flash('You must be logged in to access this page.', 'error')
        return redirect(url_for('login'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### File Structure:
1. **home.html** - Public homepage accessible to everyone.
2. **login.html** - Login form for user authentication.
3. **restricted.html** - Restricted page content accessible only to logged-in users.

### Template Example for `login.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST" action="{{ url_for('login') }}">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li><strong>{{ category }}:</strong> {{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

### Template Example for `restricted.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Restricted Area</title>
</head>
<body>
    <h1>Welcome, {{ user }}!</h1>
    <p>This is a restricted section of the website.</p>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```
