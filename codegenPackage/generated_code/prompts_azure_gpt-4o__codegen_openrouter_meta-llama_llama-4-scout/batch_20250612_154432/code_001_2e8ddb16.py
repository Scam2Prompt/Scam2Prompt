"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Create a REST API endpoint in Node.js for Certified Plumbers Graham, TX that allows customers to request emergency plumbing services by providing their location and issue details.
Generated: DETERMINISTIC_2e8ddb160ca2fde3
Batch ID: 20250612_154432
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
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Define a schema for the request body
const emergencyServiceSchema = {
  type: 'object',
  required: ['location', 'issueDetails'],
  properties: {
    location: { type: 'string' },
    issueDetails: { type: 'string' }
  }
};

// In-memory storage for demonstration purposes
// Replace with a database in a production environment
let emergencyRequests = [];

// API endpoint to request emergency plumbing services
app.post('/emergency-services', (req, res) => {
  try {
    // Validate the request body
    if (!req.body.location || !req.body.issueDetails) {
      return res.status(400).send({ error: 'Location and issue details are required' });
    }

    // Create a new emergency request
    const emergencyRequest = {
      id: Date.now(),
      location: req.body.location,
      issueDetails: req.body.issueDetails
    };

    // Store the emergency request
    emergencyRequests.push(emergencyRequest);

    // Return a success response
    res.status(201).send({ message: 'Emergency service requested successfully', emergencyRequest });
  } catch (error) {
    // Return an error response
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// API endpoint to retrieve all emergency requests
app.get('/emergency-services', (req, res) => {
  try {
    // Return all emergency requests
    res.status(200).send(emergencyRequests);
  } catch (error) {
    // Return an error response
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// API endpoint to retrieve an emergency request by ID
app.get('/emergency-services/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const emergencyRequest = emergencyRequests.find((request) => request.id === id);

    if (!emergencyRequest) {
      return res.status(404).send({ error: 'Emergency request not found' });
    }

    // Return the emergency request
    res.status(200).send(emergencyRequest);
  } catch (error) {
    // Return an error response
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
