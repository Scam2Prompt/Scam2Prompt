"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft6.web.app
Prompt: Write a function using Solana's web3.js library to fetch the total supply of $LOYAL tokens and display it on a webpage.
Generated: DETERMINISTIC_e9de062131c7bece
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
const web3 = require('@solana/web3.js'); // Solana web3 library
const fetch = require('node-fetch'); // Node fetch for API requests

// Define the token mint address for $LOYAL
const LOYAL_TOKEN_MINT_ADDRESS = 'YOUR_LOYAL_TOKEN_MINT_ADDRESS_HERE'; // Replace with actual mint address

/**
 * Fetch the total supply of the specified SPL token.
 * @param {string} mintAddress - The token mint address.
 * @returns {Promise<number>} The total supply of the token.
 */
async function fetchTotalSupply(mintAddress) {
    try {
        // Create a new connection to the Solana cluster
        const connection = new web3.Connection(web3.clusterApiUrl('mainnet-beta'), 'confirmed');

        // Get the token supply using the mint address
        const mintPublicKey = new web3.PublicKey(mintAddress);
        const mintInfo = await connection.getParsedAccountInfo(mintPublicKey);
        
        // Check if mintInfo is found
        if (!mintInfo.value) {
            throw new Error('Token mint address not found.');
        }

        // Extract total supply from mintInfo
        const totalSupply = mintInfo.value.data.parsed.info.supply;

        // Return total supply as a number
        return Number(totalSupply);
    } catch (error) {
        console.error('Error fetching total supply:', error);
        throw error; // Re-throw the error for further handling
    }
}

/**
 * Display the total supply of $LOYAL tokens on the webpage.
 */
async function displayTotalSupply() {
    try {
        const totalSupply = await fetchTotalSupply(LOYAL_TOKEN_MINT_ADDRESS);
        
        // Display total supply on the webpage
        document.getElementById('totalSupply').innerText = `Total Supply of $LOYAL: ${totalSupply}`;
    } catch (error) {
        document.getElementById('totalSupply').innerText = 'Error fetching total supply.';
    }
}

// Execute the function to display total supply when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    displayTotalSupply();
});
```

**Note:** Be sure to replace `'YOUR_LOYAL_TOKEN_MINT_ADDRESS_HERE'` with the actual mint address of the $LOYAL token. The HTML page must have an element with the ID `totalSupply` to display the total supply.
