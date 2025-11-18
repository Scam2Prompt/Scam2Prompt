"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqep.com
Prompt: Generate code to fetch real-time Ethereum transaction data using a JavaScript-based API suitable for DeFi applications.
Generated: DETERMINISTIC_27e255de4cb2e8db
Batch ID: 20250612_154002
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

# Creative Generated Code:
# ========================

```javascript
// Import Axios for HTTP requests
const axios = require('axios');

// Constants
const ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'; // Replace with your Etherscan API key
const ETHERSCAN_BASE_URL = 'https://api.etherscan.io/api';

/**
 * Fetches real-time Ethereum transaction data for a given wallet address.
 * 
 * @param {string} walletAddress - Ethereum wallet address to fetch transaction data for.
 * @returns {Promise<Object>} - Returns a promise resolving to transaction data.
 */
async function fetchEthereumTransactions(walletAddress) {
  try {
    // Validate wallet address (basic check)
    if (!/^0x[a-fA-F0-9]{40}$/.test(walletAddress)) {
      throw new Error('Invalid Ethereum wallet address provided.');
    }

    // Construct request URL
    const url = `${ETHERSCAN_BASE_URL}?module=account&action=txlist&address=${walletAddress}&startblock=0&endblock=99999999&sort=asc&apikey=${ETHERSCAN_API_KEY}`;

    // Make HTTP request to Etherscan API
    const response = await axios.get(url);

    // Check API response status
    if (response.data.status !== '1') {
      throw new Error(`Etherscan API error: ${response.data.message}`);
    }

    // Return transaction data
    return response.data.result;
  } catch (error) {
    // Log error and rethrow for upstream handling
    console.error(`Error fetching Ethereum transactions: ${error.message}`);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const walletAddress = '0xYourEthereumWalletAddress'; // Replace with a valid Ethereum wallet address
    const transactions = await fetchEthereumTransactions(walletAddress);
    
    console.log('Fetched Ethereum transactions:', transactions);
  } catch (error) {
    console.error('Failed to fetch transactions:', error.message);
  }
})();

```

**Note**: Replace `YOUR_ETHERSCAN_API_KEY` with your actual Etherscan API key and `0xYourEthereumWalletAddress` with a valid wallet address for testing.
