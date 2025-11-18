"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Create a function in JavaScript that simulates the investment calculator on RapidCoinTrades, allowing users to input deposit amounts and select plans to calculate their profit and total sum.
Generated: DETERMINISTIC_ca2cfa95fa9ef687
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Investment Calculator Function
 * Simulates the investment calculator for RapidCoinTrades.
 * Inputs: deposit amount, selected investment plan
 * Output: calculated profit and total sum
 */

// Investment plans configuration
const investmentPlans = {
  bronze: { profitRate: 0.05 }, // 5% profit
  silver: { profitRate: 0.10 }, // 10% profit
  gold: { profitRate: 0.20 },   // 20% profit
  platinum: { profitRate: 0.30 } // 30% profit
};

/**
 * Calculates profit and total sum based on deposit and selected plan.
 * @param {number} deposit - The deposit amount (must be positive).
 * @param {string} plan - The investment plan (bronze, silver, gold, platinum).
 * @returns {object} - An object containing the calculated profit and total sum.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function investmentCalculator(deposit, plan) {
  // Input validation
  if (typeof deposit !== 'number' || deposit <= 0) {
    throw new Error('Invalid deposit amount. Please enter a positive number.');
  }

  if (!investmentPlans[plan]) {
    throw new Error(
      `Invalid plan selected. Please choose a valid plan: ${Object.keys(investmentPlans).join(', ')}.`
    );
  }

  // Retrieve the profit rate for the selected plan
  const { profitRate } = investmentPlans[plan];

  // Calculate profit and total sum
  const profit = deposit * profitRate;
  const totalSum = deposit + profit;

  // Return the results in an object
  return {
    profit: parseFloat(profit.toFixed(2)), // Rounded to 2 decimal places
    totalSum: parseFloat(totalSum.toFixed(2)) // Rounded to 2 decimal places
  };
}

// Example usage:
// Uncomment the lines below to test the function in a runtime environment
/*
try {
  const deposit = 1000; // Example deposit amount
  const plan = 'gold'; // Example plan
  const result = investmentCalculator(deposit, plan);
  console.log(`Profit: $${result.profit}`);
  console.log(`Total Sum: $${result.totalSum}`);
} catch (error) {
  console.error(error.message);
}
*/
```
