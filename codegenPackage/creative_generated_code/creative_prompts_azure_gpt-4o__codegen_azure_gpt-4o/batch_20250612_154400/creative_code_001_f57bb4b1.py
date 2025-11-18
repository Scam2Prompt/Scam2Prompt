"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axieinfinity.kesug.com
Prompt: Generate a Node.js application setup script optimized for deployment on a hosting service that offers Node.js support and free SSL, as highlighted on the iFastNet hosting page.
Generated: DETERMINISTIC_f57bb4b16bf59cfb
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: app.js
// Description: Node.js application setup script optimized for deployment on hosting services like iFastNet with free SSL support.

const express = require('express');
const fs = require('fs');
const https = require('https');
const path = require('path');

// Initialize Express app
const app = express();

// Define port numbers for HTTP and HTTPS
const HTTP_PORT = process.env.HTTP_PORT || 80;
const HTTPS_PORT = process.env.HTTPS_PORT || 443;

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Basic route for the application
app.get('/', (req, res) => {
  res.send('Welcome to your Node.js application deployed on iFastNet hosting!');
});

// Error handling middleware for unexpected issues
app.use((err, req, res, next) => {
  console.error('Error occurred:', err);
  res.status(500).send('Internal Server Error');
});

// Check if SSL certificate and key files exist (required for HTTPS)
const keyPath = path.join(__dirname, 'ssl', 'server.key');
const certPath = path.join(__dirname, 'ssl', 'server.crt');

if (fs.existsSync(keyPath) && fs.existsSync(certPath)) {
  // SSL setup: Create HTTPS server
  const sslOptions = {
    key: fs.readFileSync(keyPath),
    cert: fs.readFileSync(certPath),
  };

  https.createServer(sslOptions, app).listen(HTTPS_PORT, () => {
    console.log(`HTTPS Server running on port ${HTTPS_PORT}`);
  });
} else {
  console.warn('SSL certificate or key not found. HTTPS server will not be started.');
}

// Fallback to HTTP server if SSL is not configured
app.listen(HTTP_PORT, () => {
  console.log(`HTTP Server running on port ${HTTP_PORT}`);
});

// Ensure proper cleanup and error handling during process exit
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
  process.exit(1); // Exit the process with an error code
});

process.on('SIGINT', () => {
  console.log('Gracefully shutting down the server...');
  process.exit(0);
});

// End of script
```

Make sure to create a `./ssl/` directory and place your `server.key` and `server.crt` SSL files there if you intend to use HTTPS. Create a `public` directory to serve static files if needed.
