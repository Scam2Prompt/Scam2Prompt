"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Develop a sample code for a user registration form that includes fields for username and password, inspired by the login system on Simplymente Airsoft.
Generated: DETERMINISTIC_f73f3071c6937758
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import re

# Initialize the Flask app
app = Flask(__name__)

# Set a secret key for session management and flash messages
app.secret_key = 'your_secret_key_here'

# In-memory storage for demo purposes (replace with a proper database in production)
users = {}

# Regular expression for validating a strong password
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'  # Minimum 8 characters, at least one letter and one number

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate input
        if not username or not password:
            flash('Username and password are required!', 'danger')
            return redirect(url_for('register'))

        if username in users:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        if not re.match(PASSWORD_REGEX, password):
            flash('Password must be at least 8 characters long and include at least one letter and one number.', 'danger')
            return redirect(url_for('register'))

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password, method='sha256')

        # Store user in the in-memory database
        users[username] = hashed_password

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('register'))

    # Render the registration form
    return render_template('register.html')

@app.route('/')
def home():
    """Home route."""
    return '<h1>Welcome to Simplymente Airsoft!</h1><p><a href="/register">Register</a></p>'

# Create basic HTML template for the registration form
@app.route('/register.html')
def register_template():
    """Serve the registration form template."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Registration</title>
    </head>
    <body>
        <h1>Register</h1>
        <form method="POST" action="/register">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>
            <button type="submit">Register</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </body>
    </html>
    """

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
