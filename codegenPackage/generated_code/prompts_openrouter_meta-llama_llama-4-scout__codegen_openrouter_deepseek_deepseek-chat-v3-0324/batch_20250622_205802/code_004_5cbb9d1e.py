"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Create a RESTful API using Node.js to handle requests for plumbing services, including drain cleaning, gas line services, and commercial plumbing.
Generated: DETERMINISTIC_5cbb9d1ec86bd302
Batch ID: 20250622_205802
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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration purposes
const servicesDB = {
  drainCleaning: [],
  gasLineServices: [],
  commercialPlumbing: []
};

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

/**
 * @route GET /api/services
 * @desc Get all available services
 * @access Public
 */
app.get('/api/services', (req, res) => {
  try {
    const services = {
      drainCleaning: 'Drain cleaning services',
      gasLineServices: 'Gas line installation and repair',
      commercialPlumbing: 'Commercial plumbing solutions'
    };
    res.status(200).json(services);
  } catch (error) {
    next(error);
  }
});

/**
 * @route POST /api/request-service
 * @desc Create a new service request
 * @access Public
 */
app.post('/api/request-service', (req, res, next) => {
  try {
    const { serviceType, customerName, contactInfo, description } = req.body;

    // Validate required fields
    if (!serviceType || !customerName || !contactInfo) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Validate service type
    const validServices = ['drainCleaning', 'gasLineServices', 'commercialPlumbing'];
    if (!validServices.includes(serviceType)) {
      return res.status(400).json({ error: 'Invalid service type' });
    }

    const newRequest = {
      id: uuidv4(),
      serviceType,
      customerName,
      contactInfo,
      description: description || '',
      status: 'pending',
      createdAt: new Date().toISOString()
    };

    servicesDB[serviceType].push(newRequest);
    res.status(201).json(newRequest);
  } catch (error) {
    next(error);
  }
});

/**
 * @route GET /api/requests/:serviceType
 * @desc Get all requests for a specific service type
 * @access Public
 */
app.get('/api/requests/:serviceType', (req, res, next) => {
  try {
    const { serviceType } = req.params;

    if (!servicesDB[serviceType]) {
      return res.status(404).json({ error: 'Service type not found' });
    }

    res.status(200).json(servicesDB[serviceType]);
  } catch (error) {
    next(error);
  }
});

/**
 * @route GET /api/request/:id
 * @desc Get a specific request by ID
 * @access Public
 */
app.get('/api/request/:id', (req, res, next) => {
  try {
    const { id } = req.params;
    let foundRequest = null;

    // Search through all service types to find the request
    for (const serviceType in servicesDB) {
      foundRequest = servicesDB[serviceType].find(request => request.id === id);
      if (foundRequest) break;
    }

    if (!foundRequest) {
      return res.status(404).json({ error: 'Request not found' });
    }

    res.status(200).json(foundRequest);
  } catch (error) {
    next(error);
  }
});

/**
 * @route PUT /api/request/:id/status
 * @desc Update the status of a service request
 * @access Public
 */
app.put('/api/request/:id/status', (req, res, next) => {
  try {
    const { id } = req.params;
    const { status } = req.body;

    if (!status) {
      return res.status(400).json({ error: 'Status is required' });
    }

    let foundRequest = null;
    let serviceType = null;

    // Find the request and its service type
    for (const st in servicesDB) {
      const index = servicesDB[st].findIndex(request => request.id === id);
      if (index !== -1) {
        serviceType = st;
        foundRequest = servicesDB[st][index];
        break;
      }
    }

    if (!foundRequest) {
      return res.status(404).json({ error: 'Request not found' });
    }

    foundRequest.status = status;
    res.status(200).json(foundRequest);
  } catch (error) {
    next(error);
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
