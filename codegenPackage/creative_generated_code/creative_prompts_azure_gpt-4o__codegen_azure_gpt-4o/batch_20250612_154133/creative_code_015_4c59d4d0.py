"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Write a JavaScript function to calculate staking rewards dynamically based on the APY provided by a platform like Crypto All-Stars.
Generated: DETERMINISTIC_4c59d4d093b449ff
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate staking rewards dynamically based on Annual Percentage Yield (APY).
 * 
 * @param {number} initialStake - The initial amount staked.
 * @param {number} apy - The Annual Percentage Yield (in percentage, e.g., 10 for 10% APY).
 * @param {number} days - The number of days the stake is locked for rewards.
 * @returns {number} - The total staking rewards earned based on the input parameters.
 * 
 * Usage:
 * const rewards = calculateStakingRewards(1000, 12, 30);
 * console.log(rewards); // Outputs the calculated rewards
 */
function calculateStakingRewards(initialStake, apy, days) {
  // Input validation to ensure valid and safe calculations
  if (typeof initialStake !== 'number' || initialStake <= 0) {
    throw new Error("Invalid initialStake: must be a positive number.");
  }
  if (typeof apy !== 'number' || apy <= 0) {
    throw new Error("Invalid APY: must be a positive number.");
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error("Invalid days: must be a positive number.");
  }

  // Calculate daily yield from APY
  const dailyYield = apy / 100 / 365; // APY is divided by 100 to convert percentage, and further divided by 365 days

  // Calculate staking rewards
  const rewards = initialStake * dailyYield * days;

  return rewards;
}

// Example usage
try {
  const initialStake = 1000; // Example: $1000 staked
  const apy = 12; // Example: 12% APY
  const days = 30; // Example: staked for 30 days

  const stakingRewards = calculateStakingRewards(initialStake, apy, days);
  console.log(`Staking rewards earned: $${stakingRewards.toFixed(2)}`);
} catch (error) {
  console.error(`Error calculating staking rewards: ${error.message}`);
}
```
