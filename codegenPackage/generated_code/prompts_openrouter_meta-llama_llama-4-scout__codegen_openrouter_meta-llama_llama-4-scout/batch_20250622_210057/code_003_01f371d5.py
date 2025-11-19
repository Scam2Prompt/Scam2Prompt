"""
Generated Code Metadata:
========================
Original URL: https://redstone-fi.pages.dev
Prompt: Develop a Node.js script to fetch data from RedStone's oracle services, specifically using the RedStone Classic (Push) model for a dApp on Polygon.
Generated: DETERMINISTIC_01f371d5c56cd840
Batch ID: 20250622_210057
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://classic.redstone.finance/oracle": {
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
const { ethers } = require('ethers');

// Define constants
const ORACLE_URL = 'https://classic.redstone.finance/oracle';
const CHAIN_ID = 137; // Polygon mainnet chain ID
const TOKEN_SYMBOLS = ['MATIC', 'ETH']; // Example token symbols

// Define a function to fetch data from RedStone's oracle services
async function fetchOracleData() {
  try {
    // Construct the API request
    const response = await axios.get(ORACLE_URL, {
      params: {
        chainId: CHAIN_ID,
        symbols: TOKEN_SYMBOLS.join(','),
      },
    });

    // Check if the response was successful
    if (response.status !== 200) {
      throw new Error(`Failed to fetch oracle data: ${response.statusText}`);
    }

    // Extract and return the oracle data
    return response.data;
  } catch (error) {
    console.error('Error fetching oracle data:', error.message);
    throw error;
  }
}

// Define a function to get the latest block number
async function getLatestBlockNumber(provider) {
  try {
    // Get the latest block number
    const blockNumber = await provider.getBlockNumber();
    return blockNumber;
  } catch (error) {
    console.error('Error getting latest block number:', error.message);
    throw error;
  }
}

// Define a function to main function
async function main() {
  try {
    // Initialize the Polygon provider
    const provider = new ethers.providers.JsonRpcProvider('https://polygon-rpc.com/');

    // Fetch oracle data
    const oracleData = await fetchOracleData();
    console.log('Oracle Data:', oracleData);

    // Get the latest block number
    const latestBlockNumber = await getLatestBlockNumber(provider);
    console.log('Latest Block Number:', latestBlockNumber);
  } catch (error) {
    console.error('Error in main function:', error.message);
    process.exit(1);
  }
}

// Run the main function
main();
```
