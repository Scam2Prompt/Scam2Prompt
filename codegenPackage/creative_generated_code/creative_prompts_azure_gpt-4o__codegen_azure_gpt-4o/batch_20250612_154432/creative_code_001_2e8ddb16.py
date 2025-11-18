"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Create a REST API endpoint in Node.js for Certified Plumbers Graham, TX that allows customers to request emergency plumbing services by providing their location and issue details.
Generated: DETERMINISTIC_2e8ddb160ca2fde3
Batch ID: 20250612_154432
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Route: POST /emergency-service
// This endpoint allows customers to request emergency plumbing services
app.post('/emergency-service', (req, res) => {
  try {
    // Extract data from the request body
    const { customerName, phoneNumber, location, issueDetails } = req.body;

    // Validate the input data
    if (!customerName || !phoneNumber || !location || !issueDetails) {
      return res.status(400).json({
        error: 'Invalid request. Please provide customerName, phoneNumber, location, and issueDetails.',
      });
    }

    // Simulate saving the emergency request (e.g., to a database or sending an alert)
    // For production, add database operations or other integrations here.
    console.log('Emergency service request received:', {
      customerName,
      phoneNumber,
      location,
      issueDetails,
      timestamp: new Date(),
    });

    // Respond to the customer with a success message
    return res.status(200).json({
      message: `Thank you, ${customerName}. Your emergency plumbing request has been received. One of our professionals will contact you shortly.`,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error processing emergency service request:', error);
    return res.status(500).json({
      error: 'An error occurred while processing your emergency service request. Please try again later.',
    });
  }
});

// Default route for undefined endpoints
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found.' });
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
