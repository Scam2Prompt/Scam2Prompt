"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Write a JavaScript function to simulate the investment process on Centraltraderz, allowing users to input their deposit amount and select an investment plan to see projected returns.
Generated: DETERMINISTIC_b1da72af9da1dd88
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the investment process and calculates projected returns.
 * 
 * @param {number} deposit - The amount the user wants to invest.
 * @param {string} plan - The investment plan chosen by the user ('basic', 'standard', 'premium').
 * @returns {object} - An object containing the selected plan, deposit, and projected returns.
 * 
 * Supported plans:
 * - 'basic': 5% return per month
 * - 'standard': 10% return per month
 * - 'premium': 15% return per month
 * 
 * Example:
 * const result = simulateInvestment(1000, 'standard');
 * console.log(result);
 */
function simulateInvestment(deposit, plan) {
  // Validate input
  if (typeof deposit !== 'number' || deposit <= 0) {
    throw new Error("Deposit must be a positive number.");
  }

  if (typeof plan !== 'string' || !['basic', 'standard', 'premium'].includes(plan.toLowerCase())) {
    throw new Error("Invalid investment plan. Choose 'basic', 'standard', or 'premium'.");
  }

  // Define return rates for each plan
  const returnRates = {
    basic: 0.05, // 5%
    standard: 0.10, // 10%
    premium: 0.15, // 15%
  };

  // Calculate projected return
  const rate = returnRates[plan.toLowerCase()];
  const projectedMonthlyReturn = deposit * rate;
  const projectedAnnualReturn = projectedMonthlyReturn * 12; // Assuming a 12-month period

  // Return the simulation results
  return {
    plan: plan.toLowerCase(),
    deposit: deposit,
    projectedMonthlyReturn: projectedMonthlyReturn.toFixed(2),
    projectedAnnualReturn: projectedAnnualReturn.toFixed(2),
  };
}

// Example usage:
try {
  const result = simulateInvestment(1000, 'premium');
  console.log(result);
  // Output: { plan: 'premium', deposit: 1000, projectedMonthlyReturn: '150.00', projectedAnnualReturn: '1800.00' }
} catch (error) {
  console.error(error.message);
}
```
