"""
Generated Code Metadata:
========================
Original URL: https://injective.news
Prompt: "Create a basic example of a decentralized application (dApp) that utilizes Injective's oracle for price feeds."
Generated: DETERMINISTIC_a0bd55c510202bb0
Batch ID: 20250622_205436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import necessary libraries
const Web3 = require('web3');
const InjectiveOracle = require('@injectivelabs/oracle'); // Ensure you have the Injective Oracle SDK installed

// Initialize Web3 and Injective Oracle
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID
const oracle = new InjectiveOracle.Oracle();

// Define the main function to fetch price data
async function fetchPriceData(asset) {
    try {
        // Fetch price data from Injective's oracle
        const priceData = await oracle.getPrice(asset);
        
        // Log the fetched price data
        console.log(`Price of ${asset}:`, priceData);
        
        return priceData;
    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching price data:', error);
        throw new Error('Failed to fetch price data');
    }
}

// Example usage of the fetchPriceData function
(async () => {
    const asset = 'BTC/USD'; // Specify the asset for which you want to fetch the price
    try {
        const price = await fetchPriceData(asset);
        // Further processing can be done with the price data here
    } catch (error) {
        console.error('Error in main execution:', error);
    }
})();
```

### Notes:
- Ensure you have the necessary packages installed by running:
  ```bash
  npm install web3 @injectivelabs/oracle
  ```
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- This code is a basic example and should be expanded with additional features and security measures for production use.
