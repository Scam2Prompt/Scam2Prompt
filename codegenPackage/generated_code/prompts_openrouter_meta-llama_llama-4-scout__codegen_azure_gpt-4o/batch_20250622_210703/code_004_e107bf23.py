"""
Generated Code Metadata:
========================
Original URL: https://medanresortcity.com
Prompt: Create a Node.js application for handling inquiries and contact requests from potential buyers of Medan Resort City properties.
Generated: DETERMINISTIC_e107bf23e0fc79a9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const nodemailer = require('nodemailer'); // Module for sending emails
const dotenv = require('dotenv'); // Module for managing environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Middleware to parse URL-encoded request bodies
app.use(bodyParser.urlencoded({ extended: true }));

// Route to handle inquiries and contact requests
app.post('/contact', async (req, res) => {
  try {
    // Extract data from the request body
    const { name, email, phone, message } = req.body;

    // Validate required fields
    if (!name || !email || !message) {
      return res.status(400).json({ error: 'Name, email, and message are required.' });
    }

    // Create a transporter for sending emails
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: process.env.SMTP_PORT,
      secure: process.env.SMTP_SECURE === 'true', // Use TLS if specified
      auth: {
        user: process.env.SMTP_USER, // SMTP username
        pass: process.env.SMTP_PASS, // SMTP password
      },
    });

    // Email content
    const mailOptions = {
      from: process.env.SMTP_FROM, // Sender address
      to: process.env.CONTACT_EMAIL, // Recipient address
      subject: `New Inquiry from ${name}`, // Email subject
      text: `You have received a new inquiry:\n\nName: ${name}\nEmail: ${email}\nPhone: ${phone || 'N/A'}\nMessage: ${message}`, // Plain text body
    };

    // Send the email
    await transporter.sendMail(mailOptions);

    // Respond with success
    res.status(200).json({ message: 'Inquiry sent successfully.' });
  } catch (error) {
    // Log the error and respond with a failure message
    console.error('Error sending inquiry:', error);
    res.status(500).json({ error: 'Failed to send inquiry. Please try again later.' });
  }
});

// Route to handle health checks
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Create a `.env` file in the root directory with the following variables:
   ```
   PORT=3000
   SMTP_HOST=smtp.example.com
   SMTP_PORT=587
   SMTP_SECURE=false
   SMTP_USER=your_smtp_username
   SMTP_PASS=your_smtp_password
   SMTP_FROM=your_email@example.com
   CONTACT_EMAIL=recipient_email@example.com
   ```
2. Install required dependencies using:
   ```
   npm install express body-parser nodemailer dotenv
   ```
3. Run the application using:
   ```
   node app.js
   ```
