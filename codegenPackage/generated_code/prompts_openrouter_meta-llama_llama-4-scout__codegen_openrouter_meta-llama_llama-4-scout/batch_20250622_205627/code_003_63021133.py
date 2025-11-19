"""
Generated Code Metadata:
========================
Original URL: https://lava2.pages.dev
Prompt: "Describe how to integrate the Lava SDK into a web3 application for data access."
Generated: DETERMINISTIC_63021133f61ef873
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { LavaClient, QueryRequest } = require('@lava-tech/lava-sdk');

// Define a class for Lava SDK integration
class LavaSDKIntegration {
  /**
   * Initialize the LavaClient with the provided API key and chain IDs
   * @param {string} apiKey - The Lava API key
   * @param {string[]} chainIds - The chain IDs to query
   */
  constructor(apiKey, chainIds) {
    this.lavaClient = new LavaClient(apiKey);
    this.chainIds = chainIds;
  }

  /**
   * Query data from the Lava network
   * @param {string} chainId - The chain ID to query
   * @param {string} method - The query method (e.g. 'getBalance')
   * @param {object} params - The query parameters
   * @returns {Promise<object>} The query response
   */
  async queryData(chainId, method, params) {
    try {
      // Create a QueryRequest instance
      const request = new QueryRequest(chainId, method, params);

      // Send the query request to the Lava network
      const response = await this.lavaClient.query(request);

      // Return the query response
      return response;
    } catch (error) {
      // Handle query errors
      console.error(`Error querying data: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get the balance of an address on a specific chain
   * @param {string} chainId - The chain ID to query
   * @param {string} address - The address to query
   * @returns {Promise<object>} The balance response
   */
  async getBalance(chainId, address) {
    // Define the query parameters
    const params = { address };

    // Query the balance data
    return this.queryData(chainId, 'getBalance', params);
  }

  /**
   * Get the transaction history of an address on a specific chain
   * @param {string} chainId - The chain ID to query
   * @param {string} address - The address to query
   * @param {number} limit - The number of transactions to return
   * @returns {Promise<object>} The transaction history response
   */
  async getTransactionHistory(chainId, address, limit) {
    // Define the query parameters
    const params = { address, limit };

    // Query the transaction history data
    return this.queryData(chainId, 'getTransactionHistory', params);
  }
}

// Example usage
async function main() {
  // Define the Lava API key and chain IDs
  const apiKey = 'YOUR_LAVA_API_KEY';
  const chainIds = ['ethereum', 'polygon'];

  // Create a LavaSDKIntegration instance
  const lavaIntegration = new LavaSDKIntegration(apiKey, chainIds);

  // Get the balance of an address on Ethereum
  const balanceResponse = await lavaIntegration.getBalance('ethereum', '0x...address...');
  console.log(`Balance: ${balanceResponse.balance}`);

  // Get the transaction history of an address on Polygon
  const transactionHistoryResponse = await lavaIntegration.getTransactionHistory('polygon', '0x...address...', 10);
  console.log(`Transaction History: ${JSON.stringify(transactionHistoryResponse.transactions)}`);
}

// Run the example usage
main().catch((error) => {
  console.error(`Error: ${error.message}`);
});
```
