"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain.tryethernal.com
Prompt: Generate code to enable JavaScript-based integration with Ethernal for tracking Ethereum transactions and blocks.
Generated: DETERMINISTIC_49ed6856c63520cb
Batch ID: 20250612_150018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ethernal.io/v1": {
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
// Import the required libraries
const axios = require('axios');

// Define the Ethernal API base URL
const ETHERNAL_API_URL = 'https://api.ethernal.io/v1';

// Create a class to interact with the Ethernal API
class EthernalAPI {
    constructor(apiKey) {
        this.apiKey = apiKey; // Store the API key for authentication
    }

    // Method to get transaction details by transaction hash
    async getTransaction(hash) {
        try {
            const response = await axios.get(`${ETHERNAL_API_URL}/tx/${hash}`, {
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`
                }
            });
            return response.data; // Return transaction details
        } catch (error) {
            this.handleError(error); // Handle any errors that occur
        }
    }

    // Method to get block details by block number or hash
    async getBlock(identifier) {
        try {
            const response = await axios.get(`${ETHERNAL_API_URL}/block/${identifier}`, {
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`
                }
            });
            return response.data; // Return block details
        } catch (error) {
            this.handleError(error); // Handle any errors that occur
        }
    }

    // Method to handle errors and log them
    handleError(error) {
        if (error.response) {
            // The request was made and the server responded with a status code
            console.error(`Error: ${error.response.status} - ${error.response.data.message}`);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('Error: No response received from Ethernal API');
        } else {
            // Something happened in setting up the request
            console.error(`Error: ${error.message}`);
        }
    }
}

// Example usage of the EthernalAPI class
(async () => {
    const apiKey = 'YOUR_API_KEY_HERE'; // Replace with your Ethernal API key
    const ethernal = new EthernalAPI(apiKey);

    // Track a specific transaction
    const transactionHash = '0x123...'; // Replace with a valid transaction hash
    const transactionDetails = await ethernal.getTransaction(transactionHash);
    console.log('Transaction Details:', transactionDetails);

    // Track a specific block
    const blockIdentifier = '1234567'; // Replace with a valid block number or hash
    const blockDetails = await ethernal.getBlock(blockIdentifier);
    console.log('Block Details:', blockDetails);
})();
```
