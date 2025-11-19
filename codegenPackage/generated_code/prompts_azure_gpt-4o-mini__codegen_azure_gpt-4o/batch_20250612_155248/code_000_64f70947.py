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
// Import the required modules
const express = require('express');
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Define a sample route
app.get('/', (req, res) => {
  res.send('Welcome to the homepage!');
});

// Catch-all middleware to handle 404 errors
app.use((req, res, next) => {
  // Create a custom error object for 404
  const error = new Error('Resource not found');
  error.status = 404;
  next(error); // Pass the error to the error-handling middleware
});

// Error-handling middleware
app.use((err, req, res, next) => {
  // Set the status code to the error's status or default to 500
  const statusCode = err.status || 500;

  // Log the error for debugging purposes (optional in production)
  console.error(`[Error] ${statusCode}: ${err.message}`);

  // Send a JSON response with the error details
  res.status(statusCode).json({
    error: {
      message: err.message || 'Internal Server Error',
      status: statusCode,
    },
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
