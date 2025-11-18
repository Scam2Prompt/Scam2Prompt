"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.thsite.top
Prompt: Generate a Node.js script to configure and deploy a secure web application on a hosting service that supports free domain names and SSL certificates.
Generated: DETERMINISTIC_5abb864a911caf05
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const http = require('http');
const https = require('https');
const fs = require('fs');
const { exec } = require('child_process');

// Load environment variables from .env file
require('dotenv').config();

// Create an instance of an Express app
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Define a simple route for the web application
app.get('/', (req, res) => {
    res.send('Welcome to the secure web application!');
});

// Function to create HTTPS server
function createHttpsServer() {
    // Load SSL certificates
    const privateKey = fs.readFileSync(process.env.SSL_PRIVATE_KEY, 'utf8');
    const certificate = fs.readFileSync(process.env.SSL_CERTIFICATE, 'utf8');
    const ca = fs.readFileSync(process.env.SSL_CA, 'utf8');

    // Create HTTPS credentials
    const credentials = {
        key: privateKey,
        cert: certificate,
        ca: ca,
    };

    // Create HTTPS server
    const httpsServer = https.createServer(credentials, app);

    // Start the server on the specified port
    httpsServer.listen(process.env.PORT || 443, () => {
        console.log(`HTTPS Server running on port ${process.env.PORT || 443}`);
    });
}

// Function to configure domain name and SSL certificate
function configureDomainAndSSL() {
    const domain = process.env.DOMAIN;

    // Command to configure domain and obtain SSL certificate using Let's Encrypt
    const command = `certbot --nginx -d ${domain} --non-interactive --agree-tos --email ${process.env.EMAIL}`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error configuring domain and SSL: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`Error output: ${stderr}`);
            return;
        }
        console.log(`Domain and SSL configuration output: ${stdout}`);
    });
}

// Invoke functions to set up server and configuration
try {
    configureDomainAndSSL();
    createHttpsServer();
} catch (error) {
    console.error(`Failed to set up the web application: ${error.message}`);
}

// Catch and handle unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});

// Catch and handle uncaught exceptions
process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
});
```

Make sure to create a `.env` file with the following variables before running the script:
```
SSL_PRIVATE_KEY=path/to/your/private.key
SSL_CERTIFICATE=path/to/your/certificate.crt
SSL_CA=path/to/your/ca_bundle.crt
DOMAIN=yourdomain.com
EMAIL=youremail@example.com
PORT=443
```
