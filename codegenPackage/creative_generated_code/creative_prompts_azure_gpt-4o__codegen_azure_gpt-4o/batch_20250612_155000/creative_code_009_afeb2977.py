"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Develop a script to create a beta sign-up form for a link-sharing platform, inspired by the "Inscreva-se" feature on "Bio.links."
Generated: DETERMINISTIC_afeb2977d33c8987
Batch ID: 20250612_155000
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
import re

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for securely flashing messages

# Define a regex pattern for validating email input
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Placeholder for storing sign-up data (in production, replace with a database)
beta_signups = []

# Route to display the beta sign-up form
@app.route('/', methods=['GET', 'POST'])
def beta_signup():
    """
    Handles the display and submission of the beta sign-up form.
    """
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')

        # Validate form inputs
        if not name or not email:
            flash('Name and email are required.', 'error')
            return redirect(url_for('beta_signup'))

        if not re.match(EMAIL_REGEX, email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('beta_signup'))

        # Check for duplicate email entries
        if email in [signup['email'] for signup in beta_signups]:
            flash('This email address is already registered.', 'error')
            return redirect(url_for('beta_signup'))

        # Save the data (in production, store in a database)
        beta_signups.append({'name': name, 'email': email})
        
        flash('Thank you for signing up! We\'ll be in touch.', 'success')
        return redirect(url_for('beta_signup'))

    # Render the sign-up form
    return render_template('signup.html')

# Define the signup.html template
@app.route('/signup.html')
def render_signup_template():
    """
    This is just a placeholder to simulate the form rendering.
    In production, this would be an HTML file served by Flask.
    """
    # Example HTML form (replace with actual signup.html file in templates directory)
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Beta Sign-Up</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .form-container { max-width: 400px; margin: auto; }
            .form-group { margin-bottom: 15px; }
            .form-group label { display: block; margin-bottom: 5px; }
            .form-group input { width: 100%; padding: 8px; }
            .messages { margin-bottom: 20px; }
            .messages .error { color: red; }
            .messages .success { color: green; }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Beta Sign-Up</h1>
            <div class="messages">
                {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="{{ category }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
                {% endwith %}
            </div>
            <form method="POST">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <button type="submit">Sign Up</button>
            </form>
        </div>
    </body>
    </html>
    """

# Error handling for 404 requests
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page handler.
    """
    return "<h1>404 - Page Not Found</h1>", 404

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
