"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: How can I implement RedStone's modular oracles for LSTs and LRTs in my DeFi application?
Generated: DETERMINISTIC_7ca2c8082518acf5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
const redstone = require("redstone-protocol"); // RedStone Protocol library
const ethers = require("ethers"); // Ethereum library for blockchain interactions

// Configuration for LSTs and LRTs modular oracles
const oracleConfig = {
  LSTs: ["stETH", "rETH", "frxETH"], // List of Liquid Staking Tokens
  LRTs: ["WBTC", "WETH", "DAI"], // List of Liquid Reserve Tokens
  dataServiceId: "redstone-main", // Data service for fetching oracle prices
  requestTimeoutMs: 10000, // Timeout for fetching data
};

// Define Oracle class
class ModularOracle {
  constructor(provider) {
    this.provider = provider; // Ethereum provider instance
    this.oracle = new redstone.default.RedstoneAPI({
      dataServiceId: oracleConfig.dataServiceId,
      provider: this.provider,
    });
  }

  /**
   * Fetch prices for given tokens.
   * @param {string[]} tokens - List of token symbols.
   * @returns {Promise<Object>} - Prices indexed by token symbols.
   */
  async fetchPrices(tokens) {
    if (!Array.isArray(tokens) || tokens.length === 0) {
      throw new Error("Invalid tokens list provided.");
    }

    try {
      const prices = await this.oracle.getLatestPrices({
        symbols: tokens,
      });
      if (!prices || Object.keys(prices).length === 0) {
        throw new Error("Failed to fetch prices. No data returned.");
      }
      return prices;
    } catch (error) {
      console.error("Error fetching prices from RedStone:", error);
      throw new Error("Unable to fetch token prices. Please try again later.");
    }
  }

  /**
   * Fetch and return prices for LSTs (Liquid Staking Tokens).
   * @returns {Promise<Object>} - Prices indexed by LST symbols.
   */
  async fetchLSTPrices() {
    return await this.fetchPrices(oracleConfig.LSTs);
  }

  /**
   * Fetch and return prices for LRTs (Liquid Reserve Tokens).
   * @returns {Promise<Object>} - Prices indexed by LRT symbols.
   */
  async fetchLRTPrices() {
    return await this.fetchPrices(oracleConfig.LRTs);
  }
}

// Example usage (replace with your own Ethereum provider)
(async () => {
  const provider = new ethers.providers.JsonRpcProvider("<YOUR_RPC_URL>"); // Replace with Ethereum node RPC URL

  // Initialize ModularOracle
  const modularOracle = new ModularOracle(provider);

  try {
    // Fetch prices for LSTs
    console.log("Fetching LST prices...");
    const lstPrices = await modularOracle.fetchLSTPrices();
    console.log("LST Prices:", lstPrices);

    // Fetch prices for LRTs
    console.log("Fetching LRT prices...");
    const lrtPrices = await modularOracle.fetchLRTPrices();
    console.log("LRT Prices:", lrtPrices);
  } catch (error) {
    console.error("Error in Oracle operations:", error.message);
  }
})();
```
