"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Write a Node.js script to handle form submissions for a "Contact Me" section, as described on Muhammed Ashkar's portfolio website.
Generated: DETERMINISTIC_5affe4d51e6f72dc
Batch ID: 20250612_150440
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
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');
const logger = require('./logger'); // Assuming a custom logger module

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Define contact form submission endpoint
/**
 * Handles contact form submissions.
 * 
 * @param {string} name - The sender's name.
 * @param {string} email - The sender's email address.
 * @param {string} message - The message sent by the user.
 * 
 * @returns {object} A JSON response indicating success or failure.
 */
app.post('/contact', async (req, res) => {
    try {
        // Validate request body
        if (!req.body.name || !req.body.email || !req.body.message) {
            return res.status(400).json({ error: 'Please fill in all fields.' });
        }

        // Create transporter for sending emails
        const transporter = nodemailer.createTransport({
            host: process.env.EMAIL_HOST,
            port: process.env.EMAIL_PORT,
            secure: process.env.EMAIL_SECURE === 'true',
            auth: {
                user: process.env.EMAIL_USER,
                pass: process.env.EMAIL_PASSWORD
            }
        });

        // Define email options
        const mailOptions = {
            from: req.body.email,
            to: process.env.RECEIVER_EMAIL,
            subject: 'Contact Form Submission',
            text: `
                Name: ${req.body.name}
                Email: ${req.body.email}
                Message: ${req.body.message}
            `
        };

        // Send email
        await transporter.sendMail(mailOptions);

        // Log successful submission
        logger.info('Contact form submitted successfully.');

        // Return success response
        return res.json({ message: 'Message sent successfully!' });
    } catch (error) {
        // Log error
        logger.error('Error handling contact form submission:', error);

        // Return error response
        return res.status(500).json({ error: 'Failed to send message. Please try again.' });
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    logger.info(`Server listening on port ${PORT}`);
});
```
