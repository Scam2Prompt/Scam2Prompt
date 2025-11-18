"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Write code for a contact form that includes fields for user inquiries about room availability, inspired by the "Contact Us" functionality on Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_fe3a8677c4e1d4d5
Batch ID: 20250612_152620
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
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Route for contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Collect form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        inquiries = request.form.get('inquiries')

        # Validate required fields
        if not name or not email or not inquiries:
            flash('Name, Email, and Inquiry fields are required.', 'error')
            return redirect(url_for('contact'))

        # Validate email format
        if not is_valid_email(email):
            flash('Invalid email format.', 'error')
            return redirect(url_for('contact'))

        # Optional: Validate phone number format
        if phone and not phone.isnumeric():
            flash('Phone number should contain only digits.', 'error')
            return redirect(url_for('contact'))

        # Process the inquiry (e.g., save to database or send email)
        # Here, we're just simulating this with a success message
        flash('Your inquiry has been submitted successfully!', 'success')
        return redirect(url_for('contact'))

    # Render the contact form (GET request)
    return render_template('contact.html')

# HTML Template: contact.html
# Save this template in a folder named "templates" next to your Python script.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <!-- Flash Messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>

        <label for="phone">Phone (Optional):</label>
        <input type="text" id="phone" name="phone">
        <br>

        <label for="inquiries">Inquiry:</label>
        <textarea id="inquiries" name="inquiries" required></textarea>
        <br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
