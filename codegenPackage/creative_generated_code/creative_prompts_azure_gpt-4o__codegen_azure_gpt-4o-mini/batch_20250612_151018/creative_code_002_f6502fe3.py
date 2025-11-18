"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola-321x.carbon-app-csq.pages.dev
Prompt: Generate a script using JavaScript to send login codes via email for a Cloudflare Access-based authentication system.
Generated: DETERMINISTIC_f6502fe36b9ee285
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // For creating the server
const nodemailer = require('nodemailer'); // For sending emails
const bodyParser = require('body-parser'); // For parsing request bodies
const crypto = require('crypto'); // For generating secure random codes
const app = express(); // Initialize the Express application

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Configure the email transporter using SMTP
const transporter = nodemailer.createTransport({
    host: 'smtp.your-email-provider.com', // Replace with your email provider's SMTP server
    port: 587, // Standard port for SMTP
    secure: false, // Use true for port 465, false for other ports
    auth: {
        user: 'your-email@example.com', // Your email
        pass: 'your-email-password', // Your email password
    },
});

// Function to generate a random login code
function generateLoginCode(length) {
    return crypto.randomBytes(length).toString('hex').substring(0, length);
}

// Route to handle login code requests
app.post('/send-login-code', async (req, res) => {
    const { email } = req.body;

    // Validate email format
    if (!email || !/\S+@\S+\.\S+/.test(email)) {
        return res.status(400).json({ error: 'Invalid email format.' });
    }

    // Generate a secure login code
    const loginCode = generateLoginCode(6); // Generate a 6-character login code

    // Email options
    const mailOptions = {
        from: 'your-email@example.com', // Sender address
        to: email, // Recipient email
        subject: 'Your Login Code', // Subject of the email
        text: `Your login code is: ${loginCode}`, // Plain text body
    };

    try {
        // Send the email
        await transporter.sendMail(mailOptions);
        
        // Respond with success
        return res.status(200).json({ message: 'Login code sent successfully.' });
    } catch (error) {
        console.error('Error sending email:', error);
        return res.status(500).json({ error: 'Failed to send login code. Please try again later.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use PORT from environment or default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to replace the placeholders with your actual email service provider's details and to install the required packages using npm:

```bash
npm install express nodemailer body-parser
```
