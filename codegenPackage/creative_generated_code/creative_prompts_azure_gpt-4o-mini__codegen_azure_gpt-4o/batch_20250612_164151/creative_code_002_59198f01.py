"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Create a JavaScript function that calculates potential staking rewards based on the double staking feature of the Pepe Unchained ecosystem.
Generated: DETERMINISTIC_59198f01c094750a
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential staking rewards based on the double staking feature
 * of the Pepe Unchained ecosystem.
 *
 * @param {number} initialStake - The amount of tokens initially staked.
 * @param {number} baseRewardRate - The annual base reward rate (as a percentage).
 * @param {number} doubleStakingMultiplier - The multiplier for double staking rewards.
 * @param {number} stakingDuration - The duration of staking in days.
 * @returns {number} - The total potential reward after the staking duration.
 *
 * @throws {Error} - Throws an error if any input parameter is invalid.
 */
function calculateStakingRewards(initialStake, baseRewardRate, doubleStakingMultiplier, stakingDuration) {
  // Input validation
  if (
    typeof initialStake !== 'number' || initialStake <= 0 ||
    typeof baseRewardRate !== 'number' || baseRewardRate <= 0 ||
    typeof doubleStakingMultiplier !== 'number' || doubleStakingMultiplier <= 0 ||
    typeof stakingDuration !== 'number' || stakingDuration <= 0
  ) {
    throw new Error("Invalid input: All parameters must be positive numbers.");
  }

  // Constants
  const DAYS_IN_YEAR = 365;

  // Calculate base reward for the staking duration
  const baseReward = (initialStake * (baseRewardRate / 100)) * (stakingDuration / DAYS_IN_YEAR);

  // Calculate double staking reward using the multiplier
  const doubleStakingReward = baseReward * doubleStakingMultiplier;

  // Total reward
  const totalReward = baseReward + doubleStakingReward;

  return totalReward;
}

// Example usage
try {
  const initialStake = 1000; // Tokens
  const baseRewardRate = 10; // Annual reward rate in percentage
  const doubleStakingMultiplier = 2; // Multiplier for double staking
  const stakingDuration = 30; // Staking duration in days

  const rewards = calculateStakingRewards(initialStake, baseRewardRate, doubleStakingMultiplier, stakingDuration);
  console.log(`Total potential staking rewards: ${rewards.toFixed(2)} tokens`);
} catch (error) {
  console.error(error.message);
}
```
