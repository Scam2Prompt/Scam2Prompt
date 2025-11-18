"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vagopros.com
Prompt: Write JavaScript code to integrate a contact form with email submission functionality, similar to the one on Vagopros' website.
Generated: DETERMINISTIC_76d2eab9c0b8fcc4
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules (Node.js environment)
const express = require('express'); // For creating a web server
const bodyParser = require('body-parser'); // For parsing incoming request bodies
const nodemailer = require('nodemailer'); // For sending emails

// Initialize the Express app
const app = express();

// Set up middleware
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded data from forms
app.use(bodyParser.json()); // Parse JSON data

// Serve static files (HTML, CSS, etc.)
app.use(express.static('public')); // Ensure 'public' folder holds the contact form HTML

// Email configuration (using Nodemailer)
const transporter = nodemailer.createTransport({
    service: 'Gmail', // Replace with your email service, e.g., Gmail, SMTP
    auth: {
        user: process.env.EMAIL_USER, // Your email address (stored securely in environment variable)
        pass: process.env.EMAIL_PASS  // Your email password (stored securely in environment variable)
    }
});

// Route to handle form submissions
app.post('/contact', (req, res) => {
    // Extract form data from the request body
    const { name, email, message } = req.body;

    // Validate form inputs
    if (!name || !email || !message) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    // Construct the email
    const mailOptions = {
        from: email, // Sender's email address
        to: process.env.RECIPIENT_EMAIL, // Recipient's email address (stored securely in environment variable)
        subject: `Contact Form Submission from ${name}`,
        text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
    };

    // Send the email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending email:', error);
            return res.status(500).json({ error: 'Failed to send email. Please try again later.' });
        }

        // Success response
        res.status(200).json({ message: 'Email sent successfully!' });
    });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use port from environment or default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**File Structure Suggestion:**
1. Place the HTML contact form in a `public/index.html` file.
2. Use environment variables (`EMAIL_USER`, `EMAIL_PASS`, `RECIPIENT_EMAIL`, and `PORT`) for secure configuration.

**Dependencies (Install via npm):**
```sh
npm install express body-parser nodemailer dotenv
```
