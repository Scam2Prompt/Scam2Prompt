"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevm-network.com
Prompt: Generate code for a decentralized application (dApp) that uses Flare Time Series Oracle (FTSO) to fetch on-chain cryptocurrency price data for decision-making.
Generated: DETERMINISTIC_2f0141ab0030e364
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://flare-api.flare.network/ext/bc/C/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready code for a decentralized application (dApp) that fetches cryptocurrency price data using Flare Time Series Oracle (FTSO). The code is written in JavaScript (Node.js) and leverages the ethers.js library for interacting with the blockchain.

```javascript
// Import required libraries
const { ethers } = require("ethers");

// Constants
const RPC_URL = "https://flare-api.flare.network/ext/bc/C/rpc"; // Replace with the appropriate RPC endpoint for Flare
const FTSO_CONTRACT_ADDRESS = "0xYourFTSOContractAddress"; // Replace with actual FTSO contract address
const FTSO_ABI = [
  // Minimal ABI of FTSO to fetch price data
  {
    "inputs": [{ "internalType": "string", "name": "_symbol", "type": "string" }],
    "name": "getCurrentPrice",
    "outputs": [{ "internalType": "uint256", "name": "price", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
];

// Initialize provider
const provider = new ethers.JsonRpcProvider(RPC_URL);

// Initialize FTSO contract
const ftsoContract = new ethers.Contract(FTSO_CONTRACT_ADDRESS, FTSO_ABI, provider);

/**
 * Fetch the current price of a cryptocurrency from FTSO.
 * @param {string} symbol - The ticker symbol of the cryptocurrency (e.g., "BTC", "ETH").
 * @returns {Promise<number>} - The current price of the cryptocurrency.
 */
async function fetchCryptoPrice(symbol) {
  try {
    // Validate input
    if (!symbol || typeof symbol !== "string") {
      throw new Error("Invalid symbol. Symbol must be a non-empty string.");
    }

    // Fetch price from FTSO
    const price = await ftsoContract.getCurrentPrice(symbol);

    // Convert price to a readable number (assuming price is returned in wei)
    const readablePrice = ethers.formatUnits(price, 18);

    console.log(`Price of ${symbol}: ${readablePrice}`);
    return Number(readablePrice);
  } catch (error) {
    console.error(`Error fetching price for ${symbol}:`, error.message);
    throw error; // Rethrow the error for upstream handling
  }
}

// Example usage
(async () => {
  try {
    const btcPrice = await fetchCryptoPrice("BTC");
    console.log(`Current BTC Price: ${btcPrice}`);
  } catch (error) {
    console.error("Failed to fetch cryptocurrency price:", error.message);
  }
})();
```

### Key Points:
1. Replace `RPC_URL` and `FTSO_CONTRACT_ADDRESS` with the appropriate values for the Flare blockchain and your specific FTSO contract.
2. This code adheres to best practices in terms of input validation, error handling, and documentation.
3. You can expand the ABI if the FTSO contract includes more functions you wish to use.
