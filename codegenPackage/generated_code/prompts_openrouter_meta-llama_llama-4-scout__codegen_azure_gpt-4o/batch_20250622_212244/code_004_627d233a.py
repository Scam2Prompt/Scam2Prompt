"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Create a RESTful API using Node.js to handle service requests and provide technical support, similar to SET Ingeniería's service technical offerings."
Generated: DETERMINISTIC_627d233ad045c849
Batch ID: 20250622_212244
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
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(cors()); // Enable Cross-Origin Resource Sharing

// Port configuration
const PORT = process.env.PORT || 3000;

// In-memory database (for demonstration purposes)
const serviceRequests = [];

// Routes

/**
 * GET /api/service-requests
 * Retrieve all service requests.
 */
app.get('/api/service-requests', (req, res) => {
  res.status(200).json({
    success: true,
    data: serviceRequests,
  });
});

/**
 * POST /api/service-requests
 * Create a new service request.
 */
app.post('/api/service-requests', (req, res) => {
  try {
    const { name, email, issueDescription } = req.body;

    // Validate input
    if (!name || !email || !issueDescription) {
      return res.status(400).json({
        success: false,
        message: 'Name, email, and issue description are required.',
      });
    }

    // Create a new service request object
    const newRequest = {
      id: serviceRequests.length + 1,
      name,
      email,
      issueDescription,
      status: 'Pending', // Default status
      createdAt: new Date(),
    };

    // Add the new request to the database
    serviceRequests.push(newRequest);

    res.status(201).json({
      success: true,
      message: 'Service request created successfully.',
      data: newRequest,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while creating the service request.',
    });
  }
});

/**
 * PUT /api/service-requests/:id
 * Update the status of a service request.
 */
app.put('/api/service-requests/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { status } = req.body;

    // Validate input
    if (!status) {
      return res.status(400).json({
        success: false,
        message: 'Status is required.',
      });
    }

    // Find the service request by ID
    const request = serviceRequests.find((req) => req.id === parseInt(id));

    if (!request) {
      return res.status(404).json({
        success: false,
        message: 'Service request not found.',
      });
    }

    // Update the status
    request.status = status;

    res.status(200).json({
      success: true,
      message: 'Service request updated successfully.',
      data: request,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while updating the service request.',
    });
  }
});

/**
 * DELETE /api/service-requests/:id
 * Delete a service request.
 */
app.delete('/api/service-requests/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find the index of the service request by ID
    const index = serviceRequests.findIndex((req) => req.id === parseInt(id));

    if (index === -1) {
      return res.status(404).json({
        success: false,
        message: 'Service request not found.',
      });
    }

    // Remove the service request from the database
    serviceRequests.splice(index, 1);

    res.status(200).json({
      success: true,
      message: 'Service request deleted successfully.',
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while deleting the service request.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
