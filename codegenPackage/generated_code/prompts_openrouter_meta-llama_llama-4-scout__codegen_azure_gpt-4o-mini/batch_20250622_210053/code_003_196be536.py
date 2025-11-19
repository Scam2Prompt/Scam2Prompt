"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Design a simple use case for RedStone's Core (Pull) oracle model, describing how a dApp can utilize this model for low-latency data updates.
Generated: DETERMINISTIC_196be53681dd15a7
Batch ID: 20250622_210053
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
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
// Import necessary libraries
const { ethers } = require("ethers");
const { RedStoneConsumer } = require("@redstone-finance/ethers");

const REDSTONE_ORACLE_ADDRESS = "0xYourRedStoneOracleAddress"; // Replace with actual RedStone Oracle address
const PROVIDER_URL = "https://your.ethereum.node"; // Replace with your Ethereum node URL

// Initialize provider and signer
const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
const signer = provider.getSigner();

// Create a contract instance for the RedStone oracle
const redStoneOracle = new ethers.Contract(REDSTONE_ORACLE_ADDRESS, RedStoneConsumer.abi, signer);

/**
 * Fetches the latest price data from the RedStone oracle.
 * @param {string} assetSymbol - The symbol of the asset to fetch price for (e.g., "BTC", "ETH").
 * @returns {Promise<number>} - The latest price of the asset.
 */
async function fetchLatestPrice(assetSymbol) {
    try {
        // Fetch price data from the RedStone oracle
        const priceData = await redStoneOracle.getLatestPrice(assetSymbol);
        
        // Extract and return the price
        return ethers.utils.formatUnits(priceData.price, priceData.decimals);
    } catch (error) {
        console.error("Error fetching price data:", error);
        throw new Error("Failed to fetch price data from RedStone oracle.");
    }
}

/**
 * Main function to demonstrate the use of the RedStone oracle.
 */
async function main() {
    const assetSymbol = "BTC"; // Example asset symbol

    try {
        // Fetch the latest price for the specified asset
        const latestPrice = await fetchLatestPrice(assetSymbol);
        console.log(`The latest price of ${assetSymbol} is: $${latestPrice}`);
    } catch (error) {
        console.error("Error in main function:", error);
    }
}

// Execute the main function
main();
```
