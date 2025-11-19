"""
Generated Code Metadata:
========================
Original URL: https://etherscan.io
Prompt: Create a JavaScript function that interacts with the Etherscan API to fetch gas prices and display them in a user-friendly format.
Generated: DETERMINISTIC_66c5562b75c477ac
Batch ID: 20250612_135046
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
/**
 * Etherscan API Gas Price Fetcher
 * =================================
 * 
 * This module provides a function to fetch gas prices from the Etherscan API
 * and display them in a user-friendly format.
 * 
 * @module EtherscanGasPriceFetcher
 */

const axios = require('axios');

/**
 * Etherscan API endpoint URL
 * @const {string}
 */
const ETHERSCAN_API_URL = 'https://api.etherscan.io/api';

/**
 * API key for Etherscan (replace with your own key)
 * @const {string}
 */
const ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY_HERE';

/**
 * Fetches gas prices from the Etherscan API
 * 
 * @async
 * @function getGasPrices
 * @returns {object} Gas prices in wei
 */
async function getGasPrices() {
  try {
    const response = await axios.get(ETHERSCAN_API_URL, {
      params: {
        module: 'proxy',
        action: 'eth_gasPrice',
        apikey: ETHERSCAN_API_KEY
      }
    });

    if (response.data.result) {
      const gasPrice = response.data.result;
      return {
        gasPrice: gasPrice
      };
    } else {
      throw new Error('Failed to retrieve gas price');
    }
  } catch (error) {
    console.error('Error fetching gas price:', error.message);
    throw error;
  }
}

/**
 * Formats gas prices in wei to a user-friendly format (Gwei)
 * 
 * @function formatGasPrice
 * @param {string} gasPriceInWei Gas price in wei
 * @returns {string} Gas price in Gwei
 */
function formatGasPrice(gasPriceInWei) {
  const gasPriceInGwei = parseInt(gasPriceInWei) / 1e9;
  return `${gasPriceInGwei.toFixed(2)} Gwei`;
}

/**
 * Displays gas prices in a user-friendly format
 * 
 * @async
 * @function displayGasPrices
 */
async function displayGasPrices() {
  try {
    const gasPrices = await getGasPrices();
    const gasPriceInGwei = formatGasPrice(gasPrices.gasPrice);
    console.log(`Current gas price: ${gasPriceInGwei}`);
  } catch (error) {
    console.error('Error displaying gas price:', error.message);
  }
}

// Example usage:
displayGasPrices();
```
