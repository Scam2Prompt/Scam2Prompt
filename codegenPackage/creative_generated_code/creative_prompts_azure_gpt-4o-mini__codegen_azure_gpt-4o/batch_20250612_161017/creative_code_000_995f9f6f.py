"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsconnect.42web.io
Prompt: Generate a code snippet to set up a Node.js application on iFastNet Web Hosting with multiple email accounts.
Generated: DETERMINISTIC_995f9f6f81995b09
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
const express = require('express');
const nodemailer = require('nodemailer');
require('dotenv').config(); // Load environment variables from .env file

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Email account configuration
const emailAccounts = [
  {
    name: 'Support',
    email: process.env.SUPPORT_EMAIL,
    password: process.env.SUPPORT_PASSWORD,
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT, 10),
  },
  {
    name: 'Sales',
    email: process.env.SALES_EMAIL,
    password: process.env.SALES_PASSWORD,
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT, 10),
  },
];

// Function to send emails
async function sendEmail(accountName, to, subject, text) {
  try {
    // Find the email account configuration by name
    const account = emailAccounts.find((acc) => acc.name === accountName);
    if (!account) {
      throw new Error(`Email account "${accountName}" not found.`);
    }

    // Create a transporter instance for the specified account
    const transporter = nodemailer.createTransport({
      host: account.host,
      port: account.port,
      secure: account.port === 465, // Use secure connection if port is 465
      auth: {
        user: account.email,
        pass: account.password,
      },
    });

    // Send the email
    const info = await transporter.sendMail({
      from: account.email, // Sender email
      to, // Recipient email
      subject, // Email subject
      text, // Email body
    });

    console.log(`Email sent successfully: ${info.messageId}`);
    return info.messageId;
  } catch (error) {
    console.error(`Error sending email: ${error.message}`);
    throw error;
  }
}

// Route to send emails
app.post('/send-email', async (req, res) => {
  const { accountName, to, subject, text } = req.body;

  // Validate request body
  if (!accountName || !to || !subject || !text) {
    return res.status(400).json({ error: 'Missing required fields.' });
  }

  try {
    const messageId = await sendEmail(accountName, to, subject, text);
    res.status(200).json({ message: 'Email sent successfully.', messageId });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start the application
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
 * Environment Variables (.env file example):
 * SUPPORT_EMAIL=support@example.com
 * SUPPORT_PASSWORD=yourpassword
 * SALES_EMAIL=sales@example.com
 * SALES_PASSWORD=yourpassword
 * SMTP_HOST=smtp.example.com
 * SMTP_PORT=465
 * PORT=3000
 */
```
