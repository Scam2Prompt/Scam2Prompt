"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Write a Python script to create a web form for customers to request services like "window and door installation" or "bathroom updating" from Winger R&R, including fields for name, contact information, and service type.
Generated: DETERMINISTIC_cb691a5c23ccd0bb
Batch ID: 20250612_150343
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
app.secret_key = 'your_secret_key'  # Required for flash messages

# Regular expression for basic email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# List of available services
AVAILABLE_SERVICES = [
    "Window and Door Installation",
    "Bathroom Updating",
    "Kitchen Remodeling",
    "Flooring Installation"
]

@app.route('/')
def home():
    """
    Render the main web form.
    """
    return render_template('form.html', services=AVAILABLE_SERVICES)

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handle form submission and validate input data.
    """
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    service_type = request.form.get('service_type')

    # Input validation
    if not name or len(name.strip()) == 0:
        flash("Name is required.")
        return redirect(url_for('home'))

    if not email or not re.match(EMAIL_REGEX, email):
        flash("Valid email address is required.")
        return redirect(url_for('home'))

    if not phone or len(phone.strip()) < 10:
        flash("A valid phone number is required.")
        return redirect(url_for('home'))

    if service_type not in AVAILABLE_SERVICES:
        flash("Please select a valid service type.")
        return redirect(url_for('home'))

    # If all validations pass, process the request
    # Here, we would typically save the data to a database or send it via email
    flash(f"Thank you {name}! Your request for '{service_type}' has been submitted.")
    return redirect(url_for('home'))

# HTML Template (form.html)
# Save this code in a separate file named "templates/form.html"
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Winger R&R Service Request</title>
</head>
<body>
    <h1>Request a Service from Winger R&R</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul style="color: red;">
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form action="{{ url_for('submit') }}" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>

        <label for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone"><br><br>

        <label for="service_type">Service Type:</label><br>
        <select id="service_type" name="service_type">
            <option disabled selected>-- Select a Service --</option>
            {% for service in services %}
                <option value="{{ service }}">{{ service }}</option>
            {% endfor %}
        </select><br><br>

        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
```
