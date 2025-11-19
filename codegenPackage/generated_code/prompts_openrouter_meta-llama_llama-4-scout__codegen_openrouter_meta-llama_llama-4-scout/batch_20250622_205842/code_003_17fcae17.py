"""
Generated Code Metadata:
========================
Original URL: https://magpiexyz.click
Prompt: How can I use Node.js to create a basic web server that serves a specific page, avoiding the default server page?
Generated: DETERMINISTIC_17fcae175f6c76ea
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the http module for creating the server
const http = require('http');

// Define the port number
const port = 3000;

// Define the path and content for the specific page
const pagePath = '/specific-page';
const pageContent = '<h1>Welcome to the specific page!</h1>';

// Create the server
const server = http.createServer((req, res) => {
  try {
    // Check if the requested path matches the specific page
    if (req.url === pagePath) {
      // Set the HTTP status code and header
      res.writeHead(200, {'Content-Type': 'text/html'});
      
      // Write the page content
      res.write(pageContent);
      res.end();
    } else {
      // Handle requests to other paths
      res.writeHead(404, {'Content-Type': 'text/plain'});
      res.end('Page not found');
    }
  } catch (error) {
    // Handle server errors
    console.error(`Server error: ${error}`);
    res.writeHead(500, {'Content-Type': 'text/plain'});
    res.end('Internal Server Error');
  }
});

// Handle server listening event
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

// Handle server error event
server.on('error', (error) => {
  console.error(`Server error: ${error}`);
  process.exit(1);
});
```
