"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topdigitaltrade.com.simplebittstockoption.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans (Silver, Gold, Premium) offered by Topdigitaltrade.
Generated: DETERMINISTIC_cb86db8e69e689b1
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential profits based on investment plans.
 * @param {string} plan - The investment plan ("Silver", "Gold", "Premium").
 * @param {number} investmentAmount - The amount of money invested.
 * @returns {number|string} - The potential profit or an error message if inputs are invalid.
 */
function calculateProfit(plan, investmentAmount) {
  // Validate inputs
  if (typeof plan !== 'string' || typeof investmentAmount !== 'number' || investmentAmount <= 0) {
    return 'Invalid input. Please provide a valid plan and a positive investment amount.';
  }

  // Define profit rates for each plan
  const profitRates = {
    Silver: 0.05,    // 5% profit
    Gold: 0.1,       // 10% profit
    Premium: 0.2     // 20% profit
  };

  // Convert plan to lowercase for case-insensitivity
  const normalizedPlan = plan.trim().charAt(0).toUpperCase() + plan.trim().slice(1).toLowerCase();

  // Calculate and return profit if the plan exists
  if (profitRates[normalizedPlan]) {
    const profit = investmentAmount * profitRates[normalizedPlan];
    return profit; // Return the calculated profit
  } else {
    return 'Invalid plan. Please choose between "Silver", "Gold", or "Premium".';
  }
}

// Example usage:
console.log(calculateProfit('Silver', 1000));    // Outputs: 50
console.log(calculateProfit('Gold', 1000));      // Outputs: 100
console.log(calculateProfit('Premium', 1000));   // Outputs: 200
console.log(calculateProfit('Invalid', 1000));   // Outputs: Invalid plan. Please choose between "Silver", "Gold", or "Premium".
console.log(calculateProfit('Gold', -500));      // Outputs: Invalid input. Please provide a valid plan and a positive investment amount.
```
