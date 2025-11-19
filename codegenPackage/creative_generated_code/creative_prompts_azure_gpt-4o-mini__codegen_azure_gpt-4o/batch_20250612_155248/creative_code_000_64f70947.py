"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choruc.one
Prompt: Generate a code snippet that handles 404 errors in a web application using JavaScript.
Generated: DETERMINISTIC_64f709475a9622d3
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules (using Express.js for the web application framework)
const express = require('express');
const app = express();

// Middleware to parse incoming JSON requests (good practice for modern APIs)
app.use(express.json());

// Define a simple route for demonstration purposes
app.get('/', (req, res) => {
  res.send('Welcome to the homepage!');
});

// Catch-all route to handle 404 errors (when no matching route is found)
app.use((req, res, next) => {
  // Send a 404 error response with a descriptive message
  res.status(404).json({
    error: 'Resource not found',
    message: 'The requested URL was not found on this server.',
  });
});

// General error-handling middleware (to catch other application errors)
app.use((err, req, res, next) => {
  // Log the error for debugging (avoid exposing stack traces in production)
  console.error(err.stack);

  // Send a user-friendly error response while masking internal details
  res.status(500).json({
    error: 'Internal Server Error',
    message: 'Something went wrong on the server. Please try again later.',
  });
});

// Start the server on port 3000 (or any desired port)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
