"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Create an API endpoint in Node.js that serves a maintenance status message, similar to the one on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_f6987a4a19f4a7cd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Express framework for building the API
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Define the port the server will listen on (default to 3000 if not specified in .env)
const PORT = process.env.PORT || 3000;

// Maintenance status message
const maintenanceMessage = {
  status: "Maintenance",
  message: "Our website is currently undergoing maintenance. Please check back later.",
  timestamp: new Date().toISOString(),
};

// API endpoint to serve the maintenance status
app.get('/api/maintenance-status', (req, res) => {
  try {
    // Send the maintenance status message as a JSON response
    res.status(200).json(maintenanceMessage);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error serving maintenance status:', error);
    res.status(500).json({
      status: "Error",
      message: "An unexpected error occurred. Please try again later.",
    });
  }
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
