"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiairdrop.imweb.me
Prompt: How do I create a maintenance mode feature in a Node.js application that informs users of temporary unavailability?
Generated: DETERMINISTIC_1215f91f4817b6ff
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const app = express();

// Middleware to check maintenance mode status
const maintenanceModeMiddleware = (req, res, next) => {
  // You can toggle this value to enable or disable maintenance mode
  const isMaintenanceMode = true;

  if (isMaintenanceMode) {
    // Respond with a maintenance message and appropriate HTTP status code
    res.status(503).json({
      status: 'error',
      message: 'The application is currently undergoing maintenance. Please try again later.'
    });
  } else {
    // If not in maintenance mode, proceed to the next middleware or route handler
    next();
  }
};

// Apply the maintenance mode middleware globally
app.use(maintenanceModeMiddleware);

// Define routes
app.get('/', (req, res) => {
  res.send('Welcome to the application!');
});

app.get('/status', (req, res) => {
  res.json({
    status: 'success',
    message: 'The application is operational.'
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Graceful error handling for unhandled routes
app.use((req, res) => {
  res.status(404).json({
    status: 'error',
    message: 'Resource not found'
  });
});

// General error handler
app.use((err, req, res, next) => {
  console.error('An unexpected error occurred:', err.message);

  res.status(500).json({
    status: 'error',
    message: 'An unexpected error occurred. Please try again later.'
  });
});
```
