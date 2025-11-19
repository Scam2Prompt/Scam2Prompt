"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-bonkboxes.web.app
Prompt: How do I set up a whitelist for API access in a JavaScript environment like BonkBoxes?
Generated: DETERMINISTIC_85e6234fe33454fc
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// API Whitelist Setup for BonkBoxes

// List of whitelisted IP addresses
const whitelist = [
  "192.168.1.1",  // Example IP address 1
  "203.0.113.5",  // Example IP address 2
  "198.51.100.7"  // Example IP address 3
];

// Middleware function to check if the IP is whitelisted
// This assumes an Express.js environment
const apiWhitelistMiddleware = (req, res, next) => {
  try {
    // Get the client's IP address (adjust based on your setup)
    const clientIp =
      req.headers["x-forwarded-for"] || req.connection.remoteAddress;

    // Check if the IP is in the whitelist
    if (whitelist.includes(clientIp)) {
      // IP is whitelisted, allow access to the API
      next();
    } else {
      // IP is not whitelisted, deny access with a 403 Forbidden status
      res.status(403).json({
        success: false,
        message: "Access denied. Your IP is not allowed."
      });
    }
  } catch (error) {
    // Handle any unexpected errors
    console.error("Error processing whitelist check:", error);
    res.status(500).json({
      success: false,
      message: "An internal error occurred. Please try again later."
    });
  }
};

// Example usage
const express = require("express");
const app = express();

// Apply middleware to protect the API route
app.use("/api/protected", apiWhitelistMiddleware, (req, res) => {
  res.status(200).json({
    success: true,
    message: "Welcome to the protected API route!"
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Note:
// - Ensure the IP addresses in the whitelist match your requirements.
// - Customize IP extraction logic based on your infrastructure (e.g., proxy setup).
// - Replace `req.connection.remoteAddress` with proper logic for IPv6 if needed.
```
