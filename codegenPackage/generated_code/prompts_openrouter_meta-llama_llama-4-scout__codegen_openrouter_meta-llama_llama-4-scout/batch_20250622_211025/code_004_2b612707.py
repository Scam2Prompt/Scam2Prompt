"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Generate a Node.js library to interact with Bluwhale's API for retrieving wallet insights, transaction history, and NFT data, and for sending dynamically priced on-chain messages.
Generated: DETERMINISTIC_2b6127076f77e7f9
Batch ID: 20250622_211025
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bluwhale.com": {
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
 * Bluwhale API Library for Node.js
 * =================================
 * This library provides an interface to interact with Bluwhale's API for retrieving wallet insights,
 * transaction history, and NFT data, and for sending dynamically priced on-chain messages.
 */

const axios = require('axios');

class BluwhaleAPI {
  /**
   * Constructor for BluwhaleAPI
   * @param {string} apiKey - Bluwhale API key
   * @param {string} apiEndpoint - Bluwhale API endpoint
   */
  constructor(apiKey, apiEndpoint = 'https://api.bluwhale.com') {
    this.apiKey = apiKey;
    this.apiEndpoint = apiEndpoint;
  }

  /**
   * Get wallet insights
   * @param {string} walletAddress - Wallet address
   * @returns {Promise<object>} Wallet insights data
   */
  async getWalletInsights(walletAddress) {
    try {
      const response = await axios.get(`${this.apiEndpoint}/wallet/insights`, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        },
        params: {
          wallet_address: walletAddress
        }
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to retrieve wallet insights: ${error.message}`);
    }
  }

  /**
   * Get transaction history
   * @param {string} walletAddress - Wallet address
   * @param {number} [limit=10] - Number of transactions to retrieve
   * @returns {Promise<object>} Transaction history data
   */
  async getTransactionHistory(walletAddress, limit = 10) {
    try {
      const response = await axios.get(`${this.apiEndpoint}/wallet/transactions`, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        },
        params: {
          wallet_address: walletAddress,
          limit: limit
        }
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to retrieve transaction history: ${error.message}`);
    }
  }

  /**
   * Get NFT data
   * @param {string} walletAddress - Wallet address
   * @returns {Promise<object>} NFT data
   */
  async getNFTData(walletAddress) {
    try {
      const response = await axios.get(`${this.apiEndpoint}/wallet/nfts`, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        },
        params: {
          wallet_address: walletAddress
        }
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to retrieve NFT data: ${error.message}`);
    }
  }

  /**
   * Send dynamically priced on-chain message
   * @param {string} walletAddress - Wallet address
   * @param {string} message - Message to send
   * @returns {Promise<object>} Transaction data
   */
  async sendOnChainMessage(walletAddress, message) {
    try {
      const response = await axios.post(`${this.apiEndpoint}/message/send`, {
        wallet_address: walletAddress,
        message: message
      }, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        }
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to send on-chain message: ${error.message}`);
    }
  }
}

module.exports = BluwhaleAPI;
```

```javascript
// Example usage:
const BluwhaleAPI = require('./BluwhaleAPI');

const api = new BluwhaleAPI('YOUR_API_KEY');

async function main() {
  try {
    const walletAddress = '0x...';

    const walletInsights = await api.getWalletInsights(walletAddress);
    console.log(walletInsights);

    const transactionHistory = await api.getTransactionHistory(walletAddress);
    console.log(transactionHistory);

    const nftData = await api.getNFTData(walletAddress);
    console.log(nftData);

    const message = 'Hello, world!';
    const transactionData = await api.sendOnChainMessage(walletAddress, message);
    console.log(transactionData);
  } catch (error) {
    console.error(error);
  }
}

main();
```
