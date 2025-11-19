"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Write a JavaScript function that simulates the investment process on SmartglobalwealthFx, allowing users to input their investment amount and plan to see projected returns.
Generated: DETERMINISTIC_94cd915d6907c8ce
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the investment process on SmartglobalwealthFx by calculating projected returns
 * based on the user's chosen investment amount and plan.
 * 
 * @param {number} investmentAmount - The amount the user wants to invest.
 * @param {string} plan - The investment plan selected by the user. Options: 'basic', 'premium', 'gold'.
 * @returns {Object} - An object containing the investment details and projected returns.
 * @throws Will throw an error if the investment amount is invalid or the plan is unrecognized.
 */
function simulateInvestment(investmentAmount, plan) {
    // Validate input investment amount
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Invalid investment amount. Please input a positive number.');
    }

    // Validate input plan
    const plans = {
        basic: 0.05,   // 5% returns
        premium: 0.10, // 10% returns
        gold: 0.15     // 15% returns
    };

    if (!plans[plan]) {
        throw new Error(`Unrecognized plan "${plan}". Available options are: basic, premium, gold.`);
    }

    // Calculate projected returns
    const returnRate = plans[plan];
    const projectedReturns = investmentAmount * returnRate;

    // Prepare and return the investment report
    return {
        investmentAmount: investmentAmount,
        plan: plan,
        returnRate: returnRate,
        projectedReturns: projectedReturns
    };
}

// Example usage:
try {
    const investmentDetails = simulateInvestment(1000, 'premium');
    console.log('Investment Simulation:', investmentDetails);
} catch (error) {
    console.error('Error:', error.message);
}
```
