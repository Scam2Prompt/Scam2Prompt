"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanchain-drop.pages.dev
Prompt: Create a dApp that integrates Swan Chain's Multi-Chain Storage solution to store data securely across multiple blockchains.
Generated: DETERMINISTIC_e602736ebcc338ce
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * dApp integrating Swan Chain's Multi-Chain Storage solution to securely store data across multiple blockchains.
 * This example assumes the Swan Chain SDK is available and provides necessary methods for interacting with their storage solution.
 */

// Import required modules and SDK
const SwanChainSDK = require('swan-chain-sdk'); // Hypothetical SDK for Swan Chain
const express = require('express'); // Web framework for dApp server
const bodyParser = require('body-parser'); // Middleware to parse incoming request bodies

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // Parse JSON payloads

// Swan Chain Storage configuration (replace with actual credentials and network details)
const swanChainConfig = {
  apiKey: 'YOUR_API_KEY', // Replace with your Swan Chain API Key
  network: 'mainnet', // Choose 'mainnet' or 'testnet'
};

// Initialize Swan Chain SDK
const swanChainClient = new SwanChainSDK(swanChainConfig);

/**
 * Endpoint to securely store data across multiple blockchains.
 * @route POST /store-data
 */
app.post('/store-data', async (req, res) => {
  try {
    const { data, metadata } = req.body;

    // Input validation
    if (!data || typeof data !== 'string') {
      return res.status(400).json({ error: 'Invalid input: "data" must be a non-empty string.' });
    }

    // Metadata is optional, ensure it's an object if provided
    if (metadata && typeof metadata !== 'object') {
      return res.status(400).json({ error: 'Invalid input: "metadata" must be an object.' });
    }

    // Securely store data using Swan Chain's Multi-Chain Storage solution
    const storageResponse = await swanChainClient.storeData({
      data,
      metadata: metadata || {}, // Default to an empty object if metadata is not provided
    });

    // Respond with success and the storage response info
    res.status(200).json({
      message: 'Data stored successfully.',
      storageDetails: storageResponse,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error storing data:', error);

    if (error.response) {
      // Handle API-specific errors
      res.status(error.response.status).json({ error: error.response.data });
    } else {
      // Handle general errors
      res.status(500).json({ error: 'An internal server error occurred.' });
    }
  }
});

/**
 * Endpoint to retrieve data stored across multiple blockchains.
 * @route GET /retrieve-data/:id
 */
app.get('/retrieve-data/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Input validation
    if (!id || typeof id !== 'string') {
      return res.status(400).json({ error: 'Invalid input: "id" must be a non-empty string.' });
    }

    // Retrieve data using Swan Chain's Multi-Chain Storage solution
    const dataResponse = await swanChainClient.retrieveData({ id });

    // Respond with retrieved data
    res.status(200).json({
      message: 'Data retrieved successfully.',
      dataDetails: dataResponse,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error retrieving data:', error);

    if (error.response) {
      // Handle API-specific errors
      res.status(error.response.status).json({ error: error.response.data });
    } else {
      // Handle general errors
      res.status(500).json({ error: 'An internal server error occurred.' });
    }
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
