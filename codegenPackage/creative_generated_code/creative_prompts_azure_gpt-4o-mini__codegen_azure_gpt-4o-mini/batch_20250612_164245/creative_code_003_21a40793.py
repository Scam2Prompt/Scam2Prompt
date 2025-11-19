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
// Import the required modules
const express = require('express');

// Create an instance of an Express application
const app = express();

// Middleware to check for secure connections (HTTPS)
const secureConnectionMiddleware = (req, res, next) => {
    // Check if the request is secure
    if (req.secure || req.headers['x-forwarded-proto'] === 'https') {
        // If secure, proceed to the next middleware or route handler
        next();
    } else {
        // If not secure, respond with a 403 Forbidden status
        res.status(403).send('Secure connection required.');
    }
};

// Use the middleware in the application
app.use(secureConnectionMiddleware);

// Example route to demonstrate the middleware in action
app.get('/', (req, res) => {
    res.send('Hello, you are connected securely!');
});

// Error handling middleware for catching unexpected errors
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack for debugging
    res.status(500).send('Something went wrong!'); // Respond with a 500 status
});

// Start the server on a specific port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
