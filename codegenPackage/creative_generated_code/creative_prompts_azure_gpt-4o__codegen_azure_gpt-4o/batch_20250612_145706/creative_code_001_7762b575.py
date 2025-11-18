"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrax.io
Prompt: Generate a function in JavaScript that calculates the return on investment (ROI) for arbitrage strategies, using the profit values and minimum investment amounts provided by Arbitrax.
Generated: DETERMINISTIC_7762b575ac1c832e
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the return on investment (ROI) for arbitrage strategies.
 * 
 * @param {number} profit - The profit value from the arbitrage strategy.
 * @param {number} minInvestment - The minimum investment amount required.
 * @returns {number} - The ROI in percentage, rounded to two decimal places.
 * 
 * @throws {Error} If profit or minInvestment are not positive numbers.
 */
function calculateROI(profit, minInvestment) {
    // Input validation
    if (typeof profit !== 'number' || typeof minInvestment !== 'number') {
        throw new Error("Both profit and minInvestment must be numbers.");
    }
    if (profit <= 0 || minInvestment <= 0) {
        throw new Error("Both profit and minInvestment must be positive values.");
    }

    // Calculate ROI as a percentage
    const roi = (profit / minInvestment) * 100;

    // Return ROI rounded to two decimal places
    return parseFloat(roi.toFixed(2));
}

// Example Usage
try {
    const profit = 500; // Example profit value
    const minInvestment = 2500; // Example minimum investment amount
    const roi = calculateROI(profit, minInvestment);
    console.log(`The ROI is ${roi}%`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
