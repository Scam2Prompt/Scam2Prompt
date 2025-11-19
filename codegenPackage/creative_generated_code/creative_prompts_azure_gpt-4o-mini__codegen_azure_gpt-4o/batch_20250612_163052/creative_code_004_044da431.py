"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-matrix.net
Prompt: Create a JavaScript function that simulates the trading strategy used by Immediate 1.4 Evista, focusing on executing trades only when profitable conditions are met.
Generated: DETERMINISTIC_044da4313c3f2650
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a trading strategy similar to Immediate 1.4 Evista.
 * Executes trades only when profitable conditions are met.
 * 
 * Strategy:
 * - Buy asset if the price is expected to rise significantly.
 * - Sell asset if the price is expected to fall significantly.
 * - Avoid trades if conditions are not profitable.
 * 
 * Assumptions:
 * - Historical and real-time market data are provided.
 * - Profitability is determined by a simple threshold logic.
 */

/**
 * Simulates the trading strategy.
 * @param {Array} marketData - Array of market data objects containing price and trend information.
 * @param {Object} thresholds - Thresholds for buying and selling decisions.
 * @param {number} thresholds.buyThreshold - Minimum percentage increase expected for buying.
 * @param {number} thresholds.sellThreshold - Minimum percentage decrease expected for selling.
 * @returns {Array} tradeLog - Log of executed trades with details.
 */
function simulateTradingStrategy(marketData, thresholds) {
    // Validate input parameters
    if (!Array.isArray(marketData) || typeof thresholds !== 'object') {
        throw new Error("Invalid input: marketData must be an array and thresholds must be an object.");
    }
    if (typeof thresholds.buyThreshold !== 'number' || typeof thresholds.sellThreshold !== 'number') {
        throw new Error("Invalid thresholds: buyThreshold and sellThreshold must be numbers.");
    }

    // Initialize trade log to record executed trades
    const tradeLog = [];

    // Process each market data entry
    marketData.forEach((entry, index) => {
        // Validate market data entry
        if (!entry.price || typeof entry.price !== 'number' || !entry.expectedChange || typeof entry.expectedChange !== 'number') {
            throw new Error(`Invalid market data entry at index ${index}: price and expectedChange must be numbers.`);
        }

        // Determine trading action
        if (entry.expectedChange >= thresholds.buyThreshold) {
            // Execute buy trade
            tradeLog.push({
                action: "buy",
                price: entry.price,
                expectedChange: entry.expectedChange,
                profitPotential: entry.expectedChange - thresholds.buyThreshold,
                timestamp: new Date().toISOString()
            });
        } else if (entry.expectedChange <= -thresholds.sellThreshold) {
            // Execute sell trade
            tradeLog.push({
                action: "sell",
                price: entry.price,
                expectedChange: entry.expectedChange,
                profitPotential: Math.abs(entry.expectedChange) - thresholds.sellThreshold,
                timestamp: new Date().toISOString()
            });
        } else {
            // No trade executed as conditions are not profitable
            tradeLog.push({
                action: "hold",
                price: entry.price,
                expectedChange: entry.expectedChange,
                timestamp: new Date().toISOString()
            });
        }
    });

    // Return the log of executed trades
    return tradeLog;
}

// Example usage of the trading strategy
const exampleMarketData = [
    { price: 100, expectedChange: 5 },  // Expected 5% increase
    { price: 105, expectedChange: -3 }, // Expected 3% decrease
    { price: 102, expectedChange: 0 }   // No expected change
];

const exampleThresholds = {
    buyThreshold: 4,  // Minimum 4% increase to buy
    sellThreshold: 2  // Minimum 2% decrease to sell
};

const trades = simulateTradingStrategy(exampleMarketData, exampleThresholds);
console.log("Executed Trades:", trades);
```
