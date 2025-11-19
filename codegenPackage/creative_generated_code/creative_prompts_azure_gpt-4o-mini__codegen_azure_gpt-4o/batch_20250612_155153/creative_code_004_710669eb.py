"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cave.fi
Prompt: How can I notify users about maintenance mode in a web application, similar to the approach used by CAVE?
Generated: DETERMINISTIC_710669ebc4417db2
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation for notifying users about maintenance mode in a web application using middleware in a Node.js application with the Express framework:

```javascript
/**
 * Middleware to notify users about maintenance mode
 * This middleware intercepts incoming requests and checks whether the application is in maintenance mode.
 * If maintenance mode is active, it returns a proper response to the user.
 */

const express = require('express');
const app = express();

// Configuration for maintenance mode
const config = {
  maintenanceMode: true, // Set to `true` to enable maintenance mode
  maintenanceMessage: 'Our application is currently undergoing scheduled maintenance. Please try again later.',
  statusCode: 503, // HTTP status code for service unavailable
};

/**
 * Maintenance mode middleware.
 * If maintenance mode is active, all requests will be intercepted and a response sent to the client.
 */
const maintenanceMiddleware = (req, res, next) => {
  if (config.maintenanceMode) {
    // Send the maintenance message to the client
    res.status(config.statusCode).json({
      success: false,
      message: config.maintenanceMessage,
    });
  } else {
    // Proceed to the next middleware or route handler if maintenance mode is off
    next();
  }
};

// Use the maintenance middleware for all routes
app.use(maintenanceMiddleware);

// Example route for normal operation
app.get('/', (req, res) => {
  res.json({
    success: true,
    message: 'Welcome to the application!',
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('An error occurred:', err);
  res.status(500).json({
    success: false,
    message: 'An internal server error occurred.',
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Key Features:
- **Middleware-Based Approach:** Maintenance mode is implemented as middleware to intercept incoming requests.
- **Configurable:** Maintenance mode can be toggled on/off via the `config` object.
- **HTTP Status Code:** Returns the standard HTTP status code `503` for service unavailable.
- **Error Handling:** Includes a basic error-handling middleware for unexpected server errors.
- **Scalable:** The approach is modular, making it easy to integrate with larger applications.
