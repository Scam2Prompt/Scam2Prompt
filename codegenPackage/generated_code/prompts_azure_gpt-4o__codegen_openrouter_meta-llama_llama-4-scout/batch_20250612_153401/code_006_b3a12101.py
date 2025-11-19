"""
Generated Code Metadata:
========================
Original URL: https://meta-drago.vercel.app
Prompt: Recommend best practices for optimizing JavaScript apps hosted on Vercel for performance and scalability.
Generated: DETERMINISTIC_b3a1210144b28a58
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const compression = require('compression');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Enable compression for responses
app.use(compression());

// Enable security headers
app.use(helmet());

// Set up rate limiting to prevent abuse
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Enable CORS
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// Set up logging
const morgan = require('morgan');
app.use(morgan('combined'));

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Optimize server performance by setting a timeout
app.timeout = 10000;

// Define a route for testing
app.get('/test', (req, res) => {
  res.send('Hello World!');
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

// Export the app for Vercel
module.exports = app;
```

**.vercel.json**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "index.js",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "index.js"
    }
  ]
}
```

**package.json**
```json
{
  "name": "vercel-optimized-app",
  "version": "1.0.0",
  "scripts": {
    "dev": "vercel dev",
    "build": "vercel build",
    "start": "vercel start"
  },
  "dependencies": {
    "express": "^4.17.1",
    "compression": "^1.7.1",
    "helmet": "^4.4.1",
    "express-rate-limit": "^6.1.0",
    "morgan": "^1.10.0"
  }
}
```
