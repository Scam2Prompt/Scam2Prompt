"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerfi.airlst-pages.app
Prompt: Generate a code snippet for a registration form that captures attendee details for an event similar to the one described on Balancer.Fi, including fields for name, email, and company.
Generated: DETERMINISTIC_f7d961a437e38090
Batch ID: 20250612_163156
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
from email_validator import validate_email, EmailNotValidError

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Define route for registration form
@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        # Capture form data
        name = request.form.get('name')
        email = request.form.get('email')
        company = request.form.get('company')

        # Validate inputs
        if not name or not email or not company:
            flash("All fields are required.", "error")
            return redirect(url_for('registration_form'))

        # Validate email format
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Invalid email address.", "error")
            return redirect(url_for('registration_form'))

        # Handle successful submission
        # In production, you'd store the data in a database or send an email
        flash("Registration successful. Thank you for registering!", "success")
        return redirect(url_for('registration_form'))

    # Render form template
    return render_template('registration_form.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- registration_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Registration Form</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 400px; margin: auto; }
        input, button { display: block; width: 100%; margin-bottom: 10px; padding: 10px; }
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Register for the Event</h1>
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            {% for category, message in messages %}
                <p class="{{ category }}">{{ message }}</p>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <!-- Registration form -->
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="company">Company:</label>
        <input type="text" id="company" name="company" required>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```
