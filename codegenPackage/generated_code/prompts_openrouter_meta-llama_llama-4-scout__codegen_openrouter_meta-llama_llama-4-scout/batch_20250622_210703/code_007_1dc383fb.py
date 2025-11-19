"""
Generated Code Metadata:
========================
Original URL: https://nashad.in
Prompt: "Write a code snippet to implement a free quote or inquiry form for an educational website like Nashad.in, handling user input and sending emails."
Generated: DETERMINISTIC_1dc383fb1679c916
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a function to send email
def send_email(name, email, phone, message):
    """
    Send an email to the admin with the user's inquiry details.

    Args:
        name (str): The user's name.
        email (str): The user's email address.
        phone (str): The user's phone number.
        message (str): The user's inquiry message.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    try:
        # Define email configuration
        sender_email = "your-email@gmail.com"
        sender_password = "your-email-password"
        receiver_email = "receiver-email@example.com"

        # Create a message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Inquiry from Nashad.in"

        # Set email body
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Set up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Define a route for the inquiry form
@app.route('/inquiry', methods=['POST'])
def inquiry():
    """
    Handle the inquiry form submission.

    Returns:
        jsonify: A JSON response with a success message or error details.
    """
    try:
        # Get user input from the form
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Validate user input
        if not name or not email or not phone or not message:
            return jsonify({'error': 'Please fill in all fields.'}), 400

        # Send email
        if send_email(name, email, phone, message):
            return jsonify({'message': 'Inquiry sent successfully.'}), 200
        else:
            return jsonify({'error': 'Failed to send inquiry.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// Alternatively, a JavaScript and HTML example using Node.js and Express

// server.js
const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
app.use(express.json());

// Email configuration
const senderEmail = "your-email@gmail.com";
const senderPassword = "your-email-password";
const receiverEmail = "receiver-email@example.com";

// Create a transporter
const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false, // or 'STARTTLS'
    auth: {
        user: senderEmail,
        pass: senderPassword
    }
});

// Define a route for the inquiry form
app.post('/inquiry', (req, res) => {
    try {
        // Get user input from the form
        const { name, email, phone, message } = req.body;

        // Validate user input
        if (!name || !email || !phone || !message) {
            return res.status(400).json({ error: 'Please fill in all fields.' });
        }

        // Send email
        const mailOptions = {
            from: senderEmail,
            to: receiverEmail,
            subject: "Inquiry from Nashad.in",
            text: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nMessage: ${message}`
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                return res.status(500).json({ error: 'Failed to send inquiry.' });
            }
            return res.json({ message: 'Inquiry sent successfully.' });
        });
    } catch (error) {
        return res.status(500).json({ error: error.message });
    }
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Form</title>
</head>
<body>
    <form id="inquiry-form">
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

    <script>
        const form = document.getElementById('inquiry-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            try {
                const formData = new FormData(form);
                const data = Object.fromEntries(formData);
                const response = await fetch('/inquiry', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                console.log(result);
                if (result.message) {
                    alert(result.message);
                    form.reset();
                } else {
                    alert(result.error);
                }
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
