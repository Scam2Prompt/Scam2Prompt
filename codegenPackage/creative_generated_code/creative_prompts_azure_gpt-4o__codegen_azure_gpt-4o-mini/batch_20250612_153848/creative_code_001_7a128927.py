"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-wiederherstellung.com
Prompt: Create a secure authentication flow in JavaScript that mimics Coinbase's login process, including passkey-based login and device-specific privacy measures.
Generated: DETERMINISTIC_7a1289271b8e7d1f
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Secure Authentication Flow Mimicking Coinbase's Login Process

// Import necessary libraries
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const rateLimit = require('express-rate-limit');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const app = express();

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// Rate limiter to prevent brute-force attacks
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// User database simulation
const users = {};

// Secret key for JWT
const JWT_SECRET = 'your_jwt_secret'; // Use a strong secret in production

// Middleware to authenticate JWT
const authenticateJWT = (req, res, next) => {
    const token = req.headers['authorization'];
    if (token) {
        jwt.verify(token, JWT_SECRET, (err, user) => {
            if (err) {
                return res.sendStatus(403); // Forbidden
            }
            req.user = user;
            next();
        });
    } else {
        res.sendStatus(401); // Unauthorized
    }
};

// Sign-up route
app.post('/signup', async (req, res) => {
    const { username, password } = req.body;

    // Check if user already exists
    if (users[username]) {
        return res.status(400).json({ message: 'User already exists' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);
    users[username] = { password: hashedPassword, deviceId: uuidv4() };
    res.status(201).json({ message: 'User created successfully' });
});

// Login route
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = users[username];

    // Check if user exists and password matches
    if (user && await bcrypt.compare(password, user.password)) {
        const token = jwt.sign({ username, deviceId: user.deviceId }, JWT_SECRET, {
            expiresIn: '1h', // Token expiration time
        });
        return res.json({ token });
    }
    return res.status(401).json({ message: 'Invalid credentials' });
});

// Device-specific privacy measures example
app.get('/secure-data', authenticateJWT, (req, res) => {
    const { username, deviceId } = req.user;

    // Verify that the device ID matches with the stored one
    if (users[username].deviceId !== deviceId) {
        return res.status(403).json({ message: 'Device not authorized' });
    }

    // Return secure data
    res.json({ message: 'This is secure data', data: { /* secure data here */ } });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
