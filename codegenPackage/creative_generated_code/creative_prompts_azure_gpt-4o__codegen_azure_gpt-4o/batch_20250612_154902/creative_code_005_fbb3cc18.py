"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: Suggest best practices for implementing "Keep me signed in" functionality in a web application like CCBase.net.
Generated: DETERMINISTIC_fbb3cc184626be01
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: auth.js

/**
 * Implements "Keep me signed in" functionality in a web application.
 *
 * Best practices include:
 * - Using secure, HTTP-only cookies.
 * - Encrypting the data stored in the cookies.
 * - Setting a reasonable expiration time for the cookie.
 * - Refreshing tokens periodically for improved security.
 * - Allowing users to log out and invalidate the token manually.
 */

// Import necessary modules
const crypto = require('crypto');
const jwt = require('jsonwebtoken');

// Configuration (Use environment variables for sensitive data)
const SECRET_KEY = process.env.JWT_SECRET_KEY || 'your-secure-key-here'; // NEVER expose sensitive keys in code
const COOKIE_NAME = 'auth_token';
const COOKIE_OPTIONS = {
  httpOnly: true, // Prevent access from client-side JavaScript
  secure: true, // Ensure cookies are sent via HTTPS only
  sameSite: 'Strict', // Prevent CSRF attacks
  maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days in milliseconds
};

// Function to generate a signed token
function generateAuthToken(userId) {
  const payload = { userId }; // Store only essential data
  const options = {
    expiresIn: '7d', // Token will expire in 7 days
  };
  return jwt.sign(payload, SECRET_KEY, options);
}

// Middleware to handle authentication
function authenticateUser(req, res, next) {
  try {
    const token = req.cookies[COOKIE_NAME];

    if (!token) {
      // If no cookie is found, the user is not authenticated
      res.status(401).json({ error: 'Authentication required' });
      return;
    }

    // Verify the token
    const decoded = jwt.verify(token, SECRET_KEY);
    req.userId = decoded.userId; // Attach userId to request object
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid or expired token' });
  }
}

// Function to set the authentication cookie
function setAuthCookie(res, userId) {
  const token = generateAuthToken(userId);
  res.cookie(COOKIE_NAME, token, COOKIE_OPTIONS);
}

// Function to clear the authentication cookie on logout
function clearAuthCookie(res) {
  res.clearCookie(COOKIE_NAME, COOKIE_OPTIONS);
}

// Example usage in an Express application
const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();

app.use(cookieParser());

// Example login route
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Replace with actual user validation logic
  if (username === 'testuser' && password === 'securepassword') {
    const userId = '12345'; // Replace with actual user ID
    setAuthCookie(res, userId);
    res.json({ message: 'Login successful', userId });
  } else {
    res.status(401).json({ error: 'Invalid username or password' });
  }
});

// Example protected route
app.get('/dashboard', authenticateUser, (req, res) => {
  res.json({ message: 'Welcome to your dashboard', userId: req.userId });
});

// Example logout route
app.post('/logout', (req, res) => {
  clearAuthCookie(res);
  res.json({ message: 'Logout successful' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

/**
 * Notes:
 * - Always use HTTPS in production.
 * - Store sensitive credentials like SECRET_KEY in environment variables.
 * - Regularly rotate keys and invalidate old tokens for enhanced security.
 * - Apply rate limiting and CAPTCHA in login endpoints to prevent brute-force attacks.
 */
```
