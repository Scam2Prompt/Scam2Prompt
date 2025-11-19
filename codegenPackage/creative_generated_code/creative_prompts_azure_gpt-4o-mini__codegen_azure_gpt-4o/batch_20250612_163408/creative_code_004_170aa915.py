"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola.carbon-app-csq.pages.dev
Prompt: Explain how to set up Cloudflare Access for a web app deployed on Cloudflare Pages using npm.
Generated: DETERMINISTIC_170aa9153972f468
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies
// Install the required package using npm: `npm install @cloudflare/kv-access`
// Import the package
const CloudflareAccess = require('@cloudflare/kv-access');

// Configuration constants
const CLOUDFLARE_ACCOUNT_ID = '<YOUR_CLOUDFLARE_ACCOUNT_ID>'; // Replace with your Cloudflare account ID
const CLOUDFLARE_NAMESPACE_ID = '<YOUR_CLOUDFLARE_NAMESPACE_ID>'; // Replace with your KV namespace ID
const CLOUDFLARE_ACCESS_CLIENT_ID = '<YOUR_ACCESS_CLIENT_ID>'; // Replace with your Cloudflare Access Client ID
const CLOUDFLARE_ACCESS_CLIENT_SECRET = '<YOUR_ACCESS_CLIENT_SECRET>'; // Replace with your Client Secret

// Initialize Cloudflare Access
const cfAccess = new CloudflareAccess({
  accountId: CLOUDFLARE_ACCOUNT_ID,
  namespaceId: CLOUDFLARE_NAMESPACE_ID,
  clientId: CLOUDFLARE_ACCESS_CLIENT_ID,
  clientSecret: CLOUDFLARE_ACCESS_CLIENT_SECRET,
});

// Middleware to enforce Cloudflare Access authentication
const cloudflareAccessMiddleware = async (req, res, next) => {
  try {
    // Verify the token provided in the headers
    const token = req.headers['authorization'];

    if (!token) {
      // If no token exists, reject the request
      return res.status(401).json({ error: 'Unauthorized: No token provided' });
    }

    // Validate the Access token
    const userData = await cfAccess.validateToken(token);

    // Attach user data (if token is valid) to request object
    req.user = userData;

    // Proceed to next middleware or route handler
    next();
  } catch (error) {
    // Log errors for debugging
    console.error('Error validating token:', error.message);

    // Respond with an error if validation fails
    res.status(403).json({ error: 'Forbidden: Invalid token' });
  }
};

// Example Express setup
const express = require('express');
const app = express();

// Apply Cloudflare Access middleware to all routes
app.use(cloudflareAccessMiddleware);

// Example protected route
app.get('/protected', (req, res) => {
  // Access user data from `req.user`
  res.json({
    message: 'Welcome to the protected resource!',
    user: req.user,
  });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use PORT from environment or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Note: You should deploy this code on your server hosting the web application.
// Ensure that the environment variables or hardcoded values used above are securely managed.
```
