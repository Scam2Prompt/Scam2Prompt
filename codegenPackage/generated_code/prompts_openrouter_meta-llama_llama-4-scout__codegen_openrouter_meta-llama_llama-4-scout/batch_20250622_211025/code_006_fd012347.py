"""
Generated Code Metadata:
========================
Original URL: https://blueswhale.pages.dev
Prompt: Write a Node.js script to interact with the Bluwhale API and retrieve wallet insights and profiling data for a given set of wallet addresses.
Generated: DETERMINISTIC_fd012347002f3230
Batch ID: 20250622_211025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Bluwhale API Client for Node.js
 * 
 * This script interacts with the Bluwhale API to retrieve wallet insights and profiling data.
 * 
 * @author [Your Name]
 */

// Import required libraries
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

/**
 * Bluwhale API Client class
 */
class BluwhaleClient {
  /**
   * Constructor
   * 
   * @param {string} apiKey - Bluwhale API key
   * @param {string} apiUrl - Bluwhale API URL
   */
  constructor(apiKey, apiUrl) {
    this.apiKey = apiKey;
    this.apiUrl = apiUrl;
  }

  /**
   * Get wallet insights for a given set of wallet addresses
   * 
   * @param {string[]} walletAddresses - Array of wallet addresses
   * @returns {Promise<object>} Wallet insights data
   */
  async getWalletInsights(walletAddresses) {
    try {
      const response = await axios.post(`${this.apiUrl}/wallet/insights`, {
        wallet_addresses: walletAddresses,
      }, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
        },
      });

      return response.data;
    } catch (error) {
      throw new Error(`Failed to retrieve wallet insights: ${error.message}`);
    }
  }

  /**
   * Get wallet profiling data for a given set of wallet addresses
   * 
   * @param {string[]} walletAddresses - Array of wallet addresses
   * @returns {Promise<object>} Wallet profiling data
   */
  async getWalletProfiling(walletAddresses) {
    try {
      const response = await axios.post(`${this.apiUrl}/wallet/profiling`, {
        wallet_addresses: walletAddresses,
      }, {
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
        },
      });

      return response.data;
    } catch (error) {
      throw new Error(`Failed to retrieve wallet profiling data: ${error.message}`);
    }
  }
}

// Main function
async function main() {
  // Bluwhale API credentials
  const apiKey = process.env.BLUWHALE_API_KEY;
  const apiUrl = process.env.BLUWHALE_API_URL;

  if (!apiKey || !apiUrl) {
    throw new Error('Bluwhale API credentials are missing');
  }

  // Create Bluwhale API client
  const client = new BluwhaleClient(apiKey, apiUrl);

  // Example wallet addresses
  const walletAddresses = ['0x1234567890abcdef', '0x9876543210fedcba'];

  try {
    // Get wallet insights
    const walletInsights = await client.getWalletInsights(walletAddresses);
    console.log('Wallet Insights:');
    console.log(walletInsights);

    // Get wallet profiling data
    const walletProfiling = await client.getWalletProfiling(walletAddresses);
    console.log('Wallet Profiling:');
    console.log(walletProfiling);
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

// Run main function
main();
```
