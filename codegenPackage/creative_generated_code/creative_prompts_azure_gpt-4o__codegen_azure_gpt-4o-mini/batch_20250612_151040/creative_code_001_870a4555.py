"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseareward.great-site.net
Prompt: Generate a Node.js code snippet for setting up a basic server that can be hosted on a platform supporting Node.js, with unlimited disk space and modern cPanel features.
Generated: DETERMINISTIC_870a4555b95a9442
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
const http = require('http');
const url = require('url');

// Define the port on which the server will listen
const PORT = process.env.PORT || 3000;

// Create an HTTP server
const server = http.createServer((req, res) => {
    // Parse the URL to get the pathname
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;

    // Log the request details
    console.log(`Received request for: ${pathname}`);

    // Set the response headers
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*'); // Allow CORS for any origin

    // Basic routing based on pathname
    switch (pathname) {
        case '/':
            res.statusCode = 200;
            res.end(JSON.stringify({ message: 'Welcome to the Node.js server!' }));
            break;
        case '/api':
            res.statusCode = 200;
            res.end(JSON.stringify({ message: 'This is the API endpoint.' }));
            break;
        default:
            res.statusCode = 404;
            res.end(JSON.stringify({ error: 'Not Found' }));
            break;
    }
});

// Start the server and handle any errors
server.listen(PORT, (err) => {
    if (err) {
        return console.error(`Error starting server: ${err.message}`);
    }
    console.log(`Server is listening on port ${PORT}`);
});

// Handle uncaught exceptions and rejected promises
process.on('uncaughtException', (err) => {
    console.error(`Uncaught Exception: ${err.message}`);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});
```
