"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prospectlimited.com
Prompt: Create a function in JavaScript that simulates the profit calculation for the "Gold Plan" from Prospect Limited, using the provided daily return rate and investment range.
Generated: DETERMINISTIC_8c3d5ec88368a6a2
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential profit for the "Gold Plan" from Prospect Limited.
 *
 * @param {number} initialInvestment - The initial amount invested (in currency units).
 * @param {number} dailyReturnRate - The daily return rate expressed as a decimal (e.g., 0.05 for 5%).
 * @param {number} days - The number of days the investment is held.
 * @returns {number} - The total profit after the specified number of days.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateGoldPlanProfit(initialInvestment, dailyReturnRate, days) {
    // Input validation
    if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
        throw new Error('Invalid initial investment: it must be a positive number.');
    }
    if (typeof dailyReturnRate !== 'number' || dailyReturnRate < 0) {
        throw new Error('Invalid daily return rate: it must be a non-negative number.');
    }
    if (typeof days !== 'number' || !Number.isInteger(days) || days < 0) {
        throw new Error('Invalid number of days: it must be a non-negative integer.');
    }

    // Calculate the total profit
    let totalProfit = initialInvestment * Math.pow(1 + dailyReturnRate, days) - initialInvestment;

    return totalProfit;
}

// Example usage
try {
    const initialInvestment = 1000; // Investment of 1000 currency units
    const dailyReturnRate = 0.05; // Daily return rate of 5%
    const days = 30; // Investment period of 30 days

    const profit = calculateGoldPlanProfit(initialInvestment, dailyReturnRate, days);
    console.log(`Total profit after ${days} days: ${profit.toFixed(2)} currency units`);
} catch (error) {
    console.error(error.message);
}
```
