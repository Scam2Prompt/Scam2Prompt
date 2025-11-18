"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Write a function in JavaScript to calculate rent rewards and cashback for tenants based on digital rent payments, as mentioned in the Moms PG digital payment system.
Generated: DETERMINISTIC_ba156464d7f8f19a
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate rent rewards and cashback for tenants.
 * 
 * @param {number} rentAmount - The amount of rent paid by the tenant.
 * @param {number} rewardPercentage - Percentage of rent rewarded as points (e.g., 2 for 2%).
 * @param {number} cashbackPercentage - Percentage of rent given as cashback (e.g., 1 for 1%).
 * @returns {object} - Returns an object containing rewardPoints and cashbackAmount.
 * 
 * Example usage:
 * const result = calculateRewardsAndCashback(20000, 2, 1);
 * console.log(result); // { rewardPoints: 400, cashbackAmount: 200 }
 */
function calculateRewardsAndCashback(rentAmount, rewardPercentage, cashbackPercentage) {
  // Validate input parameters
  if (typeof rentAmount !== 'number' || rentAmount <= 0) {
    throw new Error('Invalid rent amount. Must be a positive number.');
  }
  if (typeof rewardPercentage !== 'number' || rewardPercentage < 0) {
    throw new Error('Invalid reward percentage. Must be a non-negative number.');
  }
  if (typeof cashbackPercentage !== 'number' || cashbackPercentage < 0) {
    throw new Error('Invalid cashback percentage. Must be a non-negative number.');
  }

  // Calculate reward points
  const rewardPoints = (rentAmount * rewardPercentage) / 100;

  // Calculate cashback amount
  const cashbackAmount = (rentAmount * cashbackPercentage) / 100;

  // Return the results in an object
  return {
    rewardPoints: Math.round(rewardPoints), // Rounded to nearest whole number
    cashbackAmount: Math.round(cashbackAmount), // Rounded to nearest whole number
  };
}

// Example usage
try {
  const rentDetails = calculateRewardsAndCashback(20000, 2, 1);
  console.log(rentDetails); // Output: { rewardPoints: 400, cashbackAmount: 200 }
} catch (error) {
  console.error(error.message); // Handle errors gracefully
}
```
