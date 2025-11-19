"""
Generated Code Metadata:
========================
Original URL: https://starrytrades.org
Prompt: Write a JavaScript function that calculates potential returns based on the investment plans offered by Starry Trades, specifically for the Beginner Plan and Standard Plan.
Generated: DETERMINISTIC_cc172805370a98a6
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential returns based on the investment plans offered by Starry Trades.
 * 
 * @module StarryTradesInvestmentPlans
 */

/**
 * Enum for investment plans.
 * @enum {string}
 */
const InvestmentPlan = {
  BEGINNER: 'beginner',
  STANDARD: 'standard'
};

/**
 * Calculates the potential return for the given investment plan.
 * 
 * @param {InvestmentPlan} plan - The investment plan.
 * @param {number} investmentAmount - The amount invested.
 * @param {number} [years=1] - The number of years (default is 1).
 * @returns {number} The potential return.
 */
function calculatePotentialReturn(plan, investmentAmount, years = 1) {
  // Validate input parameters
  if (!Object.values(InvestmentPlan).includes(plan)) {
    throw new Error(`Invalid investment plan: ${plan}`);
  }
  if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
    throw new Error(`Invalid investment amount: ${investmentAmount}`);
  }
  if (typeof years !== 'number' || years <= 0) {
    throw new Error(`Invalid number of years: ${years}`);
  }

  // Define the interest rates for each plan
  const interestRates = {
    [InvestmentPlan.BEGINNER]: 0.05, // 5% per annum
    [InvestmentPlan.STANDARD]: 0.10  // 10% per annum
  };

  // Calculate the potential return
  const interestRate = interestRates[plan];
  const potentialReturn = investmentAmount * Math.pow(1 + interestRate, years) - investmentAmount;

  return potentialReturn;
}

// Example usage:
try {
  const beginnerPlanReturn = calculatePotentialReturn(InvestmentPlan.BEGINNER, 1000, 5);
  console.log(`Beginner Plan potential return: $${beginnerPlanReturn.toFixed(2)}`);

  const standardPlanReturn = calculatePotentialReturn(InvestmentPlan.STANDARD, 5000, 3);
  console.log(`Standard Plan potential return: $${standardPlanReturn.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
