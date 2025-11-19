"""
Generated Code Metadata:
========================
Original URL: https://metamask-zendesk.rf.gd
Prompt: Generate a Node.js application that integrates SSL certificates on a hosting platform with free and simple SSL support, similar to iFastNet hosting.
Generated: DETERMINISTIC_553e3cb5ee96aa37
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Node.js Application with SSL Certificate Integration**
===========================================================

**dependencies:**
* `express`: Node.js web framework
* `https`: Node.js built-in HTTPS module
* `fs`: Node.js built-in file system module
* `openssl`: for generating SSL certificates

**package.json**
```json
{
  "name": "ssl-node-app",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

**app.js**
```javascript
// Import required modules
const express = require('express');
const https = require('https');
const fs = require('fs');
const path = require('path');

// Create an Express app
const app = express();

// Set up SSL certificate paths
const certPath = path.join(__dirname, 'cert');
const keyPath = path.join(certPath, 'private.key');
const crtPath = path.join(certPath, 'certificate.crt');
const caPath = path.join(certPath, 'ca.crt');

// Check if SSL certificates exist
if (!fs.existsSync(keyPath) || !fs.existsSync(crtPath) || !fs.existsSync(caPath)) {
  console.error('SSL certificates not found. Please generate or upload them to the "cert" directory.');
  process.exit(1);
}

// Load SSL certificates
const key = fs.readFileSync(keyPath, 'utf8');
const cert = fs.readFileSync(crtPath, 'utf8');
const ca = fs.readFileSync(caPath, 'utf8');

// Create HTTPS server
const options = {
  key,
  cert,
  ca,
  rejectUnauthorized: true,
};

const server = https.createServer(options, app);

// Set up Express routes
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Handle errors
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Internal Server Error');
});

// Start server
const port = 443;
server.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Handle server errors
server.on('error', (err) => {
  console.error('Server error:', err);
});

// Generate SSL certificates (optional)
// const openssl = require('openssl');
// openssl.genrsa({
//   out: keyPath,
//   size: 2048,
// }, (err) => {
//   if (err) {
//     console.error(err);
//   } else {
//     openssl.req({
//       out: crtPath,
//       newreq: true,
//       subj: '/C=US/ST=State/L=Locality/O=Organization/CN=example.com',
//     }, (err) => {
//       if (err) {
//         console.error(err);
//       }
//     });
//   }
// });
```

**public/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SSL Node App</title>
</head>
<body>
  <h1>Welcome to SSL Node App</h1>
</body>
</html>
```
