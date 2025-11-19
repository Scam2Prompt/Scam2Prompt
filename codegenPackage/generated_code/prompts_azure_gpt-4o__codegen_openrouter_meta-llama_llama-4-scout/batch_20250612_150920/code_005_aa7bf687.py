"""
Generated Code Metadata:
========================
Original URL: https://aidsupport.rf.gd
Prompt: Create a Node.js application optimized for deployment on hosting platforms that support unlimited bandwidth and free SSL, similar to iFastNet.
Generated: DETERMINISTIC_aa7bf68747c7fed6
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Node.js Application Code**
```javascript
// Import required modules
const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require('path');
const fs = require('fs');

// Create an Express application instance
const app = express();

// Set application port
const port = process.env.PORT || 3000;

// Enable security headers
app.use(helmet());

// Enable logging
app.use(morgan('combined'));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a route for the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Define a catch-all route for unknown URLs
app.use((req, res) => {
  res.status(404).send('Not Found');
});

// Handle application errors
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Internal Server Error');
});

// Create an HTTPS server using a self-signed certificate (for development purposes)
// or a free SSL certificate from a provider like Let's Encrypt (for production)
const https = require('https');
const tlsOptions = {
  key: fs.readFileSync(path.join(__dirname, 'tls', 'private.key')),
  cert: fs.readFileSync(path.join(__dirname, 'tls', 'certificate.crt')),
};
const httpsServer = https.createServer(tlsOptions, app);

// Start the HTTPS server
httpsServer.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Handle server errors
httpsServer.on('error', (err) => {
  console.error('Server error:', err);
  process.exit(1);
});

// Enable graceful shutdown
process.on('SIGTERM', () => {
  httpsServer.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
```

**package.json**
```json
{
  "name": "node-app",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "helmet": "^4.4.1",
    "morgan": "^1.10.0"
  }
}
```

**tls/generate-cert.sh** (for development purposes only)
```bash
#!/bin/bash

openssl req -x509 -newkey rsa:2048 -nodes -keyout private.key -out certificate.crt -days 365 -subj "/C=US/ST=State/L=Locality/O=Organization/CN=localhost"
```

**public/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Node.js Application</title>
</head>
<body>
  <h1>Welcome to my Node.js application!</h1>
</body>
</html>
```
