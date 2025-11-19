"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Write a JavaScript function that calculates potential returns from the Coinex Tradings investment plans, given an initial investment amount and the plan selected.
Generated: DETERMINISTIC_7082cbf2815f0548
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential returns from Coinex Tradings investment plans.
 *
 * @param {number} initialInvestment - The initial investment amount.
 * @param {string} plan - The selected investment plan ('Basic', 'Pro', 'Elite').
 * @returns {number} - The calculated potential returns.
 * @throws Will throw an error if the input is invalid.
 */
function calculatePotentialReturns(initialInvestment, plan) {
  // Validate input
  if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
    throw new Error('Initial investment must be a positive number.');
  }

  if (!['Basic', 'Pro', 'Elite'].includes(plan)) {
    throw new Error('Invalid plan selected. Choose "Basic", "Pro", or "Elite".');
  }

  // Define the return rates for each plan
  const returnRates = {
    Basic: 0.05,  // 5% monthly return
    Pro: 0.1,     // 10% monthly return
    Elite: 0.15   // 15% monthly return
  };

  // Calculate potential returns
  const monthlyRate = returnRates[plan];
  const potentialReturns = initialInvestment * monthlyRate;

  // Return the calculated potential returns
  return potentialReturns;
}

// Example usage:
try {
  const initialInvestment = 1000; // Replace with your investment amount
  const plan = 'Pro'; // Replace with your selected plan ('Basic', 'Pro', 'Elite')
  const returns = calculatePotentialReturns(initialInvestment, plan);
  console.log(`Potential returns for ${plan} plan: $${returns.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
