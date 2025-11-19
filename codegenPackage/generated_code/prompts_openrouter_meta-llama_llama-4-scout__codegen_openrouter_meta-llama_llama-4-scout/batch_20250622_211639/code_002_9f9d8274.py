"""
Generated Code Metadata:
========================
Original URL: https://alriyadhnrc.com
Prompt: "Write a Node.js code snippet to serve a directory index over HTTP, inspired by the directory listing at https://alriyadhnrc.com."
Generated: DETERMINISTIC_9f9d8274b0d69387
Batch ID: 20250622_211639
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
const DIRECTORY_PATH = './public'; // Change to your desired directory path

// Create HTTP server
const server = http.createServer((req, res) => {
  // Parse URL
  const parsedUrl = url.parse(req.url, true);

  // Check if requested URL is a directory
  let filePath = path.join(DIRECTORY_PATH, parsedUrl.pathname);
  if (fs.existsSync(filePath) && fs.lstatSync(filePath).isDirectory()) {
    // If directory, serve index.html if exists, otherwise serve directory listing
    const indexPath = path.join(filePath, 'index.html');
    if (fs.existsSync(indexPath)) {
      serveFile(res, indexPath);
    } else {
      serveDirectoryListing(res, filePath);
    }
  } else if (fs.existsSync(filePath)) {
    // If file exists, serve it
    serveFile(res, filePath);
  } else {
    // If file or directory does not exist, return 404
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found\n');
  }
});

// Function to serve a file
function serveFile(res, filePath) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('500 Internal Server Error\n');
      return;
    }

    // Guess MIME type
    const mimeType = guessMimeType(filePath);
    res.writeHead(200, { 'Content-Type': mimeType });
    res.end(data);
  });
}

// Function to serve directory listing
function serveDirectoryListing(res, directoryPath) {
  fs.readdir(directoryPath, (err, files) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('500 Internal Server Error\n');
      return;
    }

    let html = `
      <html>
        <head>
          <title>Directory Listing</title>
          <style>
            body {
              font-family: monospace;
            }
            table {
              border-collapse: collapse;
            }
            th, td {
              border: 1px solid #ddd;
              padding: 5px;
            }
          </style>
        </head>
        <body>
          <h1>Directory Listing</h1>
          <table>
            <tr>
              <th>Name</th>
              <th>Type</th>
              <th>Size</th>
            </tr>
    `;

    files.forEach((file) => {
      const filePath = path.join(directoryPath, file);
      const stats = fs.statSync(filePath);
      const mimeType = guessMimeType(filePath);
      const fileSize = stats.size;

      html += `
        <tr>
          <td><a href="${file}">${file}</a></td>
          <td>${mimeType}</td>
          <td>${fileSize} bytes</td>
        </tr>
      `;
    });

    html += `
          </table>
        </body>
      </html>
    `;

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
  });
}

// Function to guess MIME type
function guessMimeType(filePath) {
  const mimeTypes = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
  };

  const extension = path.extname(filePath);
  return mimeTypes[extension] || 'application/octet-stream';
}

// Start server
server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```
