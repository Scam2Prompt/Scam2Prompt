"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choruc.one
Prompt: Create a sample code for a middleware in Node.js that captures 404 errors and serves a user-friendly message.
Generated: DETERMINISTIC_a1f279ad9b42b71e
Batch ID: 20250612_155248
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
const express = require('express');

// Create an Express application
const app = express();

/**
 * Middleware to handle routes that are not found (404 errors)
 * This middleware should be placed after all route handlers
 */
app.use((req, res, next) => {
  // Create a user-friendly message for the 404 error
  const errorMessage = {
    status: 404,
    message: 'The resource you are looking for could not be found.',
  };

  // Respond with the error message in JSON format
  res.status(404).json(errorMessage);
});

/**
 * General error-handling middleware
 * This middleware handles any other errors that may occur in the application
 */
app.use((err, req, res, next) => {
  // Log the error for debugging purposes
  console.error(err.stack);

  // Respond with a user-friendly error message and status code
  res.status(err.status || 500).json({
    status: err.status || 500,
    message: err.message || 'An unexpected error occurred. Please try again later.',
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
