"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Generate Node.js code for setting up a server on a hosting platform that offers modern cPanel and free SSL, referencing iFastNet hosting features.
Generated: DETERMINISTIC_551b167672a28f81
Batch ID: 20250612_150947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules
const express = require('express'); // Web framework for Node.js
const https = require('https'); // Module for HTTPS server
const fs = require('fs'); // File system module for reading the SSL certificate
const path = require('path'); // Module for handling file paths

// Create an instance of an Express application
const app = express();

// Define the port for the server to listen on
const PORT = process.env.PORT || 443; // Default to 443 for HTTPS

// Middleware to serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Example route
app.get('/', (req, res) => {
    res.send('<h1>Welcome to My Secure Node.js Server!</h1>');
});

// Read SSL certificate and key files
const sslOptions = {
    key: fs.readFileSync(path.join(__dirname, 'ssl', 'privatekey.pem')), // Path to the private key
    cert: fs.readFileSync(path.join(__dirname, 'ssl', 'certificate.pem')), // Path to the certificate
};

// Create HTTPS server with Express app
const server = https.createServer(sslOptions, app);

// Start the server and handle errors
server.listen(PORT, (err) => {
    if (err) {
        console.error('Error starting server:', err);
        process.exit(1); // Exit the process with an error code if server fails to start
    }
    console.log(`Server is running securely on https://localhost:${PORT}`);
});

// Handle process termination gracefully
process.on('SIGINT', () => {
    console.log('Shutting down server...');
    server.close(() => {
        console.log('Server shut down gracefully.');
        process.exit(0);
    });
});

// Export the app for testing or further configuration
module.exports = app;
```

### Directory Structure
Ensure your project has the following structure:
```
/your-project
│
├── /ssl
│   ├── privatekey.pem
│   └── certificate.pem
│
├── /public
│   └── (static files here)
│
├── server.js
└── package.json
```

### Note
- Ensure to replace the paths in `sslOptions` with the actual paths to your SSL certificate and private key.
- Install the necessary packages by running: 
```bash
npm install express
``` 
- Deploy this code on a hosting platform that supports Node.js, such as iFastNet, and you will benefit from their modern cPanel and free SSL features.
