"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Create a RESTful API endpoint in Node.js that allows users to submit requests for polygraph tests related to fidelity verification.
Generated: DETERMINISTIC_38db552f4be1f647
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs

// Create an instance of Express
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory storage for polygraph requests (for demonstration purposes)
// In production, this should be replaced with a database
const polygraphRequests = [];

/**
 * POST /polygraph-tests
 * Endpoint to submit a request for a polygraph test
 * Request Body:
 * - clientName: string - Name of the client requesting the test
 * - clientContact: string - Contact information for the client
 * - subjectName: string - Name of the subject to be tested
 * - subjectContact: string - Contact information for the subject
 * - reason: string - Reason for requesting the test
 * Response:
 * - status: string - Status of the operation
 * - requestId: string - Unique ID for the submitted request
 */
app.post('/polygraph-tests', (req, res) => {
  try {
    const { clientName, clientContact, subjectName, subjectContact, reason } = req.body;

    // Validate input data
    if (!clientName || !clientContact || !subjectName || !subjectContact || !reason) {
      return res.status(400).json({
        status: 'error',
        message: 'All fields (clientName, clientContact, subjectName, subjectContact, reason) are required.',
      });
    }

    // Create a new polygraph test request
    const newRequest = {
      requestId: uuidv4(),
      clientName,
      clientContact,
      subjectName,
      subjectContact,
      reason,
      createdAt: new Date(),
    };

    // Save the request to the in-memory storage
    polygraphRequests.push(newRequest);

    // Respond with the unique ID of the created request
    res.status(201).json({
      status: 'success',
      requestId: newRequest.requestId,
      message: 'Polygraph test request created successfully.',
    });
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error('Error creating polygraph test request:', error);
    res.status(500).json({
      status: 'error',
      message: 'An unexpected error occurred. Please try again later.',
    });
  }
});

// Start the server and listen for incoming requests
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

```
