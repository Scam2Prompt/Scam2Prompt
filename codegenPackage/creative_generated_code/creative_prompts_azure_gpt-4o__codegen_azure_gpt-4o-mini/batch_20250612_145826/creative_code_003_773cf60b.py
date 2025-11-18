"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.vip
Prompt: Generate code in Node.js to verify user sessions and handle session expiration errors.
Generated: DETERMINISTIC_773cf60b1cae9bf4
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const session = require('express-session');

// Initialize the Express application
const app = express();

// Set up session middleware with secure settings
app.use(session({
    secret: 'your-secret-key', // Change to a strong secret key
    resave: false,              // Prevent resaving of sessions
    saveUninitialized: false,   // Do not save uninitialized sessions
    cookie: {
        maxAge: 1000 * 60 * 30, // Set session expiration to 30 minutes
        httpOnly: true,         // Prevent client-side JavaScript from accessing cookies
        secure: true            // Use secure cookies (only if using HTTPS)
    }
}));

// Middleware to verify user sessions
const verifySession = (req, res, next) => {
    // Check if session exists
    if (req.session && req.session.userId) {
        // User is authenticated; proceed to the next middleware or route handler
        return next();
    } else {
        // Session expired or not authenticated; send an error response
        return res.status(401).json({ error: 'Session expired or not authenticated.' });
    }
};

// Example route that requires authentication
app.get('/protected', verifySession, (req, res) => {
    // If the user is verified, return a success message
    res.status(200).json({ message: 'You have access to this protected route!', userId: req.session.userId });
});

// Route to log in a user and create a session
app.post('/login', (req, res) => {
    // Simulated user authentication
    const { username } = req.body;
    
    // In a real application, you would verify user credentials from a database
    if (username) {
        // Create a session for the user
        req.session.userId = username; // Using username for demonstration
        return res.status(200).json({ message: 'User logged in successfully!' });
    } else {
        // Invalid login attempt; send an error response
        return res.status(400).json({ error: 'Invalid username provided.' });
    }
});

// Route to log out a user and destroy the session
app.post('/logout', (req, res) => {
    req.session.destroy(err => {
        if (err) {
            return res.status(500).json({ error: 'Failed to log out.' });
        }
        // Successfully logged out
        res.status(200).json({ message: 'User logged out successfully!' });
    });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace
    res.status(500).json({ error: 'An unexpected error occurred.' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
