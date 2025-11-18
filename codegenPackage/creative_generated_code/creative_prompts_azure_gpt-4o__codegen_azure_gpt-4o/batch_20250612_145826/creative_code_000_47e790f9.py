"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.top
Prompt: Write code to detect and handle session expiration in a web application, ensuring users are prompted to request a new session.
Generated: DETERMINISTIC_47e790f9b4222ebb
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// server.js
// Node.js server-side code for session expiration detection and handling

const express = require('express');
const session = require('express-session');

const app = express();

// Middleware for parsing JSON
app.use(express.json());

// Configure session middleware
app.use(
  session({
    secret: 'your-secret-key', // Keep this secret in a production app
    resave: false,
    saveUninitialized: true,
    cookie: {
      maxAge: 15 * 60 * 1000, // Session expires after 15 minutes
    },
  })
);

// Middleware to check session expiration
function checkSessionExpiration(req, res, next) {
  if (!req.session || !req.session.user) {
    return res.status(401).json({
      message: 'Session expired. Please request a new session.',
    });
  }
  next();
}

// Example route that requires an active session
app.get('/protected', checkSessionExpiration, (req, res) => {
  res.status(200).json({
    message: 'Welcome to the protected resource!',
    user: req.session.user,
  });
});

// Route to create a new session/login
app.post('/login', (req, res) => {
  const { username } = req.body;

  // Basic validation
  if (!username) {
    return res.status(400).json({
      message: 'Username is required to login.',
    });
  }

  // Create session and store user info
  req.session.user = { username };
  res.status(200).json({
    message: 'Session created successfully!',
    user: req.session.user,
  });
});

// Route to end a session/logout
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({
        message: 'Error while ending the session.',
      });
    }
    res.status(200).json({
      message: 'Session ended successfully.',
    });
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
