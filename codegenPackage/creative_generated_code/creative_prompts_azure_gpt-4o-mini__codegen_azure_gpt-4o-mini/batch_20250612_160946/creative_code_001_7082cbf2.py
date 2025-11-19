"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Write a JavaScript function that calculates potential returns from the Coinex Tradings investment plans, given an initial investment amount and the plan selected.
Generated: DETERMINISTIC_7082cbf2815f0548
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns from Coinex Trading investment plans.
 * 
 * @param {number} initialInvestment - The amount of money invested.
 * @param {string} plan - The investment plan selected. Options are 'basic', 'premium', and 'vip'.
 * @returns {number} The potential returns based on the selected plan.
 * @throws {Error} Throws an error if the input is invalid or if the plan is not recognized.
 */
function calculateInvestmentReturns(initialInvestment, plan) {
    // Validate initialInvestment
    if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
        throw new Error('Invalid initial investment amount. It must be a positive number.');
    }

    // Define potential return rates for the different plans
    const plans = {
        basic: 0.05,   // 5% return for basic plan
        premium: 0.10, // 10% return for premium plan
        vip: 0.15      // 15% return for VIP plan
    };

    // Validate the selected plan
    if (!plans.hasOwnProperty(plan)) {
        throw new Error('Invalid plan selected. Please choose between "basic", "premium", or "vip".');
    }

    // Calculate potential returns
    const returnRate = plans[plan];
    const potentialReturns = initialInvestment * (1 + returnRate);

    return potentialReturns;
}

// Example usage:
try {
    const investment = 1000; // Initial investment amount
    const selectedPlan = 'premium'; // Selected investment plan
    const returns = calculateInvestmentReturns(investment, selectedPlan);
    console.log(`Potential returns for the ${selectedPlan} plan: $${returns.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
