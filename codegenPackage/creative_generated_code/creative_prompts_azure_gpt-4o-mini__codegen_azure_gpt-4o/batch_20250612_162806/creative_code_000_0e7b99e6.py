"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: Write a code snippet to create a request form for a paving service quote similar to the one on Bedford Paving's website.
Generated: DETERMINISTIC_0e7b99e622c79c03
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import re

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key

# Define a regex pattern for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Route for rendering the quote request form
@app.route('/')
def request_form():
    return render_template('request_form.html')  # HTML form should be created in templates/request_form.html

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        service_requested = request.form.get('service_requested')
        additional_details = request.form.get('additional_details')

        # Input validation
        if not name or not email or not phone or not address or not service_requested:
            flash('All fields are required.', 'error')
            return redirect(url_for('request_form'))

        if not re.match(EMAIL_REGEX, email):
            flash('Invalid email address.', 'error')
            return redirect(url_for('request_form'))

        if not phone.isdigit():
            flash('Phone number must contain only digits.', 'error')
            return redirect(url_for('request_form'))

        # Simulate form submission success (replace with database integration or email logic as needed)
        flash('Request submitted successfully! We will get back to you shortly.', 'success')
        return redirect(url_for('request_form'))

    except Exception as e:
        # Handle unexpected errors
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('request_form'))

# Run the application
if __name__ == '__main__':
    # Debug mode should be disabled in production
    app.run(debug=True)
```

### HTML Template (`templates/request_form.html`)
Save this file as `templates/request_form.html` in your project directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paving Service Quote Request</title>
    <style>
        form {
            max-width: 500px;
            margin: auto;
            padding: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        label {
            display: block;
            margin-bottom: 0.5em;
        }
        input, textarea, select {
            width: 100%;
            padding: 0.5em;
            margin-bottom: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 0.5em 1em;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .flash {
            margin: auto;
            margin-top: 1em;
            max-width: 500px;
            padding: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f8f9fa;
        }
    </style>
</head>
<body>
    <h1>Request a Paving Service Quote</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <div class="flash">
          {% for category, message in messages %}
            <p class="{{ category }}">{{ message }}</p>
          {% endfor %}
        </div>
      {% endif %}
    {% endwith %}
    <form method="POST" action="/submit">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required>

        <label for="service_requested">Service Requested:</label>
        <select id="service_requested" name="service_requested" required>
            <option value="Driveway Paving">Driveway Paving</option>
            <option value="Parking Lot Paving">Parking Lot Paving</option>
            <option value="Sidewalk Paving">Sidewalk Paving</option>
            <option value="Other">Other</option>
        </select>

        <label for="additional_details">Additional Details:</label>
        <textarea id="additional_details" name="additional_details" rows="4"></textarea>

        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```
