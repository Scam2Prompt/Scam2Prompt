"""
Generated Code Metadata:
========================
Original URL: https://choruc.one
Prompt: Generate a code snippet that handles 404 errors in a web application using JavaScript.
Generated: DETERMINISTIC_64f709475a9622d3
Batch ID: 20250612_155248
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
 * Custom 404 error handler for web applications.
 * 
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Express next middleware function.
 */
const handle404Error = (req, res, next) => {
  // Log the 404 error for debugging purposes
  console.error(`404 error: ${req.method} ${req.url}`);

  // Render a custom 404 error page
  res.status(404).render('404', {
    title: 'Page Not Found',
    message: 'The page you are looking for does not exist.',
  });
};

/**
 * Global error handler for unhandled errors.
 * 
 * @param {Error} err - Error object.
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Express next middleware function.
 */
const globalErrorHandler = (err, req, res, next) => {
  // Log the error for debugging purposes
  console.error(`Error: ${err.message}`);

  // Check if the error is a 404 error
  if (err.status === 404) {
    return handle404Error(req, res, next);
  }

  // Render a custom error page for server errors
  res.status(500).render('error', {
    title: 'Internal Server Error',
    message: 'An unexpected error occurred.',
  });
};

// Export the error handlers
module.exports = {
  handle404Error,
  globalErrorHandler,
};
```

```javascript
// app.js
const express = require('express');
const { handle404Error, globalErrorHandler } = require('./error-handler');

const app = express();

// Set up routes
app.get('/', (req, res) => {
  res.render('index');
});

// Handle 404 errors
app.use(handle404Error);

// Global error handler
app.use(globalErrorHandler);

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
