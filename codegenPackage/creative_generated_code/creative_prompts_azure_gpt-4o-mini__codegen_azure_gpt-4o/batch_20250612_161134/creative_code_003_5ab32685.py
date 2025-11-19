"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiwebio.rf.gd
Prompt: Explain how to set up a free SSL certificate on iFastNet Web Hosting and provide a code example for securing a Node.js application.
Generated: DETERMINISTIC_5ab32685c532a4c3
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required modules
const https = require('https'); // For creating an HTTPS server
const fs = require('fs'); // For reading SSL certificate files
const express = require('express'); // For handling HTTP requests

// Create an instance of Express application
const app = express();

// Middleware for parsing JSON requests
app.use(express.json());

// Route for testing SSL setup
app.get('/', (req, res) => {
  res.send('Your Node.js application is now secured with SSL!');
});

// SSL certificate setup
// Replace file paths with the actual paths to your SSL certificate and key provided by iFastNet
const sslOptions = {
  key: fs.readFileSync('/path/to/your/ssl/private.key'), // Private key file
  cert: fs.readFileSync('/path/to/your/ssl/certificate.crt'), // Certificate file
  ca: fs.readFileSync('/path/to/your/ssl/ca_bundle.crt') // Optional: CA bundle file, if provided
};

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error for debugging purposes
  res.status(500).send('Something went wrong!'); // Send a generic error response to the client
});

// Create an HTTPS server
https.createServer(sslOptions, app).listen(443, () => {
  console.log('Secure Node.js application is running on port 443.');
});
```

### Notes:
1. Replace `/path/to/your/ssl/private.key`, `/path/to/your/ssl/certificate.crt`, and `/path/to/your/ssl/ca_bundle.crt` with the actual file paths to your SSL files downloaded from iFastNet.
2. Ensure that your web hosting plan supports SSL and HTTPS.
3. Update DNS settings to point to your iFastNet server before testing SSL.
4. Make sure ports 443 (HTTPS) and 80 (HTTP) are open on the server.
