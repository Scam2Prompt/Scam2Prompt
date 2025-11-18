"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: How can I use Cloudflare Access to secure a web application with multiple sign-in methods, including Google and email-based authentication?
Generated: DETERMINISTIC_580774f99bbcfc44
Batch ID: 20250612_150927
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://<your-cloudflare-team-name>.cloudflareaccess.com/cdn-cgi/access/certs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Node.js example using Express to secure a web application with Cloudflare Access, supporting Google and email-based authentication.

```javascript
// Import required modules
const express = require("express");
const axios = require("axios");
const jwt = require("jsonwebtoken");
require("dotenv").config();

const app = express();

// Port configuration
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(express.json());

// Cloudflare Access public keys endpoint
const CLOUDFLARE_ACCESS_KEYS_URL = "https://<your-cloudflare-team-name>.cloudflareaccess.com/cdn-cgi/access/certs";

// Routes

/**
 * Public route: Test the server.
 */
app.get("/", (req, res) => {
  res.send("Welcome to the Cloudflare Access-secured app!");
});

/**
 * Middleware to verify Cloudflare Access JWT.
 */
async function verifyCloudflareAccessJWT(req, res, next) {
  try {
    const accessToken = req.headers["cf-access-jwt"]; // Extract JWT from headers
    if (!accessToken) {
      return res.status(401).json({ error: "Missing Cloudflare Access JWT" });
    }

    // Fetch Cloudflare Access public keys
    const { data } = await axios.get(CLOUDFLARE_ACCESS_KEYS_URL);
    const keys = data.keys;
    
    // Decode the JWT to find the key ID
    const decodedTokenHeader = jwt.decode(accessToken, { complete: true }).header;
    const keyId = decodedTokenHeader.kid;

    // Locate the matching key
    const publicKey = keys.find((key) => key.kid === keyId);
    if (!publicKey) {
      return res.status(401).json({ error: "Invalid JWT key ID" });
    }

    // Verify the JWT using the public key
    const verifiedPayload = jwt.verify(accessToken, publicKey.pem, {
      algorithms: ["RS256"],
      audience: process.env.CLOUDFLARE_APP_DOMAIN, // Ensure audience matches your domain
    });

    // Attach payload to the request object for further use
    req.user = verifiedPayload;

    next(); // Proceed to the next middleware/route handler
  } catch (error) {
    console.error("Error verifying Cloudflare Access JWT:", error.message);
    res.status(401).json({ error: "Invalid or expired JWT" });
  }
}

/**
 * Protected route: Accessible only with a valid Cloudflare Access JWT.
 */
app.get("/protected", verifyCloudflareAccessJWT, (req, res) => {
  res.json({
    message: "You have accessed a protected route!",
    user: req.user, // Information from the JWT payload
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Steps:
1. Replace `<your-cloudflare-team-name>` with your Cloudflare Team name.
2. Set the `CLOUDFLARE_APP_DOMAIN` environment variable to your application domain.
3. Configure Cloudflare Access to require authentication using Google and email sign-in methods.

The code handles JWT validation securely and allows access only to authenticated users, adhering to Cloudflare Access protocols.
