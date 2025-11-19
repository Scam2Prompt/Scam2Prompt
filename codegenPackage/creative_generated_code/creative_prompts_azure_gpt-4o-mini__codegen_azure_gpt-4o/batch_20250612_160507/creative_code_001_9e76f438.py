"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenarisfunds.com
Prompt: Write a JavaScript function that calculates potential returns based on the investment plans offered by Tenaris Funds, given an initial investment amount and duration.
Generated: DETERMINISTIC_9e76f43830898361
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns based on investment plans offered by Tenaris Funds.
 * 
 * Tenaris Funds has the following plans:
 *  - Short-Term Plan: Annual interest rate of 5%, minimum duration of 1 year, maximum of 3 years.
 *  - Mid-Term Plan: Annual interest rate of 7%, minimum duration of 4 years, maximum of 7 years.
 *  - Long-Term Plan: Annual interest rate of 10%, minimum duration of 8 years, maximum of 20 years.
 * 
 * @param {number} investmentAmount - The initial amount invested (must be > 0).
 * @param {number} durationInYears - The investment duration in years.
 * @returns {string} - Returns a message with the calculated potential return or an error message.
 */
function calculatePotentialReturns(investmentAmount, durationInYears) {
    // Validate input
    if (investmentAmount <= 0) {
        return "Error: Investment amount must be greater than 0.";
    }
    if (durationInYears <= 0 || !Number.isInteger(durationInYears)) {
        return "Error: Duration must be a positive integer greater than 0.";
    }

    // Define investment plans
    const investmentPlans = [
        { name: "Short-Term Plan", rate: 0.05, minYears: 1, maxYears: 3 },
        { name: "Mid-Term Plan", rate: 0.07, minYears: 4, maxYears: 7 },
        { name: "Long-Term Plan", rate: 0.10, minYears: 8, maxYears: 20 }
    ];

    // Find a suitable plan
    const selectedPlan = investmentPlans.find(plan =>
        durationInYears >= plan.minYears && durationInYears <= plan.maxYears
    );

    if (!selectedPlan) {
        return "Error: No suitable investment plan found for the given duration.";
    }

    // Calculate potential return using compound interest formula: A = P(1 + r)^t
    const potentialReturn = investmentAmount * Math.pow(1 + selectedPlan.rate, durationInYears);

    // Format output
    return `Based on the ${selectedPlan.name}, with an initial investment of $${investmentAmount.toFixed(2)} over ${durationInYears} years, your potential return is $${potentialReturn.toFixed(2)}.`;
}

// Example Usage:
// console.log(calculatePotentialReturns(1000, 5)); // Test with valid input
// console.log(calculatePotentialReturns(0, 5)); // Test with invalid investment amount
// console.log(calculatePotentialReturns(1000, 25)); // Test with invalid duration
```
