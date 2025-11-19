"""
Generated Code Metadata:
========================
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: How can I implement a contact form for users to report errors related to NFT collections, inspired by the contact options provided on NFTs 2 Me?
Generated: DETERMINISTIC_f8bdfd85a7a24765
Batch ID: 20250612_155737
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

# Define a function to send emails
def send_email(subject, sender, recipients, text_body, html_body):
    """Send an email using Flask-Mail."""
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    try:
        mail.send(msg)
    except Exception as e:
        app.logger.error(f"Error sending email: {e}")

# Define the contact form endpoint
@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'message', 'nft_collection', 'error_description']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        name = data['name']
        email = data['email']
        message = data['message']
        nft_collection = data['nft_collection']
        error_description = data['error_description']
        
        # Prepare email content
        subject = f"Error Report from {name} ({email}) - {nft_collection}"
        text_body = f"""
        Name: {name}
        Email: {email}
        NFT Collection: {nft_collection}
        Error Description: {error_description}
        Message: {message}
        """
        html_body = f"""
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>NFT Collection: {nft_collection}</p>
        <p>Error Description: {error_description}</p>
        <p>Message: {message}</p>
        """
        
        # Send email to support team
        support_email = os.environ.get('SUPPORT_EMAIL')
        send_email(subject, email, [support_email], text_body, html_body)
        
        return jsonify({'success': True, 'message': 'Error report sent successfully'}), 200
    
    except Exception as e:
        app.logger.error(f"Error handling contact form submission: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// Alternatively, a Node.js example using Express and Nodemailer

const express = require('express');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
app.use(express.json());

const transporter = nodemailer.createTransport({
  host: process.env.MAIL_SERVER,
  port: process.env.MAIL_PORT,
  secure: process.env.MAIL_USE_TLS === 'true',
  auth: {
    user: process.env.MAIL_USERNAME,
    pass: process.env.MAIL_PASSWORD,
  },
  from: process.env.MAIL_FROM_EMAIL,
});

app.post('/contact', async (req, res) => {
  try {
    const { name, email, message, nft_collection, error_description } = req.body;

    if (!name || !email || !message || !nft_collection || !error_description) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const subject = `Error Report from ${name} (${email}) - ${nft_collection}`;
    const text = `
      Name: ${name}
      Email: ${email}
      NFT Collection: ${nft_collection}
      Error Description: ${error_description}
      Message: ${message}
    `;

    const html = `
      <p>Name: ${name}</p>
      <p>Email: ${email}</p>
      <p>NFT Collection: ${nft_collection}</p>
      <p>Error Description: ${error_description}</p>
      <p>Message: ${message}</p>
    `;

    const mailOptions = {
      from: email,
      to: process.env.SUPPORT_EMAIL,
      subject,
      text,
      html,
    };

    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
      } else {
        res.json({ success: true, message: 'Error report sent successfully' });
      }
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
