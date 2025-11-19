"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-olxuahorder824114.pages.dev
Prompt: How can I implement a security check for user connections in a web application using JavaScript?
Generated: DETERMINISTIC_c132cb294e9b6bb0
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Security Check for User Connections in a Web Application
 * This code validates user connections by checking if certain security conditions are met.
 * It ensures safe connections to the application using JWT authentication and IP whitelisting.
 */

// Import necessary modules (e.g., for JWT verification)
const jwt = require('jsonwebtoken');
const allowedIPs = ['192.168.1.1', '203.0.113.42']; // Example whitelist of allowed IPs

// Secret key for JWT verification (store in environment variables in production)
const JWT_SECRET = process.env.JWT_SECRET || "your-secure-secret";

// Middleware function for security check
const securityCheckMiddleware = (req, res, next) => {
    try {
        // Extract the client's IP address
        const clientIP = req.ip || req.connection.remoteAddress;

        // Check if the client's IP is in the whitelist
        if (!allowedIPs.includes(clientIP)) {
            return res.status(403).json({ error: "Access denied: Unauthorized IP" });
        }

        // Extract the JWT from the "Authorization" header
        const authHeader = req.headers.authorization;
        if (!authHeader || !authHeader.startsWith("Bearer ")) {
            return res.status(401).json({ error: "Access denied: Missing or invalid token" });
        }

        const token = authHeader.split(" ")[1];

        // Verify the JWT
        jwt.verify(token, JWT_SECRET, (err, decoded) => {
            if (err) {
                return res.status(401).json({ error: "Access denied: Invalid token" });
            }

            // Attach decoded user info to the request object for downstream use
            req.user = decoded;

            // Proceed to the next middleware or route handler
            next();
        });
    } catch (error) {
        // Handle unexpected errors
        console.error("Security check error:", error);
        res.status(500).json({ error: "An unexpected error occurred during security check" });
    }
};

// Example usage in an Express.js application
const express = require('express');
const app = express();

// Apply the security check middleware to all routes
app.use(securityCheckMiddleware);

// Example route
app.get('/secure-data', (req, res) => {
    res.json({ message: "Access granted", user: req.user });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
