"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitinvestcoin.com
Prompt: Create a function in JavaScript to automate the calculation of daily profit returns for investment plans like those described on BitInvestCoin, with varying percentage profits.
Generated: DETERMINISTIC_95f6c85a125bc154
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate daily profit returns for investment plans.
 * 
 * @param {number} principal - The initial investment amount in USD.
 * @param {number} dailyRate - The daily profit percentage rate (e.g., 2 for 2%).
 * @param {number} days - The number of days the investment will be active.
 * @returns {number} - The total profit at the end of the given period.
 * 
 * Example:
 * const profit = calculateDailyProfit(1000, 2, 30);
 * console.log(profit); // Returns total profit for 30 days
 */
function calculateDailyProfit(principal, dailyRate, days) {
  // Input validation
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error('Invalid principal amount. Must be a positive number.');
  }
  if (typeof dailyRate !== 'number' || dailyRate <= 0) {
    throw new Error('Invalid daily rate. Must be a positive number.');
  }
  if (typeof days !== 'number' || !Number.isInteger(days) || days <= 0) {
    throw new Error('Invalid number of days. Must be a positive integer.');
  }

  // Daily profit calculation formula
  const dailyRateDecimal = dailyRate / 100; // Convert percentage to decimal
  let totalProfit = 0;

  for (let i = 1; i <= days; i++) {
    const dailyProfit = principal * dailyRateDecimal; // Calculate daily profit
    totalProfit += dailyProfit;
  }

  return totalProfit;
}

// Example usage
try {
  const principal = 1000; // Investment amount in USD
  const dailyRate = 2; // Daily profit percentage
  const days = 30; // Investment period in days
  
  const profit = calculateDailyProfit(principal, dailyRate, days);
  console.log(`Total profit after ${days} days: $${profit.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
