"""
Generated Code Metadata:
========================
Original URL: https://bitsotrade.com
Prompt: "Write a JavaScript function to simulate the performance of a Forex trading strategy using historical data, considering factors such as currency exchange rates and trading volume."
Generated: DETERMINISTIC_a7108bfbcdd83b13
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates a Forex trading strategy using historical data.
 * 
 * @param {Array} historicalData - An array of historical data objects containing exchange rates and trading volumes.
 * @param {number} initialCapital - The initial amount of capital to start trading with.
 * @param {number} tradeVolume - The volume of currency to trade in each transaction.
 * @param {number} profitTarget - The target profit percentage for each trade.
 * @param {number} stopLoss - The stop loss percentage for each trade.
 * @returns {Object} - An object containing the final capital and total trades executed.
 */
function simulateForexTrading(historicalData, initialCapital, tradeVolume, profitTarget, stopLoss) {
    // Validate input parameters
    if (!Array.isArray(historicalData) || historicalData.length === 0) {
        throw new Error("Invalid historical data provided.");
    }
    if (initialCapital <= 0 || tradeVolume <= 0 || profitTarget <= 0 || stopLoss <= 0) {
        throw new Error("Initial capital, trade volume, profit target, and stop loss must be positive numbers.");
    }

    let capital = initialCapital;
    let totalTrades = 0;

    // Iterate through the historical data
    for (let i = 0; i < historicalData.length; i++) {
        const { exchangeRate, volume } = historicalData[i];

        // Check if there is enough capital to trade
        if (capital < tradeVolume * exchangeRate) {
            console.warn(`Insufficient capital to trade at index ${i}. Skipping trade.`);
            continue;
        }

        // Calculate potential profit and loss
        const potentialProfit = tradeVolume * exchangeRate * (profitTarget / 100);
        const potentialLoss = tradeVolume * exchangeRate * (stopLoss / 100);

        // Simulate trade execution
        const tradeOutcome = Math.random() < 0.5; // Randomly determine if the trade is successful

        if (tradeOutcome) {
            // Successful trade
            capital += potentialProfit;
            console.log(`Trade successful at index ${i}. New capital: ${capital.toFixed(2)}`);
        } else {
            // Unsuccessful trade
            capital -= potentialLoss;
            console.log(`Trade unsuccessful at index ${i}. New capital: ${capital.toFixed(2)}`);
        }

        totalTrades++;
    }

    return {
        finalCapital: capital.toFixed(2),
        totalTrades: totalTrades
    };
}

// Example usage
const historicalData = [
    { exchangeRate: 1.1, volume: 1000 },
    { exchangeRate: 1.2, volume: 1500 },
    { exchangeRate: 1.15, volume: 1200 },
    // Add more historical data as needed
];

try {
    const result = simulateForexTrading(historicalData, 10000, 1000, 10, 5);
    console.log(`Final Capital: $${result.finalCapital}, Total Trades: ${result.totalTrades}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
