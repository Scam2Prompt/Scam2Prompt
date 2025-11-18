"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zendesk-metamask.rf.gd
Prompt: Generate a Node.js application setup script optimized for deployment on iFastNet hosting, ensuring compatibility with multiple versions of Node.js and SSL.
Generated: DETERMINISTIC_c0fd98209f51a915
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: setup.js
// Description: A Node.js application setup script optimized for deployment on iFastNet hosting.
// This script ensures compatibility with multiple Node.js versions and SSL configuration.

// Import necessary modules
const fs = require('fs');
const https = require('https');
const path = require('path');
const express = require('express');

// Load environment variables from .env (if present)
require('dotenv').config();

// Application constants
const PORT = process.env.PORT || 3000; // Default port for the app
const NODE_ENV = process.env.NODE_ENV || 'production'; // Environment setting
const SSL_KEY_PATH = process.env.SSL_KEY_PATH || '/path/to/ssl/key.pem'; // Path to SSL key
const SSL_CERT_PATH = process.env.SSL_CERT_PATH || '/path/to/ssl/cert.pem'; // Path to SSL certificate

// Initialize an Express app
const app = express();

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Middleware for parsing JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Health check route
app.get('/health', (req, res) => {
  res.status(200).json({ message: 'Server is healthy', environment: NODE_ENV });
});

// Root route
app.get('/', (req, res) => {
  res.status(200).send('<h1>Welcome to My Node.js App!</h1>');
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err.message);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Function to start the server
function startServer() {
  if (fs.existsSync(SSL_KEY_PATH) && fs.existsSync(SSL_CERT_PATH)) {
    // SSL configuration found, start HTTPS server
    const sslOptions = {
      key: fs.readFileSync(SSL_KEY_PATH),
      cert: fs.readFileSync(SSL_CERT_PATH),
    };

    https.createServer(sslOptions, app).listen(PORT, () => {
      console.log(`Server running securely on port ${PORT}`);
    });
  } else {
    // No SSL configuration found, start HTTP server
    app.listen(PORT, () => {
      console.log(`Server running on port ${PORT}`);
      console.warn('SSL configuration not found. Running in HTTP mode.');
    });
  }
}

// Start server
startServer();

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('Shutting down server...');
  process.exit(0);
});

process.on('SIGTERM', () => {
  console.log('Server terminated.');
  process.exit(0);
});
```

Make sure to adjust the `SSL_KEY_PATH` and `SSL_CERT_PATH` environment variables to point to your SSL certificate files when deploying on iFastNet hosting.
