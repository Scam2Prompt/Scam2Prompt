"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: Explain how to utilize the Rangers Protocol Oracle in a dApp and provide a sample code for querying data.
Generated: DETERMINISTIC_101f2b66d0d89939
Batch ID: 20250612_135144
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.rangersprotocol.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const Web3 = require('web3');

// Initialize Web3 instance connected to the Rangers Protocol network
const web3 = new Web3('https://rpc.rangersprotocol.com');

// Define the Rangers Protocol Oracle contract ABI
const oracleABI = [
  {
    "constant": true,
    "inputs": [
      { "name": "_queryId", "type": "bytes32" }
    ],
    "name": "getQueryResult",
    "outputs": [
      { "name": "result", "type": "string" }
    ],
    "type": "function"
  }
];

// Define the Oracle contract address (replace with the actual address)
const oracleAddress = '0xYourOracleContractAddressHere';

// Create a contract instance
const oracleContract = new web3.eth.Contract(oracleABI, oracleAddress);

/**
 * Function to query data from the Rangers Protocol Oracle
 * @param {string} queryId - The unique identifier for the query
 * @returns {Promise<string>} - The result of the query
 */
async function queryOracle(queryId) {
  try {
    // Validate input
    if (!web3.utils.isHexStrict(queryId)) {
      throw new Error('Invalid queryId format. Must be a valid hex string.');
    }

    // Query the Oracle contract
    const result = await oracleContract.methods.getQueryResult(queryId).call();

    // Return the result
    return result;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error querying the Oracle:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Replace with a valid queryId
    const queryId = '0xYourQueryIdHere';

    // Query the Oracle and log the result
    const result = await queryOracle(queryId);
    console.log('Query Result:', result);
  } catch (error) {
    console.error('Failed to query the Oracle:', error.message);
  }
})();
```
