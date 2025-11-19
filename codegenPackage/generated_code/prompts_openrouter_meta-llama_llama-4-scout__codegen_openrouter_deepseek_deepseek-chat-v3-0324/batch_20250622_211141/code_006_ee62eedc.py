"""
Generated Code Metadata:
========================
Original URL: https://nft-spark.com
Prompt: Create a simple Web3 service using MetaMask's Delegation Toolkit to manage API keys and endpoints.
Generated: DETERMINISTIC_ee62eedc142d95b4
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const cors = require('cors');
const { Delegation } = require('@delegatable/delegatable.js');
const { ethers } = require('ethers');

// Initialize Express app
const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// In-memory storage for API keys and endpoints (replace with database in production)
const apiKeys = new Map();
const endpoints = new Map();

// Initialize Delegation
const delegation = new Delegation({
  chainId: 1, // Mainnet (change as needed)
  contractAddress: '0x0000000000000000000000000000000000000000', // Replace with your contract address
  provider: ethers.getDefaultProvider('homestead') // Replace with your provider
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

/**
 * Middleware to verify delegation signature
 */
async function verifyDelegation(req, res, next) {
  try {
    const { signature, delegation: delegationData } = req.body;
    
    if (!signature || !delegationData) {
      return res.status(400).json({ error: 'Missing signature or delegation data' });
    }

    const isValid = await delegation.verifyDelegationSignature(
      delegationData,
      signature
    );

    if (!isValid) {
      return res.status(401).json({ error: 'Invalid delegation signature' });
    }

    req.delegationData = delegationData;
    next();
  } catch (error) {
    next(error);
  }
}

/**
 * Route to create a new API key
 */
app.post('/api/keys', verifyDelegation, async (req, res) => {
  try {
    const { delegationData } = req;
    const { name } = req.body;

    if (!name) {
      return res.status(400).json({ error: 'Name is required' });
    }

    const apiKey = ethers.utils.hexlify(ethers.utils.randomBytes(32));
    apiKeys.set(apiKey, {
      name,
      owner: delegationData.delegate,
      createdAt: new Date()
    });

    res.status(201).json({ apiKey });
  } catch (error) {
    next(error);
  }
});

/**
 * Route to get all API keys for the delegator
 */
app.get('/api/keys', verifyDelegation, async (req, res) => {
  try {
    const { delegationData } = req;
    const keys = [];

    apiKeys.forEach((value, key) => {
      if (value.owner === delegationData.delegate) {
        keys.push({ apiKey: key, ...value });
      }
    });

    res.json({ keys });
  } catch (error) {
    next(error);
  }
});

/**
 * Route to delete an API key
 */
app.delete('/api/keys/:apiKey', verifyDelegation, async (req, res) => {
  try {
    const { delegationData } = req;
    const { apiKey } = req.params;

    const keyData = apiKeys.get(apiKey);
    if (!keyData) {
      return res.status(404).json({ error: 'API key not found' });
    }

    if (keyData.owner !== delegationData.delegate) {
      return res.status(403).json({ error: 'Not authorized to delete this API key' });
    }

    apiKeys.delete(apiKey);
    res.status(204).end();
  } catch (error) {
    next(error);
  }
});

/**
 * Route to register an endpoint
 */
app.post('/api/endpoints', verifyDelegation, async (req, res) => {
  try {
    const { delegationData } = req;
    const { url, name } = req.body;

    if (!url || !name) {
      return res.status(400).json({ error: 'URL and name are required' });
    }

    endpoints.set(name, {
      url,
      owner: delegationData.delegate,
      createdAt: new Date()
    });

    res.status(201).json({ name, url });
  } catch (error) {
    next(error);
  }
});

/**
 * Route to get all endpoints
 */
app.get('/api/endpoints', verifyDelegation, async (req, res) => {
  try {
    const { delegationData } = req;
    const endpointList = [];

    endpoints.forEach((value, key) => {
      if (value.owner === delegationData.delegate) {
        endpointList.push({ name: key, ...value });
      }
    });

    res.json({ endpoints: endpointList });
  } catch (error) {
    next(error);
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Web3 service running on port ${port}`);
});

// Export app for testing
module.exports = app;
```
