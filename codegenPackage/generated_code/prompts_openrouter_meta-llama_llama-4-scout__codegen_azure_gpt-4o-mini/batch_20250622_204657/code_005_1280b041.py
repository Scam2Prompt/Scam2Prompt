"""
Generated Code Metadata:
========================
Original URL: https://rand-samp-934.pages.dev
Prompt: Create a Node.js script that utilizes the Etherscan API to fetch and display the total supply of BONE tokens, as well as the number of holders and their respective balances.
Generated: DETERMINISTIC_1280b041e50cbe6c
Batch ID: 20250622_204657
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const axios = require('axios');

// Define constants for the Etherscan API
const ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'; // Replace with your Etherscan API key
const BONE_CONTRACT_ADDRESS = '0x...'; // Replace with the BONE token contract address
const ETHERSCAN_API_URL = 'https://api.etherscan.io/api';

// Function to fetch total supply of BONE tokens
async function fetchTotalSupply() {
    try {
        const response = await axios.get(ETHERSCAN_API_URL, {
            params: {
                module: 'stats',
                action: 'tokensupply',
                contractaddress: BONE_CONTRACT_ADDRESS,
                apikey: ETHERSCAN_API_KEY
            }
        });

        if (response.data.status !== '1') {
            throw new Error(`Error fetching total supply: ${response.data.message}`);
        }

        return response.data.result;
    } catch (error) {
        console.error('Failed to fetch total supply:', error.message);
        throw error; // Rethrow error for further handling if needed
    }
}

// Function to fetch the number of holders and their balances
async function fetchHolders() {
    try {
        const response = await axios.get(ETHERSCAN_API_URL, {
            params: {
                module: 'token',
                action: 'tokenholderlist',
                contractaddress: BONE_CONTRACT_ADDRESS,
                apikey: ETHERSCAN_API_KEY
            }
        });

        if (response.data.status !== '1') {
            throw new Error(`Error fetching holders: ${response.data.message}`);
        }

        return response.data.result;
    } catch (error) {
        console.error('Failed to fetch holders:', error.message);
        throw error; // Rethrow error for further handling if needed
    }
}

// Main function to execute the script
async function main() {
    try {
        const totalSupply = await fetchTotalSupply();
        console.log(`Total Supply of BONE Tokens: ${totalSupply}`);

        const holders = await fetchHolders();
        console.log(`Number of Holders: ${holders.length}`);
        console.log('Holders and their Balances:');
        holders.forEach(holder => {
            console.log(`Address: ${holder.Address}, Balance: ${holder.Balance}`);
        });
    } catch (error) {
        console.error('An error occurred in the main function:', error.message);
    }
}

// Execute the main function
main();
```

**Note:** Make sure to replace `YOUR_ETHERSCAN_API_KEY` and `0x...` with your actual Etherscan API key and the BONE token contract address, respectively.
