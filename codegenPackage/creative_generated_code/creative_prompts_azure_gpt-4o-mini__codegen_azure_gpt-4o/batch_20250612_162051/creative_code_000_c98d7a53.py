"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jsa.academy
Prompt: How can I write a code snippet to create a volunteer registration form for a sports academy similar to Jambalaya Soccer Academy?
Generated: DETERMINISTIC_c98d7a530e535622
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# volunteer_registration_form.py

from flask import Flask, render_template, request, redirect, url_for, flash
import re

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Used for secure flash messages

# Helper function to validate email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Route for the volunteer registration form
@app.route('/', methods=['GET', 'POST'])
def register_volunteer():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        availability = request.form.get('availability')
        skills = request.form.get('skills')

        errors = []

        # Validate name
        if not name or len(name) < 2:
            errors.append("Name must be at least 2 characters long.")

        # Validate email
        if not email or not is_valid_email(email):
            errors.append("Invalid email address.")

        # Validate phone
        if not phone or not phone.isdigit() or len(phone) != 10:
            errors.append("Phone must be a 10-digit number.")

        # Validate availability
        if not availability or availability.strip() == "":
            errors.append("Availability cannot be empty.")

        # Validate skills
        if not skills or len(skills) < 5:
            errors.append("Skills description must be at least 5 characters long.")

        # If there are validation errors, show them to the user
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html', name=name, email=email, phone=phone, availability=availability, skills=skills)

        # If validation passes, process the registration
        flash("Thank you for registering as a volunteer!", 'success')
        return redirect(url_for('register_volunteer'))

    # Render the registration form for GET requests
    return render_template('register.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Registration Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .flash-message {
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .flash-message.error {
            background-color: #f8d7da;
            color: #721c24;
        }
        .flash-message.success {
            background-color: #d4edda;
            color: #155724;
        }
    </style>
</head>
<body>

<h2>Volunteer Registration Form</h2>
<div>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash-message {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
</div>
<form action="/" method="post">
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" value="{{ name or '' }}" required>

    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" value="{{ email or '' }}" required>

    <label for="phone">Phone Number:</label>
    <input type="text" id="phone" name="phone" value="{{ phone or '' }}" required>

    <label for="availability">Availability (e.g., weekends, weekdays):</label>
    <input type="text" id="availability" name="availability" value="{{ availability or '' }}" required>

    <label for="skills">Skills/Experience:</label>
    <textarea id="skills" name="skills" rows="4" required>{{ skills or '' }}</textarea>

    <button type="submit">Register</button>
</form>

</body>
</html>
```
