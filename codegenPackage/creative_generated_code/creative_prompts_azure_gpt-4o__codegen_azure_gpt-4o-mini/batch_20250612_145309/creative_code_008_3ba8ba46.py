"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://post-customsgovua.infinityfreeapp.com
Prompt: Write a Node.js script to manage SSL certificates for a website hosted on iFastNet.
Generated: DETERMINISTIC_3ba8ba46d57eee2e
Batch ID: 20250612_145309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const fs = require('fs');
const https = require('https');
const path = require('path');

// Configuration for your SSL certificate
const certConfig = {
    key: path.join(__dirname, 'path/to/your/private.key'),     // Path to your private key
    cert: path.join(__dirname, 'path/to/your/certificate.crt'), // Path to your SSL certificate
    ca: path.join(__dirname, 'path/to/your/ca_bundle.crt')       // Path to your CA bundle (if any)
};

// Function to check if a file exists
const fileExists = (filePath) => {
    return new Promise((resolve) => {
        fs.access(filePath, fs.constants.F_OK, (err) => {
            resolve(!err);
        });
    });
};

// Function to load SSL certificates
const loadCertificates = async () => {
    try {
        const keyExists = await fileExists(certConfig.key);
        const certExists = await fileExists(certConfig.cert);
        const caExists = await fileExists(certConfig.ca);

        if (!keyExists || !certExists || (certConfig.ca && !caExists)) {
            throw new Error('One or more SSL certificate files are missing.');
        }

        return {
            key: fs.readFileSync(certConfig.key),
            cert: fs.readFileSync(certConfig.cert),
            ca: certConfig.ca ? fs.readFileSync(certConfig.ca) : null
        };
    } catch (error) {
        console.error(`Error loading SSL certificates: ${error.message}`);
        process.exit(1); // Exit the process with an error
    }
};

// Function to create an HTTPS server
const createServer = (certificates) => {
    const server = https.createServer(certificates, (req, res) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello, secure world!\n');
    });

    server.listen(443, () => {
        console.log('HTTPS Server running on port 443');
    });

    server.on('error', (error) => {
        console.error(`Server error: ${error.message}`);
        process.exit(1); // Exit process on server error
    });
};

// Main function to manage SSL certificates
const manageSSLCertificates = async () => {
    const certificates = await loadCertificates();
    createServer(certificates);
};

// Execute the main function
manageSSLCertificates();
```

### Notes:
- Make sure to replace `path/to/your/private.key`, `path/to/your/certificate.crt`, and `path/to/your/ca_bundle.crt` with the actual paths to your SSL files.
- Run this script with appropriate permissions on your server, as it listens on port 443.
