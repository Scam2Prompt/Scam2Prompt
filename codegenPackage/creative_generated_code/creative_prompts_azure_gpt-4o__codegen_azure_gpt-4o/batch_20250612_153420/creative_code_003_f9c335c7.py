"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3nodedapp.pages.dev
Prompt: Create a function using ethers.js to retrieve and display the trading volume and floor price of NFTs, referencing collections like "CryptoPunks" and "Moonbirds" from SearchDapps.xyz.
Generated: DETERMINISTIC_f9c335c77ba83731
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchdapps.xyz/v1": {
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
// Import ethers.js and axios - ethers.js is used for interacting with Ethereum and axios for HTTP requests
const { ethers } = require("ethers");
const axios = require("axios");

/**
 * Function to retrieve and display the trading volume and floor price of NFTs from SearchDapps.xyz.
 * @param {string} collectionName - The name of the NFT collection (e.g., "CryptoPunks", "Moonbirds").
 * @returns {Promise<void>} - Logs the trading volume and floor price of the NFT collection to the console.
 */
async function getNFTMetrics(collectionName) {
  // Validate input
  if (!collectionName || typeof collectionName !== "string") {
    throw new Error("Invalid collection name. Please provide a valid string.");
  }

  try {
    // Base URL for SearchDapps.xyz API
    const baseURL = "https://api.searchdapps.xyz/v1";

    // Construct API endpoint for the specific NFT collection
    const endpoint = `${baseURL}/collections/${collectionName.toLowerCase()}`;

    // Fetch data from SearchDapps.xyz API
    const response = await axios.get(endpoint);

    // Check if the response contains the necessary data
    if (!response.data || !response.data.tradingVolume || !response.data.floorPrice) {
      throw new Error("Unexpected response structure from SearchDapps.xyz API.");
    }

    // Extract trading volume and floor price from API response
    const tradingVolume = response.data.tradingVolume; // Example: "100 ETH"
    const floorPrice = response.data.floorPrice;       // Example: "5 ETH"

    // Log the metrics to the console
    console.log(`Collection: ${collectionName}`);
    console.log(`Trading Volume: ${tradingVolume}`);
    console.log(`Floor Price: ${floorPrice}`);
  } catch (error) {
    // Handle errors and display appropriate messages
    console.error(`Failed to retrieve metrics for collection "${collectionName}".`);
    console.error(`Error: ${error.message}`);
  }
}

// Example usage
(async () => {
  try {
    await getNFTMetrics("CryptoPunks");
    await getNFTMetrics("Moonbirds");
  } catch (error) {
    console.error("An error occurred during execution:", error.message);
  }
})();
```

**Note:** Ensure that you have installed `ethers` and `axios` as dependencies for the project. You can install these libraries via npm:
```bash
npm install ethers axios
```
