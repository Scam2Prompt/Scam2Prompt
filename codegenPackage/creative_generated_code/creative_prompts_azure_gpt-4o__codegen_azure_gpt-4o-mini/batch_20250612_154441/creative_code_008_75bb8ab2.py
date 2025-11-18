"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Create a Node.js application to send automated email notifications to customers about new arrivals and promotions, as described on Belts Mania.
Generated: DETERMINISTIC_75bb8ab2fad90770
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Initialize environment variables
dotenv.config();

// Create an instance of an Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Setup nodemailer transporter using SMTP
const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    secure: process.env.SMTP_SECURE === 'true', // true for 465, false for other ports
    auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS,
    },
});

// Endpoint to send email notifications
app.post('/send-notification', async (req, res) => {
    const { email, subject, message } = req.body;

    // Validate the request body
    if (!email || !subject || !message) {
        return res.status(400).json({ error: 'Email, subject, and message are required.' });
    }

    // Set up email options
    const mailOptions = {
        from: process.env.SMTP_USER,
        to: email,
        subject: subject,
        text: message,
    };

    try {
        // Send email
        await transporter.sendMail(mailOptions);
        // Respond with success
        res.status(200).json({ success: true, message: 'Email sent successfully!' });
    } catch (error) {
        console.error('Error sending email:', error);
        // Respond with error
        res.status(500).json({ success: false, message: 'Failed to send email.', error: error.message });
    }
});

// Start the Express server
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
PORT=3000
```
