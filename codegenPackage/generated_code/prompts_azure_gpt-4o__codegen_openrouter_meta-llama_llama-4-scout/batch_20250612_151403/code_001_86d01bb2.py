"""
Generated Code Metadata:
========================
Original URL: https://metamask-pon.infinityfreeapp.com
Prompt: Generate Node.js code for setting up a server that can be hosted on a platform offering unlimited bandwidth and modern cPanel, like the one mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_86d01bb23f127124
Batch ID: 20250612_151403
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
const https = require('https');
const fs = require('fs');
const path = require('path');

// Create an Express application
const app = express();

// Define port
const port = process.env.PORT || 8080;

// Set up middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Define a basic route
app.get('/', (req, res) => {
  res.send('Server is running successfully!');
});

// Error handling middleware
app.use((req, res, next) => {
  const error = new Error('Not Found');
  error.status = 404;
  next(error);
});

app.use((error, req, res, next) => {
  console.error(error);
  res.status(error.status || 500);
  res.json({ error: error.message });
});

// Create an HTTP server
const httpServer = http.createServer(app);

// Create an HTTPS server (optional, requires SSL certificates)
const httpsOptions = {
  key: fs.readFileSync(path.join(__dirname, 'ssl', 'private.key')),
  cert: fs.readFileSync(path.join(__dirname, 'ssl', 'certificate.crt')),
};

const httpsServer = https.createServer(httpsOptions, app);

// Start servers
httpServer.listen(port, () => {
  console.log(`HTTP server listening on port ${port}`);
});

httpsServer.listen(8443, () => {
  console.log('HTTPS server listening on port 8443');
});

// Handle server errors
httpServer.on('error', (error) => {
  console.error('HTTP server error:', error);
});

httpsServer.on('error', (error) => {
  console.error('HTTPS server error:', error);
});
```
