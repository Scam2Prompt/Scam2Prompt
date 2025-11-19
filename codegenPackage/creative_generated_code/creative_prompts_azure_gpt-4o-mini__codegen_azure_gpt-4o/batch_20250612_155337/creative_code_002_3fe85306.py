"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepbook.online
Prompt: Create an API endpoint in Node.js that handles emergency plumbing requests, including features for logging the type of service needed and customer contact information.
Generated: DETERMINISTIC_3fe853066ff49a11
Batch ID: 20250612_155337
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
const bodyParser = require('body-parser');
const fs = require('fs'); // For logging requests to a file
const path = require('path');

// Initialize the application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define a simple log file for emergency plumbing requests
const logFilePath = path.join(__dirname, 'emergencyRequests.log');

// Utility function to log requests to a file
const logRequestToFile = (data) => {
  const logEntry = `${new Date().toISOString()} | Service: ${data.serviceType}, Name: ${data.customerName}, Contact: ${data.contactInfo}\n`;
  fs.appendFile(logFilePath, logEntry, (err) => {
    if (err) {
      console.error('Failed to log request:', err); // Log error to console
    }
  });
};

// API endpoint to handle emergency plumbing requests
app.post('/api/emergency-plumbing', (req, res) => {
  try {
    // Validate the incoming request body
    const { serviceType, customerName, contactInfo } = req.body;

    // Check that all required fields are present
    if (!serviceType || !customerName || !contactInfo) {
      return res.status(400).json({
        error: 'Missing required fields: serviceType, customerName, contactInfo',
      });
    }

    // Log the request data
    logRequestToFile({ serviceType, customerName, contactInfo });

    // Respond to the client indicating success
    res.status(200).json({
      message: 'Emergency plumbing request received successfully',
      requestDetails: { serviceType, customerName, contactInfo },
    });
  } catch (err) {
    // Handle unexpected errors gracefully
    console.error('Error handling plumbing request:', err);

    res.status(500).json({
      error: 'Internal server error. Please try again later.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
