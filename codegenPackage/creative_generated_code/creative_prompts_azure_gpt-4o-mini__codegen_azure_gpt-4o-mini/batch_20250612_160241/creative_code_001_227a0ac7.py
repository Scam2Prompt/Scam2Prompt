"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinstantmining.com
Prompt: Write a code snippet in JavaScript that calculates potential profits based on the investment plans offered by Globalinstantmining, such as the Silver, Gold, and Premium accounts.
Generated: DETERMINISTIC_227a0ac78d8a0b65
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Investment Profit Calculator for Globalinstantmining
 * This module calculates potential profits based on investment plans.
 */

// Investment plans with their respective rates and minimum investments
const investmentPlans = {
    Silver: { rate: 0.05, minInvestment: 100 },
    Gold: { rate: 0.1, minInvestment: 500 },
    Premium: { rate: 0.15, minInvestment: 1000 }
};

/**
 * Calculates profit based on the selected investment plan and amount.
 * 
 * @param {string} plan - The investment plan (Silver, Gold, Premium)
 * @param {number} investmentAmount - The amount to invest
 * @returns {number} - Calculated profit or an error message
 */
function calculateProfit(plan, investmentAmount) {
    // Validate the inputs
    if (!investmentPlans[plan]) {
        throw new Error(`Invalid investment plan: ${plan}. Choose from Silver, Gold, or Premium.`);
    }
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error(`Invalid investment amount: ${investmentAmount}. Must be a positive number.`);
    }

    const { rate, minInvestment } = investmentPlans[plan];

    // Validate if the investment amount meets the minimum requirement for the selected plan
    if (investmentAmount < minInvestment) {
        throw new Error(`Investment amount must be at least ${minInvestment} for the ${plan} plan.`);
    }

    // Calculate profit
    const profit = investmentAmount * rate;
    return profit;
}

// Example usage:
try {
    const plan = 'Gold'; // Investment plan can be Silver, Gold, or Premium
    const investmentAmount = 700; // User's investment amount
    const profit = calculateProfit(plan, investmentAmount);
    console.log(`Your potential profit for the ${plan} plan with an investment of ${investmentAmount} is: ${profit}`);
} catch (error) {
    console.error(`Error calculating profit: ${error.message}`);
}
```
