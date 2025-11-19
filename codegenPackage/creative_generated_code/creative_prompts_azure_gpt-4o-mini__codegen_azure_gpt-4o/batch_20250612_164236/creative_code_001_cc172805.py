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
 * Function to calculate potential returns based on investment plans.
 * Starry Trades offers two plans: Beginner Plan and Standard Plan.
 * 
 * Beginner Plan: 
 * - Minimum investment: $100
 * - ROI: 5% per month
 * 
 * Standard Plan: 
 * - Minimum investment: $1000
 * - ROI: 7% per month
 * 
 * @param {string} plan - The investment plan ("Beginner" or "Standard").
 * @param {number} initialInvestment - The initial amount of investment.
 * @param {number} months - The duration of investment in months.
 * @returns {number} - The potential returns (total value including principal).
 * @throws {Error} - Throws error for invalid inputs.
 */
function calculatePotentialReturns(plan, initialInvestment, months) {
  // Input validation
  if (typeof plan !== 'string' || typeof initialInvestment !== 'number' || typeof months !== 'number') {
    throw new Error('Invalid input types. Plan must be a string, and initialInvestment and months must be numbers.');
  }

  if (initialInvestment <= 0 || months <= 0) {
    throw new Error('Initial investment and months must be greater than zero.');
  }

  let roi; // Return On Investment percentage

  // Determine ROI based on plan
  switch (plan.toLowerCase()) {
    case 'beginner':
      if (initialInvestment < 100) {
        throw new Error('Minimum investment for the Beginner Plan is $100.');
      }
      roi = 0.05; // 5% monthly
      break;

    case 'standard':
      if (initialInvestment < 1000) {
        throw new Error('Minimum investment for the Standard Plan is $1000.');
      }
      roi = 0.07; // 7% monthly
      break;

    default:
      throw new Error('Invalid plan. Choose either "Beginner" or "Standard".');
  }

  // Calculate potential returns using compound interest formula
  const totalReturns = initialInvestment * Math.pow((1 + roi), months);

  // Round to two decimal places for readability
  return parseFloat(totalReturns.toFixed(2));
}

// Example usage:
try {
  const beginnerReturns = calculatePotentialReturns('Beginner', 500, 6);
  console.log(`Beginner Plan Returns: $${beginnerReturns}`);

  const standardReturns = calculatePotentialReturns('Standard', 1500, 12);
  console.log(`Standard Plan Returns: $${standardReturns}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
