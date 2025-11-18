"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Develop a JavaScript function to calculate cashback rewards for users based on the tiered system described in VZ99's promotions.
Generated: DETERMINISTIC_887e1af898056726
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate cashback rewards based on a tiered system.
 * 
 * Cashback tiers:
 * - Tier 1: Spend up to $100, cashback rate is 1%.
 * - Tier 2: Spend between $101 and $500, cashback rate is 2%.
 * - Tier 3: Spend above $500, cashback rate is 5%.
 *
 * @param {number} spendingAmount - The total amount spent by the user.
 * @returns {number} - The cashback reward earned.
 * @throws {Error} - If the spendingAmount is not a valid positive number.
 */
function calculateCashback(spendingAmount) {
  // Validate input
  if (typeof spendingAmount !== 'number' || spendingAmount < 0) {
    throw new Error('Invalid spending amount. It must be a positive number.');
  }

  let cashbackReward = 0;

  // Tier calculations
  if (spendingAmount <= 100) {
    cashbackReward = spendingAmount * 0.01; // 1% cashback for Tier 1
  } else if (spendingAmount <= 500) {
    cashbackReward = 100 * 0.01 + (spendingAmount - 100) * 0.02; // Calculate Tier 1 + Tier 2
  } else {
    cashbackReward = 100 * 0.01 + 400 * 0.02 + (spendingAmount - 500) * 0.05; // Calculate Tier 1 + Tier 2 + Tier 3
  }

  // Round cashback reward to two decimal places for consistency
  cashbackReward = parseFloat(cashbackReward.toFixed(2));

  return cashbackReward;
}

// Example usage
try {
  const spendingAmount = 750; // Replace with dynamic input as needed
  const cashback = calculateCashback(spendingAmount);
  console.log(`Cashback Reward: $${cashback}`);
} catch (error) {
  console.error(error.message);
}
```
