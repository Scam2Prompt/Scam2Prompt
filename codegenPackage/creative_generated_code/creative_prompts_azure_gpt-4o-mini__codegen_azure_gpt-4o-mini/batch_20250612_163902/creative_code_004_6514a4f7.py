"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collab.top
Prompt: What libraries can assist with session management in Node.js applications?
Generated: DETERMINISTIC_6514a4f74af9e688
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express'); // Web framework
const session = require('express-session'); // Session management middleware
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Create an Express application
const app = express();

// Middleware setup
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded bodies
app.use(bodyParser.json()); // Parse JSON bodies

// Session configuration
app.use(session({
    secret: 'your_secret_key', // Secret key for signing the session ID cookie
    resave: false, // Forces session to be saved back to the session store
    saveUninitialized: true, // Forces a session that is uninitialized to be saved to the store
    cookie: {
        maxAge: 1000 * 60 * 60 * 24 // Set the cookie to expire in 1 day
    }
}));

// Route to set a session variable
app.post('/login', (req, res) => {
    const { username } = req.body;
    
    // Basic error handling for missing username
    if (!username) {
        return res.status(400).json({ error: 'Username is required' });
    }

    // Set session variable
    req.session.username = username;
    res.status(200).json({ message: `User ${username} logged in successfully` });
});

// Route to get session information
app.get('/session', (req, res) => {
    // Check if session exists
    if (req.session.username) {
        res.status(200).json({ username: req.session.username });
    } else {
        res.status(404).json({ error: 'No active session' });
    }
});

// Route to log out and destroy the session
app.post('/logout', (req, res) => {
    // Destroy the session
    req.session.destroy(err => {
        if (err) {
            return res.status(500).json({ error: 'Failed to log out' });
        }
        res.status(200).json({ message: 'Logged out successfully' });
    });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error for debugging
    res.status(500).send('Something broke!'); // Send a generic error response
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
