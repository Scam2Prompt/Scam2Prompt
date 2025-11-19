"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Generate Node.js code for deploying a web application on a hosting platform that provides modern cPanel and no daily hit limits, as described on the iFastNet hosting page.
Generated: DETERMINISTIC_a41adec4e919e4eb
Batch ID: 20250612_154413
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
const path = require('path');
const helmet = require('helmet');
const morgan = require('morgan');

// Create an Express application
const app = express();

// Set port for the application
const PORT = process.env.PORT || 3000;

// Enable security headers
app.use(helmet());

// Enable logging
app.use(morgan('combined'));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve static files from the 'public' directory with custom options
app.use('/static', express.static(path.join(__dirname, 'public/static'), {
  maxAge: '1y', // Cache for 1 year
}));

// Handle GET requests to the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/index.html'));
});

// Handle errors
app.use((req, res, next) => {
  const error = new Error('Not Found');
  error.status = 404;
  next(error);
});

// Error handler
app.use((error, req, res, next) => {
  console.error(error);
  res.status(error.status || 500);
  res.json({ error: error.message });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});

// Handle termination signals
process.on('SIGTERM', () => {
  console.log('Server stopping...');
  app.close(() => {
    console.log('Server stopped.');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('Server stopping...');
  app.close(() => {
    console.log('Server stopped.');
    process.exit(0);
  });
});

process.on('uncaughtException', (err) => {
  console.error('Uncaught exception:', err);
  process.exit(1);
});
```
