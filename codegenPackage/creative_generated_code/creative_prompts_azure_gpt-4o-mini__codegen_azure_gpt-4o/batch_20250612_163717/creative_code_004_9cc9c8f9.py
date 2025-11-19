"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5f8d9eb3.d10f05e59e81e2f9cfa61b7e.workers.dev
Prompt: How do I integrate performance monitoring with security checks in my web application?
Generated: DETERMINISTIC_9cc9c8f9faeaf11e
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, working code for integrating performance monitoring with security checks in a web application using Node.js with Express.js and middleware:

```javascript
// Import required modules
const express = require('express');
const responseTime = require('response-time'); // Middleware for performance monitoring
const helmet = require('helmet'); // Middleware for security headers
const rateLimit = require('express-rate-limit'); // Middleware for rate limiting
const morgan = require('morgan'); // Middleware for HTTP logging

// Initialize Express app
const app = express();

// Middleware: Security headers using helmet
// Adds headers to secure the app from common vulnerabilities
app.use(helmet());

// Middleware: Rate limiting
// Protects against brute force and denial-of-service attacks
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes window
  max: 100, // Limit each IP to 100 requests per windowMs
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
});
app.use(limiter);

// Middleware: HTTP logging using morgan
// Logs HTTP requests for monitoring and debugging
app.use(morgan('combined'));

// Middleware: Response time monitoring
// Adds X-Response-Time header to track request processing time
app.use(responseTime());

// Middleware: JSON parser
// Handles parsing of incoming JSON payloads
app.use(express.json());

// Route: Sample route with security check and performance monitoring
app.get('/api/data', (req, res) => {
  try {
    // Simulated business logic
    const data = {
      message: 'Performance monitoring and security checks integrated successfully!',
    };

    // Send response
    res.status(200).json(data);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error occurred:', error.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Middleware: 404 handler for unknown routes
app.use((req, res, next) => {
  res.status(404).json({ error: 'Route not found' });
});

// Middleware: Error handling
// Catches any unhandled errors in the request pipeline
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err.message);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Feel free to install the required dependencies using:

```bash
npm install express response-time helmet express-rate-limit morgan
```
