"""
Generated Code Metadata:
========================
Original URL: https://oliveiragomesadv.com.br
Prompt: Generate a code snippet for a simple contact form similar to the one found on oliveiragomesadv.com.br.
Generated: DETERMINISTIC_6144d8cde1df1298
Batch ID: 20250622_210443
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

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

# Define a function to send emails
def send_email(name, email, phone, message):
    try:
        msg = Message('New Contact Form Submission',
                      sender='your-email@gmail.com',
                      recipients=['your-email@gmail.com'])
        msg.body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        mail.send(msg)
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# Define the contact form endpoint
@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'message': 'No data provided'}), 400
        
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        if not all([name, email, phone, message]):
            return jsonify({'success': False, 'message': 'Please fill all fields'}), 400

        send_email(name, email, phone, message)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

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

        if (result.success) {
            console.log(result.message);
            form.reset();
        } else {
            console.error(result.message);
        }
    } catch (error) {
        console.error(error);
    }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    <script src="contact-form.js"></script>
</body>
</html>
```
