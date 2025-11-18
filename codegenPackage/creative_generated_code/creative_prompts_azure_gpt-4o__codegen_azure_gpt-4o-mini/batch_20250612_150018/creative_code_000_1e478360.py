"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain.tryethernal.com
Prompt: Write a JavaScript function to interact with the Ethernal API for querying blockchain data, ensuring compatibility with Ethereum-based networks.
Generated: DETERMINISTIC_1e478360ab24c764
Batch ID: 20250612_150018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ethernal.io/v1/address/${address}/transactions`;": {
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
/**
 * A function to interact with the Ethernal API for querying blockchain data.
 * This function fetches transaction details from a given Ethereum address.
 * 
 * @param {string} address - The Ethereum address to query.
 * @param {string} apiKey - The API key to authenticate with the Ethernal API.
 * @returns {Promise<object>} - A promise that resolves to the transaction details.
 * @throws {Error} - Throws an error if the request fails or if the address is invalid.
 */
async function getEthereumTransactions(address, apiKey) {
    // Validate the Ethereum address format
    if (!/^0x[a-fA-F0-9]{40}$/.test(address)) {
        throw new Error('Invalid Ethereum address format.');
    }

    const apiUrl = `https://api.ethernal.io/v1/address/${address}/transactions`;

    try {
        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            }
        });

        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();
        return data;

    } catch (error) {
        // Log the error to the console for debugging
        console.error('Error fetching data from Ethernal API:', error.message);
        throw new Error('Failed to fetch Ethereum transaction data.');
    }
}

// Example usage (uncomment to use)
// const address = '0xYourEthereumAddress';
// const apiKey = 'yourEthernalApiKey';
// getEthereumTransactions(address, apiKey)
//     .then(data => console.log(data))
//     .catch(error => console.error(error));
```
