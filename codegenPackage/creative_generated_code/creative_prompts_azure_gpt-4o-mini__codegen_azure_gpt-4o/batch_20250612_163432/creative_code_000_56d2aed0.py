"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orderly-network.pages.dev
Prompt: How can I integrate the Orderly SDK to build a customizable trading front-end for my DApp?
Generated: DETERMINISTIC_56d2aed013620c88
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Integration of Orderly SDK to build a customizable trading front-end for a DApp.
 * This code demonstrates how to initialize the SDK, fetch market data, and handle trades.
 * Ensure that you have installed the Orderly SDK via npm before running this code:
 * `npm install orderly-sdk`
 */

import { Orderly } from 'orderly-sdk';

// Configuration for the Orderly SDK
const orderlyConfig = {
  apiKey: 'YOUR_API_KEY', // Replace with your actual API key
  environment: 'mainnet', // Use 'testnet' for testing environment
};

// Initialize the Orderly SDK
let orderlyClient;
try {
  orderlyClient = new Orderly(orderlyConfig);
  console.log('Orderly SDK initialized successfully.');
} catch (error) {
  console.error('Failed to initialize Orderly SDK:', error.message);
  process.exit(1); // Exit the process if initialization fails
}

/**
 * Fetch available markets and display them to the user.
 */
async function fetchMarkets() {
  try {
    const markets = await orderlyClient.getMarkets();
    console.log('Available Markets:', markets);
    return markets;
  } catch (error) {
    console.error('Failed to fetch markets:', error.message);
    throw error;
  }
}

/**
 * Place a trade (buy or sell) on a specified market.
 * @param {string} market - The market identifier (e.g., 'BTC-USDT').
 * @param {string} side - The side of trade ('buy' or 'sell').
 * @param {number} price - The price at which to trade.
 * @param {number} amount - The amount to trade.
 */
async function placeTrade(market, side, price, amount) {
  try {
    const tradeResult = await orderlyClient.placeOrder({
      market,
      side,
      price,
      amount,
    });
    console.log('Trade executed successfully:', tradeResult);
    return tradeResult;
  } catch (error) {
    console.error('Failed to execute trade:', error.message);
    throw error;
  }
}

/**
 * Main function to build the trading front-end logic.
 */
async function main() {
  try {
    console.log('Fetching markets...');
    const markets = await fetchMarkets();

    // Example: Choose the first market in the list
    const selectedMarket = markets[0]?.marketSymbol || 'BTC-USDT';

    console.log(`Selected Market: ${selectedMarket}`);

    // Example: Place a trade on the selected market
    const side = 'buy'; // Trade side: 'buy' or 'sell'
    const price = 50000; // Example price
    const amount = 1; // Example amount

    console.log(`Placing a trade on market ${selectedMarket}...`);
    await placeTrade(selectedMarket, side, price, amount);

    console.log('Trading operation completed.');
  } catch (error) {
    console.error('An error occurred in the trading operation:', error.message);
  }
}

// Execute the main function
main();
```

### Notes:
1. Ensure that you replace `'YOUR_API_KEY'` with a valid API key obtained from the Orderly platform.
2. The SDK may have updates or changes in API methods, so verify the documentation of the Orderly SDK for the latest details.
3. This code demonstrates the core functionality; you might want to expand upon it with features like user authentication, live market updates, or more advanced error handling for production use.
