"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalwealthinvestmentltd.com
Prompt: Write a JavaScript function that calculates potential returns based on the investment plans offered by Capital Wealth Investment Ltd, specifically for the Classic, Pro, and Gold plans.
Generated: DETERMINISTIC_52af75100c0c055c
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
 * Calculates potential returns based on the investment plans offered by Capital Wealth Investment Ltd.
 * 
 * @param {number} investmentAmount - The amount of money to invest.
 * @param {string} plan - The investment plan chosen ("Classic", "Pro", or "Gold").
 * @returns {number} - The potential return from the investment.
 * @throws {Error} - Throws an error if the investment amount is not a positive number or if the plan is invalid.
 */
function calculateInvestmentReturn(investmentAmount, plan) {
    // Validate the investment amount
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Investment amount must be a positive number.');
    }

    // Define potential return rates for each plan
    const plans = {
        Classic: 0.05, // 5% return
        Pro: 0.1,      // 10% return
        Gold: 0.15     // 15% return
    };

    // Validate the plan
    if (!plans.hasOwnProperty(plan)) {
        throw new Error('Invalid investment plan. Please choose "Classic", "Pro", or "Gold".');
    }

    // Calculate potential return
    const returnRate = plans[plan];
    const potentialReturn = investmentAmount * (1 + returnRate);

    return potentialReturn;
}

// Example usage
try {
    const investment = 1000; // Example investment amount
    const selectedPlan = 'Pro'; // Example selected plan
    const returnAmount = calculateInvestmentReturn(investment, selectedPlan);
    console.log(`Potential return for ${selectedPlan} plan: $${returnAmount.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
