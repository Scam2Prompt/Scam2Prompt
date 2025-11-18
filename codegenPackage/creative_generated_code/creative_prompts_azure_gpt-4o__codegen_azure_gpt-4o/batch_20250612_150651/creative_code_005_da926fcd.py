"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Provide a step-by-step guide for integrating MultiTMS into an existing logistics software stack for end-to-end shipment management.
Generated: DETERMINISTIC_da926fcdf2f015f7
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready, clean code for integrating MultiTMS into an existing logistics software stack. This example assumes you're working with Node.js and its ecosystem, specifically focusing on integration with REST APIs, proper error handling, and a modular structure.

```javascript
// File: multiTmsIntegration.js

// Import required modules
const axios = require('axios'); // For making HTTP requests
require('dotenv').config();    // Load environment variables from a .env file
const express = require('express'); // Express for potential API integration within the app

// Step 1: Load configuration (API credentials, base URL) from environment variables
const MULTI_TMS_API_BASE_URL = process.env.MULTI_TMS_API_BASE_URL;
const MULTI_TMS_API_KEY = process.env.MULTI_TMS_API_KEY;

// Validate configuration
if (!MULTI_TMS_API_BASE_URL || !MULTI_TMS_API_KEY) {
  throw new Error('MultiTMS API credentials or base URL are not set. Check your environment variables.');
}

// Step 2: Create a reusable API client for MultiTMS
const multiTmsClient = axios.create({
  baseURL: MULTI_TMS_API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${MULTI_TMS_API_KEY}` // Use API key for authentication
  },
  timeout: 5000, // Set timeout for requests
});

// Helper function to handle API errors consistently
const handleApiError = (error) => {
  if (error.response) {
    // The request was made, server responded with a status code outside 2xx
    console.error('MultiTMS API Error:', error.response.data);
    throw new Error(`API Error: ${error.response.status} - ${error.response.data.message || 'Unknown error'}`);
  } else if (error.request) {
    // The request was made but no response was received
    console.error('MultiTMS API Timeout or Network Error:', error.request);
    throw new Error('Network or Timeout Error: Unable to reach the MultiTMS API.');
  } else {
    // Something happened during request setup
    console.error('Unexpected Error:', error.message);
    throw new Error('Unexpected Error during API call: ' + error.message);
  }
};

// Step 3: Implement core integration functions

/**
 * Fetch available carriers from MultiTMS
 * @returns {Promise<Array>} List of carriers
 */
async function getAvailableCarriers() {
  try {
    const response = await multiTmsClient.get('/carriers');
    return response.data; // Assuming API returns an array of carriers
  } catch (error) {
    handleApiError(error);
  }
}

/**
 * Create a new shipment in MultiTMS
 * @param {Object} shipmentData - Shipment details (e.g., origin, destination, weight)
 * @returns {Promise<Object>} Created shipment data
 */
async function createShipment(shipmentData) {
  try {
    const response = await multiTmsClient.post('/shipments', shipmentData);
    return response.data; // Assuming API returns the created shipment object
  } catch (error) {
    handleApiError(error);
  }
}

/**
 * Track an existing shipment by its ID
 * @param {string} shipmentId - The shipment ID
 * @returns {Promise<Object>} Shipment tracking details
 */
async function trackShipment(shipmentId) {
  try {
    const response = await multiTmsClient.get(`/shipments/${shipmentId}/track`);
    return response.data; // Assuming API returns a tracking object
  } catch (error) {
    handleApiError(error);
  }
}

// Step 4: Expose integration functions for use in the larger software stack
module.exports = {
  getAvailableCarriers,
  createShipment,
  trackShipment,
};

// Usage Example (Comment this out in production)
// (Uncomment to test)
// (async () => {
//   try {
//     const carriers = await getAvailableCarriers();
//     console.log('Available Carriers:', carriers);

//     const shipment = await createShipment({
//       origin: 'New York, NY',
//       destination: 'Los Angeles, CA',
//       weight: 100,
//       dimensions: { length: 50, width: 50, height: 50 },
//       transportMode: 'Air',
//     });
//     console.log('Created Shipment:', shipment);

//     const tracking = await trackShipment(shipment.id);
//     console.log('Shipment Tracking Details:', tracking);
//   } catch (err) {
//     console.error(err.message);
//   }
// })();

// Step 5: Add an optional Express server to expose these functionalities via HTTP API
const app = express();
app.use(express.json());

// Endpoint to get carriers
app.get('/api/carriers', async (req, res) => {
  try {
    const carriers = await getAvailableCarriers();
    res.json(carriers);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Endpoint to create a shipment
app.post('/api/shipments', async (req, res) => {
  try {
    const shipment = await createShipment(req.body);
    res.json(shipment);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Endpoint to track a shipment
app.get('/api/shipments/:id/track', async (req, res) => {
  try {
    const tracking = await trackShipment(req.params.id);
    res.json(tracking);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server (if needed)
if (process.env.NODE_ENV !== 'test') {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
}
```

This code fully integrates with the MultiTMS API, provides reusable functions, and even includes an optional Express API layer for use in a microservices architecture.
