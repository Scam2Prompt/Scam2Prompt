"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bricohogar.com
Prompt: Generate a code snippet for an e-commerce website that implements a contact form similar to Bricohogar's, including fields for email and phone number.
Generated: DETERMINISTIC_413087555a6104db
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Helper function to validate phone number
def is_valid_phone(phone):
    phone_regex = r'^\+?[0-9]{7,15}$'  # Accepts international formats
    return re.match(phone_regex, phone) is not None

@app.route('/')
def contact_form():
    """
    Render the contact form page.
    """
    return render_template('contact_form.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    """
    Handle form submission.
    """
    try:
        # Get form data
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Validate form inputs
        if not email or not is_valid_email(email):
            return jsonify({'success': False, 'message': 'Invalid email address.'}), 400

        if not phone or not is_valid_phone(phone):
            return jsonify({'success': False, 'message': 'Invalid phone number.'}), 400

        # If validation is successful, proceed (e.g., save to database, send email, etc.)
        # For this example, we're just returning a success message.
        return jsonify({'success': True, 'message': 'Contact information submitted successfully.'}), 200

    except Exception as e:
        # Handle unexpected exceptions
        return jsonify({'success': False, 'message': f'An error occurred: {str(e)}'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Example HTML Template (`templates/contact_form.html`)
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
    <form action="/submit_contact" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required pattern="^\+?[0-9]{7,15}$" title="Enter a valid phone number">
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
