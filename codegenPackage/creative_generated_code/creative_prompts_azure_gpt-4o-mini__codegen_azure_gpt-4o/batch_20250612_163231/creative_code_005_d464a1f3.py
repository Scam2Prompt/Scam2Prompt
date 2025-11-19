"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://08pf.cn
Prompt: How do I set up a notification system for price alerts using the OKX API in a Node.js application?
Generated: DETERMINISTIC_d464a1f31b3846ca
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com": {
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
// Import necessary modules
const axios = require('axios'); // For making HTTP requests
const EventEmitter = require('events'); // For setting up the notification system

// Configuration constants
const API_URL = 'https://www.okx.com'; // Base URL for OKX API
const PRICE_ENDPOINT = '/api/v5/market/ticker'; // Endpoint for market ticker
const SYMBOL = 'BTC-USDT'; // Cryptocurrency pair to monitor
const PRICE_ALERT_THRESHOLD = 30000; // Alert threshold price
const CHECK_INTERVAL_MS = 60000; // Time interval to check price (in ms)

// Initialize an EventEmitter for notifications
const priceAlertEmitter = new EventEmitter();

/**
 * Fetch the latest price for a specific cryptocurrency pair from OKX API.
 * @returns {Promise<number>} The current price of the cryptocurrency pair.
 */
async function fetchCurrentPrice() {
  try {
    const response = await axios.get(`${API_URL}${PRICE_ENDPOINT}`, {
      params: { instId: SYMBOL },
    });

    // Extract the price from the response
    const tickerData = response?.data?.data?.[0];
    if (!tickerData) {
      throw new Error('Failed to fetch ticker data.');
    }

    const currentPrice = parseFloat(tickerData.last);
    return currentPrice;
  } catch (error) {
    // Log error and rethrow for upstream handling
    console.error('Failed to fetch current price:', error.message);
    throw error;
  }
}

/**
 * Checks the current price against the alert threshold and emits a notification if necessary.
 */
async function checkPriceAndNotify() {
  try {
    const currentPrice = await fetchCurrentPrice();

    console.log(`Current price of ${SYMBOL}: $${currentPrice}`);

    // Compare current price with alert threshold
    if (currentPrice >= PRICE_ALERT_THRESHOLD) {
      // Emit an alert notification
      priceAlertEmitter.emit('priceAlert', {
        symbol: SYMBOL,
        price: currentPrice,
        message: `Price alert: ${SYMBOL} has reached $${currentPrice}, exceeding the threshold of $${PRICE_ALERT_THRESHOLD}.`,
      });
    }
  } catch (error) {
    console.error('Error checking price:', error.message);
  }
}

/**
 * Sets up a listener for price alerts and logs the alert message.
 */
function setupNotificationListener() {
  priceAlertEmitter.on('priceAlert', (alert) => {
    console.log('*** PRICE ALERT ***');
    console.log(`Symbol: ${alert.symbol}`);
    console.log(`Price: $${alert.price}`);
    console.log(alert.message);
    console.log('*******************');
  });
}

/**
 * Starts the price monitoring loop.
 */
function startPriceMonitoring() {
  console.log(`Starting price monitoring for ${SYMBOL}...`);
  setupNotificationListener();

  // Check price at regular intervals
  setInterval(checkPriceAndNotify, CHECK_INTERVAL_MS);
}

// Start the application
startPriceMonitoring();
```
