"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcloud.com
Prompt: Provide an example of how to enable JavaScript-based functionality for interacting with Pyth Network's price feed oracles in a web application.
Generated: DETERMINISTIC_0c34c0f039b16c34
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import dependencies
// Assumes you have installed pyth packages using npm: npm install @pythnetwork/client
import { PythHttpClient, getPythClusterApiUrl } from "@pythnetwork/client";

// Define the function to fetch price data from Pyth Network
async function fetchPythPrice(symbol) {
  try {
    // Initialize the Pyth HTTP client
    const cluster = "mainnet"; // Options: "mainnet", "testnet", etc.
    const pythClient = new PythHttpClient(getPythClusterApiUrl(cluster));

    // Fetch the latest price feeds
    const priceFeeds = await pythClient.getData();
    
    // Locate the specific price feed for the requested symbol
    const priceFeed = priceFeeds.find(feed => feed.base.toUpperCase() === symbol.toUpperCase());

    if (!priceFeed) {
      throw new Error(`Price feed for symbol '${symbol}' not found.`);
    }

    // Extract and return the price data
    return {
      price: priceFeed.price,
      confidenceInterval: priceFeed.confidence,
      timestamp: priceFeed.timestamp
    };

  } catch (error) {
    // Handle any errors that occur during the process
    console.error("Error fetching price data from Pyth Network:", error.message);
    throw error; // Re-throw the error for higher-level handling
  }
}

// Example usage
(async () => {
  try {
    const symbol = "BTC/USD"; // Specify the symbol for the price feed (e.g., "BTC/USD")
    const priceData = await fetchPythPrice(symbol);

    console.log(`Price data for ${symbol}:`);
    console.log(`  Price: ${priceData.price}`);
    console.log(`  Confidence Interval: ${priceData.confidenceInterval}`);
    console.log(`  Timestamp: ${new Date(priceData.timestamp * 1000).toISOString()}`);
  } catch (error) {
    console.error("Failed to fetch price data:", error.message);
  }
})();
```

**Notes:**
1. Install the required package `@pythnetwork/client` via npm before running the code.
2. Ensure your application has internet access and is correctly configured for the desired Pyth cluster (e.g., mainnet/testnet).
