"""
Generated Code Metadata:
========================
Original URL: https://7473441704.pages.dev
Prompt: How do cookies affect web applications, and what libraries can help manage them in JavaScript?
Generated: DETERMINISTIC_c9cc54d0e0a66d44
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const cookieParser = require('cookie-parser');

// Create an Express application
const app = express();

// Use the cookie-parser middleware to parse cookies
app.use(cookieParser());

// Set a cookie
app.get('/set-cookie', (req, res) => {
    // Set a cookie with a specific name, value, and options
    res.cookie('username', 'johnDoe', {
        maxAge: 900000, // expires in 15 minutes
        httpOnly: true, // prevent client-side access
        secure: true, // only transmit over HTTPS
        sameSite: 'strict' // restrict to same-site requests
    });
    res.send('Cookie set!');
});

// Get a cookie
app.get('/get-cookie', (req, res) => {
    try {
        // Retrieve the cookie value
        const cookieValue = req.cookies.username;
        if (!cookieValue) {
            throw new Error('Cookie not found');
        }
        res.send(`Cookie value: ${cookieValue}`);
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).send('Error retrieving cookie');
    }
});

// Delete a cookie
app.get('/delete-cookie', (req, res) => {
    try {
        // Clear the cookie
        res.clearCookie('username', {
            httpOnly: true,
            secure: true,
            sameSite: 'strict'
        });
        res.send('Cookie deleted!');
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).send('Error deleting cookie');
    }
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
