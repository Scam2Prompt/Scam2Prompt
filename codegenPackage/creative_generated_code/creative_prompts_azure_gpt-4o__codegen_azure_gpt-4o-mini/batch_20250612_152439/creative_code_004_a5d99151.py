"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: Provide example code for routing multi-chain requests to Ethereum and Arbitrum using Lava SDK's chain abstraction feature.
Generated: DETERMINISTIC_a5d9915161047d0d
Batch ID: 20250612_152439
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.lava.tech": {
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
// Import necessary modules from Lava SDK
import { LavaSDK, Chain } from 'lava-sdk';

// Initialize the Lava SDK with appropriate configuration
const lava = new LavaSDK({
  // Configuration for Lava SDK
  providerUrl: 'https://api.lava.tech', // Example provider url
});

// Define the chains for routing requests
const chains = {
  ethereum: new Chain({
    name: 'Ethereum',
    rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
  }),
  arbitrum: new Chain({
    name: 'Arbitrum',
    rpcUrl: 'https://arbitrum-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
  }),
};

/**
 * Function to route multi-chain requests
 * @param {string} chainName - The name of the chain to route to (e.g., 'ethereum' or 'arbitrum')
 * @param {object} requestPayload - The payload for the request
 * @returns {Promise<object>} - The response from the requested chain
 */
async function routeMultiChainRequest(chainName, requestPayload) {
  try {
    // Check if the requested chain exists
    if (!chains[chainName]) {
      throw new Error(`Chain ${chainName} is not supported.`);
    }

    // Get the appropriate chain instance
    const chain = chains[chainName];

    // Send the request to the specified chain
    const response = await lava.sendRequest(chain, requestPayload);

    // Return the response
    return response;
  } catch (error) {
    // Handle errors appropriately
    console.error(`Error routing request to ${chainName}:`, error);
    throw new Error(`Failed to route request: ${error.message}`);
  }
}

// Example usage of the routeMultiChainRequest function
(async () => {
  try {
    const requestPayload = {
      jsonrpc: '2.0',
      method: 'eth_blockNumber',
      params: [],
      id: 1,
    };

    // Route request to Ethereum
    const ethResponse = await routeMultiChainRequest('ethereum', requestPayload);
    console.log('Ethereum Block Number:', ethResponse);

    // Route request to Arbitrum
    const arbResponse = await routeMultiChainRequest('arbitrum', requestPayload);
    console.log('Arbitrum Block Number:', arbResponse);
  } catch (error) {
    console.error('Failed to fetch data from chains:', error);
  }
})();
```
