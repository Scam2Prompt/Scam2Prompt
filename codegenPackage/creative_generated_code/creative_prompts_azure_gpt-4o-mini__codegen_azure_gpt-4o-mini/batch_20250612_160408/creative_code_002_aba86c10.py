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
 * Calculates potential profits and losses based on trading conditions.
 * 
 * @param {number} initialInvestment - The amount of money invested initially.
 * @param {number} entryPrice - The price at which the asset is bought.
 * @param {number} exitPrice - The price at which the asset is sold.
 * @param {number} spread - The difference between the buying and selling price (broker's fee).
 * @param {number} leverage - The leverage ratio applied to the investment.
 * @returns {object} An object containing potential profit/loss and net profit/loss after spread.
 * @throws {Error} Throws an error if any of the parameters are invalid (non-positive numbers).
 */
function calculateProfitLoss(initialInvestment, entryPrice, exitPrice, spread, leverage) {
    // Validate input parameters
    if (initialInvestment <= 0 || entryPrice <= 0 || exitPrice <= 0 || spread < 0 || leverage <= 0) {
        throw new Error('All parameters must be positive numbers and spread cannot be negative.');
    }

    // Calculate the total invested amount considering leverage
    const totalInvestment = initialInvestment * leverage;

    // Calculate the gross profit/loss before spread
    const grossPL = (exitPrice - entryPrice) * totalInvestment;

    // Calculate net profit/loss after accounting for spread
    const netPL = grossPL - spread;

    return {
        grossProfitLoss: grossPL,
        netProfitLoss: netPL
    };
}

// Example usage
try {
    const result = calculateProfitLoss(1000, 50, 55, 5, 10);
    console.log(`Gross Profit/Loss: ${result.grossProfitLoss}`);
    console.log(`Net Profit/Loss after spread: ${result.netProfitLoss}`);
} catch (error) {
    console.error('Error calculating profit/loss:', error.message);
}
```
