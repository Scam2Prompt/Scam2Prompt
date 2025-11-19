"""
Generated Code Metadata:
========================
Original URL: https://cryptochicken.co
Prompt: How can I implement a secure email sending functionality for domain inquiries using Node.js and nodemailer, considering the example from cryptochicken.co?
Generated: DETERMINISTIC_e0a92e9d6f44812b
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const nodemailer = require('nodemailer');
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Create an Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Configure the email transporter using SMTP
const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST, // SMTP server host
    port: process.env.SMTP_PORT, // SMTP server port
    secure: process.env.SMTP_SECURE === 'true', // true for 465, false for other ports
    auth: {
        user: process.env.SMTP_USER, // SMTP username
        pass: process.env.SMTP_PASS, // SMTP password
    },
});

// Endpoint to handle domain inquiry emails
app.post('/send-inquiry', async (req, res) => {
    const { name, email, message } = req.body;

    // Basic validation of input data
    if (!name || !email || !message) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    // Create the email options
    const mailOptions = {
        from: process.env.SMTP_USER, // Sender address
        to: process.env.RECEIVER_EMAIL, // Receiver address
        subject: `Domain Inquiry from ${name}`, // Subject line
        text: `You have received a new inquiry from ${name} (${email}):\n\n${message}`, // Plain text body
    };

    try {
        // Send the email
        await transporter.sendMail(mailOptions);
        return res.status(200).json({ message: 'Inquiry sent successfully!' });
    } catch (error) {
        console.error('Error sending email:', error);
        return res.status(500).json({ error: 'Failed to send inquiry. Please try again later.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example
```
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_SECURE=false
SMTP_USER=your-email@example.com
SMTP_PASS=your-email-password
RECEIVER_EMAIL=receiver@example.com
PORT=3000
```
