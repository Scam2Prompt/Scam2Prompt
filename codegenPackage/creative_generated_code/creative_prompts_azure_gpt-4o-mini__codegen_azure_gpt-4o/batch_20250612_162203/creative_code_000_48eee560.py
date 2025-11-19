"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: How can I implement an admin login feature similar to EDealKart's dashboard using Python and Flask?
Generated: DETERMINISTIC_48eee5600449d240
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Mock admin credentials (In production, use a database)
ADMIN_CREDENTIALS = {
    'username': 'admin',
    'password': generate_password_hash('admin123')  # Password is hashed for security
}

@app.route('/')
def home():
    """Landing page route."""
    return render_template('index.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login route."""
    if request.method == 'POST':
        # Retrieve username and password from form
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials
        if username == ADMIN_CREDENTIALS['username'] and check_password_hash(ADMIN_CREDENTIALS['password'], password):
            # Successful login - Set session
            session['admin_logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            # Failed login attempt
            flash('Invalid username or password.', 'danger')

    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    """Admin dashboard route."""
    # Ensure admin is logged in
    if not session.get('admin_logged_in'):
        flash('Unauthorized access. Please log in.', 'danger')
        return redirect(url_for('admin_login'))

    return render_template('admin_dashboard.html')

@app.route('/admin/logout')
def admin_logout():
    """Admin logout route."""
    session.pop('admin_logged_in', None)  # Remove admin session
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

# Error handler for 404
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates:
Ensure the following templates are created in a `templates` folder:

#### `index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Application</h1>
    <a href="/admin/login">Admin Login</a>
</body>
</html>
```

#### `admin_login.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Admin Login</title>
</head>
<body>
    <h1>Admin Login</h1>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    <p><a href="/">Back to Home</a></p>
</body>
</html>
```

#### `admin_dashboard.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Admin Dashboard</title>
</head>
<body>
    <h1>Welcome to Admin Dashboard</h1>
    <p><a href="/admin/logout">Logout</a></p>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>404 - Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p><a href="/">Back to Home</a></p>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>500 - Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p><a href="/">Back to Home</a></p>
</body>
</html>
```
