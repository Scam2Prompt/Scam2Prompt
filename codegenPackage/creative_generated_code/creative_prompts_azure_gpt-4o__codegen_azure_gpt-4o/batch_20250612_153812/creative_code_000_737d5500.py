"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Write code to implement a user registration form with fields for username, phone number, password, confirm password, and referral code, as described on the bonaeac.com website.
Generated: DETERMINISTIC_737d55009a460830
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Helper function to validate phone number format
def is_valid_phone_number(phone_number):
    # Validate phone number (example: 10-digit number)
    return re.match(r'^\d{10}$', phone_number)

# Helper function to validate password strength
def is_valid_password(password):
    # Example: At least 8 characters, one uppercase, one lowercase, one number
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration form submission.
    """
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        referral_code = request.form.get('referral_code')

        # Validation
        if not username:
            flash("Username is required.", "error")
        elif not phone_number or not is_valid_phone_number(phone_number):
            flash("Invalid phone number. Must be a 10-digit number.", "error")
        elif not password or not is_valid_password(password):
            flash("Password must be at least 8 characters with one uppercase, one lowercase, and one number.", "error")
        elif password != confirm_password:
            flash("Passwords do not match.", "error")
        else:
            # Simulate saving to database (replace with real DB operation)
            # Example: db.save_user(username, phone_number, password, referral_code)
            flash("Registration successful!", "success")
            return redirect(url_for('register'))

    return render_template('register.html')

# Example HTML template for registration form (to be placed in 'templates/register.html')
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>
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
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>

        <label for="phone_number">Phone Number:</label><br>
        <input type="text" id="phone_number" name="phone_number"><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>

        <label for="confirm_password">Confirm Password:</label><br>
        <input type="password" id="confirm_password" name="confirm_password"><br><br>

        <label for="referral_code">Referral Code:</label><br>
        <input type="text" id="referral_code" name="referral_code"><br><br>

        <button type="submit">Register</button>
    </form>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
