"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-cftc-us8-73s.pages.dev
Prompt: Generate a sample configuration for integrating Cloudflare's security features in a Node.js application.
Generated: DETERMINISTIC_e77812ebcb3848fe
Batch ID: 20250612_161134
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const app = express();

// Set the Cloudflare IP ranges for whitelisting (modify as needed)
const cloudflareIps = [
    '104.16.0.0/12',
    '108.162.192.0/18',
    '131.0.72.0/22',
    // Add more IP ranges as necessary
];

// Middleware for security headers
app.use(helmet());

// Rate limiter configuration
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // Limit each IP to 100 requests per windowMs
    message: 'Too many requests from this IP, please try again later.'
});

// Apply the rate limiter to all requests
app.use(limiter);

// Middleware to restrict access to Cloudflare IPs only
app.use((req, res, next) => {
    const clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    
    // Check if the client's IP is in the Cloudflare IP ranges
    if (!isCloudflareIp(clientIp)) {
        return res.status(403).json({ error: 'Access denied. Only Cloudflare IPs are allowed.' });
    }
    next();
});

// Function to check if IP is part of Cloudflare ranges
function isCloudflareIp(ip) {
    // This is a simple check for demonstration purposes. 
    // For production, consider using a library like `ip6` or `ip6` for better range checks.
    return cloudflareIps.some(range => ipInCIDR(ip, range));
}

// Simple IP address in CIDR range check
function ipInCIDR(ip, cidr) {
    const [range, bits] = cidr.split('/');
    const mask = ~((1 << (32 - bits)) - 1);
    const ipNum = ipToInt(ip);
    const rangeNum = ipToInt(range);
    
    return (ipNum & mask) === (rangeNum & mask);
}

// Convert IP address to an integer
function ipToInt(ip) {
    return ip.split('.').reduce((acc, octet) => (acc << 8) + parseInt(octet, 10), 0) >>> 0;
}

// Sample route
app.get('/', (req, res) => {
    res.send('Hello, Cloudflare secured application!');
});

// Error handling middleware for production
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
