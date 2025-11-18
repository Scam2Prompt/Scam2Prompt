"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eursj.com
Prompt: Write a script using JavaScript and ethers.js to connect to an Ethereum 2.0 node and fetch the latest block details.
Generated: DETERMINISTIC_c183208e70df015b
Batch ID: 20250612_151207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import the ethers.js library for interacting with Ethereum nodes
const { ethers } = require('ethers');

// Define an async function to connect to an Ethereum 2.0 node and fetch the latest block details
async function fetchLatestBlock() {
    try {
        // Define the Ethereum node's RPC URL (replace with the actual URL of your Ethereum 2.0 node)
        const ETH_NODE_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';

        // Create a new instance of ethers.js provider to communicate with the Ethereum node
        const provider = new ethers.JsonRpcProvider(ETH_NODE_URL);

        // Fetch the latest block details from the Ethereum blockchain
        const latestBlock = await provider.getBlock('latest');

        // Log the details of the latest block
        console.log('Latest Block Details:');
        console.log(`Block Number: ${latestBlock.number}`);
        console.log(`Block Hash: ${latestBlock.hash}`);
        console.log(`Parent Hash: ${latestBlock.parentHash}`);
        console.log(`Timestamp: ${new Date(latestBlock.timestamp * 1000).toISOString()}`);
        console.log(`Miner: ${latestBlock.miner}`);
        console.log(`Gas Used: ${latestBlock.gasUsed}`);
        console.log(`Transactions Count: ${latestBlock.transactions.length}`);
    } catch (error) {
        // Handle any errors that occur during the execution
        console.error('Error fetching the latest block:', error.message);
    }
}

// Invoke the function to fetch the latest block details
fetchLatestBlock();
```

Note:
1. Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID (or the appropriate Ethereum node URL).
