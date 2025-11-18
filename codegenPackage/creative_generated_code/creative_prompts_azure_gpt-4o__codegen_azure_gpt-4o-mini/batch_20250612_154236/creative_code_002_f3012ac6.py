"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubfix.rf.gd
Prompt: Generate a Node.js server configuration script optimized for deployment on a hosting platform that supports Node.js and provides unlimited bandwidth, as described on iFastNet.
Generated: DETERMINISTIC_f3012ac696c13174
Batch ID: 20250612_154236
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const http = require('http');
const path = require('path');
const morgan = require('morgan');
const bodyParser = require('body-parser');

// Create an instance of the express application
const app = express();

// Configure Express to use body-parser for JSON and URL-encoded form bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Set up logging with morgan
app.use(morgan('combined'));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a simple route for the home page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Handle 404 errors
app.use((req, res, next) => {
    res.status(404).send('404 Not Found');
});

// Global error handler middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('500 Internal Server Error');
});

// Create an HTTP server and listen on the specified port
const PORT = process.env.PORT || 3000; // Allow for dynamic port assignment
const server = http.createServer(app);

server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Handle process termination signals for graceful shutdown
process.on('SIGINT', () => {
    console.log('Gracefully shutting down from SIGINT (Ctrl+C)');
    server.close(() => {
        console.log('Server closed.');
        process.exit(0);
    });
});

process.on('SIGTERM', () => {
    console.log('Gracefully shutting down from SIGTERM');
    server.close(() => {
        console.log('Server closed.');
        process.exit(0);
    });
});
```
