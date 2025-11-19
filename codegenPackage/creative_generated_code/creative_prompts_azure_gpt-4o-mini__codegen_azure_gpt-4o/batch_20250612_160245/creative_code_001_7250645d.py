"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxbinaryinvestpro.com
Prompt: Write a JavaScript function to calculate potential returns based on the investment plans offered by Fxbinaryinvestpro.
Generated: DETERMINISTIC_7250645de9ef3397
Batch ID: 20250612_160245
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
 * @param {number} principal - The initial investment amount.
 * @param {string} plan - The investment plan ("silver", "gold", "platinum").
 * @param {number} duration - The investment duration in months.
 * @returns {number} - The potential returns from the investment.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculatePotentialReturns(principal, plan, duration) {
  // Validate inputs
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error('Invalid principal amount. It must be a positive number.');
  }
  if (typeof plan !== 'string' || !["silver", "gold", "platinum"].includes(plan.toLowerCase())) {
    throw new Error('Invalid investment plan. Choose from "silver", "gold", or "platinum".');
  }
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error('Invalid duration. It must be a positive number.');
  }

  // Define the rate of returns for each plan (monthly percentage rates)
  const rates = {
    silver: 0.05,     // 5% monthly return
    gold: 0.07,       // 7% monthly return
    platinum: 0.10    // 10% monthly return
  };

  // Calculate the total returns
  const monthlyRate = rates[plan.toLowerCase()];
  const totalReturns = principal * Math.pow(1 + monthlyRate, duration);

  // Return the rounded total returns
  return Number(totalReturns.toFixed(2));
}

// Example usage:
try {
  const principal = 1000; // Investment amount in dollars
  const plan = "gold";    // Investment plan
  const duration = 12;    // Duration in months

  const returns = calculatePotentialReturns(principal, plan, duration);
  console.log(`The potential returns for your investment are: $${returns}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
