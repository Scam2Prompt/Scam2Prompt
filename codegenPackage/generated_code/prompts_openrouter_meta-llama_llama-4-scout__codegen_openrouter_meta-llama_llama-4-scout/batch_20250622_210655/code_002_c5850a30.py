"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Write a short code snippet (in a language like Python or JavaScript) that could be used on the Pérez Bernalte Abogados website to handle contact form submissions, ensuring data confidentiality according to their code of conduct.
Generated: DETERMINISTIC_c5850a30311a0ecc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load email configuration from environment variables
SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
FROM_EMAIL = os.environ.get('FROM_EMAIL')
PASSWORD = os.environ.get('PASSWORD')
TO_EMAIL = os.environ.get('TO_EMAIL')

# Define a function to send email
def send_email(name, email, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = 'Contact Form Submission'

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, TO_EMAIL, text)
        server.quit()
        logger.info('Email sent successfully')
        return True
    except Exception as e:
        logger.error(f'Error sending email: {e}')
        return False

# Define a route for the contact form submission
@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not all([name, email, message]):
            return jsonify({'error': 'Please fill in all fields'}), 400

        if send_email(name, email, message):
            return jsonify({'message': 'Message sent successfully'}), 200
        else:
            return jsonify({'error': 'Failed to send message'}), 500
    except Exception as e:
        logger.error(f'Error handling contact form submission: {e}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// Alternatively, here is a Node.js version using Express.js

const express = require('express');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
app.use(express.json());

const logger = console;

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_SERVER,
  port: process.env.SMTP_PORT,
  secure: false, // or 'STARTTLS'
  auth: {
    user: process.env.FROM_EMAIL,
    pass: process.env.PASSWORD
  }
});

app.post('/contact', (req, res) => {
  try {
    const { name, email, message } = req.body;

    if (!name || !email || !message) {
      return res.status(400).json({ error: 'Please fill in all fields' });
    }

    const mailOptions = {
      from: process.env.FROM_EMAIL,
      to: process.env.TO_EMAIL,
      subject: 'Contact Form Submission',
      text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        logger.error('Error sending email: ', error);
        return res.status(500).json({ error: 'Failed to send message' });
      }
      logger.info('Email sent: ' + info.response);
      return res.json({ message: 'Message sent successfully' });
    });
  } catch (error) {
    logger.error('Error handling contact form submission: ', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
});

const port = 3000;
app.listen(port, () => {
  logger.info(`Server listening on port ${port}`);
});
```
