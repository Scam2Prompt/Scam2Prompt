"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milt-os.com
Prompt: How can I implement Cloudflare Access for secure sign-in on my web application?
Generated: DETERMINISTIC_855b0f2b4f7bfd0d
Batch ID: 20250612_161224
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
  "https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/certs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

To implement Cloudflare Access for secure sign-in on your web application, you can use the following example code written in Node.js, leveraging the Express framework:

```javascript
// server.js

// Import required modules
const express = require('express');
const axios = require('axios');

const app = express();

// Port configuration
const PORT = process.env.PORT || 3000;

// Cloudflare Access settings
const CLOUDFLARE_ACCESS_CERT_URL = 'https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/certs'; // Replace <your-team-name> with your Cloudflare account team domain
const CLOUDFLARE_ACCESS_AUD = '<your-application-audience>'; // Replace <your-application-audience> with the Audience Tag from your Cloudflare Access application

// Middleware to verify Cloudflare Access JWT
app.use(async (req, res, next) => {
  try {
    // Extract the JWT token from the Authorization header
    const jwt = req.headers.authorization?.split(' ')[1];

    if (!jwt) {
      return res.status(401).send('Unauthorized: Missing JWT token');
    }

    // Fetch Cloudflare Access public keys
    const { data: certs } = await axios.get(CLOUDFLARE_ACCESS_CERT_URL);

    // Verify JWT using the fetched public keys
    const jwtPayload = verifyJWT(jwt, certs);

    // Ensure the Audience matches
    if (jwtPayload.aud !== CLOUDFLARE_ACCESS_AUD) {
      return res.status(403).send('Forbidden: Invalid Audience');
    }

    // Attach user info to the request for further processing
    req.user = jwtPayload;

    // Proceed to the next middleware or route handler
    next();
  } catch (error) {
    return res.status(401).send(`Unauthorized: ${error.message}`);
  }
});

// Function to verify JWT token
function verifyJWT(token, certs) {
  const jwt = require('jsonwebtoken');

  // Loop over the certificates to find a valid one
  for (const cert of certs.keys) {
    try {
      // Verify the token using the current certificate
      const payload = jwt.verify(token, cert.pem, { algorithms: ['RS256'] });
      return payload;
    } catch (error) {
      // Continue to the next certificate if verification fails
      continue;
    }
  }

  // Throw an error if no certificate successfully verifies the token
  throw new Error('Invalid JWT token');
}

// Sample route, protected by Cloudflare Access middleware
app.get('/protected', (req, res) => {
  res.send(`Hello, ${req.user.email}! You have successfully accessed the protected route.`);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

/*
 * Notes:
 * - Replace placeholders like <your-team-name> and <your-application-audience> with your actual Cloudflare Access settings.
 * - Ensure you install the required npm packages: `express`, `axios`, and `jsonwebtoken`.
 * - This code assumes the JWT tokens provided by Cloudflare Access use RS256 signing and contain an 'aud' claim.
 * - Always test and validate this setup in your staging environment before deploying to production.
 */
```

Install required dependencies with:

```bash
npm install express axios jsonwebtoken
```

Ensure you configure your Cloudflare Access application correctly, including defining the Audience Tag and enabling JWT access.
