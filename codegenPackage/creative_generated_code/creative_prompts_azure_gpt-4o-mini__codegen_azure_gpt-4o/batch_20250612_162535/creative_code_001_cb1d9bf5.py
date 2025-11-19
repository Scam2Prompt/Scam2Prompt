"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskchain.top
Prompt: Can you provide code examples for handling HTTP errors in a web service using JavaScript?
Generated: DETERMINISTIC_cb1d9bf5fc795d71
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express framework for creating web services

// Initialize the Express app
const app = express();

// Middleware for parsing JSON request bodies
app.use(express.json());

// A sample route to demonstrate HTTP error handling
app.get('/data', (req, res, next) => {
  try {
    // Simulate data retrieval logic
    const data = getDataFromDatabase(); // Hypothetical function

    // If no data is found, throw a 404 error
    if (!data) {
      const error = new Error('Data not found');
      error.statusCode = 404;
      throw error;
    }

    // Respond with the retrieved data
    res.status(200).json({ success: true, data });
  } catch (error) {
    // Pass errors to the error-handling middleware
    next(error);
  }
});

// Error-handling middleware
app.use((err, req, res, next) => {
  // Log the error (production-level apps should log to external systems)
  console.error(err.message);

  // Respond with an appropriate HTTP error status and message
  res.status(err.statusCode || 500).json({
    success: false,
    message: err.message || 'Internal Server Error',
  });
});

// Fallback for undefined routes (404 error)
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Route not found',
  });
});

// Utility function for simulating data retrieval (example only)
function getDataFromDatabase() {
  // Simulated database logic
  const data = null; // Simulate no data found
  return data;
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
