"""
Generated Code Metadata:
========================
Original URL: https://prospectlimited.com
Prompt: Create a function in JavaScript that simulates the profit calculation for the "Gold Plan" from Prospect Limited, using the provided daily return rate and investment range.
Generated: DETERMINISTIC_8c3d5ec88368a6a2
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the potential profit for the "Gold Plan" from Prospect Limited.
 * 
 * @param {number} dailyReturnRate - The daily return rate as a percentage (e.g., 5 for 5%).
 * @param {number} investmentAmount - The amount invested in the Gold Plan.
 * @param {number} days - The number of days the investment is held.
 * @returns {number} - The total profit after the specified number of days.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateGoldPlanProfit(dailyReturnRate, investmentAmount, days) {
    // Validate input parameters
    if (typeof dailyReturnRate !== 'number' || dailyReturnRate < 0) {
        throw new Error('Invalid daily return rate. It must be a non-negative number.');
    }
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Invalid investment amount. It must be a positive number.');
    }
    if (typeof days !== 'number' || days < 0) {
        throw new Error('Invalid number of days. It must be a non-negative number.');
    }

    // Calculate the profit using the formula: Profit = Investment * (1 + Daily Return Rate/100) ^ Days - Investment
    const profit = investmentAmount * (Math.pow((1 + dailyReturnRate / 100), days)) - investmentAmount;

    // Return the calculated profit
    return profit;
}

// Example usage:
try {
    const dailyReturnRate = 5; // 5%
    const investmentAmount = 1000; // $1000
    const days = 30; // 30 days

    const profit = calculateGoldPlanProfit(dailyReturnRate, investmentAmount, days);
    console.log(`Total profit after ${days} days: $${profit.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating profit: ${error.message}`);
}
```
