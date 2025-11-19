"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multihelp.pages.dev
Prompt: Describe how to implement multi-factor authentication in a DApp to enhance user security, referencing DAPP SHIELD's security features.
Generated: DETERMINISTIC_b9adfa1a19f18ef3
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const speakeasy = require('speakeasy');
const QRCode = require('qrcode');

// Initialize the Express application
const app = express();

// Configure middleware
app.use(bodyParser.json());
app.use(session({
    secret: 'your_secret_key', // Replace with a strong secret
    resave: false,
    saveUninitialized: true
}));

// In-memory store for user data (should be replaced with a database in production)
const users = {};

// Route to register a new user
app.post('/register', (req, res) => {
    const { username, email } = req.body;

    // Basic validation
    if (!username || !email) {
        return res.status(400).json({ message: 'Username and email are required.' });
    }
    
    // Generate a secret for 2FA
    const secret = speakeasy.generateSecret({ length: 20 });
    
    // Store user information
    users[username] = { email, secret: secret.base32, verified: false };

    // Generate a QR code for the user to scan
    QRCode.toDataURL(secret.otpauth_url, (err, data_url) => {
        if (err) {
            return res.status(500).json({ message: 'Error generating QR code.' });
        }
        res.json({ message: 'User registered. Scan the QR code.', qrCode: data_url });
    });
});

// Route to verify the 2FA code
app.post('/verify', (req, res) => {
    const { username, token } = req.body;

    // Check if user exists
    if (!users[username]) {
        return res.status(400).json({ message: 'User not found.' });
    }

    // Verify the token
    const isVerified = speakeasy.totp.verify({
        secret: users[username].secret,
        encoding: 'base32',
        token,
    });

    if (isVerified) {
        users[username].verified = true;
        return res.json({ message: '2FA successfully verified.' });
    } else {
        return res.status(400).json({ message: 'Invalid token.' });
    }
});

// Route to send a security code via email
app.post('/send-code', (req, res) => {
    const { username } = req.body;

    // Check if user exists and is verified
    if (!users[username] || !users[username].verified) {
        return res.status(400).json({ message: 'User must be registered and verified.' });
    }

    // Generate a random security code
    const securityCode = Math.floor(100000 + Math.random() * 900000).toString();

    // Send the security code via email
    const transporter = nodemailer.createTransport({
        service: 'gmail', // Use your email provider
        auth: {
            user: 'your_email@example.com',
            pass: 'your_email_password', // Use environment variables in production
        },
    });

    const mailOptions = {
        from: 'your_email@example.com',
        to: users[username].email,
        subject: 'Your Security Code',
        text: `Your security code is: ${securityCode}`,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return res.status(500).json({ message: 'Error sending email.' });
        }
        // Store the code for later verification
        users[username].securityCode = securityCode;
        res.json({ message: 'Security code sent to your email.' });
    });
});

// Route to verify the security code
app.post('/verify-code', (req, res) => {
    const { username, code } = req.body;

    // Check if user exists
    if (!users[username]) {
        return res.status(400).json({ message: 'User not found.' });
    }

    // Verify the security code
    if (users[username].securityCode === code) {
        return res.json({ message: 'Security code verified. Access granted.' });
    } else {
        return res.status(400).json({ message: 'Invalid security code.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
