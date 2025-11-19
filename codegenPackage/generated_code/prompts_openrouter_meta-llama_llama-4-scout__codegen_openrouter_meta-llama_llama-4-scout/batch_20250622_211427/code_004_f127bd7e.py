"""
Generated Code Metadata:
========================
Original URL: https://destiro.com
Prompt: Create a simple Node.js server that mimics the directory listing functionality of an Apache server, similar to the one at destiro.com.
Generated: DETERMINISTIC_f127bd7e2bf61179
Batch ID: 20250622_211427
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
const ROOT_DIR = './public';

// Create server
const server = http.createServer((req, res) => {
  // Parse URL
  const parsedUrl = url.parse(req.url, true);

  // Get requested file path
  let filePath = path.join(ROOT_DIR, parsedUrl.pathname);

  // Check if file exists
  fs.stat(filePath, (err, stats) => {
    if (err) {
      // File does not exist, check if it's a directory
      if (err.code === 'ENOENT') {
        // If it's a directory, list files
        listDirectory(filePath, req, res);
      } else {
        // Handle other errors
        handleError(err, req, res);
      }
    } else if (stats.isDirectory()) {
      // If it's a directory, list files
      listDirectory(filePath, req, res);
    } else {
      // If it's a file, serve it
      serveFile(filePath, req, res);
    }
  });
});

// Function to list directory contents
function listDirectory(dirPath, req, res) {
  fs.readdir(dirPath, (err, files) => {
    if (err) {
      handleError(err, req, res);
    } else {
      // Create HTML directory listing
      let html = `
        <html>
          <head>
            <title>Directory Listing</title>
          </head>
          <body>
            <h1>Directory Listing for ${dirPath}</h1>
            <ul>
              ${files.map(file => `<li><a href="${path.relative(ROOT_DIR, dirPath)}/${file}">${file}</a></li>`).join('')}
            </ul>
          </body>
        </html>
      `;

      // Send HTML response
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(html);
    }
  });
}

// Function to serve a file
function serveFile(filePath, req, res) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      handleError(err, req, res);
    } else {
      // Get MIME type
      let mimeType = getMimeType(path.extname(filePath));

      // Send file response
      res.writeHead(200, {'Content-Type': mimeType});
      res.end(data);
    }
  });
}

// Function to handle errors
function handleError(err, req, res) {
  console.error(err);
  res.writeHead(500, {'Content-Type': 'text/plain'});
  res.end('Internal Server Error');
}

// Function to get MIME type
function getMimeType(ext) {
  switch (ext) {
    case '.html':
      return 'text/html';
    case '.css':
      return 'text/css';
    case '.js':
      return 'application/javascript';
    default:
      return 'application/octet-stream';
  }
}

// Start server
server.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
```
