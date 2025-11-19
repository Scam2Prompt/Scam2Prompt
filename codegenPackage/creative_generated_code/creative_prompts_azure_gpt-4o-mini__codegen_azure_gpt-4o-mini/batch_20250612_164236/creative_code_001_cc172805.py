"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starrytrades.org
Prompt: Write a JavaScript function that calculates potential returns based on the investment plans offered by Starry Trades, specifically for the Beginner Plan and Standard Plan.
Generated: DETERMINISTIC_cc172805370a98a6
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns based on the investment amount and plan type.
 * 
 * @param {number} investmentAmount - The amount of money invested.
 * @param {string} planType - The type of investment plan ("Beginner" or "Standard").
 * @returns {number} - The potential return based on the selected plan.
 * @throws {Error} - Throws an error if the investment amount is less than or equal to zero
 *                   or if the plan type is not recognized.
 */
function calculatePotentialReturns(investmentAmount, planType) {
    // Validate the investment amount
    if (investmentAmount <= 0) {
        throw new Error("Investment amount must be greater than zero.");
    }

    // Define potential returns for each plan
    const plans = {
        Beginner: {
            rateOfReturn: 0.05, // 5% return
            description: "Beginner Plan offers a stable return of 5%."
        },
        Standard: {
            rateOfReturn: 0.10, // 10% return
            description: "Standard Plan offers a more aggressive return of 10%."
        }
    };

    // Check if the provided plan type is valid
    if (!plans[planType]) {
        throw new Error("Invalid plan type. Please choose 'Beginner' or 'Standard'.");
    }

    // Calculate potential returns based on the selected plan
    const returnRate = plans[planType].rateOfReturn;
    const potentialReturn = investmentAmount * returnRate;

    return potentialReturn;
}

// Example usage:
// try {
//     const investment = 1000;
//     const plan = 'Beginner';
//     const returns = calculatePotentialReturns(investment, plan);
//     console.log(`Potential returns for the ${plan} Plan: $${returns.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
