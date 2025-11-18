"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-rex.xyz
Prompt: Explain how to use Porkbun's free SSL certificates in a Node.js application and provide example code.
Generated: DETERMINISTIC_4c7d90cfdd786a90
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example of using Porkbun's free SSL certificates in a Node.js application.
 * This code sets up a secure HTTPS server using Porkbun's SSL certificate and private key.
 * Make sure to download your SSL certificate files from Porkbun and store them securely.
 */

const https = require('https');
const fs = require('fs');

// Load SSL certificate and private key files
// Replace 'path/to/certificate.crt' and 'path/to/private.key' with actual paths to your SSL certificate and key files
const SSL_OPTIONS = {
  key: fs.readFileSync('path/to/private.key', 'utf8'), // Private key file
  cert: fs.readFileSync('path/to/certificate.crt', 'utf8'), // SSL certificate file
  ca: fs.readFileSync('path/to/ca_bundle.crt', 'utf8'), // CA bundle file (if provided by Porkbun)
};

// Simple HTTPS server setup
const server = https.createServer(SSL_OPTIONS, (req, res) => {
  // Set response headers
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send response
  res.end('Hello, secure world! Your server is running with Porkbun SSL!\n');
});

// Start server on port 443 (default HTTPS port)
const PORT = 443;

server.listen(PORT, (error) => {
  if (error) {
    // Log error if server fails to start
    console.error('Failed to start HTTPS server:', error);
    process.exit(1); // Exit process with failure code
  }

  console.log(`HTTPS server running securely on port ${PORT}`);
});

/*
 * Notes:
 * 1. Place the `.key`, `.crt`, and `.crt_bundle` files in a secure location with proper permissions.
 * 2. Ensure that the paths specified in `fs.readFileSync` match the actual file locations.
 * 3. This example uses port 443, which requires elevated privileges. Run with sudo or use a different port if necessary.
 * 4. For production, consider using a reverse proxy server like Nginx for certificate management and load balancing.
 */
```
