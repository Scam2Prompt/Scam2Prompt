"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitinvestcoin.com
Prompt: Create a function in JavaScript to automate the calculation of daily profit returns for investment plans like those described on BitInvestCoin, with varying percentage profits.
Generated: DETERMINISTIC_95f6c85a125bc154
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates daily profit returns for investment plans.
 * 
 * @param {number} investmentAmount - The initial amount invested.
 * @param {number} dailyProfitPercentage - The daily profit percentage as a decimal (e.g., 0.05 for 5%).
 * @param {number} days - The number of days for which to calculate the profit.
 * @returns {number} - The total profit earned after the specified number of days.
 * @throws {Error} - Throws an error if the investment amount is negative or zero, 
 *                   if the daily profit percentage is not between 0 and 1, 
 *                   or if the number of days is not a positive integer.
 */
function calculateDailyProfitReturns(investmentAmount, dailyProfitPercentage, days) {
    // Validate inputs
    if (investmentAmount <= 0) {
        throw new Error('Investment amount must be greater than zero.');
    }
    if (dailyProfitPercentage < 0 || dailyProfitPercentage > 1) {
        throw new Error('Daily profit percentage must be between 0 and 1.');
    }
    if (!Number.isInteger(days) || days <= 0) {
        throw new Error('Number of days must be a positive integer.');
    }

    // Calculate total profit
    let totalProfit = 0;
    for (let i = 0; i < days; i++) {
        totalProfit += investmentAmount * dailyProfitPercentage;
    }

    return totalProfit;
}

// Example usage (uncomment to run):
// try {
//     const initialInvestment = 1000; // Initial investment amount
//     const dailyProfitRate = 0.05;    // Daily profit percentage (5%)
//     const durationInDays = 30;        // Duration in days
//     
//     const profit = calculateDailyProfitReturns(initialInvestment, dailyProfitRate, durationInDays);
//     console.log(`Total profit after ${durationInDays} days: $${profit.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
