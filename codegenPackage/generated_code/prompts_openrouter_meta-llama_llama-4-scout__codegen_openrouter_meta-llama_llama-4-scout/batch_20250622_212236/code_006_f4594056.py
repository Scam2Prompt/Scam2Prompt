"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Develop a Node.js server-side application to handle contact form submissions from the Sakura Dance Studio website, including email notifications and data storage.
Generated: DETERMINISTIC_f4594056a0b9ec2f
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const port = 3000;
const nodemailer = require('nodemailer');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for contact form data
const contactFormSchema = new mongoose.Schema({
  name: String,
  email: String,
  message: String,
});

// Create model for contact form data
const ContactForm = mongoose.model('ContactForm', contactFormSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Define function to send email notifications
async function sendEmailNotification(name, email, message) {
  try {
    // Create transporter for nodemailer
    const transporter = nodemailer.createTransport({
      host: process.env.EMAIL_HOST,
      port: process.env.EMAIL_PORT,
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASSWORD,
      },
    });

    // Define email options
    const mailOptions = {
      from: email,
      to: process.env.RECEIVER_EMAIL,
      subject: 'Sakura Dance Studio Contact Form Submission',
      text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`,
    };

    // Send email
    await transporter.sendMail(mailOptions);
  } catch (error) {
    console.error('Error sending email notification:', error);
  }
}

// API endpoint to handle contact form submissions
app.post('/contact', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.name || !req.body.email || !req.body.message) {
      return res.status(400).json({ error: 'Please provide all required fields' });
    }

    // Create new contact form document
    const contactForm = new ContactForm(req.body);

    // Save contact form data to MongoDB
    await contactForm.save();

    // Send email notification
    await sendEmailNotification(req.body.name, req.body.email, req.body.message);

    // Return success response
    res.json({ message: 'Contact form submission successful' });
  } catch (error) {
    console.error('Error handling contact form submission:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).json({ error: 'Internal server error' });
});
```
