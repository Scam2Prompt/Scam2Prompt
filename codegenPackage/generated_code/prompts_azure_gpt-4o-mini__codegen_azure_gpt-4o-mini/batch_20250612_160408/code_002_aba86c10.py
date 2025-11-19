"""
Generated Code Metadata:
========================
Original URL: https://firstglobalmarket.com
Prompt: Create a JavaScript function that calculates potential profits and losses based on the trading conditions provided by firstglobalmarket, including spreads and leverage.
Generated: DETERMINISTIC_aba86c1049e0b480
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential profits and losses based on trading conditions.
 * 
 * @param {number} entryPrice - The price at which the asset is bought or sold.
 * @param {number} exitPrice - The price at which the asset is sold or bought back.
 * @param {number} positionSize - The size of the position in units.
 * @param {number} spread - The difference between the buying and selling price.
 * @param {number} leverage - The leverage used for the trade.
 * @returns {Object} An object containing potential profit or loss and the effective investment.
 * @throws {Error} Throws an error if any input is invalid.
 */
function calculateTradingOutcome(entryPrice, exitPrice, positionSize, spread, leverage) {
    // Validate inputs
    if (typeof entryPrice !== 'number' || typeof exitPrice !== 'number' ||
        typeof positionSize !== 'number' || typeof spread !== 'number' ||
        typeof leverage !== 'number') {
        throw new Error('All inputs must be numbers.');
    }

    if (entryPrice <= 0 || exitPrice <= 0 || positionSize <= 0 || spread < 0 || leverage <= 0) {
        throw new Error('Entry price, exit price, position size must be greater than 0; spread must be non-negative; leverage must be greater than 0.');
    }

    // Calculate the effective entry and exit prices considering the spread
    const effectiveEntryPrice = entryPrice + spread;
    const effectiveExitPrice = exitPrice - spread;

    // Calculate potential profit or loss
    const profitOrLoss = (effectiveExitPrice - effectiveEntryPrice) * positionSize;

    // Calculate the effective investment considering leverage
    const effectiveInvestment = (effectiveEntryPrice * positionSize) / leverage;

    // Return the results
    return {
        profitOrLoss: profitOrLoss,
        effectiveInvestment: effectiveInvestment
    };
}

// Example usage
try {
    const result = calculateTradingOutcome(100, 110, 10, 2, 10);
    console.log(`Potential Profit/Loss: ${result.profitOrLoss}`);
    console.log(`Effective Investment: ${result.effectiveInvestment}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
