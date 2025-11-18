"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-a.infinityfreeapp.com
Prompt: Generate a Node.js application that can be hosted on a platform with unlimited bandwidth and disk space, such as iFastNet.
Generated: DETERMINISTIC_4bc20b065f70e606
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const path = require('path'); // Utility module for working with file paths
const morgan = require('morgan'); // HTTP request logger middleware
const dotenv = require('dotenv'); // For environment variable configuration

// Initialize environment variables from .env file
dotenv.config();

// Create an instance of the Express application
const app = express();

// Set the port from environment variables or default to 3000
const PORT = process.env.PORT || 3000;

// Middleware for logging HTTP requests
app.use(morgan('combined'));

// Middleware for parsing JSON requests
app.use(express.json());

// Middleware for serving static files (e.g., HTML, CSS, JS files) from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a basic route to verify the server is running
app.get('/', (req, res) => {
  res.send('Welcome to the Node.js application hosted on iFastNet!');
});

// Example API route
app.get('/api/hello', (req, res) => {
  try {
    res.json({ message: 'Hello, world!' });
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error('Error in /api/hello route:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// 404 handler for undefined routes
app.use((req, res, next) => {
  res.status(404).send('404 Not Found');
});

// Global error handler
app.use((err, req, res, next) => {
  console.error('Unexpected error:', err);
  res.status(500).send('Internal Server Error');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes for Deployment:
1. Create a `public` folder in the root directory of your project for static files.
2. Add a `.env` file in the root directory for environment variables (e.g., `PORT=3000`).
3. Install dependencies: `npm install express morgan dotenv`.
4. Host the application on a platform like iFastNet by uploading all files, including `package.json` and `node_modules`. Ensure Node.js is supported.
5. Use a process manager like `pm2` if necessary for scaling and managing the app in production.
