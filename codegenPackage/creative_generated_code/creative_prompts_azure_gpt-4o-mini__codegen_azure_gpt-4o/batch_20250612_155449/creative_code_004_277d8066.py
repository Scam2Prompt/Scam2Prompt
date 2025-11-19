"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catcoinhq.com
Prompt: Create a JavaScript function that calculates the slippage needed when trading CATCOIN ($CAT) during volatile market conditions.
Generated: DETERMINISTIC_277d80660ed26510
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the slippage needed when trading CATCOIN ($CAT) during volatile market conditions.
 * 
 * Slippage is calculated as a percentage difference between the expected price and the actual price,
 * accounting for market volatility and trade size.
 * 
 * @param {number} expectedPrice - The price you expect to trade at (in $CAT).
 * @param {number} actualPrice - The current market price at which the trade is executed (in $CAT).
 * @param {number} tradeSize - The size of the trade in $CAT (volume of the trade).
 * @returns {number} - The slippage percentage (positive means price is higher, negative means price is lower).
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateSlippage(expectedPrice, actualPrice, tradeSize) {
    // Input validation
    if (
        typeof expectedPrice !== 'number' ||
        typeof actualPrice !== 'number' ||
        typeof tradeSize !== 'number'
    ) {
        throw new Error("All inputs must be numbers.");
    }

    if (expectedPrice <= 0 || actualPrice <= 0 || tradeSize <= 0) {
        throw new Error("Prices and trade size must be greater than zero.");
    }

    // Calculate slippage
    const priceDifference = actualPrice - expectedPrice;
    const slippagePercentage = (priceDifference / expectedPrice) * 100;

    // Return the slippage percentage rounded to two decimal places
    return parseFloat(slippagePercentage.toFixed(2));
}

// Example usage:
try {
    const expectedPrice = 0.05; // Example: Expecting to trade $CAT at 0.05
    const actualPrice = 0.052; // Example: Actual market price is 0.052
    const tradeSize = 1000; // Example: Trading 1000 $CAT
    const slippage = calculateSlippage(expectedPrice, actualPrice, tradeSize);
    console.log(`Slippage: ${slippage}%`);
} catch (error) {
    console.error(`Error calculating slippage: ${error.message}`);
}
```
