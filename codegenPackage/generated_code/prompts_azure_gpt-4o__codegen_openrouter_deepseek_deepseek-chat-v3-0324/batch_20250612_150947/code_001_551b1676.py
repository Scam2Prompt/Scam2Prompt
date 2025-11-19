"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Generate Node.js code for setting up a server on a hosting platform that offers modern cPanel and free SSL, referencing iFastNet hosting features.
Generated: DETERMINISTIC_551b167672a28f81
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// server.js - Node.js server setup for iFastNet hosting with cPanel and free SSL

const express = require('express');
const https = require('https');
const fs = require('fs');
const path = require('path');

// Environment variables setup
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON and urlencoded form data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Static files serving from public directory
app.use(express.static(path.join(__dirname, 'public')));

// Basic route for health check
app.get('/', (req, res) => {
  res.status(200).json({ status: 'Server is running' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// SSL certificate paths (assuming they are in the home directory as per iFastNet setup)
const sslOptions = {
  key: fs.readFileSync(path.join(process.env.HOME, 'ssl', 'privkey.pem')),
  cert: fs.readFileSync(path.join(process.env.HOME, 'ssl', 'fullchain.pem'))
};

// Create HTTPS server if SSL files exist, otherwise HTTP
let server;
try {
  server = https.createServer(sslOptions, app);
  console.log('SSL certificates found. Starting HTTPS server.');
} catch (err) {
  console.log('No SSL certificates found. Starting HTTP server.');
  server = app;
}

// Start the server
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Handle process termination
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully.');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully.');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

// Export the app for testing purposes
module.exports = app;
```
