"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneytreestaking.xyz
Prompt: Create a function in JavaScript to calculate staking rewards for a platform similar to Money Tree Staking.
Generated: DETERMINISTIC_2d3803508f89e60f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate staking rewards.
 * @param {number} stakedAmount - The amount of tokens staked by the user.
 * @param {number} annualPercentageRate - The annual percentage rate (APR) for staking (in percentage).
 * @param {number} daysStaked - The number of days the user has staked their tokens.
 * @returns {number} - The calculated staking rewards.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateStakingRewards(stakedAmount, annualPercentageRate, daysStaked) {
  // Input validation
  if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
    throw new Error("Invalid staked amount. Must be a positive number.");
  }
  if (typeof annualPercentageRate !== 'number' || annualPercentageRate < 0) {
    throw new Error("Invalid annual percentage rate. Must be a non-negative number.");
  }
  if (typeof daysStaked !== 'number' || daysStaked <= 0) {
    throw new Error("Invalid days staked. Must be a positive number.");
  }

  // Constants
  const daysInYear = 365; // Number of days in a year

  // Calculate staking rewards
  const dailyRate = annualPercentageRate / 100 / daysInYear; // Daily staking rate as a decimal
  const rewards = stakedAmount * dailyRate * daysStaked; // Total rewards

  return rewards;
}

// Example usage
try {
  const stakedAmount = 1000; // User has staked 1000 tokens
  const annualPercentageRate = 12; // APR is 12%
  const daysStaked = 30; // Tokens are staked for 30 days

  const rewards = calculateStakingRewards(stakedAmount, annualPercentageRate, daysStaked);
  console.log(`Staking rewards: ${rewards.toFixed(2)} tokens`);
} catch (error) {
  console.error(error.message);
}
```
