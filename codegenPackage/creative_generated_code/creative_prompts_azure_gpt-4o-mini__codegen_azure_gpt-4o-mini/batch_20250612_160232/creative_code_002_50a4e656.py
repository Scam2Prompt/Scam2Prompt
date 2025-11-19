"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sirixfinance.com
Prompt: Create a function in JavaScript that calculates potential returns based on the investment plans offered by Zirix Finance, including daily, weekly, and hourly returns.
Generated: DETERMINISTIC_50a4e656d6f59803
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns based on the investment plans offered by Zirix Finance.
 * Investment plans include daily, weekly, and hourly returns.
 * 
 * @param {number} principal - The initial amount of money invested.
 * @param {string} plan - The investment plan type ('daily', 'weekly', 'hourly').
 * @param {number} duration - The duration in the respective time unit (days, weeks, hours).
 * @returns {number} - The calculated potential return.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculatePotentialReturns(principal, plan, duration) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number.');
    }

    let rate;

    // Determine the rate based on the investment plan
    switch (plan.toLowerCase()) {
        case 'daily':
            rate = 0.01; // Example: 1% daily return
            break;
        case 'weekly':
            rate = 0.07; // Example: 7% weekly return
            break;
        case 'hourly':
            rate = 0.005; // Example: 0.5% hourly return
            break;
        default:
            throw new Error('Invalid investment plan. Choose "daily", "weekly", or "hourly".');
    }

    // Calculate potential return
    const potentialReturn = principal * Math.pow(1 + rate, duration);

    return potentialReturn;
}

// Example usage
try {
    const investment = 1000; // Principal investment amount
    const planType = 'daily'; // Investment plan type
    const investmentDuration = 30; // Duration in days, weeks, or hours

    const returns = calculatePotentialReturns(investment, planType, investmentDuration);
    console.log(`Potential returns for a ${planType} plan over ${investmentDuration} units: $${returns.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating potential returns:', error.message);
}
```
