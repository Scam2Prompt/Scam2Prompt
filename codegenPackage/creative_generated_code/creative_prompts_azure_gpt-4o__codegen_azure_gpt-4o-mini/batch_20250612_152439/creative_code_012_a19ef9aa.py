"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Provide a JavaScript example that uses LavaSDK to send a relay request to the Arbitrum Mainnet RPC and fetch the latest block number.
Generated: DETERMINISTIC_a19ef9aa22434346
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required LavaSDK package
const { Lava } = require('lavacask');

// Define the main function to fetch the latest block number
async function fetchLatestBlockNumber() {
    try {
        // Initialize the LavaSDK with the appropriate configuration
        const lava = new Lava({
            chain: 'Arbitrum', // Specify the chain to interact with
            network: 'mainnet', // Specify the network to use
            apiKey: 'YOUR_API_KEY', // Replace with your Lava API key
        });

        // Prepare the request to get the latest block number
        const request = {
            jsonrpc: '2.0',
            id: 1,
            method: 'eth_blockNumber',
            params: [],
        };

        // Send the relay request to the Arbitrum Mainnet RPC
        const response = await lava.request(request);

        // Check if the response contains a valid result
        if (response && response.result) {
            // Convert the block number from hex to decimal
            const blockNumber = parseInt(response.result, 16);
            console.log(`Latest Block Number: ${blockNumber}`);
        } else {
            console.error('Error fetching block number:', response.error);
        }
    } catch (error) {
        // Handle any errors that occur during the request
        console.error('An error occurred while fetching the latest block number:', error);
    }
}

// Execute the function to fetch the latest block number
fetchLatestBlockNumber();
```

**Note:** Replace `'YOUR_API_KEY'` with your actual Lava API key before running the code.
