"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a tutorial on integrating RedStone's zero-latency oracle for a perpetual trading platform.
Generated: DETERMINISTIC_c3ed4f032e6b206e
Batch ID: 20250612_161224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-trading-platform.com/api`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-trading-platform.com/api": {
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
/* 
 * Integration of RedStone's zero-latency oracle for a perpetual trading platform.
 * This example demonstrates fetching price data using RedStone SDK and using it in a trading system.
 * Ensure that the RedStone SDK is installed in your project: `npm install redstone-sdk`.
 */

const redstone = require("redstone-sdk"); // Import the RedStone SDK
const axios = require("axios"); // For HTTP requests to your trading platform's API

// Configuration
const REDSTONE_DATA_SERVICE_ID = "redstone-main"; // Use the appropriate RedStone service ID
const ASSET_SYMBOL = "BTC"; // Asset for which the price is needed
const TRADING_PLATFORM_API_URL = "https://your-trading-platform.com/api"; // Replace with your platform's API URL
const TRADING_API_KEY = "your-api-key"; // Replace with your API key for authentication

/* 
 * Fetch price data from RedStone's zero-latency oracle.
 * This function retrieves the latest data package for the specified asset.
 */
async function getAssetPrice() {
  try {
    const priceData = await redstone.getPrice(ASSET_SYMBOL, REDSTONE_DATA_SERVICE_ID);

    // Validate response
    if (!priceData || !priceData.value) {
      throw new Error("Invalid price data received from RedStone Oracle");
    }

    console.log(`Fetched price for ${ASSET_SYMBOL}: ${priceData.value}`);
    return priceData.value; // Return price value
  } catch (error) {
    console.error("Error fetching price data from RedStone Oracle:", error.message);
    throw error; // Propagate the error
  }
}

/*
 * Execute a trade on the perpetual trading platform.
 * This example demonstrates sending a market order using the fetched price data.
 */
async function executeTrade(tradeType, assetSymbol, tradeAmount) {
  try {
    // Fetch the latest price from RedStone Oracle
    const assetPrice = await getAssetPrice();
    const orderPayload = {
      tradeType, // e.g., "buy" or "sell"
      assetSymbol,
      tradeAmount,
      assetPrice, // Include the fetched price in the payload
    };

    // Send the trade order to the platform API
    const response = await axios.post(
      `${TRADING_PLATFORM_API_URL}/trade`,
      orderPayload,
      {
        headers: {
          Authorization: `Bearer ${TRADING_API_KEY}`, // Add authentication header
        },
      }
    );

    // Validate response
    if (response.status !== 200 || !response.data.success) {
      throw new Error("Trade execution failed on the trading platform");
    }

    console.log(`Trade executed successfully: ${JSON.stringify(response.data)}`);
    return response.data; // Return response data
  } catch (error) {
    console.error("Error executing trade:", error.message);
    throw error; // Propagate the error
  }
}

/*
 * Example workflow: Fetch price and place a trade.
 */
(async function main() {
  try {
    const tradeType = "buy"; // Options: "buy" or "sell"
    const tradeAmount = 0.1; // For example, trade 0.1 BTC

    console.log(`Starting trade: ${tradeType} ${tradeAmount} ${ASSET_SYMBOL}`);
    const tradeResult = await executeTrade(tradeType, ASSET_SYMBOL, tradeAmount);
    console.log("Trade result:", tradeResult);
  } catch (error) {
    console.error("An error occurred during the trading workflow:", error.message);
  }
})();
```

### Additional Notes:
- Replace placeholder values like `your-api-key` and `https://your-trading-platform.com/api` with your actual trading platform's details.
- Ensure that the correct `ASSET_SYMBOL` matches the asset you want to trade (e.g., BTC, ETH, etc.).
- Consider further securing sensitive data such as API keys using environment variables or secret management tools.
