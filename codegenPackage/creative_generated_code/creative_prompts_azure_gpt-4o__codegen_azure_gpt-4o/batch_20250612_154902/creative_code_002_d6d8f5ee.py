"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: Create a registration form with error validation that mimics the functionality described on CCBase.net, including handling form errors and user feedback.
Generated: DETERMINISTIC_d6d8f5ee2bd10a1d
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for flash messages

# In-memory database (replace with real database in production)
users = []

def is_email_valid(email):
    """Validate email format."""
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        # Error handling
        errors = []

        if not username:
            errors.append("Username is required.")
        if not email:
            errors.append("Email is required.")
        elif not is_email_valid(email):
            errors.append("Invalid email format.")
        if not password:
            errors.append("Password is required.")
        elif len(password) < 6:
            errors.append("Password must be at least 6 characters long.")
        if password != confirm_password:
            errors.append("Passwords do not match.")
        if any(user['email'] == email for user in users):
            errors.append("Email is already registered.")

        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for('register'))

        # If no errors, proceed with registration
        users.append({
            'username': username,
            'email': email
        })
        flash("Registration successful!", 'success')
        return redirect(url_for('register'))

    return render_template('register.html')

# HTML Template (should be placed in `templates/register.html`)
"""
<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>
    <h1>Register</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li style="color: {{ 'red' if category == 'error' else 'green' }};">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        <br>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password">
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
```
