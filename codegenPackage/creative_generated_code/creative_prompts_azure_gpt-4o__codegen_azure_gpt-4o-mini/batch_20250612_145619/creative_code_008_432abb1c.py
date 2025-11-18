"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Explain how to use Infura or Alchemy to connect to the Ethereum network for a pledge system dApp.
Generated: DETERMINISTIC_432abb1c001e21f6
Batch ID: 20250612_145619
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://eth-mainnet.alchemyapi.io/v2/${ALCHEMY_API_KEY}`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://${NETWORK}.infura.io/v3/${INFURA_PROJECT_ID}`;": {
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
// Import the necessary libraries
const { ethers } = require('ethers');

// Define the Infura or Alchemy project ID and the desired network
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const ALCHEMY_API_KEY = 'YOUR_ALCHEMY_API_KEY'; // Replace with your Alchemy API key
const NETWORK = 'mainnet'; // Change to 'rinkeby' or 'ropsten' for test networks

// Choose the provider URL based on the service you're using
const providerUrl = `https://${NETWORK}.infura.io/v3/${INFURA_PROJECT_ID}`; // For Infura
// const providerUrl = `https://eth-mainnet.alchemyapi.io/v2/${ALCHEMY_API_KEY}`; // For Alchemy

// Create a new provider instance
const provider = new ethers.providers.JsonRpcProvider(providerUrl);

/**
 * Connects to the Ethereum network and retrieves the current block number.
 * @returns {Promise<number>} The current block number on the Ethereum network.
 */
async function getCurrentBlockNumber() {
    try {
        const blockNumber = await provider.getBlockNumber();
        return blockNumber;
    } catch (error) {
        console.error('Error fetching the current block number:', error);
        throw new Error('Failed to fetch the current block number.');
    }
}

/**
 * Main function to initialize the connection and log the current block number.
 */
async function main() {
    try {
        console.log('Connecting to Ethereum network...');
        const blockNumber = await getCurrentBlockNumber();
        console.log(`Current block number: ${blockNumber}`);
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Execute the main function
main();
```
