"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkboxes-live.web.app
Prompt: Write JavaScript code to implement a whitelist system for a web application similar to BONKBOXES, ensuring users can only access the app if they are on the whitelist.
Generated: DETERMINISTIC_111732880d038490
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Whitelist System for a Web Application

// List of whitelisted users (can be email addresses, usernames, etc.)
const whitelist = [
  'user1@example.com',
  'user2@example.com',
  'admin@example.com',
];

// Function to check if a user is on the whitelist
function isWhitelisted(userIdentifier) {
  return whitelist.includes(userIdentifier);
}

// Middleware function for protecting routes (e.g., in an Express.js app)
function whitelistMiddleware(req, res, next) {
  try {
    // Extract user identifier (e.g., email) from the request
    const userIdentifier = req.headers['x-user-identifier'];

    // Ensure the identifier exists
    if (!userIdentifier) {
      return res.status(400).json({
        success: false,
        message: 'User identifier is missing in the request headers.',
      });
    }

    // Check if the user is whitelisted
    if (!isWhitelisted(userIdentifier)) {
      return res.status(403).json({
        success: false,
        message: 'Access denied. You are not on the whitelist.',
      });
    }

    // User is authorized, proceed to the next middleware or route handler
    next();
  } catch (error) {
    // Handle unexpected errors
    console.error('Error during whitelist validation:', error);
    res.status(500).json({
      success: false,
      message: 'An internal server error occurred.',
    });
  }
}

// Example usage in an Express.js app
const express = require('express');
const app = express();

// Apply the whitelist middleware to a protected route
app.get('/protected', whitelistMiddleware, (req, res) => {
  res.json({
    success: true,
    message: 'Welcome to the protected route. You are on the whitelist!',
  });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
