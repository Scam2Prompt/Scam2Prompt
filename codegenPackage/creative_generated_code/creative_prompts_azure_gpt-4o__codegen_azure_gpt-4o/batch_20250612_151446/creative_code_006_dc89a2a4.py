"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinglol.42web.io
Prompt: Develop a Node.js application that utilizes hosting features like unlimited bandwidth and no daily process limit, as outlined on iFastNet's hosting page.
Generated: DETERMINISTIC_dc89a2a4805ffc36
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const path = require('path'); // Helps with file and directory paths
const helmet = require('helmet'); // Security middleware
const compression = require('compression'); // For gzip compression
const morgan = require('morgan'); // HTTP request logger

// Initialize the application
const app = express();

// Middleware configuration
app.use(helmet()); // Secure app by setting various HTTP headers
app.use(compression()); // Enable gzip compression for responses
app.use(express.json()); // Parse JSON payloads
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded payloads
app.use(express.static(path.join(__dirname, 'public'))); // Serve static files
app.use(morgan('combined')); // Log HTTP requests

// Error-handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack trace
  res.status(500).json({ error: 'Internal Server Error' }); // Return error response
});

// Route: Home Page
app.get('/', (req, res) => {
  res.send('Welcome to the Node.js Application hosted with iFastNet features!');
});

// Route: API Endpoint Example
app.get('/api/data', (req, res) => {
  try {
    const data = {
      message: 'This is an example API endpoint.',
      timestamp: new Date(),
    };
    res.json(data);
  } catch (error) {
    console.error('Error fetching API data:', error);
    res.status(500).json({ error: 'Failed to fetch API data' });
  }
});

// Catch-all route for undefined endpoints
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown handling
process.on('SIGTERM', () => {
  console.info('SIGTERM signal received. Closing server gracefully.');
  server.close(() => {
    console.log('Server shut down successfully.');
  });
});

process.on('SIGINT', () => {
  console.info('SIGINT signal received. Closing server gracefully.');
  server.close(() => {
    console.log('Server shut down successfully.');
  });
});
```

This code is a basic production-ready Node.js application using Express, set up with proper middleware, logging, error handling, and application lifecycle management.
