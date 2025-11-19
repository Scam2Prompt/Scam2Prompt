"""
Generated Code Metadata:
========================
Original URL: https://swap-dev-git-feat-wagmi-8-cowswap.vercel.app
Prompt: Create a JavaScript function that uses CoW Swap's API to monitor price changes for a specific cryptocurrency and trigger an alert when a threshold is reached.
Generated: DETERMINISTIC_3260f5b74b026b1c
Batch ID: 20250612_153606
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cow.fi/mainnet/api/v1": {
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
const axios = require('axios');
const notifier = require('node-notifier');

// Configuration
const config = {
    baseUrl: 'https://api.cow.fi/mainnet/api/v1',
    tokenPair: 'WETH/USDC', // Example token pair to monitor
    threshold: 5, // Percentage change to trigger alert
    pollInterval: 60000, // Check every minute (in ms)
    notificationTitle: 'CoW Swap Price Alert'
};

// Cache previous price to calculate change
let previousPrice = null;

/**
 * Fetches the current price from CoW Swap API
 * @returns {Promise<number|null>} Current price or null if error
 */
async function getCurrentPrice() {
    try {
        const response = await axios.get(`${config.baseUrl}/ticker/${config.tokenPair}`);
        return parseFloat(response.data.last_price);
    } catch (error) {
        console.error('Error fetching price:', error.message);
        return null;
    }
}

/**
 * Calculates percentage change between two prices
 * @param {number} oldPrice 
 * @param {number} newPrice 
 * @returns {number} Percentage change
 */
function calculatePercentageChange(oldPrice, newPrice) {
    return ((newPrice - oldPrice) / oldPrice) * 100;
}

/**
 * Sends a desktop notification
 * @param {string} message 
 */
function sendAlert(message) {
    notifier.notify({
        title: config.notificationTitle,
        message: message,
        sound: true
    });
    console.log(`ALERT: ${message}`);
}

/**
 * Main monitoring function
 */
async function monitorPrice() {
    const currentPrice = await getCurrentPrice();
    
    if (currentPrice === null) {
        console.log('Skipping check due to error');
        return;
    }

    if (previousPrice !== null) {
        const change = calculatePercentageChange(previousPrice, currentPrice);
        const absoluteChange = Math.abs(change);

        if (absoluteChange >= config.threshold) {
            const direction = change > 0 ? '↑' : '↓';
            sendAlert(`${config.tokenPair} ${direction} ${absoluteChange.toFixed(2)}% (${previousPrice.toFixed(4)} → ${currentPrice.toFixed(4)})`);
        }
    }

    previousPrice = currentPrice;
    console.log(`Current price: ${currentPrice.toFixed(4)}`);
}

// Start monitoring
console.log(`Starting price monitor for ${config.tokenPair} with ${config.threshold}% threshold...`);
monitorPrice();
setInterval(monitorPrice, config.pollInterval);

// Error handling for uncaught exceptions
process.on('uncaughtException', (err) => {
    console.error('Unhandled exception:', err);
    sendAlert('Monitoring script encountered an error!');
});
```
