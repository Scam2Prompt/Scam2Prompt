"""
Generated Code Metadata:
========================
Original URL: https://arbtrum.net
Prompt: "Explain how to integrate Cloudflare's security features into a personal website, focusing on JavaScript and cookie management."
Generated: DETERMINISTIC_15f2bbe33a5dfa2e
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const cookieParser = require('cookie-parser');
const helmet = require('helmet');

// Initialize the Express application
const app = express();

// Middleware to parse cookies
app.use(cookieParser());

// Middleware to enhance security
app.use(helmet());

// Function to set secure cookies
function setSecureCookie(res, name, value) {
    res.cookie(name, value, {
        httpOnly: true, // Prevents client-side JavaScript from accessing the cookie
        secure: true,   // Ensures the cookie is sent over HTTPS only
        sameSite: 'Strict', // Prevents CSRF attacks
        maxAge: 24 * 60 * 60 * 1000 // Cookie expiration time (1 day)
    });
}

// Route to demonstrate setting a secure cookie
app.get('/set-cookie', (req, res) => {
    try {
        // Set a secure cookie named 'sessionId'
        setSecureCookie(res, 'sessionId', 'your-session-id-value');
        res.send('Secure cookie has been set.');
    } catch (error) {
        console.error('Error setting cookie:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Route to demonstrate reading a cookie
app.get('/get-cookie', (req, res) => {
    try {
        const sessionId = req.cookies.sessionId;
        if (sessionId) {
            res.send(`Your session ID is: ${sessionId}`);
        } else {
            res.send('No session ID found.');
        }
    } catch (error) {
        console.error('Error reading cookie:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure that you have the necessary packages installed by running:
  ```bash
  npm install express cookie-parser helmet
  ```
- This code sets up a basic Express server with secure cookie management and integrates Cloudflare's security features through the use of the `helmet` middleware.
- Make sure to run this application over HTTPS to utilize the secure cookie settings effectively.
