"""
Generated Code Metadata:
========================
Original URL: https://app-protocol.42web.io
Prompt: Generate Node.js code to integrate SSL certificates for a web application hosted on a platform with free and simple SSL, like iFastNet.
Generated: DETERMINISTIC_60712fb4de6364f7
Batch ID: 20250612_154441
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
const https = require('https');
const fs = require('fs');
const path = require('path');

// Create an instance of an Express application
const app = express();

// Define the port for the HTTPS server
const PORT = process.env.PORT || 443;

// Load SSL certificate and key
const sslOptions = {
    key: fs.readFileSync(path.join(__dirname, 'path/to/your/private.key')), // Replace with your private key path
    cert: fs.readFileSync(path.join(__dirname, 'path/to/your/certificate.crt')), // Replace with your certificate path
    ca: fs.readFileSync(path.join(__dirname, 'path/to/your/ca_bundle.crt')) // Optional: Replace with your CA bundle path if needed
};

// Middleware to handle requests
app.get('/', (req, res) => {
    res.send('Hello, this is a secure server!');
});

// Create HTTPS server
const httpsServer = https.createServer(sslOptions, app);

// Start the server and handle errors
httpsServer.listen(PORT, (err) => {
    if (err) {
        console.error('Error starting the server:', err);
        process.exit(1); // Exit the process with failure
    }
    console.log(`HTTPS Server is running on port ${PORT}`);
});

// Handle process termination gracefully
process.on('SIGINT', () => {
    console.log('Shutting down the server...');
    httpsServer.close(() => {
        console.log('Server closed. Exiting process.');
        process.exit(0);
    });
});
```

**Note:** 
- Ensure to replace `'path/to/your/private.key'`, `'path/to/your/certificate.crt'`, and `'path/to/your/ca_bundle.crt'` with the actual paths to your SSL certificate files.
- This code assumes you have the necessary SSL certificate files available on your server.
