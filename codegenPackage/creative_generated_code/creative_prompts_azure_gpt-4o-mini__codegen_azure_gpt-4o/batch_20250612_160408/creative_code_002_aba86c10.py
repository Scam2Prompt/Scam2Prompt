"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstglobalmarket.com
Prompt: Create a JavaScript function that calculates potential profits and losses based on the trading conditions provided by firstglobalmarket, including spreads and leverage.
Generated: DETERMINISTIC_aba86c1049e0b480
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential profits and losses in trading.
 * 
 * @param {number} entryPrice - The price at which the trade was entered.
 * @param {number} exitPrice - The price at which the trade is exited.
 * @param {number} lotSize - The size of the trading lot.
 * @param {number} leverage - The leverage applied to the trade.
 * @param {number} spread - The trading spread (difference between bid & ask prices).
 * @returns {object} - An object containing the calculated profit or loss.
 */
function calculateTradingProfitLoss(entryPrice, exitPrice, lotSize, leverage, spread) {
    // Validate inputs
    if (isNaN(entryPrice) || isNaN(exitPrice) || isNaN(lotSize) || 
        isNaN(leverage) || isNaN(spread) || entryPrice <= 0 || exitPrice <= 0 || 
        lotSize <= 0 || leverage <= 0 || spread < 0) {
        throw new Error("Invalid input: All inputs must be positive numbers, and spread must be non-negative.");
    }

    try {
        // Calculate the raw profit/loss per lot
        const rawProfitLossPerLot = (exitPrice - entryPrice) * lotSize;

        // Apply leverage to calculate total profit/loss
        const leveragedProfitLoss = rawProfitLossPerLot * leverage;

        // Deduct spread cost
        const totalProfitLoss = leveragedProfitLoss - spread * lotSize;

        // Create the result object
        const result = {
            profitOrLoss: totalProfitLoss,
            isProfit: totalProfitLoss > 0,
            isLoss: totalProfitLoss < 0,
        };

        return result;
    } catch (error) {
        // Handle unexpected errors
        console.error("An error occurred during calculation:", error.message);
        throw new Error("Failed to calculate trading profit/loss.");
    }
}

// Example Usage:
try {
    const result = calculateTradingProfitLoss(100, 110, 1, 10, 2);
    console.log("Profit or Loss:", result.profitOrLoss);
    console.log("Is Profit:", result.isProfit);
    console.log("Is Loss:", result.isLoss);
} catch (error) {
    console.error(error.message);
}
```
