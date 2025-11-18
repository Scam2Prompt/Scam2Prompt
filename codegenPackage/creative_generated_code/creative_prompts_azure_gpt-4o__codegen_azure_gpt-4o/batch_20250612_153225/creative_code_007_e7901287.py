"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Generate code for implementing a contact form with fields for name, contact number, email, and message, as seen on Tara Media Works' website.
Generated: DETERMINISTIC_e7901287b657450c
Batch ID: 20250612_153225
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

app = Flask(__name__)

# Set a secret key for session management (used for flashing messages)
app.secret_key = 'your_secret_key_here'

# Route for the contact form page
@app.route('/')
def contact_form():
    """Render the contact form page."""
    return render_template('contact_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_contact_form():
    """
    Handle the submission of the contact form.
    Validate input data and process it safely.
    """
    try:
        # Retrieve form data
        name = request.form.get('name')
        contact_number = request.form.get('contact_number')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not contact_number or not email or not message:
            raise ValueError("All fields are required.")

        # Validate email format
        try:
            validate_email(email)  # Email validation
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {str(e)}")

        # Example: Validate contact number for numeric input
        if not contact_number.isdigit():
            raise ValueError("Contact number must contain only digits.")

        # Example: Process the data (e.g., save to database or send email)
        # Here we simulate processing with a print statement
        print(f"Contact Form Submitted: Name={name}, Contact={contact_number}, Email={email}, Message={message}")

        # Flash success message and redirect to the form page
        flash("Your message has been submitted successfully!", "success")
        return redirect(url_for('contact_form'))

    except ValueError as ve:
        # Flash error message with specific validation error
        flash(str(ve), "error")
        return redirect(url_for('contact_form'))

    except Exception as e:
        # Flash a generic error message for unexpected scenarios
        flash("An error occurred while processing your request.", "error")
        return redirect(url_for('contact_form'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**contact_form.html** (HTML template for the contact form):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>

    <!-- Display flashed messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
        {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}

    <!-- Contact form -->
    <form action="/submit" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="contact_number">Contact Number:</label><br>
        <input type="text" id="contact_number" name="contact_number" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**Note**: 
1. Replace `your_secret_key_here` with an actual secret key suitable for production.
2. This code uses Flask as the web framework and assumes Python is installed. Install dependencies (`pip install flask email-validator`) before running the code.
