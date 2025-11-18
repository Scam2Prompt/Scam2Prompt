"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Generate code for a web-based tool that allows users to request fire sprinkler installation proposals, similar to the service offered by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_a55bc91865436391
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: A web-based tool to allow users to request fire sprinkler installation proposals.
# Framework: Flask (Python)
# Note: Install Flask before running this script (`pip install flask`).

from flask import Flask, render_template, request, redirect, url_for, flash
import re
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Use environment variable for production

# Route: Home page
@app.route('/')
def index():
    """
    Render the home page with a form for requesting proposals.
    """
    return render_template('index.html')

# Route: Handle proposal requests
@app.route('/submit-proposal', methods=['POST'])
def submit_proposal():
    """
    Handle the form submission for fire sprinkler installation proposals.
    Validate the input, and show a success message if the form is valid.
    """
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        details = request.form.get('details', '').strip()

        # Input validation
        if not name or not email or not phone or not address or not details:
            flash("All fields are required.", "error")
            return redirect(url_for('index'))

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            flash("Invalid email address.", "error")
            return redirect(url_for('index'))

        if not re.match(r'^\+?\d{10,15}$', phone):
            flash("Invalid phone number.", "error")
            return redirect(url_for('index'))

        # Simulate form submission (e.g., save to database or send email)
        # For production, replace with actual database interaction or email-sending logic.
        flash("Your proposal request has been submitted successfully!", "success")
        return redirect(url_for('index'))

    except Exception as e:
        # Log the error (In production, use a proper logging mechanism)
        flash("An error occurred while processing your request. Please try again.", "error")
        print(f"Error: {e}")
        return redirect(url_for('index'))

# Start the Flask application
if __name__ == '__main__':
    # Note: Use a production-ready server (e.g., Gunicorn or uWSGI) in deployment
    app.run(debug=True)

```

```html
<!-- File: templates/index.html -->
<!-- Description: HTML template for the proposal request form. -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fire Sprinkler Proposal Request</title>
    <style>
        /* Basic styling */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        input, textarea {
            margin-bottom: 15px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .flash {
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 5px;
        }
        .flash.error {
            background-color: #f8d7da;
            color: #721c24;
        }
        .flash.success {
            background-color: #d4edda;
            color: #155724;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Request a Proposal</h1>
        <!-- Flash Messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
            <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}

        <!-- Proposal Request Form -->
        <form action="/submit-proposal" method="POST">
            <input type="text" name="name" placeholder="Full Name" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="text" name="phone" placeholder="Phone Number" required>
            <input type="text" name="address" placeholder="Installation Address" required>
            <textarea name="details" placeholder="Describe project details" rows="5" required></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
```
