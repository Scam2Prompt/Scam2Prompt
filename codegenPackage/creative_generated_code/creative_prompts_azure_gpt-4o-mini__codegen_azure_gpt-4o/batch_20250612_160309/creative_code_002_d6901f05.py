"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Create a function in JavaScript that calculates the total profit from a long-term high yield investment in a Forex-backed loan program, considering daily compounding.
Generated: DETERMINISTIC_d6901f05ec20c7e9
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate total profit from a long-term high-yield investment
 * with daily compounding interest.
 *
 * @param {number} principal - Initial investment amount (must be greater than 0).
 * @param {number} annualRate - Annual interest rate in percentage (must be between 0 and 100).
 * @param {number} years - Total investment time in years (must be greater than 0).
 * @returns {number} - Total profit from the investment (rounded to two decimal places).
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateForexInvestmentProfit(principal, annualRate, years) {
  // Input validation
  if (principal <= 0 || annualRate <= 0 || annualRate > 100 || years <= 0) {
    throw new Error(
      "Invalid input: Ensure principal > 0, annualRate between 0 and 100, and years > 0."
    );
  }

  // Convert annual rate to daily rate (assuming 365 days in a year)
  const dailyRate = annualRate / 100 / 365;

  // Calculate total number of days
  const totalDays = years * 365;

  // Apply daily compounding formula: A = P * (1 + r)^n
  const finalAmount = principal * Math.pow(1 + dailyRate, totalDays);

  // Calculate profit
  const profit = finalAmount - principal;

  // Return result rounded to two decimal places
  return parseFloat(profit.toFixed(2));
}

// Example usage of the function
try {
  const principal = 10000; // Initial investment amount in USD
  const annualRate = 12; // Annual interest rate in percentage
  const years = 5; // Investment duration in years

  const profit = calculateForexInvestmentProfit(principal, annualRate, years);
  console.log(`Total Profit: $${profit}`);
} catch (error) {
  console.error(error.message);
}
```
