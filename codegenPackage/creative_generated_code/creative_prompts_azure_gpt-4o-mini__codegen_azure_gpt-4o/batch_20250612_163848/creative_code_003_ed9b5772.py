"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4de192bb.d6c1924f22b82c8daa243716.workers.dev
Prompt: How do I set up a middleware to check the security of connections in a Node.js application?
Generated: DETERMINISTIC_ed9b5772efcd3523
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require("express");

// Create an Express application instance
const app = express();

// Middleware to check the security of connections
const securityMiddleware = (req, res, next) => {
  try {
    // Check if the connection is secure (via HTTPS)
    if (req.secure || req.headers["x-forwarded-proto"] === "https") {
      // Proceed to the next middleware or route handler
      next();
    } else {
      // Reject unsecure connections with a 403 Forbidden status
      res.status(403).json({
        error: "Connection must be secure (HTTPS).",
      });
    }
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error("Error in security middleware:", error.message);
    res.status(500).json({
      error: "Internal Server Error.",
    });
  }
};

// Apply the middleware globally
app.use(securityMiddleware);

// Example route for testing
app.get("/", (req, res) => {
  res.status(200).send("Connection is secure!");
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
