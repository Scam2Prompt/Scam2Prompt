"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cow-swap-dao.org
Prompt: What libraries or APIs can I use to enhance security features like cookie management and JavaScript checks for my web application?
Generated: DETERMINISTIC_1602e299dc4b8389
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready code snippet demonstrating enhanced security features for cookie management and JavaScript checks in a web application using Node.js and Express.js, incorporating secure libraries:

```javascript
// Import required libraries
const express = require('express');
const cookieParser = require('cookie-parser');
const helmet = require('helmet'); // For securing HTTP headers
const csrf = require('csurf'); // CSRF protection middleware

// Initialize the app
const app = express();

// Middleware for parsing cookies
app.use(cookieParser());

// Helmet for secure HTTP headers (e.g., XSS protection, content security policies, etc.)
app.use(helmet({
  contentSecurityPolicy: {
    useDefaults: true,
    directives: {
      "default-src": ["'self'"],
      "script-src": ["'self'", "'unsafe-inline'"],
      "style-src": ["'self'", "'unsafe-inline'"],
    },
  },
  crossOriginEmbedderPolicy: true,
}));

// CSRF protection using CSRF tokens
const csrfProtection = csrf({ cookie: true });

// Secure cookie settings
const cookieOptions = {
  httpOnly: true, // Prevent JavaScript access to cookies
  secure: true, // Require HTTPS for cookie transmission
  sameSite: 'strict', // Prevent cross-site request forgery
};

// Route for setting a secure cookie
app.get('/set-cookie', (req, res) => {
  try {
    // Set a secure cookie
    res.cookie('session', 'secure-value', cookieOptions);
    res.send('Secure cookie has been set.');
  } catch (error) {
    console.error('Error setting cookie:', error);
    res.status(500).send('Failed to set cookie.');
  }
});

// Route protected by CSRF middleware
app.post('/process-data', csrfProtection, (req, res) => {
  try {
    // Simulate processing data securely
    res.send('Data has been processed securely.');
  } catch (error) {
    console.error('Error processing data:', error);
    res.status(500).send('Failed to process data.');
  }
});

// Middleware for checking whether JavaScript is enabled via a custom header
app.get('/javascript-check', (req, res) => {
  try {
    const jsEnabled = req.headers['x-js-enabled'] === 'true'; // Custom client-side header
    if (jsEnabled) {
      res.send('JavaScript is enabled.');
    } else {
      res.status(400).send('JavaScript is disabled.');
    }
  } catch (error) {
    console.error('Error checking JavaScript:', error);
    res.status(500).send('Failed to check JavaScript status.');
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- This code uses `helmet` for securing HTTP headers, `csrf` for CSRF protection, and sets cookies with secure options.
- The `/javascript-check` route demonstrates how to verify if JavaScript is enabled on the client-side using a custom header (`x-js-enabled`), which must be set by the client.
- Error handling is implemented for robustness in production environments.
