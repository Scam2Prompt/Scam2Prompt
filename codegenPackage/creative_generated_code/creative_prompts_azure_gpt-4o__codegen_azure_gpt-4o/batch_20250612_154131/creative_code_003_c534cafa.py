"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knights-of-fantom.com
Prompt: Provide an example of initializing a Fantom blockchain connection in a JavaScript application using Web3.js.
Generated: DETERMINISTIC_c534cafa1dd0be3f
Batch ID: 20250612_154131
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpcapi.fantom.network": {
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
// Import the Web3 library
const Web3 = require('web3');

// Define the Fantom RPC URL (this example uses the public RPC endpoint)
/**
 * Replace 'https://rpcapi.fantom.network' with your preferred Fantom RPC endpoint.
 * For production, consider using a reliable RPC provider like Alchemy or Infura
 * for better performance and reliability.
 */
const FANTOM_RPC_URL = 'https://rpcapi.fantom.network';

try {
    // Initialize Web3 instance
    /**
     * Create a Web3 instance connected to the Fantom blockchain
     * using the specified RPC endpoint.
     */
    const web3 = new Web3(new Web3.providers.HttpProvider(FANTOM_RPC_URL));

    // Verify connection to the Fantom blockchain
    /**
     * Perform a simple check by retrieving the latest block number.
     * If the connection is successful, this will return a valid integer block number.
     */
    web3.eth.getBlockNumber()
        .then((blockNumber) => {
            console.log(`Successfully connected to Fantom blockchain.`);
            console.log(`Current block number: ${blockNumber}`);
        })
        .catch((error) => {
            console.error(`Error retrieving block number:`, error);
        });
} catch (error) {
    // Handle initialization errors
    console.error(`Failed to initialize Web3 connection:`, error);
}

/**
 * From this point onward, the `web3` instance can be used to interact
 * with the Fantom blockchain, such as querying account balances,
 * sending transactions, interacting with smart contracts, etc.
 */
```
