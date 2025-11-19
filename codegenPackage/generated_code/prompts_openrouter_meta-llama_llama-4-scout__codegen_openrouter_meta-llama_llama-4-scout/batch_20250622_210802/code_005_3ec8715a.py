"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a code example that demonstrates how to use cookies for analytics purposes while respecting user consent preferences, as discussed in the context of the Masa application.
Generated: DETERMINISTIC_3ec8715a6068d497
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// analytics.js

/**
 * Analytics cookie management module.
 * 
 * This module provides functionality to set and get analytics cookies
 * while respecting user consent preferences.
 */

// Import required modules
const express = require('express');
const cookieParser = require('cookie-parser');

// Initialize express app and cookie parser
const app = express();
app.use(cookieParser());

// Define constants for cookie names and expiration time
const COOKIE_NAME = 'analytics_consent';
const EXPIRATION_TIME = 30 * 24 * 60 * 60 * 1000; // 30 days

/**
 * Set analytics cookie if user has given consent.
 * 
 * @param {object} req - Express request object.
 * @param {object} res - Express response object.
 * @param {boolean} consent - User consent status.
 */
function setAnalyticsCookie(req, res, consent) {
    // Check if user has given consent
    if (consent) {
        // Set cookie with expiration time
        res.cookie(COOKIE_NAME, 'true', {
            maxAge: EXPIRATION_TIME,
            httpOnly: true,
            secure: true,
            sameSite: 'strict'
        });
    } else {
        // Clear cookie if user has withdrawn consent
        res.clearCookie(COOKIE_NAME);
    }
}

/**
 * Get user consent status from cookie.
 * 
 * @param {object} req - Express request object.
 * @returns {boolean} User consent status.
 */
function getUserConsent(req) {
    // Check if cookie exists and has value 'true'
    const cookieValue = req.cookies[COOKIE_NAME];
    return cookieValue === 'true';
}

// Example usage
app.get('/set-consent', (req, res) => {
    try {
        const consent = req.query.consent === 'true';
        setAnalyticsCookie(req, res, consent);
        res.send(`Consent set to ${consent}`);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error setting consent');
    }
});

app.get('/get-consent', (req, res) => {
    try {
        const consent = getUserConsent(req);
        res.send(`Consent status: ${consent}`);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error getting consent');
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
