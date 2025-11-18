"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dripdrip.pages.dev
Prompt: Write a JavaScript function to monitor $DRIP token transactions and log details about its liquidity and burn percentage using blockchain explorer APIs.
Generated: DETERMINISTIC_53c2dbacc5cbbc73
Batch ID: 20250612_151219
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchainexplorer.com": {
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
 * Monitor $DRIP token transactions and log details about its liquidity and burn percentage.
 * Uses blockchain explorer APIs to fetch transaction details.
 */

const axios = require('axios');

/**
 * Fetches transaction details for the specified token from a blockchain explorer API.
 * @param {string} apiKey - The API key for the blockchain explorer.
 * @param {string} contractAddress - The contract address of the $DRIP token.
 * @param {string} apiUrl - The base URL of the blockchain explorer API.
 * @returns {Promise<Object>} - A promise that resolves to the transaction details.
 */
async function fetchTokenTransactions(apiKey, contractAddress, apiUrl) {
    try {
        const response = await axios.get(`${apiUrl}/tokens/${contractAddress}/transactions`, {
            headers: {
                'Authorization': `Bearer ${apiKey}`
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error fetching token transactions:", error);
        throw new Error('Could not fetch transactions. Please check your API key and contract address.');
    }
}

/**
 * Calculates the liquidity and burn percentage from the transaction data.
 * @param {Array} transactions - The list of transactions for the $DRIP token.
 * @returns {Object} - An object containing liquidity and burn percentage.
 */
function calculateLiquidityAndBurn(transactions) {
    let liquidity = 0;
    let totalSupply = 0;
    let burnedAmount = 0;

    transactions.forEach(transaction => {
        if (transaction.type === 'transfer') {
            totalSupply += transaction.value;
            if (transaction.to === '0x0000000000000000000000000000000000000000') {
                burnedAmount += transaction.value; // Assuming burn transactions go to the zero address
            } else {
                liquidity += transaction.value;
            }
        }
    });

    const burnPercentage = (burnedAmount / totalSupply) * 100 || 0;

    return {
        liquidity,
        burnPercentage: burnPercentage.toFixed(2)
    };
}

/**
 * Monitors the $DRIP token transactions and logs liquidity and burn percentage.
 * @param {string} apiKey - The API key for the blockchain explorer.
 * @param {string} contractAddress - The contract address of the $DRIP token.
 * @param {string} apiUrl - The base URL of the blockchain explorer API.
 */
async function monitorDripToken(apiKey, contractAddress, apiUrl) {
    try {
        const transactions = await fetchTokenTransactions(apiKey, contractAddress, apiUrl);
        const { liquidity, burnPercentage } = calculateLiquidityAndBurn(transactions);

        console.log(`Liquidity: ${liquidity}`);
        console.log(`Burn Percentage: ${burnPercentage}%`);
    } catch (error) {
        console.error("Monitoring failed:", error.message);
    }
}

// Example usage
const API_KEY = 'your_api_key'; // Replace with your blockchain explorer API key
const CONTRACT_ADDRESS = 'your_contract_address'; // Replace with the $DRIP token contract address
const API_URL = 'https://api.blockchainexplorer.com'; // Replace with the appropriate API URL

monitorDripToken(API_KEY, CONTRACT_ADDRESS, API_URL);
```
