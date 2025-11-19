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
 * Calculates the potential returns based on the investment plan.
 * 
 * Capital Wealth Investment Ltd offers the following plans:
 * - Classic: 5% annual return
 * - Pro: 8% annual return
 * - Gold: 12% annual return
 * 
 * @param {string} plan - The investment plan ("Classic", "Pro", or "Gold").
 * @param {number} principal - The initial investment amount (must be positive).
 * @param {number} years - The duration of the investment in years (must be positive).
 * @returns {number} - The total returns after the specified duration, rounded to two decimal places.
 * @throws Will throw an error if the input is invalid or the plan is unsupported.
 */
function calculateReturns(plan, principal, years) {
  // Validate inputs
  if (typeof plan !== 'string' || !["Classic", "Pro", "Gold"].includes(plan)) {
    throw new Error("Invalid plan. Supported plans are 'Classic', 'Pro', and 'Gold'.");
  }
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error("Invalid principal amount. It must be a positive number.");
  }
  if (typeof years !== 'number' || years <= 0) {
    throw new Error("Invalid number of years. It must be a positive number.");
  }

  // Define annual return rates for each plan
  const annualRates = {
    "Classic": 0.05,
    "Pro": 0.08,
    "Gold": 0.12
  };

  // Calculate potential returns using compound interest formula
  const rate = annualRates[plan];
  const totalReturns = principal * Math.pow((1 + rate), years);

  // Return the result rounded to two decimal places
  return parseFloat(totalReturns.toFixed(2));
}

// Example usage:
try {
  const plan = "Gold";
  const principal = 10000;
  const years = 5;
  const returns = calculateReturns(plan, principal, years);
  console.log(`Potential returns for ${plan} plan: $${returns}`);
} catch (error) {
  console.error(error.message);
}
```
