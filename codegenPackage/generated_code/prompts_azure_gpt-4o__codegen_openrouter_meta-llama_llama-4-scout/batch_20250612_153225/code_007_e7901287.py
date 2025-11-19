"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: Generate code for implementing a contact form with fields for name, contact number, email, and message, as seen on Tara Media Works' website.
Generated: DETERMINISTIC_e7901287b657450c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# contact_form.py

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_FROM_EMAIL'] = os.environ.get('MAIL_FROM_EMAIL')

mail = Mail(app)

# Define the contact form class
class ContactForm:
    def __init__(self, name, contact_number, email, message):
        self.name = name
        self.contact_number = contact_number
        self.email = email
        self.message = message

# Route for handling contact form submissions
@app.route('/contact', methods=['POST'])
def handle_contact_form():
    try:
        # Get form data from the request
        data = request.json

        # Validate form data
        if not all(key in data for key in ['name', 'contact_number', 'email', 'message']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new ContactForm instance
        form = ContactForm(
            name=data['name'],
            contact_number=data['contact_number'],
            email=data['email'],
            message=data['message']
        )

        # Send an email using Flask-Mail
        msg = Message(
            'New Contact Form Submission',
            sender=os.environ.get('MAIL_FROM_EMAIL'),
            recipients=[os.environ.get('MAIL_TO_EMAIL')]
        )
        msg.body = f"""
        Name: {form.name}
        Contact Number: {form.contact_number}
        Email: {form.email}
        Message: {form.message}
        """
        mail.send(msg)

        return jsonify({'message': 'Form submitted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// contact-form.js

const form = document.getElementById('contact-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            console.log(result.message);
            form.reset();
        } else {
            console.error(result.error);
        }
    } catch (error) {
        console.error(error);
    }
});
```

```html
<!-- contact-form.html -->

<form id="contact-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br><br>
    <label for="contact_number">Contact Number:</label>
    <input type="tel" id="contact_number" name="contact_number" required><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br><br>
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea><br><br>
    <input type="submit" value="Submit">
</form>
```

```bash
# .env

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-password
MAIL_FROM_EMAIL=your-email@gmail.com
MAIL_TO_EMAIL=recipient-email@gmail.com
```
