"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappddrop.pages.dev
Prompt: Provide an example of a middleware that checks for valid routes in a Node.js application.
Generated: DETERMINISTIC_8c73bd24aba32c6d
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary modules
const express = require('express');
const app = express();

// Middleware to check for valid routes
const validRouteChecker = (req, res, next) => {
  // List of valid routes
  const validRoutes = [
    '/',
    '/about',
    '/contact',
    '/api/data',
  ];

  // Check if the requested route exists in the list of valid routes
  if (validRoutes.includes(req.path)) {
    // Proceed to the next middleware or route handler
    next();
  } else {
    // Respond with a 404 Not Found error for invalid routes
    res.status(404).json({ error: 'Route not found', requestedRoute: req.path });
  }
};

// Use the validRouteChecker middleware for all incoming requests
app.use(validRouteChecker);

// Define route handlers
app.get('/', (req, res) => {
  res.send('Welcome to the homepage!');
});

app.get('/about', (req, res) => {
  res.send('About us page');
});

app.get('/contact', (req, res) => {
  res.send('Contact us page');
});

app.get('/api/data', (req, res) => {
  res.json({ message: 'Here is some API data' });
});

// Error handling middleware for any unexpected server errors
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack trace
  res.status(500).json({ error: 'Internal server error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
