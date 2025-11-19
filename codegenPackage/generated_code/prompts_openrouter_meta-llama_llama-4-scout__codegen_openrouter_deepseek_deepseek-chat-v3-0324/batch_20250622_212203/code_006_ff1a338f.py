"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: "Create a simple Node.js server to serve static files for a web application, potentially similar to Rarecrew’s setup."
Generated: DETERMINISTIC_ff1a338f638c7799
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const path = require('path');
const fs = require('fs');
const morgan = require('morgan');
const helmet = require('helmet');

// Initialize express app
const app = express();

// Security middleware
app.use(helmet());

// Logging middleware
app.use(morgan('combined'));

// Set the static files directory
const staticDir = path.join(__dirname, 'public');

// Check if static directory exists
if (!fs.existsSync(staticDir)) {
  console.error(`Static directory not found: ${staticDir}`);
  process.exit(1);
}

// Serve static files
app.use(express.static(staticDir, {
  dotfiles: 'ignore',
  etag: true,
  extensions: ['html', 'htm'],
  fallthrough: true,
  immutable: false,
  index: 'index.html',
  maxAge: '1d',
  redirect: true
}));

// Handle 404
app.use((req, res) => {
  res.status(404).sendFile(path.join(staticDir, '404.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Internal Server Error');
});

// Set port and start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Handle process termination
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully.');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully.');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});
```
