"""
Generated Code Metadata:
========================
Original URL: https://eth-today.rf.gd
Prompt: Generate Node.js code for setting up a server on a hosting platform that offers unlimited disk space and a modern cPanel, as mentioned on iFastNet's hosting services.
Generated: DETERMINISTIC_9e06e1e648d15e9a
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const http = require('http');
const path = require('path');

// Create an Express application
const app = express();

// Define the port
const port = process.env.PORT || 3000;

// Set up middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Set up a route for the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Catch-all route for handling 404 errors
app.use((req, res, next) => {
    res.status(404).send('Page not found');
});

// Error-handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Internal Server Error');
});

// Create an HTTP server
const server = http.createServer(app);

// Listen on the specified port
server.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

// Handle server errors
server.on('error', (err) => {
    console.error('Server error:', err);
});

// Handle server close event
server.on('close', () => {
    console.log('Server closed');
});

// Graceful shutdown
process.on('SIGINT', () => {
    server.close(() => {
        console.log('Server closed due to SIGINT');
        process.exit(0);
    });
});

process.on('SIGTERM', () => {
    server.close(() => {
        console.log('Server closed due to SIGTERM');
        process.exit(0);
    });
});
```
