"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-bonkboxes.web.app
Prompt: What are the steps to create a whitelist for user access in a web app using JavaScript?
Generated: DETERMINISTIC_bc5af5f1c3deef26
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * User Access Whitelist Implementation for a Web App
 * 
 * This code demonstrates how to create and enforce a whitelist for user access
 * to a web application using JavaScript. It includes error handling and follows
 * best practices for clean, efficient, and maintainable code.
 */

/**
 * Whitelist of authorized users
 * Replace with actual user data (e.g., database queries or API calls).
 */
const userWhitelist = [
  'user1@example.com',
  'user2@example.com',
  'admin@example.com',
];

/**
 * Function to check if a user is whitelisted
 * @param {string} email - The email of the user to be checked.
 * @returns {boolean} - Returns true if the user is whitelisted, otherwise false.
 */
function isUserWhitelisted(email) {
  // Return true if the email exists in the whitelist, false otherwise
  return userWhitelist.includes(email);
}

/**
 * Middleware function to enforce whitelist access
 * For use in a Node.js/Express web application.
 * @param {Object} req - The HTTP request object.
 * @param {Object} res - The HTTP response object.
 * @param {Function} next - The next middleware function.
 */
function whitelistMiddleware(req, res, next) {
  try {
    // Extract user email from the request (e.g., from headers or body)
    const userEmail = req.headers['user-email'];

    // Validate email presence
    if (!userEmail) {
      return res.status(400).json({ error: 'User email is required.' });
    }

    // Check if the user is whitelisted
    if (!isUserWhitelisted(userEmail)) {
      return res.status(403).json({ error: 'Access denied. User is not whitelisted.' });
    }

    // If whitelisted, proceed to the next middleware or route handler
    next();
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error('Error in whitelist middleware:', error);
    return res.status(500).json({ error: 'An internal server error occurred.' });
  }
}

// Example usage in a Node.js/Express application
const express = require('express');
const app = express();

// Middleware to parse JSON in the request body (if needed)
app.use(express.json());

// Apply the whitelist middleware
app.use(whitelistMiddleware);

// Sample route
app.get('/protected-resource', (req, res) => {
  res.json({ message: 'Welcome to the protected resource!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
