"""
Generated Code Metadata:
========================
Original URL: https://lavanet-get.pages.dev
Prompt: Create a JavaScript example using Lava SDK to interact with the Avalanche blockchain and retrieve the latest block details.
Generated: DETERMINISTIC_8f9a999bbca5f097
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the necessary libraries from the Lava SDK
const { Lava } = require('lava-sdk');

// Initialize the Lava SDK with your API key and desired network
const lava = new Lava({
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
    network: 'mainnet' // Specify the network: mainnet, testnet, etc.
});

// Function to retrieve the latest block details from the Avalanche blockchain
async function getLatestBlock() {
    try {
        // Fetch the latest block details
        const latestBlock = await lava.getBlock('latest');

        // Check if the response is valid
        if (!latestBlock) {
            throw new Error('Failed to retrieve the latest block.');
        }

        // Log the latest block details
        console.log('Latest Block Details:', latestBlock);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error retrieving the latest block:', error.message);
    }
}

// Execute the function to get the latest block details
getLatestBlock();
```

Make sure to replace `'YOUR_API_KEY'` with your actual Lava SDK API key before running the code.
