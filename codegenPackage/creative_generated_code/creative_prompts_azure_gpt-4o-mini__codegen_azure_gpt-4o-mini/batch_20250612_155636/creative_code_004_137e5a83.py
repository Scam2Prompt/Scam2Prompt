"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldliberty.wiki
Prompt: Illustrate how to implement two-factor authentication in a decentralized application (dApp) for enhanced security on the WLFI platform.
Generated: DETERMINISTIC_137e5a83d34894a8
Batch ID: 20250612_155636
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const nodemailer = require('nodemailer');
const crypto = require('crypto');

const app = express();
app.use(express.json());

// Secrets and configuration
const JWT_SECRET = 'your_jwt_secret'; // Replace with your own secret
const emailTransporter = nodemailer.createTransport({
    service: 'gmail', // Use a suitable email service
    auth: {
        user: 'your_email@gmail.com', // Replace with your email
        pass: 'your_email_password' // Replace with your email password
    }
});

// Simulated user database
const users = {};

// Generate a random verification code
function generateVerificationCode() {
    return crypto.randomBytes(3).toString('hex'); // 6-character hex code
}

// Register user
app.post('/register', async (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).json({ error: 'Username and password are required.' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    users[username] = { password: hashedPassword, isVerified: false };

    return res.status(201).json({ message: 'User registered. Please verify your email.' });
});

// Send verification email
app.post('/send-verification', async (req, res) => {
    const { username } = req.body;

    if (!users[username]) {
        return res.status(404).json({ error: 'User not found.' });
    }

    const verificationCode = generateVerificationCode();
    users[username].verificationCode = verificationCode;

    // Send email logic
    const mailOptions = {
        from: 'your_email@gmail.com', // Replace with your email
        to: username, // Use username as email
        subject: 'Your Verification Code',
        text: `Your verification code is: ${verificationCode}`
    };

    try {
        await emailTransporter.sendMail(mailOptions);
        return res.status(200).json({ message: 'Verification email sent.' });
    } catch (error) {
        return res.status(500).json({ error: 'Error sending verification email.' });
    }
});

// Verify user
app.post('/verify', async (req, res) => {
    const { username, code } = req.body;

    if (!users[username] || users[username].verificationCode !== code) {
        return res.status(400).json({ error: 'Invalid username or verification code.' });
    }

    users[username].isVerified = true;
    delete users[username].verificationCode; // Clean up
    return res.status(200).json({ message: 'User verified successfully.' });
});

// Login with two-factor authentication
app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    if (!users[username] || !users[username].isVerified) {
        return res.status(401).json({ error: 'Invalid credentials or user not verified.' });
    }

    const isPasswordValid = await bcrypt.compare(password, users[username].password);
    if (!isPasswordValid) {
        return res.status(401).json({ error: 'Invalid credentials.' });
    }

    // Generate JWT token
    const token = jwt.sign({ username }, JWT_SECRET, { expiresIn: '24h' });
    return res.status(200).json({ token });
});

// Middleware to protect routes
function authenticateToken(req, res, next) {
    const token = req.headers['authorization'] && req.headers['authorization'].split(' ')[1];
    if (!token) return res.sendStatus(401);

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
}

// Protected route example
app.get('/secure-data', authenticateToken, (req, res) => {
    res.json({ message: 'This is secure data.', user: req.user });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
