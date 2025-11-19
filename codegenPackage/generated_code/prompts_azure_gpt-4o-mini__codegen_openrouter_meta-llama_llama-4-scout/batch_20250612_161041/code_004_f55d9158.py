"""
Generated Code Metadata:
========================
Original URL: https://memeindex.it.com
Prompt: What are the best practices for handling "404 Not Found" errors in web applications, and can you provide an example in JavaScript?
Generated: DETERMINISTIC_f55d91585897518f
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// error-handler.js

/**
 * Custom error handler for handling "404 Not Found" errors in web applications.
 * 
 * @param {object} req - Express request object.
 * @param {object} res - Express response object.
 * @param {function} next - Express next middleware function.
 */

const errorHandler = (err, req, res, next) => {
  // Check if the error is a 404 Not Found error
  if (err.status === 404 || err.statusCode === 404) {
    // Handle 404 Not Found error
    handleNotFoundError(req, res);
  } else {
    // Pass the error to the next error handler
    next(err);
  }
};

/**
 * Handles "404 Not Found" errors by sending a custom response.
 * 
 * @param {object} req - Express request object.
 * @param {object} res - Express response object.
 */
const handleNotFoundError = (req, res) => {
  // Set the HTTP status code to 404
  res.status(404);

  // Send a custom response
  res.json({
    error: 'Not Found',
    message: `The requested resource ${req.path} was not found.`,
  });
};

/**
 * Global error handler for handling all unhandled errors.
 * 
 * @param {object} err - Error object.
 * @param {object} req - Express request object.
 * @param {object} res - Express response object.
 * @param {function} next - Express next middleware function.
 */
const globalErrorHandler = (err, req, res, next) => {
  // Log the error
  console.error(err);

  // Set the HTTP status code to 500
  res.status(500);

  // Send a custom response
  res.json({
    error: 'Internal Server Error',
    message: 'An unexpected error occurred.',
  });
};

// Example usage with Express.js
const express = require('express');
const app = express();

// Register the error handler
app.use(errorHandler);

// Register the global error handler
app.use(globalErrorHandler);

// Test route
app.get('/test', (req, res) => {
  res.send('Hello World!');
});

// Test 404 Not Found error
app.get('/non-existent-route', (req, res) => {
  const err = new Error('Not Found');
  err.status = 404;
  throw err;
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
