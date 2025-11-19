"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Write a JavaScript function that simulates the investment process on MET LIFE INVESTS, allowing users to select a plan and view potential returns.
Generated: DETERMINISTIC_6d756b6c7f023225
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates an investment process for MET LIFE INVESTS.
 * Allows users to select a plan and view potential returns.
 * 
 * @param {string} plan - The investment plan selected by the user (e.g., "basic", "standard", "premium").
 * @param {number} amount - The investment amount in USD.
 * @param {number} years - The number of years the investment will mature.
 * @returns {string} Resulting message with potential returns or an error message.
 */
function calculateInvestmentReturns(plan, amount, years) {
    // Validate input types
    if (typeof plan !== 'string' || typeof amount !== 'number' || typeof years !== 'number') {
        return "Error: Invalid input. Please ensure 'plan' is a string, 'amount' and 'years' are numbers.";
    }

    // Validate input values
    if (amount <= 0 || years <= 0) {
        return "Error: Investment amount and years must be greater than zero.";
    }

    // Investment plans and their annual interest rates (compounded annually)
    const plans = {
        basic: 0.03,     // 3% annual interest
        standard: 0.05,  // 5% annual interest
        premium: 0.07    // 7% annual interest
    };

    // Check if the selected plan exists
    if (!plans[plan.toLowerCase()]) {
        return "Error: Invalid plan selected. Available plans are: basic, standard, premium.";
    }

    // Retrieve the interest rate for the selected plan
    const annualRate = plans[plan.toLowerCase()];

    // Compound interest calculation formula: A = P * (1 + r)^t
    // A is the final amount, P is the principal, r is the annual rate, and t is the time in years
    const finalAmount = amount * Math.pow(1 + annualRate, years);

    // Format the result for readability
    const formattedFinalAmount = finalAmount.toFixed(2);

    return `For the ${plan} plan, investing $${amount} for ${years} years will result in a potential return of $${formattedFinalAmount}.`;
}

// Example usage:
console.log(calculateInvestmentReturns("premium", 1000, 5)); // Expected output: For the premium plan, investing $1000 for 5 years will result in a potential return of $1402.55.
```
