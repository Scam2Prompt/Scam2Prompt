"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glveaways-metamasks-lo.html-5.me
Prompt: Generate Node.js code to configure a web server with SSL support for deployment on a hosting platform like iFastNet that offers unlimited bandwidth.
Generated: DETERMINISTIC_e74f071f1791df86
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const https = require('https');
const fs = require('fs');
const express = require('express');

// Create an instance of an Express application
const app = express();

// Middleware to serve static files from the 'public' directory
app.use(express.static('public'));

// Sample route to demonstrate server functionality
app.get('/', (req, res) => {
    res.send('<h1>Welcome to the Secure Web Server!</h1>');
});

// Load SSL certificate and private key
const sslOptions = {
    key: fs.readFileSync('path/to/your/private/key.pem'), // Path to your SSL key
    cert: fs.readFileSync('path/to/your/certificate.pem') // Path to your SSL certificate
};

// Create HTTPS server with SSL options
const server = https.createServer(sslOptions, app);

// Start the server on port 443 (default for HTTPS)
const PORT = 443;
server.listen(PORT, () => {
    console.log(`Server is running securely on port ${PORT}`);
});

// Error Handling: Handle server listen errors
server.on('error', (error) => {
    console.error('Error occurred:', error);
    process.exit(1); // Exit process on fatal error
});

// Optional: Graceful shutdown on termination signals
process.on('SIGINT', () => {
    console.log('Shutting down the server...');
    server.close(() => {
        console.log('Server closed. Exiting process.');
        process.exit(0);
    });
});
``` 

**Note**: Replace `'path/to/your/private/key.pem'` and `'path/to/your/certificate.pem'` with the actual paths to your SSL private key and certificate files. Ensure the `public` directory exists for serving static files.
