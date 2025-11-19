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
// Import necessary modules
const express = require('express');

// Create an instance of an Express application
const app = express();

// Middleware to handle 404 errors
app.use((req, res, next) => {
    // If no route matches, respond with a 404 status code
    res.status(404).json({
        error: 'Not Found',
        message: 'The requested resource could not be found.'
    });
});

// Example route for demonstration
app.get('/', (req, res) => {
    res.send('Welcome to the homepage!');
});

// Global error handling middleware
app.use((err, req, res, next) => {
    // Log the error for debugging purposes
    console.error(err.stack);
    
    // Respond with a 500 status code for server errors
    res.status(500).json({
        error: 'Internal Server Error',
        message: 'An unexpected error occurred.'
    });
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
