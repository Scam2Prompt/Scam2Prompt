"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swifttradeexpress.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans offered by SwiftTrade Express.
Generated: DETERMINISTIC_f3eb8f7999a42cae
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential profits based on investment plans.
 * @param {number} principal - The initial amount of money invested.
 * @param {number} rate - The annual interest rate (as a percentage).
 * @param {number} years - The number of years the money is invested for.
 * @returns {number} The total profit earned over the investment period.
 * @throws {Error} Throws an error if the principal, rate, or years are negative or non-numeric.
 */
function calculatePotentialProfit(principal, rate, years) {
    // Input validation
    if (typeof principal !== 'number' || typeof rate !== 'number' || typeof years !== 'number') {
        throw new Error('Principal, rate, and years must be numeric values.');
    }
    
    if (principal < 0 || rate < 0 || years < 0) {
        throw new Error('Principal, rate, and years must be non-negative values.');
    }

    // Calculate profit using the formula: Profit = Principal * (1 + (Rate / 100)) ^ Years - Principal
    const totalAmount = principal * Math.pow((1 + (rate / 100)), years);
    const profit = totalAmount - principal;

    return profit;
}

// Example usage
try {
    const principal = 1000; // Initial investment amount
    const rate = 5;         // Annual interest rate in percent
    const years = 10;       // Investment duration in years

    const potentialProfit = calculatePotentialProfit(principal, rate, years);
    console.log(`Potential profit after ${years} years: $${potentialProfit.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating profit: ${error.message}`);
}
```
