"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compound-v2.site
Prompt: What are the best practices for setting up a web server to avoid default pages like the one at https://compound-v2.site?
Generated: DETERMINISTIC_7f413e11d1b5ff89
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation for setting up a web server in Node.js using the Express framework, with best practices to avoid default pages and ensure proper configuration.

```javascript
// Import required modules
const express = require('express');
const helmet = require('helmet'); // Security middleware
const path = require('path');

// Initialize the Express application
const app = express();

// Port configuration (use environment variables for production)
const PORT = process.env.PORT || 3000;

// Apply middleware for security best practices
app.use(helmet()); // Helps secure the app by setting various HTTP headers

// Serve static files (if needed) from a designated directory
const staticDir = path.join(__dirname, 'public');
app.use(express.static(staticDir));

// Disable default error messages for static files
app.use((req, res, next) => {
  res.setHeader('X-Powered-By', 'Custom-Web-Server'); // Hide Express default header
  next(); // Proceed to the next middleware
});

// Custom 404 page for undefined routes
app.use((req, res, next) => {
  res.status(404).send('Page Not Found'); // Send a custom 404 error message
});

// Error handling middleware for production
app.use((err, req, res, next) => {
  console.error('Server error:', err.stack); // Log detailed error (only visible in logs)
  res.status(500).send('Internal Server Error'); // Send a generic error message
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Key Features:
1. **Helmet for Security**: Secures the app by setting various HTTP headers.
2. **Custom 404 Handling**: Ensures no default pages are exposed by crafting a custom error response.
3. **Error Middleware**: Provides robust error handling for unexpected server issues.
4. **Static Directory**: Configured to serve static files from a specific folder (`public`).
5. **Environment Variables**: Uses `process.env.PORT`, following best practices for flexible deployment.
