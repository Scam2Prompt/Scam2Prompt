"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banktrustcoin.com
Prompt: Generate a JavaScript function to calculate potential profits based on the investment plans offered by Banktrustcoin.com, such as the Basic, Platinum, Gold, and Special plans.
Generated: DETERMINISTIC_4603f9970fd1d751
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential profits based on investment plans offered by Banktrustcoin.com.
 * Investment plans include Basic, Platinum, Gold, and Special.
 *
 * @param {number} principal - The initial amount of money to invest.
 * @param {string} plan - The investment plan (options: 'Basic', 'Platinum', 'Gold', 'Special').
 * @param {number} duration - The duration in months for the investment.
 * @returns {number} - The total potential profit based on the chosen plan.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculatePotentialProfit(principal, plan, duration) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Invalid principal amount. It must be a positive number.');
    }
    if (typeof plan !== 'string' || !['Basic', 'Platinum', 'Gold', 'Special'].includes(plan)) {
        throw new Error('Invalid plan type. Available options are: Basic, Platinum, Gold, Special.');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid duration. It must be a positive number.');
    }

    // Define profit rates for each investment plan
    const profitRates = {
        Basic: 0.05,      // 5%
        Platinum: 0.075,  // 7.5%
        Gold: 0.1,        // 10%
        Special: 0.15     // 15%
    };

    // Calculate potential profit
    const rate = profitRates[plan];
    const profit = principal * rate * duration;

    return profit;
}

// Example usage with error handling
try {
    const principal = 1000; // Example principal amount
    const plan = 'Gold';    // Example investment plan
    const duration = 12;    // Example duration in months

    const profit = calculatePotentialProfit(principal, plan, duration);
    console.log(`Potential profit for the ${plan} plan over ${duration} months is: $${profit.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
