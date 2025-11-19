"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.epizy.com
Prompt: Generate a code snippet to set up a Node.js application hosted on iFastNet with unlimited bandwidth.
Generated: DETERMINISTIC_d4bbc7a212b3e564
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Web framework for Node.js
const path = require('path'); // Module to handle file paths
const fs = require('fs'); // Module for filesystem interactions

// Initialize the Express app
const app = express();

// Middleware to parse JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from the 'public' directory
const staticDir = path.join(__dirname, 'public');
app.use(express.static(staticDir));

// Define a basic route
app.get('/', (req, res) => {
  res.send('Welcome to your Node.js app hosted on iFastNet with unlimited bandwidth!');
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err.message); // Log error to the console
  res.status(err.status || 500).json({ error: 'Internal Server Error' }); // Send generic error response
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Ensure that all necessary environment variables exist for production
if (!process.env.PORT) {
  console.warn('Warning: PORT environment variable is not set. Defaulting to port 3000.');
}

// Create a 'public' directory if it doesn't exist (useful for deployment on iFastNet)
if (!fs.existsSync(staticDir)) {
  fs.mkdirSync(staticDir);
  console.log('Created "public" directory for serving static files.');
}

// Export the app instance (useful for testing or extending functionality later)
module.exports = app;
```
