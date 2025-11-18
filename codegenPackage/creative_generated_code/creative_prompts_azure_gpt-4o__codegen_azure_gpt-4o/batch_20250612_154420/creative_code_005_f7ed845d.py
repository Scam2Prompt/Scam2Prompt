"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Develop code for a web form that allows customers to submit service requests for HVAC repairs or tune-ups, including fields for contact information, service type (e.g., air conditioning repair, duct cleaning), and preferred appointment time.
Generated: DETERMINISTIC_f7ed845dbfd557dd
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code using Flask for creating a basic web form for HVAC service requests.

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Helper function to validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Route to render the service request form
@app.route('/')
def index():
    return render_template('service_request_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_request():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service_type = request.form.get('service_type')
        appointment_time = request.form.get('appointment_time')

        # Input validation
        if not name or not email or not phone or not service_type or not appointment_time:
            flash('All fields are required.', 'error')
            return redirect(url_for('index'))
        
        if not is_valid_email(email):
            flash('Invalid email format.', 'error')
            return redirect(url_for('index'))

        # Parse appointment time
        try:
            appointment_datetime = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid appointment time format. Use YYYY-MM-DD HH:MM.', 'error')
            return redirect(url_for('index'))

        # Simulate saving data (replace this with database integration)
        # For production, replace print statements with database storage logic
        print(f"Service Request Received:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Service Type: {service_type}")
        print(f"Preferred Appointment Time: {appointment_datetime}")

        flash('Service request submitted successfully!', 'success')
        return redirect(url_for('index'))
    
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
        return redirect(url_for('index'))

# HTML form template (should be saved as 'templates/service_request_form.html')
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HVAC Service Request Form</title>
</head>
<body>
    <h1>HVAC Service Request Form</h1>
    <form action="/submit" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        
        <label for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone" required><br>

        <label for="service_type">Service Type:</label><br>
        <select id="service_type" name="service_type" required>
            <option value="Air Conditioning Repair">Air Conditioning Repair</option>
            <option value="Duct Cleaning">Duct Cleaning</option>
            <option value="Tune-Up">Tune-Up</option>
        </select><br>

        <label for="appointment_time">Preferred Appointment Time (YYYY-MM-DD HH:MM):</label><br>
        <input type="text" id="appointment_time" name="appointment_time" required><br>

        <button type="submit">Submit Request</button>
    </form>

    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            {% for category, message in messages %}
                <p style="color: {% if category == 'error' %}red{% elif category == 'success' %}green{% endif %};">{{ message }}</p>
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
