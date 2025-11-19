"""
Generated Code Metadata:
========================
Original URL: https://injective.news
Prompt: "Create a basic example of a decentralized application (dApp) that utilizes Injective's oracle for price feeds."
Generated: DETERMINISTIC_a0bd55c510202bb0
Batch ID: 20250622_205436
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oracle.injective.network": {
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
const Web3 = require('web3');
const axios = require('axios');

// Define constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const INJECTIVE_ORACLE_URL = 'https://oracle.injective.network';
const CHAIN_ID = 'injective-1';

// Initialize Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`));

// Define a function to get price feeds from Injective's oracle
async function getPriceFeeds() {
  try {
    // Make a request to Injective's oracle for price feeds
    const response = await axios.get(`${INJECTIVE_ORACLE_URL}/price-feeds`);

    // Check if the response was successful
    if (response.status !== 200) {
      throw new Error(`Failed to retrieve price feeds: ${response.statusText}`);
    }

    // Extract the price feeds from the response
    const priceFeeds = response.data;

    // Return the price feeds
    return priceFeeds;
  } catch (error) {
    // Log and rethrow any errors
    console.error('Error getting price feeds:', error);
    throw error;
  }
}

// Define a function to get a specific price feed from Injective's oracle
async function getPriceFeed(baseAsset, quoteAsset) {
  try {
    // Make a request to Injective's oracle for a specific price feed
    const response = await axios.get(`${INJECTIVE_ORACLE_URL}/price-feeds/${baseAsset}/${quoteAsset}`);

    // Check if the response was successful
    if (response.status !== 200) {
      throw new Error(`Failed to retrieve price feed: ${response.statusText}`);
    }

    // Extract the price feed from the response
    const priceFeed = response.data;

    // Return the price feed
    return priceFeed;
  } catch (error) {
    // Log and rethrow any errors
    console.error('Error getting price feed:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Get all price feeds
    const priceFeeds = await getPriceFeeds();
    console.log('Price Feeds:');
    console.log(priceFeeds);

    // Get a specific price feed
    const baseAsset = 'inj';
    const quoteAsset = 'usdt';
    const priceFeed = await getPriceFeed(baseAsset, quoteAsset);
    console.log(`\nPrice Feed for ${baseAsset}/${quoteAsset}:`);
    console.log(priceFeed);
  } catch (error) {
    // Log any errors
    console.error('Error:', error);
  }
}

// Run the example usage
main();
```
