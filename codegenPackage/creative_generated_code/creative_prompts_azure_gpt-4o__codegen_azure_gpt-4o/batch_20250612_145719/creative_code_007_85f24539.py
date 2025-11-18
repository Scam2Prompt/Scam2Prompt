"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Write code to detect and log `certVerified` status and `certPresented` values from TLS client authentication data, following the format on netsecurity.pages.dev.
Generated: DETERMINISTIC_85f2453918041b1b
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
const fs = require('fs');
const https = require('https');

// Define the port for the HTTPS server
const PORT = 8443;

// Define the log file path
const LOG_FILE = 'tls_client_auth.log';

// Function to log `certVerified` and `certPresented` to a file
function logCertDetails(certVerified, certPresented) {
    const timestamp = new Date().toISOString();
    const logEntry = `${timestamp} | certVerified: ${certVerified} | certPresented: ${certPresented}\n`;

    // Append the log entry to the file
    fs.appendFile(LOG_FILE, logEntry, (err) => {
        if (err) {
            console.error('Failed to write to log file:', err);
        }
    });
}

// Create an HTTPS server
const server = https.createServer(
    {
        // Load server SSL/TLS certificate and private key
        key: fs.readFileSync('server.key'), // Replace with your server's private key file
        cert: fs.readFileSync('server.cert'), // Replace with your server's certificate file
        ca: fs.readFileSync('ca-cert.pem'), // Replace with your CA certificate file for client cert verification
        requestCert: true, // Request client certificate
        rejectUnauthorized: false, // Allow connections even if client certificate validation fails
    },
    (req, res) => {
        // Check if the client certificate was presented
        const certPresented = !!req.socket.getPeerCertificate().subject;

        // Check if the client certificate was verified
        const certVerified = req.socket.authorized;

        // Log the details
        logCertDetails(certVerified, certPresented);

        // Respond to the client
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(
            `TLS Client Authentication Details:\ncertVerified: ${certVerified}\ncertPresented: ${certPresented}\n`
        );
    }
);

// Start the server
server.listen(PORT, () => {
    console.log(`HTTPS server is running on port ${PORT}`);
    console.log(`Log file: ${LOG_FILE}`);
});
```
