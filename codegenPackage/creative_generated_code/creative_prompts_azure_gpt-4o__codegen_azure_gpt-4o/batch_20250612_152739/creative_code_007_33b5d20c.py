"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Develop a Node.js application to send automated email notifications to students about course updates, similar to the communication system used by Araform.
Generated: DETERMINISTIC_33b5d20c0b2e230d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const nodemailer = require('nodemailer'); // For sending emails
const express = require('express'); // For HTTP server
const bodyParser = require('body-parser'); // For parsing incoming request data

// Initialize Express application
const app = express();

// Use body-parser middleware to parse JSON data
app.use(bodyParser.json());

// Configuration for the email service
const transporter = nodemailer.createTransport({
  service: 'Gmail', // Using Gmail as the email service
  auth: {
    user: process.env.EMAIL_USER, // Email account (set in environment variables)
    pass: process.env.EMAIL_PASS, // Email password (set in environment variables)
  },
});

// Route to send course update email notifications
app.post('/send-email', async (req, res) => {
  try {
    // Validate the input data
    const { studentEmail, courseName, updateMessage } = req.body;

    if (!studentEmail || !courseName || !updateMessage) {
      return res.status(400).json({
        error: 'Missing required fields: studentEmail, courseName, or updateMessage',
      });
    }

    // Email content
    const mailOptions = {
      from: process.env.EMAIL_USER, // Sender email address
      to: studentEmail, // Recipient email address
      subject: `Course Update: ${courseName}`, // Email subject
      text: `Hello,\n\nThere is an update for your course "${courseName}":\n\n${updateMessage}\n\nBest regards,\nYour Course Team`, // Email body
    };

    // Send the email
    await transporter.sendMail(mailOptions);

    // Respond with success message
    res.status(200).json({
      message: 'Email sent successfully!',
    });
  } catch (error) {
    // Handle errors
    console.error('Error sending email:', error.message);
    res.status(500).json({
      error: 'Failed to send email. Please try again later.',
    });
  }
});

// Route to check the health status of the server
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'Server is running!',
  });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable for port or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Note: Ensure the following environment variables are set:
// - EMAIL_USER: The email account username
// - EMAIL_PASS: The email account password
// - PORT: The port number for the server (optional)
```
