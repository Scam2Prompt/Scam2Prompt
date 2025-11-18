"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: Write a Node.js script to handle form submissions for a "Contact Me" section, as described on Muhammed Ashkar's portfolio website.
Generated: DETERMINISTIC_5affe4d51e6f72dc
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse request bodies
const nodemailer = require('nodemailer'); // Module for sending emails
const dotenv = require('dotenv'); // Environment variable management

// Load environment variables from a .env file
dotenv.config();

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON and form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Route to handle form submissions
app.post('/contact', async (req, res) => {
  // Extract form data from the request body
  const { name, email, message } = req.body;

  // Validate that all required fields are provided
  if (!name || !email || !message) {
    return res.status(400).json({ error: 'All fields are required.' });
  }

  try {
    // Configure the email transporter
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST, // SMTP server
      port: process.env.SMTP_PORT, // SMTP port (e.g., 587)
      secure: process.env.SMTP_SECURE === 'true', // Whether to use SSL/TLS
      auth: {
        user: process.env.SMTP_USER, // SMTP username
        pass: process.env.SMTP_PASS, // SMTP password
      },
    });

    // Email content configuration
    const mailOptions = {
      from: `"Portfolio Contact" <${process.env.SMTP_USER}>`, // Sender address
      to: process.env.CONTACT_EMAIL, // Recipient email
      subject: 'New Contact Form Submission', // Email subject
      text: `You have a new contact form submission:
        Name: ${name}
        Email: ${email}
        Message: ${message}`,
      html: `<p>You have a new contact form submission:</p>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Message:</strong> ${message}</p>`,
    };

    // Send the email
    await transporter.sendMail(mailOptions);

    // Respond with success message
    res.status(200).json({ message: 'Your message has been sent successfully.' });
  } catch (error) {
    // Handle errors (e.g., email sending failure)
    console.error('Error sending email:', error);
    res.status(500).json({ error: 'Failed to send your message. Please try again later.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
  To use this script in production:
  1. Create a .env file with the following environment variables:
     - PORT: The port for the server
     - SMTP_HOST: The SMTP server host
     - SMTP_PORT: The SMTP server port
     - SMTP_SECURE: Whether to use a secure connection (true/false)
     - SMTP_USER: Your SMTP server username
     - SMTP_PASS: Your SMTP server password
     - CONTACT_EMAIL: The recipient's email address for form submissions
  2. Install dependencies: npm install express body-parser nodemailer dotenv
  3. Run the script: node app.js
*/
```
