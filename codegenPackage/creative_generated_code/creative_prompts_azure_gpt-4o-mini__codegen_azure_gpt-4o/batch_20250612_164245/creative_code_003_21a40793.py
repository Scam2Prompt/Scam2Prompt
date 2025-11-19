"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://b40d9440.90257743f86d9260ea5a8bbd.workers.dev
Prompt: How do I set up a middleware in Node.js to check for secure connections before processing requests?
Generated: DETERMINISTIC_21a4079326358efb
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const app = express();

// Middleware to check for secure connections (HTTPS)
const checkSecureConnection = (req, res, next) => {
  // Check if the request is secure (HTTPS)
  if (req.secure || req.headers['x-forwarded-proto'] === 'https') {
    // If secure, proceed to the next middleware or route handler
    next();
  } else {
    // If not secure, reject the request and respond with 400 Bad Request
    res.status(400).json({
      error: 'Secure connection required. Please use HTTPS.'
    });
  }
};

// Use the middleware globally for all incoming requests
app.use(checkSecureConnection);

// Example route for testing purposes
app.get('/', (req, res) => {
  res.send('Secure connection verified. Welcome!');
});

// Error handling middleware for unhandled errors
app.use((err, req, res, next) => {
  console.error('Internal Server Error:', err.message);
  res.status(500).json({
    error: 'Internal Server Error. Please try again later.'
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Note: To test this middleware, ensure your server is configured to handle HTTPS,
// or use a reverse proxy (e.g., Nginx) to forward requests with 'x-forwarded-proto' headers.
```
