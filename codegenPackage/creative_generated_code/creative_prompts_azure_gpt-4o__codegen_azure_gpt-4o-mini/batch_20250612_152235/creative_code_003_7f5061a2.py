"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgo.web.app
Prompt: Write code to enable JavaScript-based authentication for a whitelist system modeled after the Shibonk Gang web app.
Generated: DETERMINISTIC_7f5061a240c681fc
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse request bodies
const session = require('express-session'); // Middleware for session management
const crypto = require('crypto'); // Module for cryptographic functions
const app = express(); // Create an instance of an Express application

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(session({ 
    secret: 'your-secret-key', // Secret key for session signing
    resave: false, // Don't resave session if unmodified
    saveUninitialized: true, // Save uninitialized sessions
    cookie: { secure: false } // Set to true if using HTTPS
}));

// Sample whitelist (in a real app, this should be stored in a database)
const whitelist = new Set(['user1@example.com', 'user2@example.com']);

// Utility function to hash passwords for storage
function hashPassword(password) {
    return crypto.createHash('sha256').update(password).digest('hex');
}

// Simulated user database (username: {password, isWhitelisted})
const users = {
    'user1@example.com': { password: hashPassword('password1'), isWhitelisted: true },
    'user2@example.com': { password: hashPassword('password2'), isWhitelisted: true },
    'user3@example.com': { password: hashPassword('password3'), isWhitelisted: false }
};

// Authentication middleware
function authenticate(req, res, next) {
    if (req.session.user) {
        next(); // Proceed to the next middleware or route handler
    } else {
        res.status(401).send('Unauthorized'); // Unauthorized access
    }
}

// Login route
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    // Validate request body
    if (!email || !password) {
        return res.status(400).send('Email and password are required.');
    }

    // Check if the user exists
    const user = users[email];
    if (user && user.password === hashPassword(password)) {
        // Check if user is whitelisted
        if (user.isWhitelisted) {
            req.session.user = { email }; // Store user info in session
            return res.status(200).send('Login successful.');
        } else {
            return res.status(403).send('Access denied. User is not whitelisted.'); // Not whitelisted
        }
    }
    
    return res.status(401).send('Invalid email or password.'); // Invalid credentials
});

// Logout route
app.post('/logout', authenticate, (req, res) => {
    req.session.destroy(err => {
        if (err) {
            return res.status(500).send('Could not log out.'); // Error during logout
        }
        res.status(200).send('Logout successful.'); // Successful logout
    });
});

// Protected route example
app.get('/protected', authenticate, (req, res) => {
    res.status(200).send(`Welcome, ${req.session.user.email}! This is a protected route.`); // Access granted
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace
    res.status(500).send('Something broke!'); // Server error response
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log the server start message
});
```
