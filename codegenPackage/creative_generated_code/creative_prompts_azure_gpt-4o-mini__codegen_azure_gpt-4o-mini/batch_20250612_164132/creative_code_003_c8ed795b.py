"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bsc-scan.net
Prompt: Create a JavaScript function that calculates weekly and monthly profits based on the investment amount and the selected plan from BSC Scan.
Generated: DETERMINISTIC_c8ed795b49d3479e
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates weekly and monthly profits based on the investment amount and selected plan.
 * 
 * @param {number} investmentAmount - The total amount of money invested.
 * @param {string} plan - The selected investment plan (e.g., "basic", "premium", "vip").
 * @returns {Object} An object containing the weekly and monthly profits.
 * @throws Will throw an error if the investment amount is less than or equal to zero,
 *         or if the specified plan is invalid.
 */
function calculateProfits(investmentAmount, plan) {
    // Error handling for invalid investment amount
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Investment amount must be a positive number.');
    }

    // Define profit rates for different plans
    const profitRates = {
        basic: { weekly: 0.05, monthly: 0.20 },
        premium: { weekly: 0.10, monthly: 0.40 },
        vip: { weekly: 0.15, monthly: 0.60 },
    };

    // Error handling for invalid plan
    if (!profitRates[plan]) {
        throw new Error('Invalid plan selected. Please choose from "basic", "premium", or "vip".');
    }

    // Calculate weekly and monthly profits
    const weeklyProfit = investmentAmount * profitRates[plan].weekly;
    const monthlyProfit = investmentAmount * profitRates[plan].monthly;

    // Return the calculated profits
    return {
        weeklyProfit: parseFloat(weeklyProfit.toFixed(2)), // Rounded to 2 decimal places
        monthlyProfit: parseFloat(monthlyProfit.toFixed(2)), // Rounded to 2 decimal places
    };
}

// Example usage (uncomment to test):
// try {
//     const profits = calculateProfits(1000, 'premium');
//     console.log(profits); // { weeklyProfit: 100, monthlyProfit: 400 }
// } catch (error) {
//     console.error(error.message);
// }
```
