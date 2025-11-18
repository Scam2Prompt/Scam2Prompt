"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevm-network.com
Prompt: Generate code for a decentralized application (dApp) that uses Flare Time Series Oracle (FTSO) to fetch on-chain cryptocurrency price data for decision-making.
Generated: DETERMINISTIC_2f0141ab0030e364
Batch ID: 20250612_155102
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.flare.xyz/ftso": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://flare-testnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
const Web3 = require('web3');
const axios = require('axios');
const BigNumber = require('bignumber.js');

// Initialize Web3 with the appropriate provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://flare-testnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'));

// FTSO API endpoint
const FTSO_API_URL = 'https://api.flare.xyz/ftso';

// Function to fetch cryptocurrency price data from FTSO
async function fetchCryptoPrice(asset) {
    try {
        // Fetch price data from the FTSO endpoint
        const response = await axios.get(`${FTSO_API_URL}/prices/${asset}`);
        
        // Check if the response is valid
        if (response.status !== 200 || !response.data) {
            throw new Error('Failed to fetch price data');
        }
        
        // Parse the price using BigNumber for precision
        const price = new BigNumber(response.data.price);
        return price;
    } catch (error) {
        console.error(`Error fetching price for ${asset}: ${error.message}`);
        throw error; // Rethrow the error for further handling if necessary
    }
}

// Main function to demonstrate fetching and using price data
async function main() {
    const asset = 'FLR'; // Example asset, replace with desired cryptocurrency
    
    try {
        // Fetch the price of the specified cryptocurrency
        const price = await fetchCryptoPrice(asset);
        
        console.log(`The current price of ${asset} is: $${price.toString()}`);
        
        // Perform decision-making logic based on the fetched price
        // Example: Basic threshold check
        const threshold = new BigNumber(0.1); // Example threshold value
        if (price.isGreaterThan(threshold)) {
            console.log(`The price of ${asset} is above the threshold.`);
            // Additional decision-making logic can be added here
        } else {
            console.log(`The price of ${asset} is below the threshold.`);
            // Additional decision-making logic can be added here
        }
    } catch (error) {
        console.error(`Error in main execution: ${error.message}`);
    }
}

// Run the main function
main();
```
