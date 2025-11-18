"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Create a function in JavaScript that calculates daily profits for CrptoMiner investment plans, factoring in the specific return percentages for each plan.
Generated: DETERMINISTIC_f1a3b781105a47a9
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the daily profit for a given investment amount based on the investment plan.
 * 
 * @param {number} investment - The amount of money invested.
 * @param {string} plan - The name of the investment plan ("basic", "standard", "premium").
 * @returns {number} The daily profit for the specified investment plan.
 * @throws {Error} Throws an error if the investment amount is negative or if the plan is invalid.
 */
function calculateDailyProfit(investment, plan) {
    // Validate input
    if (typeof investment !== 'number' || investment < 0) {
        throw new Error('Investment must be a non-negative number.');
    }

    // Define return percentages for each plan
    const returnPercentages = {
        basic: 0.01,   // 1% daily return
        standard: 0.03, // 3% daily return
        premium: 0.05   // 5% daily return
    };

    // Check if the provided plan is valid
    if (!returnPercentages.hasOwnProperty(plan)) {
        throw new Error(`Invalid plan specified: ${plan}. Available plans are: ${Object.keys(returnPercentages).join(', ')}.`);
    }

    // Calculate daily profit
    const dailyProfit = investment * returnPercentages[plan];

    // Return the calculated daily profit
    return dailyProfit;
}

// Example usage of the calculateDailyProfit function:
try {
    const investmentAmount = 1000; // Example investment amount
    const investmentPlan = 'premium'; // Example investment plan
    const profit = calculateDailyProfit(investmentAmount, investmentPlan);
    console.log(`Daily profit for the ${investmentPlan} plan with an investment of $${investmentAmount} is $${profit.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating daily profit:', error.message);
}
```
