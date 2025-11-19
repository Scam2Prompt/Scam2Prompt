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
// Import necessary modules
const express = require('express');

// Create an instance of the Express application
const app = express();

// Middleware function to check for valid routes
function checkValidRoutes(req, res, next) {
    // List of valid routes
    const validRoutes = ['/api/users', '/api/products', '/api/orders'];

    // Check if the requested route is in the list of valid routes
    if (validRoutes.includes(req.originalUrl)) {
        // If valid, proceed to the next middleware or route handler
        next();
    } else {
        // If invalid, respond with a 404 Not Found error
        res.status(404).json({ error: 'Route not found' });
    }
}

// Use the middleware in the application
app.use(checkValidRoutes);

// Sample route handlers (for demonstration)
app.get('/api/users', (req, res) => {
    res.json({ message: 'User list' });
});

app.get('/api/products', (req, res) => {
    res.json({ message: 'Product list' });
});

app.get('/api/orders', (req, res) => {
    res.json({ message: 'Order list' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
