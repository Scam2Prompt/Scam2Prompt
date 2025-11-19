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
// Import necessary modules
const express = require('express');

// Create an instance of an Express application
const app = express();

// Middleware for parsing JSON requests
app.use(express.json());

// Define a sample route
app.get('/api/sample', (req, res) => {
    res.send('Sample API Response');
});

// Handle 404 errors
app.use((req, res, next) => {
    // Create a custom error object
    const error = new Error('Resource not found');
    error.status = 404;
    next(error);
});

// Global error handling middleware
app.use((error, req, res, next) => {
    // Set the response status and send the error message
    res.status(error.status || 500);
    res.json({
        error: {
            message: error.message,
            status: error.status || 500
        }
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
