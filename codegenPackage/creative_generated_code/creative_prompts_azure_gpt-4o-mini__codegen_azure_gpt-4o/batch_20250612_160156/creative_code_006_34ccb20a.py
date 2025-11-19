"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitablecryptosignal.com.tb-investment.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans offered by Profitable Crypto Signal.
Generated: DETERMINISTIC_34ccb20a40c1b17e
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential profits based on investment plans
 * offered by Profitable Crypto Signal.
 * 
 * @param {number} initialInvestment - The amount of money to invest.
 * @param {number} profitRate - The expected profit rate (as a percentage).
 * @param {number} durationMonths - The duration of the investment in months.
 * @returns {object} - Returns an object containing the initial investment, 
 *                     total profit, and final amount after the investment period.
 * 
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculatePotentialProfits(initialInvestment, profitRate, durationMonths) {
  // Input validation
  if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
    throw new Error("Initial investment must be a positive number.");
  }
  if (typeof profitRate !== 'number' || profitRate <= 0) {
    throw new Error("Profit rate must be a positive number.");
  }
  if (!Number.isInteger(durationMonths) || durationMonths <= 0) {
    throw new Error("Duration must be a positive integer.");
  }

  // Convert profitRate from percentage to decimal (e.g., 5% -> 0.05)
  const monthlyProfitRate = profitRate / 100;

  // Calculate total profit
  const totalProfit = initialInvestment * monthlyProfitRate * durationMonths;

  // Calculate final amount after the investment duration
  const finalAmount = initialInvestment + totalProfit;

  // Return the results as an object
  return {
    initialInvestment: initialInvestment,
    totalProfit: totalProfit,
    finalAmount: finalAmount
  };
}

// Example usage:
// try {
//   const result = calculatePotentialProfits(1000, 5, 12);
//   console.log(result);
// } catch (error) {
//   console.error(error.message);
// }
```
