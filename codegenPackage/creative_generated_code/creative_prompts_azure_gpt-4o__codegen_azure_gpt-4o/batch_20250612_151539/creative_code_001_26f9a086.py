"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extensionsrect.rf.gd
Prompt: Generate a Node.js server configuration suitable for deployment on a hosting platform with no daily hit limit and free SSL, like iFastNet.
Generated: DETERMINISTIC_26f9a0867a7f3d5c
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Express framework for building HTTP servers
const https = require('https'); // HTTPS module for SSL support
const fs = require('fs'); // File system module to read SSL certificate files
const path = require('path'); // Path module for handling file paths
const compression = require('compression'); // Compression middleware for reducing response size
const helmet = require('helmet'); // Helmet middleware for securing HTTP headers

// Initialize the app
const app = express();

// Port configuration
const PORT = 3000; // Default HTTP port
const SSL_PORT = 443; // Default HTTPS port

// Directory paths for SSL certificates (update paths accordingly)
const SSL_CERT_DIR = path.join(__dirname, 'ssl');
const SSL_KEY_PATH = path.join(SSL_CERT_DIR, 'server.key');
const SSL_CERT_PATH = path.join(SSL_CERT_DIR, 'server.cert');

// Middleware configuration
app.use(compression()); // Enable compression for responses
app.use(helmet()); // Secure headers to prevent attacks
app.use(express.json()); // Parse incoming JSON payloads
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded payloads

// Serve static files if required
// Update 'public' to your actual static folder path
app.use(express.static(path.join(__dirname, 'public')));

// Basic route for testing server
app.get('/', (req, res) => {
  res.send('Welcome to the Node.js server!');
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error
  res.status(500).send('Something went wrong!'); // Send generic error response
});

// Load SSL credentials
let credentials;
try {
  credentials = {
    key: fs.readFileSync(SSL_KEY_PATH, 'utf8'),
    cert: fs.readFileSync(SSL_CERT_PATH, 'utf8'),
  };
} catch (error) {
  console.error('Error loading SSL credentials:', error.message);
  process.exit(1); // Exit process if SSL credentials are unavailable
}

// Create HTTP server for fallback (optional)
const httpServer = app.listen(PORT, () => {
  console.log(`HTTP server is running on port ${PORT}`);
});

// Create HTTPS server for secure connections
const httpsServer = https.createServer(credentials, app);

// Start the HTTPS server
httpsServer.listen(SSL_PORT, () => {
  console.log(`HTTPS server is running on port ${SSL_PORT}`);
});

// Proper shutdown handling
process.on('SIGINT', () => {
  console.log('Shutting down server gracefully...');
  httpServer.close(() => console.log('HTTP server closed.'));
  httpsServer.close(() => console.log('HTTPS server closed.'));
  process.exit(0);
});

// Notes:
// 1. Ensure the hosting platform supports custom SSL certificate installation.
// 2. Replace SSL certificate paths with the actual locations provided by your hosting service.
// 3. This code assumes your hosting platform allows Node.js applications and custom SSL certificates.
```
