"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: How can I implement a simple web server that serves an index of files from a directory in Node.js?
Generated: DETERMINISTIC_3c51fa6ef89048f9
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

// Define constants
const PORT = 3000;
const DIRECTORY = './public';

/**
 * Serves an index of files from a directory.
 * @param {http.IncomingMessage} req - The HTTP request.
 * @param {http.ServerResponse} res - The HTTP response.
 */
function serveIndex(req, res) {
    // Check if the request is for the root URL
    if (req.url === '/') {
        // Read the directory contents
        fs.readdir(DIRECTORY, (err, files) => {
            if (err) {
                // Handle directory read error
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end(`Error reading directory: ${err.message}`);
            } else {
                // Create an HTML index of files
                let html = '<html><body><h1>Index of files:</h1><ul>';
                files.forEach((file) => {
                    html += `<li><a href="${file}">${file}</a></li>`;
                });
                html += '</ul></body></html>';

                // Send the HTML index
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(html);
            }
        });
    } else {
        // Serve files from the directory
        const filePath = path.join(DIRECTORY, req.url);
        fs.stat(filePath, (err, stats) => {
            if (err) {
                // Handle file stat error
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end(`File not found: ${req.url}`);
            } else if (stats.isFile()) {
                // Serve the file
                fs.readFile(filePath, (err, data) => {
                    if (err) {
                        // Handle file read error
                        res.writeHead(500, { 'Content-Type': 'text/plain' });
                        res.end(`Error reading file: ${err.message}`);
                    } else {
                        // Determine the MIME type
                        const mimeType = getMimeType(path.extname(filePath));
                        res.writeHead(200, { 'Content-Type': mimeType });
                        res.end(data);
                    }
                });
            } else {
                // Handle directory requests
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end(`Directory listing not supported: ${req.url}`);
            }
        });
    }
}

/**
 * Gets the MIME type for a file extension.
 * @param {string} extension - The file extension.
 * @returns {string} The MIME type.
 */
function getMimeType(extension) {
    switch (extension) {
        case '.html':
            return 'text/html';
        case '.css':
            return 'text/css';
        case '.js':
            return 'text/javascript';
        case '.png':
            return 'image/png';
        case '.jpg':
            return 'image/jpeg';
        case '.gif':
            return 'image/gif';
        default:
            return 'application/octet-stream';
    }
}

// Create the HTTP server
const server = http.createServer((req, res) => {
    serveIndex(req, res);
});

// Start the server
server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});

// Handle server errors
server.on('error', (err) => {
    console.error(`Server error: ${err.message}`);
    process.exit(1);
});
```
