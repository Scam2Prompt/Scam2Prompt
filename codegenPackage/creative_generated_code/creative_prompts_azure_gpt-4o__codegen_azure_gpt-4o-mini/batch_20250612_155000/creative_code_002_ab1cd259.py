"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain.ren
Prompt: Generate code to fetch on-chain transaction data from Ethereum 2.0 using JavaScript.
Generated: DETERMINISTIC_ab1cd259ba5d6d7f
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://beaconcha.in/api/v1/": {
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
// Import necessary libraries
const axios = require('axios');

/**
 * Fetch on-chain transaction data from Ethereum 2.0.
 * 
 * @param {string} transactionHash - The hash of the transaction to fetch.
 * @returns {Promise<Object>} - A promise that resolves to the transaction data.
 * @throws {Error} - Throws an error if the fetch operation fails or if the transaction is not found.
 */
async function fetchTransactionData(transactionHash) {
    // Validate the transaction hash
    if (!transactionHash || typeof transactionHash !== 'string') {
        throw new Error('Invalid transaction hash provided.');
    }

    const baseUrl = 'https://beaconcha.in/api/v1/'; // Beaconcha API for Ethereum 2.0 data
    const endpoint = `transaction/${transactionHash}`; // Endpoint for fetching the transaction

    try {
        // Make the API request to fetch transaction data
        const response = await axios.get(`${baseUrl}${endpoint}`);

        // Check if the response indicates an error or no data found
        if (response.data.status !== 'OK') {
            throw new Error(`Transaction not found or an error occurred: ${response.data.message}`);
        }

        // Return the transaction data
        return response.data.data;
    } catch (error) {
        // Handle errors (network issues, invalid transaction hash, etc.)
        throw new Error(`Failed to fetch transaction data: ${error.message}`);
    }
}

// Example usage
(async () => {
    const transactionHash = 'YOUR_TRANSACTION_HASH_HERE'; // Replace with a valid transaction hash

    try {
        const transactionData = await fetchTransactionData(transactionHash);
        console.log('Transaction Data:', transactionData);
    } catch (error) {
        console.error('Error fetching transaction data:', error.message);
    }
})();
```

### Notes:
- Replace `'YOUR_TRANSACTION_HASH_HERE'` with an actual transaction hash to test the code.
- Ensure that you have the `axios` library installed in your project (`npm install axios`).
- This code follows best practices, is documented, and includes error handling for production readiness.
