"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Create a Node.js application to send automated email notifications to customers about new arrivals and promotions, as described on Belts Mania.
Generated: DETERMINISTIC_75bb8ab2fad90770
Batch ID: 20250612_154441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const nodemailer = require('nodemailer'); // Library for sending emails
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse request body as JSON
app.use(bodyParser.json());

// Email configuration
const transporter = nodemailer.createTransport({
  service: 'gmail', // You may use other email services like SendGrid, Outlook, etc.
  auth: {
    user: process.env.EMAIL_USER, // Set environment variable for email account
    pass: process.env.EMAIL_PASS, // Set environment variable for email password
  },
});

// Function to send promotional email
const sendPromotionalEmail = async (customerEmail, subject, message) => {
  try {
    const mailOptions = {
      from: process.env.EMAIL_USER, // Sender's email address
      to: customerEmail, // Recipient's email address
      subject: subject, // Email subject
      text: message, // Email message
    };

    // Send the email
    await transporter.sendMail(mailOptions);
    console.log(`Email sent successfully to ${customerEmail}`);
  } catch (error) {
    console.error(`Failed to send email to ${customerEmail}:`, error.message);
    throw new Error('Email sending failed');
  }
};

// Endpoint to trigger email notifications
app.post('/send-email', async (req, res) => {
  const { customerEmail, subject, message } = req.body;

  // Input validation
  if (!customerEmail || !subject || !message) {
    return res.status(400).json({ error: 'Missing required fields: customerEmail, subject, or message' });
  }

  try {
    await sendPromotionalEmail(customerEmail, subject, message);
    res.status(200).json({ message: 'Email sent successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to send email' });
  }
});

// Default route for health check
app.get('/', (req, res) => {
  res.send('Belts Mania Email Notification Service is running!');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

/*
 * Best Practices:
 * 1. Use environment variables to store sensitive information (e.g., EMAIL_USER, EMAIL_PASS).
 * 2. Validate input data to prevent invalid or malicious input.
 * 3. Use proper error handling to avoid crashing the application.
 * 4. Modularize the code (e.g., separate email logic into its own function).
 * 5. Log important events for monitoring and debugging.
 */
```

Make sure to set the environment variables (`EMAIL_USER` and `EMAIL_PASS`) before running the application, and install required dependencies (`express`, `nodemailer`, `body-parser`) using `npm install`.
