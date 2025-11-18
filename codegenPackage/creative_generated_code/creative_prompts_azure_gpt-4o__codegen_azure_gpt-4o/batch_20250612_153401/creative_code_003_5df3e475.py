"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-insanitybets.web.app
Prompt: Generate code for a "Sign Up" form for a platform like InsanityBets, including fields for username, email, and wallet address.
Generated: DETERMINISTIC_5df3e475a1742afa
Batch ID: 20250612_153401
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
app.secret_key = 'your_secret_key'  # Replace with a secure key in production.

# Utility function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Utility function to validate wallet address format
def is_valid_wallet(wallet):
    wallet_regex = r'^[a-zA-Z0-9]{42}$'  # Example regex for Ethereum wallet addresses
    return re.match(wallet_regex, wallet)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        wallet_address = request.form.get('wallet_address')

        # Basic validation
        if not username or not email or not wallet_address:
            flash("All fields are required.", "error")
            return redirect(url_for('signup'))

        if len(username) < 3 or len(username) > 20:
            flash("Username must be between 3 and 20 characters.", "error")
            return redirect(url_for('signup'))

        if not is_valid_email(email):
            flash("Invalid email format.", "error")
            return redirect(url_for('signup'))

        if not is_valid_wallet(wallet_address):
            flash("Invalid wallet address format.", "error")
            return redirect(url_for('signup'))

        # Success message (replace with database logic in production)
        flash("Sign Up Successful! Welcome to InsanityBets.", "success")
        return redirect(url_for('signup'))

    # Render the sign-up form
    return render_template('signup.html')

# HTML Template (should be placed in a 'templates/signup.html' file):
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - InsanityBets</title>
    <link rel="stylesheet" href="/static/style.css">  <!-- Include CSS file -->
</head>
<body>
    <h1>Sign Up for InsanityBets</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form action="/signup" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="wallet_address">Wallet Address:</label>
        <input type="text" id="wallet_address" name="wallet_address" required>
        <br>
        <button type="submit">Sign Up</button>
    </form>
</body>
</html>
"""

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
