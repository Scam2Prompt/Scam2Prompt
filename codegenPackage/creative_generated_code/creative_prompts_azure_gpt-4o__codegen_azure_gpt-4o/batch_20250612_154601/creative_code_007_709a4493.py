"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opterisglobal.com
Prompt: Create a function in JavaScript to calculate scalable profits for a cryptocurrency investment plan, using the parameters from Opteris Global's investment plans.
Generated: DETERMINISTIC_709a4493f532ed3e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates scalable profits for a cryptocurrency investment plan.
 * 
 * @param {number} principal - The initial investment amount (in USD).
 * @param {number} rate - The annual profit rate (%) offered by Opteris Global.
 * @param {number} years - The number of years the investment will grow.
 * @param {number} compoundingFrequency - The number of times compounding occurs per year.
 * @returns {number} - The total profit after the specified investment period.
 * 
 * Example Usage:
 * const profit = calculateCryptoInvestmentProfit(1000, 12, 5, 4);
 * console.log(`Total Profit: $${profit.toFixed(2)}`);
 */
function calculateCryptoInvestmentProfit(principal, rate, years, compoundingFrequency) {
    // Input validation
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error("Invalid principal amount. Must be a positive number.");
    }
    if (typeof rate !== 'number' || rate <= 0) {
        throw new Error("Invalid rate. Must be a positive number.");
    }
    if (typeof years !== 'number' || years <= 0) {
        throw new Error("Invalid years. Must be a positive number.");
    }
    if (typeof compoundingFrequency !== 'number' || compoundingFrequency <= 0) {
        throw new Error("Invalid compounding frequency. Must be a positive number.");
    }

    // Annual rate converted to a decimal
    const annualRate = rate / 100;

    // Compound interest formula: A = P * (1 + r/n)^(n*t)
    const totalAmount = principal * Math.pow((1 + annualRate / compoundingFrequency), compoundingFrequency * years);

    // Calculate profit (total amount - principal)
    const profit = totalAmount - principal;

    return profit;
}

module.exports = calculateCryptoInvestmentProfit; // Exporting for use in other modules
```
