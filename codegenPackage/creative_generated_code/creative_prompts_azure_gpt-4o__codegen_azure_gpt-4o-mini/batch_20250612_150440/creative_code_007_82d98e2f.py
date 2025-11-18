"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-web-1342-explore-token-details-sea-2009d5-uniswap.vercel.app
Prompt: Create a function in JavaScript to query token details from Uniswap's blockchain data using the GraphQL API.
Generated: DETERMINISTIC_82d98e2f1bf7351a
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2": {
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
// Import the necessary libraries
const fetch = require('node-fetch');

/**
 * Fetch token details from Uniswap's GraphQL API.
 * 
 * @param {string} tokenAddress - The Ethereum address of the token to query.
 * @returns {Promise<object>} - A promise that resolves to the token details object.
 * @throws {Error} - Throws an error if the API request fails or if the token is not found.
 */
async function fetchTokenDetails(tokenAddress) {
    // Validate the token address format
    if (!/^0x[a-fA-F0-9]{40}$/.test(tokenAddress)) {
        throw new Error('Invalid token address format.');
    }

    // Define the GraphQL query to retrieve token details
    const query = `
    {
        token(id: "${tokenAddress.toLowerCase()}") {
            id
            symbol
            name
            totalSupply
            decimals
            derivedETH
            tradeVolume
            tradeVolumeUSD
        }
    }`;

    // Define the API endpoint for Uniswap's GraphQL API
    const apiUrl = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2';

    try {
        // Send the request to the GraphQL API
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });

        // Check for HTTP errors
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.statusText}`);
        }

        // Parse the JSON response
        const jsonResponse = await response.json();

        // Check if the token was found in the response
        if (jsonResponse.data.token === null) {
            throw new Error('Token not found.');
        }

        // Return the token details
        return jsonResponse.data.token;
    } catch (error) {
        // Handle any errors that occurred during the fetch
        throw new Error(`Failed to fetch token details: ${error.message}`);
    }
}

// Example usage (Uncomment to use)
// fetchTokenDetails('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
//     .then((details) => console.log(details))
//     .catch((error) => console.error(error));
```
