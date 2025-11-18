"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappwalletprotocol.rf.gd
Prompt: Generate Node.js code for setting up a server on a hosting platform that offers modern cPanel and unlimited disk space, as described by iFastNet hosting features.
Generated: DETERMINISTIC_265221a5f96feba1
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const path = require('path');
const fs = require('fs'); // For potential file system operations
require('dotenv').config(); // For environment variable management

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000; // Use environment port or default to 3000

// Middleware for parsing JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from the "public" directory
const publicDirectory = path.join(__dirname, 'public');
app.use(express.static(publicDirectory));

// Root route
app.get('/', (req, res) => {
  res.send('Welcome to the Node.js server hosted on iFastNet!');
});

// Example API route
app.get('/api/example', (req, res) => {
  res.json({ message: 'This is a sample API endpoint' });
});

// 404 Error handler for non-existing routes
app.use((req, res, next) => {
  res.status(404).json({ error: 'Route not found' });
});

// Global error handler for unexpected errors
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack trace
  res.status(500).json({ error: 'An unexpected error occurred' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown to handle termination signals
process.on('SIGTERM', () => {
  console.log('SIGTERM signal received. Shutting down gracefully...');
  process.exit(0);
});

process.on('SIGINT', () => {
  console.log('SIGINT signal received. Shutting down gracefully...');
  process.exit(0);
});

// Notes:
// - This setup assumes Node.js and Express are installed.
// - To deploy on a hosting platform, ensure you upload your `node_modules` or rebuild dependencies after deploying.
// - Use `.env` for sensitive values like API keys or database credentials.
```
