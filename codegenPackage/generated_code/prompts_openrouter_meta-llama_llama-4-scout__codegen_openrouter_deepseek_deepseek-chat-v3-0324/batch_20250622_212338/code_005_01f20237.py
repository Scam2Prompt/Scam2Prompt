"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Write a code snippet in JavaScript to calculate the rewards earned by holding Mello Tokens, given the 3% transaction distribution mechanism.
Generated: DETERMINISTIC_01f20237765e612a
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates rewards earned by holding Mello Tokens based on transaction distribution.
 * 
 * @param {number} totalTransactionAmount - Total amount of the transaction in tokens
 * @param {number} holderBalance - Current balance of the token holder
 * @param {number} totalSupply - Total supply of tokens in circulation
 * @param {number} distributionPercentage - Percentage to distribute as rewards (default: 3%)
 * @returns {number} Calculated reward amount
 * @throws {Error} If any parameter is invalid
 */
function calculateMelloRewards(
  totalTransactionAmount,
  holderBalance,
  totalSupply,
  distributionPercentage = 3
) {
  // Validate input parameters
  if (typeof totalTransactionAmount !== 'number' || totalTransactionAmount <= 0) {
    throw new Error('Total transaction amount must be a positive number');
  }
  if (typeof holderBalance !== 'number' || holderBalance < 0) {
    throw new Error('Holder balance must be a non-negative number');
  }
  if (typeof totalSupply !== 'number' || totalSupply <= 0) {
    throw new Error('Total supply must be a positive number');
  }
  if (typeof distributionPercentage !== 'number' || distributionPercentage <= 0) {
    throw new Error('Distribution percentage must be a positive number');
  }

  // Calculate reward amount
  const rewardPool = totalTransactionAmount * (distributionPercentage / 100);
  const rewardAmount = (holderBalance / totalSupply) * rewardPool;

  // Round to 8 decimal places to avoid floating point precision issues
  return parseFloat(rewardAmount.toFixed(8));
}

// Example usage:
try {
  const reward = calculateMelloRewards(1000, 5000, 1000000);
  console.log(`Reward earned: ${reward} tokens`);
} catch (error) {
  console.error('Error calculating rewards:', error.message);
}
```
