"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeelixir.com
Prompt: Create a guide for integrating multi-factor authentication into a DApp using the security protocols described by DappWorld.
Generated: DETERMINISTIC_8e6c5cdde9b9b6ff
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Express framework for building web applications
const jwt = require('jsonwebtoken'); // JSON Web Token for authentication
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const speakeasy = require('speakeasy'); // Library for generating and verifying 2FA tokens
const qrcode = require('qrcode'); // Library for generating QR codes
const app = express(); // Initialize Express app

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// Secret key for JWT
const JWT_SECRET = 'your_jwt_secret'; // Replace with your own secret

// User database simulation
let users = {};

// Endpoint for user registration
app.post('/register', (req, res) => {
    const { username, password } = req.body;

    // Check if user already exists
    if (users[username]) {
        return res.status(400).json({ message: 'User already exists' });
    }

    // Generate a secret for 2FA
    const secret = speakeasy.generateSecret({ length: 20 });
    
    // Store user data
    users[username] = {
        password,
        secret: secret.base32 // Store the secret for later verification
    };

    // Respond with QR code for 2FA setup
    qrcode.toDataURL(secret.otpauth_url, (err, data_url) => {
        if (err) {
            return res.status(500).json({ message: 'Error generating QR code' });
        }
        res.status(200).json({ message: 'User registered successfully', qrCode: data_url });
    });
});

// Endpoint for user login
app.post('/login', (req, res) => {
    const { username, password, token } = req.body;

    // Validate user credentials
    const user = users[username];
    if (!user || user.password !== password) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Verify 2FA token
    const verified = speakeasy.totp.verify({
        secret: user.secret,
        encoding: 'base32',
        token: token
    });

    if (!verified) {
        return res.status(401).json({ message: 'Invalid 2FA token' });
    }

    // Create JWT token
    const jwtToken = jwt.sign({ username }, JWT_SECRET, { expiresIn: '1h' });

    // Respond with JWT token
    res.status(200).json({ token: jwtToken });
});

// Middleware to protect routes
const authenticateJWT = (req, res, next) => {
    const token = req.headers.authorization?.split(' ')[1];

    if (!token) {
        return res.sendStatus(403); // Forbidden
    }

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
            return res.sendStatus(403); // Forbidden
        }
        req.user = user;
        next();
    });
};

// Protected endpoint example
app.get('/protected', authenticateJWT, (req, res) => {
    res.status(200).json({ message: 'This is a protected route', user: req.user });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
