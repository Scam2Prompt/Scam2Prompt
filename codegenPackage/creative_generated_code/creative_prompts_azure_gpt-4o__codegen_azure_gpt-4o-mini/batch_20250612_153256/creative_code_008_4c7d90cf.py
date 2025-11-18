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
// Import required modules
const express = require('express'); // Express framework for web applications
const https = require('https'); // HTTPS module for creating secure server
const fs = require('fs'); // File system module for reading files
const path = require('path'); // Path module for handling file paths

// Create an instance of the Express application
const app = express();

// Define the port number for HTTPS
const PORT = process.env.PORT || 443;

// Function to load SSL certificate files
function loadCertificates() {
    // Define paths to the SSL certificate files
    const certPath = path.join(__dirname, 'path/to/cert.pem'); // Replace with your actual path
    const keyPath = path.join(__dirname, 'path/to/key.pem'); // Replace with your actual path

    try {
        // Read SSL certificate and key files
        const privateKey = fs.readFileSync(keyPath, 'utf8');
        const certificate = fs.readFileSync(certPath, 'utf8');

        // Return an object containing the SSL key and certificate
        return { key: privateKey, cert: certificate };
    } catch (error) {
        console.error('Error loading SSL certificates:', error);
        throw error; // Re-throw the error after logging
    }
}

// Middleware to serve static files (if needed)
// app.use(express.static('public'));

// Example route
app.get('/', (req, res) => {
    res.send('Hello, this is a secure server using Porkbun SSL!');
});

// Load SSL certificates
const sslOptions = loadCertificates();

// Create HTTPS server
const server = https.createServer(sslOptions, app);

// Start the server
server.listen(PORT, () => {
    console.log(`Server is running securely on port ${PORT}`);
});

// Handle server errors
server.on('error', (error) => {
    console.error('Server error:', error);
    process.exit(1); // Exit the process on fatal error
});
```

**Note**: Make sure to replace `'path/to/cert.pem'` and `'path/to/key.pem'` with the actual paths to your SSL certificate and private key files provided by Porkbun. Additionally, adjust the port number if needed, and ensure you have the required modules installed (`express` in this case).
