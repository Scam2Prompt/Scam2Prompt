"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqh.com
Prompt: Provide an example of a JavaScript implementation for fetching real-time Ethereum transaction data in a DeFi application.
Generated: DETERMINISTIC_5f7324c67ab2fc63
Batch ID: 20250612_154002
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`;": {
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
const Web3 = require('web3'); // Web3.js for interacting with Ethereum blockchain
const axios = require('axios'); // Axios for making HTTP requests

// Constants
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura Project ID
const INFURA_URL = `https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`; // Infura endpoint for Ethereum Mainnet
const ETHERSCAN_API_KEY = 'your-etherscan-api-key'; // Replace with your Etherscan API key
const ETHERSCAN_API_URL = 'https://api.etherscan.io/api'; // Etherscan API base URL

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Function to fetch the latest block number
async function getLatestBlockNumber() {
  try {
    const blockNumber = await web3.eth.getBlockNumber();
    return blockNumber;
  } catch (error) {
    console.error('Error fetching latest block number:', error);
    throw error;
  }
}

// Function to fetch block data by block number
async function getBlockData(blockNumber) {
  try {
    const blockData = await web3.eth.getBlock(blockNumber, true); // Fetch block data including transactions
    return blockData;
  } catch (error) {
    console.error(`Error fetching block data for block ${blockNumber}:`, error);
    throw error;
  }
}

// Function to fetch transaction details using Etherscan API
async function getTransactionDetails(txHash) {
  try {
    const response = await axios.get(ETHERSCAN_API_URL, {
      params: {
        module: 'proxy',
        action: 'eth_getTransactionByHash',
        txhash: txHash,
        apikey: ETHERSCAN_API_KEY,
      },
    });

    if (response.data && response.data.result) {
      return response.data.result;
    } else {
      throw new Error('Transaction details not found.');
    }
  } catch (error) {
    console.error(`Error fetching transaction details for hash ${txHash}:`, error);
    throw error;
  }
}

// Main function to fetch real-time Ethereum transaction data
async function fetchRealTimeTransactionData() {
  try {
    // Fetch the latest block number
    const latestBlockNumber = await getLatestBlockNumber();
    console.log(`Latest Block Number: ${latestBlockNumber}`);

    // Fetch the latest block data
    const blockData = await getBlockData(latestBlockNumber);
    console.log(`Block Data for Block ${latestBlockNumber}:`, blockData);

    // Extract transactions from the block
    const transactions = blockData.transactions;
    console.log(`Number of Transactions in Block ${latestBlockNumber}: ${transactions.length}`);

    // Fetch detailed information for each transaction
    for (const transaction of transactions) {
      const transactionDetails = await getTransactionDetails(transaction.hash);
      console.log('Transaction Details:', transactionDetails);
    }
  } catch (error) {
    console.error('Error fetching real-time Ethereum transaction data:', error);
  }
}

// Run the main function
fetchRealTimeTransactionData();
```

---

Note:
- Replace `your-infura-project-id` and `your-etherscan-api-key` with your actual credentials.
- Install required dependencies using `npm install web3 axios` before running the script.
