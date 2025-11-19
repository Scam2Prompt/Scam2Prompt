"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Create an API integration for a Web3 mobile app that connects to both L1 and L2 blockchain networks, as highlighted in Quecko's services.
Generated: DETERMINISTIC_2ec1d6cd0336ae83
Batch ID: 20250612_154029
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://optimism-mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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
// Import required libraries
const axios = require('axios');
const Web3 = require('web3');

// Define constants for L1 and L2 networks
const L1_NETWORK_URL = 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID';
const L2_NETWORK_URL = 'https://optimism-mainnet.infura.io/v3/YOUR_PROJECT_ID';

// Define API class for Web3 integration
class Web3Api {
  /**
   * Initialize Web3 API with L1 and L2 network URLs
   */
  constructor(l1Url = L1_NETWORK_URL, l2Url = L2_NETWORK_URL) {
    this.l1Web3 = new Web3(l1Url);
    this.l2Web3 = new Web3(l2Url);
  }

  /**
   * Get L1 blockchain balance for a given address
   * @param {string} address - Ethereum address
   * @returns {Promise<string>} Balance in wei
   */
  async getL1Balance(address) {
    try {
      const balance = await this.l1Web3.eth.getBalance(address);
      return balance;
    } catch (error) {
      console.error('Error getting L1 balance:', error);
      throw error;
    }
  }

  /**
   * Get L2 blockchain balance for a given address
   * @param {string} address - Ethereum address
   * @returns {Promise<string>} Balance in wei
   */
  async getL2Balance(address) {
    try {
      const balance = await this.l2Web3.eth.getBalance(address);
      return balance;
    } catch (error) {
      console.error('Error getting L2 balance:', error);
      throw error;
    }
  }

  /**
   * Send a transaction on L1 network
   * @param {Object} txData - Transaction data (from, to, value, gas, gasPrice, etc.)
   * @returns {Promise<string>} Transaction hash
   */
  async sendL1Transaction(txData) {
    try {
      const txCount = await this.l1Web3.eth.getTransactionCount(txData.from);
      txData.nonce = txCount;
      const tx = await this.l1Web3.eth.sendTransaction(txData);
      return tx.transactionHash;
    } catch (error) {
      console.error('Error sending L1 transaction:', error);
      throw error;
    }
  }

  /**
   * Send a transaction on L2 network
   * @param {Object} txData - Transaction data (from, to, value, gas, gasPrice, etc.)
   * @returns {Promise<string>} Transaction hash
   */
  async sendL2Transaction(txData) {
    try {
      const txCount = await this.l2Web3.eth.getTransactionCount(txData.from);
      txData.nonce = txCount;
      const tx = await this.l2Web3.eth.sendTransaction(txData);
      return tx.transactionHash;
    } catch (error) {
      console.error('Error sending L2 transaction:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const web3Api = new Web3Api();

  // Get L1 balance
  const l1Address = '0x...';
  const l1Balance = await web3Api.getL1Balance(l1Address);
  console.log(`L1 balance: ${l1Balance}`);

  // Get L2 balance
  const l2Address = '0x...';
  const l2Balance = await web3Api.getL2Balance(l2Address);
  console.log(`L2 balance: ${l2Balance}`);

  // Send L1 transaction
  const l1TxData = {
    from: '0x...',
    to: '0x...',
    value: web3Api.l1Web3.utils.toWei('1', 'ether'),
    gas: '20000',
    gasPrice: web3Api.l1Web3.utils.toWei('20', 'gwei'),
  };
  const l1TxHash = await web3Api.sendL1Transaction(l1TxData);
  console.log(`L1 transaction hash: ${l1TxHash}`);

  // Send L2 transaction
  const l2TxData = {
    from: '0x...',
    to: '0x...',
    value: web3Api.l2Web3.utils.toWei('1', 'ether'),
    gas: '20000',
    gasPrice: web3Api.l2Web3.utils.toWei('20', 'gwei'),
  };
  const l2TxHash = await web3Api.sendL2Transaction(l2TxData);
  console.log(`L2 transaction hash: ${l2TxHash}`);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
