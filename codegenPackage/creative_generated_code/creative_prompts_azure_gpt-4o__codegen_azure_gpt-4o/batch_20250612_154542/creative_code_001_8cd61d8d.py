"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Create a function in JavaScript that calculates the total profit and monthly interest for CoineeHub's VIP Plan, given an initial investment amount and duration.
Generated: DETERMINISTIC_8cd61d8dd571924b
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total profit and monthly interest for CoineeHub's VIP Plan.
 * 
 * @param {number} initialInvestment - The initial investment amount in dollars.
 * @param {number} durationMonths - The duration of the investment in months.
 * @throws {Error} Throws an error if inputs are invalid (non-positive numbers).
 * @returns {Object} Returns an object containing total profit and monthly interest.
 */
function calculateVIPPlanProfit(initialInvestment, durationMonths) {
  // Validate inputs
  if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
    throw new Error('Initial investment must be a positive number.');
  }

  if (typeof durationMonths !== 'number' || durationMonths <= 0) {
    throw new Error('Duration must be a positive number.');
  }

  // Constants for VIP Plan
  const monthlyInterestRate = 0.05; // 5% monthly interest rate

  // Calculate monthly interest
  const monthlyInterest = initialInvestment * monthlyInterestRate;

  // Calculate total profit for the given duration
  const totalProfit = monthlyInterest * durationMonths;

  // Return the calculated values
  return {
    totalProfit: totalProfit.toFixed(2), // Total profit rounded to two decimal places
    monthlyInterest: monthlyInterest.toFixed(2) // Monthly interest rounded to two decimal places
  };
}

// Example usage:
try {
  const result = calculateVIPPlanProfit(1000, 12);
  console.log('Total Profit:', result.totalProfit); // Output: Total Profit: 600.00
  console.log('Monthly Interest:', result.monthlyInterest); // Output: Monthly Interest: 50.00
} catch (error) {
  console.error('Error:', error.message);
}
```
