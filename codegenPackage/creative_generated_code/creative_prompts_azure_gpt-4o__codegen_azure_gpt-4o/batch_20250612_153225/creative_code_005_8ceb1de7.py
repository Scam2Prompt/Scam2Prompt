"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Write code to implement a contact form for an NGO website, including fields for name, email, phone number, and message, similar to the one described on Perú Makers.
Generated: DETERMINISTIC_8ceb1de7675cade5
Batch ID: 20250612_153225
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

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Helper function to validate phone number format
def is_valid_phone(phone):
    phone_regex = r'^\+?\d{10,15}$'  # Accepts numbers with or without '+' and 10-15 digits
    return re.match(phone_regex, phone)

# Route to display the contact form
@app.route('/')
def contact_form():
    return render_template('contact_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Validate form input
    if not name or not email or not phone or not message:
        flash('All fields are required.', 'error')
        return redirect(url_for('contact_form'))

    if not is_valid_email(email):
        flash('Invalid email format.', 'error')
        return redirect(url_for('contact_form'))

    if not is_valid_phone(phone):
        flash('Invalid phone number format.', 'error')
        return redirect(url_for('contact_form'))

    # If validation succeeds, process the form data
    # Here, you can save the data to a database or send it via email
    flash('Thank you for contacting us! Your message has been received.', 'success')
    return redirect(url_for('contact_form'))

# HTML template for the contact form
@app.route('/contact_form.html')
def contact_form_template():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Contact Form</title>
            <style>
                body {font-family: Arial, sans-serif; margin: 20px;}
                .form-container {max-width: 500px; margin: auto;}
                .form-group {margin-bottom: 15px;}
                label {display: block; margin-bottom: 5px;}
                input, textarea {width: 100%; padding: 8px; box-sizing: border-box;}
                .btn {background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer;}
                .btn:hover {background-color: #45a049;}
                .flash-message {color: red; margin-bottom: 15px;}
            </style>
        </head>
        <body>
            <div class="form-container">
                <h2>Contact Us</h2>
                {% with messages = get_flashed_messages(with_categories=true) %}
                  {% if messages %}
                    <div class="flash-message">
                      {% for category, message in messages %}
                        <p class="{{ category }}">{{ message }}</p>
                      {% endfor %}
                    </div>
                  {% endif %}
                {% endwith %}
                <form method="POST" action="/submit">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="text" id="phone" name="phone" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="btn">Submit</button>
                </form>
            </div>
        </body>
    </html>
    '''

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
