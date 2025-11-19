"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoprohashings.vip
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans offered by CryptoProHashings, specifically for the Silver, Gold, and Premium accounts.
Generated: DETERMINISTIC_fc8d62d0e2ffdaf4
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
 * @function calculatePotentialProfit
 * @description Calculates potential profits based on the investment plan type and investment amount.
 * @param {string} planType - The type of investment plan ('Silver', 'Gold', or 'Premium').
 * @param {number} investmentAmount - The amount of investment.
 * @returns {number} - The potential profit or an error message if inputs are invalid.
 * @throws {Error} - Throws an error if the plan type is invalid or investment amount is non-positive.
 */

function calculatePotentialProfit(planType, investmentAmount) {
    // Define profit rates for each investment plan
    const profitRates = {
        Silver: 0.05,  // 5% for Silver plan
        Gold: 0.1,     // 10% for Gold plan
        Premium: 0.15  // 15% for Premium plan
    };

    // Validate inputs
    if (typeof planType !== 'string' || !profitRates.hasOwnProperty(planType)) {
        throw new Error('Invalid plan type. Please choose Silver, Gold, or Premium.');
    }

    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Investment amount must be a positive number.');
    }

    // Calculate potential profit
    const profitRate = profitRates[planType];
    const potentialProfit = investmentAmount * profitRate;

    return potentialProfit;
}

// Example usage (uncomment to test)
// try {
//     const profit = calculatePotentialProfit('Gold', 1000);
//     console.log(`Potential profit: $${profit}`);
// } catch (error) {
//     console.error(error.message);
// }
```
