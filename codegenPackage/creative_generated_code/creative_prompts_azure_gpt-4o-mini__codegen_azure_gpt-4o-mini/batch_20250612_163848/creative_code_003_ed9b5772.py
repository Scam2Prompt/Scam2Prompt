"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4de192bb.d6c1924f22b82c8daa243716.workers.dev
Prompt: How do I set up a middleware to check the security of connections in a Node.js application?
Generated: DETERMINISTIC_ed9b5772efcd3523
Batch ID: 20250612_163848
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
const helmet = require('helmet'); // Middleware for setting security HTTP headers
const rateLimit = require('express-rate-limit'); // Middleware for rate limiting

// Create an instance of an Express application
const app = express();

// Use Helmet for setting various HTTP headers for security
app.use(helmet());

// Set up rate limiting to prevent DDoS attacks
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // Limit each IP to 100 requests per windowMs
    message: 'Too many requests from this IP, please try again later.'
});

// Apply the rate limiting middleware to all requests
app.use(limiter);

// Middleware to check for secure connections
const securityCheckMiddleware = (req, res, next) => {
    // Check if the connection is secure
    if (req.secure) {
        // If secure, proceed to the next middleware
        next();
    } else {
        // If not secure, send an error response
        return res.status(403).json({ error: 'Connection is not secure. Please use HTTPS.' });
    }
};

// Apply the security check middleware to all routes
app.use(securityCheckMiddleware);

// Sample route
app.get('/', (req, res) => {
    res.send('Hello, secure world!');
});

// Error handling middleware for unexpected errors
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error for debugging
    res.status(500).send('Something went wrong!'); // Send a generic error response
});

// Start the server on the specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
