"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-edge-new-uk-roi.bestinvesthub.com
Prompt: Develop a function in JavaScript to calculate daily profits from cryptocurrency trades based on Immediate Edge's reported average of €1,111.36 per day.
Generated: DETERMINISTIC_6d50a0db752183d0
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate daily profits from cryptocurrency trades.
 * @param {number} trades - The number of trades made in a day.
 * @param {number} profitPerTrade - The profit made per trade.
 * @returns {number} - The total daily profit.
 * @throws {Error} - Throws an error if trades or profitPerTrade is not a positive number.
 */
function calculateDailyProfit(trades, profitPerTrade) {
    // Validate input parameters
    if (typeof trades !== 'number' || typeof profitPerTrade !== 'number') {
        throw new Error('Both trades and profitPerTrade must be numbers.');
    }
    if (trades < 0 || profitPerTrade < 0) {
        throw new Error('Both trades and profitPerTrade must be positive numbers.');
    }

    // Calculate total daily profit
    const totalProfit = trades * profitPerTrade;

    return totalProfit;
}

// Example usage of the function
try {
    const averageProfit = 1111.36; // Average daily profit in euros from Immediate Edge
    const numberOfTrades = 10; // Example number of trades made in a day
    const dailyProfit = calculateDailyProfit(numberOfTrades, averageProfit);
    
    console.log(`Total daily profit from ${numberOfTrades} trades: €${dailyProfit.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating daily profit: ${error.message}`);
}
```
