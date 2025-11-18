"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloud-eth.cc
Prompt: Generate code to connect to a cloud-hosted Ethereum node and fetch the latest block details using Web3.js.
Generated: DETERMINISTIC_078606ea9bb5bfac
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

/**
 * Connects to a cloud-hosted Ethereum node and fetches the latest block details.
 * 
 * @async
 * @function fetchLatestBlock
 * @param {string} nodeUrl - The URL of the cloud-hosted Ethereum node.
 * @returns {Promise<Object>} - The latest block details.
 * @throws {Error} - Throws an error if unable to connect or fetch data.
 */
async function fetchLatestBlock(nodeUrl) {
    try {
        // Initialize web3 instance with the provided node URL
        const web3 = new Web3(new Web3.providers.HttpProvider(nodeUrl));

        // Fetch the latest block number
        const latestBlockNumber = await web3.eth.getBlockNumber();

        // Fetch the latest block details
        const latestBlock = await web3.eth.getBlock(latestBlockNumber);

        return latestBlock;
    } catch (error) {
        // Handle errors such as connection issues and data fetching errors
        console.error('Error fetching the latest block:', error.message);
        throw new Error('Unable to fetch the latest block details from the Ethereum node.');
    }
}

// Example usage:
// Replace 'YOUR_CLOUD_ETHEREUM_NODE_URL' with your actual Ethereum node URL
const nodeUrl = 'YOUR_CLOUD_ETHEREUM_NODE_URL';

fetchLatestBlock(nodeUrl)
    .then((block) => {
        console.log('Latest Block Details:', block);
    })
    .catch((error) => {
        console.error('Error:', error.message);
    });
```
