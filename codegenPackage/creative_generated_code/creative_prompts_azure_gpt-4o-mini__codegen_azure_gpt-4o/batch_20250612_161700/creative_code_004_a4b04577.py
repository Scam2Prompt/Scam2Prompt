"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Design a user registration form for an online clothing store that captures essential details like email, password, and preferences, reflecting the user account setup process on Multan Designs.
Generated: DETERMINISTIC_a4b04577cc416662
Batch ID: 20250612_161700
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flashing messages

# In-memory storage for registered users (for demonstration purposes; use a database in production)
registered_users = []

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

# Function to validate password strength
def is_valid_password(password):
    return len(password) >= 8  # Enforce minimum password length (strength can be expanded)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration. Renders the registration form
    and processes user input to store the details if valid.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        preferences = request.form.get('preferences')
        
        # Server-side validation
        if not email or not is_valid_email(email):
            flash("Invalid email address. Please enter a valid email.", "danger")
            return redirect(url_for('register'))
        
        if not password or not is_valid_password(password):
            flash("Password must be at least 8 characters long.", "danger")
            return redirect(url_for('register'))
        
        if not preferences:
            flash("Please choose your preferences.", "danger")
            return redirect(url_for('register'))
        
        # Check if email is already registered
        if email in [user['email'] for user in registered_users]:
            flash("Email is already registered. Please use a different email.", "danger")
            return redirect(url_for('register'))
        
        # Store the user details (use a database in production)
        registered_users.append({
            'email': email,
            'password': password,  # Store hashed passwords in production
            'preferences': preferences
        })
        
        flash("Registration successful! Welcome to Multan Designs.", "success")
        return redirect(url_for('register'))

    # Render the registration form
    return render_template('register.html')

# HTML template for user registration (typically in a 'templates/register.html' file)
@app.route('/html/register')
def html_registration_template():
    """
    Example of the registration form HTML content.
    """
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Register - Multan Designs</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h2>Register to Multan Designs</h2>
            <form method="POST" action="/register">
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <div class="form-group">
                    <label for="preferences">Preferences (e.g., Men's Clothing, Women's Clothing, Accessories):</label>
                    <input type="text" class="form-control" id="preferences" name="preferences" required>
                </div>
                <button type="submit" class="btn btn-primary">Register</button>
            </form>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    '''

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
