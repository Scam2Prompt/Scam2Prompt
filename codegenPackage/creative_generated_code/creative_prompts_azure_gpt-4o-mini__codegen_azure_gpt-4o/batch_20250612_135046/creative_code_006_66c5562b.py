"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.io
Prompt: Create a JavaScript function that interacts with the Etherscan API to fetch gas prices and display them in a user-friendly format.
Generated: DETERMINISTIC_66c5562b75c477ac
Batch ID: 20250612_135046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=${apiKey}`;": {
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
 * Function to fetch gas prices from the Etherscan API and display them in a user-friendly format
 * 
 * Requirements:
 * - Requires an Etherscan API key. Replace 'YOUR_ETHERSCAN_API_KEY' with your actual key.
 * - Fetches current gas prices (SafeGasPrice, ProposeGasPrice, FastGasPrice).
 * - Displays the gas prices in the console in a user-friendly format.
 */
const axios = require('axios'); // Ensure axios is installed: `npm install axios`

/**
 * Fetches gas prices from Etherscan API and displays them.
 */
async function fetchAndDisplayGasPrices() {
  const apiKey = 'YOUR_ETHERSCAN_API_KEY'; // Replace with your actual Etherscan API key
  const apiUrl = `https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=${apiKey}`;

  try {
    // Fetch gas prices from Etherscan API
    const response = await axios.get(apiUrl);

    // Check if the response contains valid data
    if (response.data && response.data.status === '1' && response.data.result) {
      const gasPrices = response.data.result;

      // Extract gas price values
      const safeGasPrice = gasPrices.SafeGasPrice; // Recommended safe gas price
      const proposeGasPrice = gasPrices.ProposeGasPrice; // Recommended proposed gas price
      const fastGasPrice = gasPrices.FastGasPrice; // Recommended fast gas price

      // Display gas prices in a user-friendly format
      console.log('Current Gas Prices (in Gwei):');
      console.log(`Safe Gas Price: ${safeGasPrice} Gwei`);
      console.log(`Propose Gas Price: ${proposeGasPrice} Gwei`);
      console.log(`Fast Gas Price: ${fastGasPrice} Gwei`);
    } else {
      console.error('Failed to fetch gas prices. Please check the Etherscan API response.');
    }
  } catch (error) {
    // Handle errors (e.g., network issues or invalid API responses)
    console.error('An error occurred while fetching gas prices:', error.message);
  }
}

// Call the function to fetch and display gas prices
fetchAndDisplayGasPrices();

```

This code requires the `axios` package to make HTTP requests. Install it using `npm install axios` before running the script. Replace `YOUR_ETHERSCAN_API_KEY` with your Etherscan API key.
