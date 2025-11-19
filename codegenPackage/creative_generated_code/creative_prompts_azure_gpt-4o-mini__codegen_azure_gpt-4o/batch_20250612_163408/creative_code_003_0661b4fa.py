"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola-321x.carbon-app-csq.pages.dev
Prompt: Generate an example of using Cloudflare Access in a Node.js application with npm.
Generated: DETERMINISTIC_0661b4fa30b59b28
Batch ID: 20250612_163408
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://${CLOUDFLARE_ACCESS_TEAM_DOMAIN}/cdn-cgi/access/certs`;": {
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
/**
 * Example Node.js application using Cloudflare Access with npm
 *
 * This application verifies a JWT issued by Cloudflare Access
 * to authenticate users accessing protected routes.
 *
 * Dependencies: express, jsonwebtoken, axios
 * Run `npm install express jsonwebtoken axios` to install required packages.
 */

const express = require('express');
const jwt = require('jsonwebtoken');
const axios = require('axios');

const app = express();

/**
 * Configuration
 * Replace these values with your actual Cloudflare Access settings.
 */
const CLOUDFLARE_ACCESS_AUD = '<YOUR_CLOUDFLARE_ACCESS_AUD>'; // Your Cloudflare Access Application ID (Audience)
const CLOUDFLARE_ACCESS_TEAM_DOMAIN = '<YOUR_TEAM_DOMAIN>'; // Your Cloudflare Access Team Domain
const CF_ACCESS_PUBLIC_KEYS_URL = `https://${CLOUDFLARE_ACCESS_TEAM_DOMAIN}/cdn-cgi/access/certs`; // URL to fetch public keys

/**
 * Middleware to validate JWT issued by Cloudflare Access
 */
const validateCloudflareAccessJWT = async (req, res, next) => {
    const authHeader = req.headers.authorization;

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return res.status(401).send('Unauthorized: No token provided');
    }

    const token = authHeader.split(' ')[1];

    try {
        // Fetch Cloudflare Access public keys
        const { data: publicKeys } = await axios.get(CF_ACCESS_PUBLIC_KEYS_URL);

        // Decode the JWT header to determine the key ID
        const decodedHeader = jwt.decode(token, { complete: true });
        if (!decodedHeader || !decodedHeader.header || !decodedHeader.header.kid) {
            throw new Error('Invalid token: Missing key ID');
        }

        const keyId = decodedHeader.header.kid;

        // Find the public key that matches the key ID
        const matchingKey = publicKeys.keys.find((key) => key.kid === keyId);
        if (!matchingKey) {
            throw new Error('Invalid token: Key ID not found');
        }

        // Verify the token using the matching public key
        const verifiedPayload = jwt.verify(token, matchingKey.pem, {
            audience: CLOUDFLARE_ACCESS_AUD,
        });

        // Attach the verified payload to the request object
        req.user = verifiedPayload;

        // Proceed to the next middleware or route handler
        next();
    } catch (error) {
        console.error('JWT validation error:', error.message);
        return res.status(401).send('Unauthorized: Invalid token');
    }
};

/**
 * Protected route example
 * Users must provide a valid Cloudflare Access JWT to access this route.
 */
app.get('/protected', validateCloudflareAccessJWT, (req, res) => {
    res.send(`Hello, ${req.user.email}! You have accessed a protected route.`);
});

/**
 * Public route example
 * No authentication required.
 */
app.get('/public', (req, res) => {
    res.send('Welcome to the public route!');
});

/**
 * Start the server
 */
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

Ensure you replace `<YOUR_CLOUDFLARE_ACCESS_AUD>` and `<YOUR_TEAM_DOMAIN>` with your actual Cloudflare Access configuration values. This is production-ready code that validates JWTs issued by Cloudflare Access, handles errors gracefully, and provides clear comments for easy understanding.
