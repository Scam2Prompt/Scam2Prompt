"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-io.pages.dev
Prompt: Write JavaScript code to calculate staking rewards for $PEPU tokens based on the double staking rewards mechanism described on Pepe Unchained.
Generated: DETERMINISTIC_4c257112e5c0edc7
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate $PEPU staking rewards based on double staking rewards mechanism.
 * 
 * Double staking rewards mechanism:
 * 1. Base Reward: A fixed percentage applied to the staked amount.
 * 2. Bonus Reward: An additional percentage applied based on staking duration.
 * 
 * @param {number} stakedAmount - The amount of $PEPU tokens staked.
 * @param {number} stakingDuration - Duration of staking in days.
 * @returns {number} Total rewards (base + bonus) in $PEPU tokens.
 */

function calculateStakingRewards(stakedAmount, stakingDuration) {
  try {
    // Input validation
    if (typeof stakedAmount !== "number" || stakedAmount <= 0) {
      throw new Error("Invalid staked amount. Must be a positive number.");
    }
    if (typeof stakingDuration !== "number" || stakingDuration <= 0) {
      throw new Error("Invalid staking duration. Must be a positive number.");
    }

    // Constants
    const BASE_REWARD_PERCENTAGE = 0.10; // 10% base reward
    const BONUS_REWARD_PERCENTAGE = 0.001; // 0.1% bonus per day

    // Calculate base reward
    const baseReward = stakedAmount * BASE_REWARD_PERCENTAGE;

    // Calculate bonus reward (capped at 30 days for bonus calculation)
    const cappedDuration = Math.min(stakingDuration, 30); // Maximum bonus duration is 30 days
    const bonusReward = stakedAmount * (BONUS_REWARD_PERCENTAGE * cappedDuration);

    // Calculate total reward
    const totalReward = baseReward + bonusReward;

    return totalReward;
  } catch (error) {
    console.error("Error calculating staking rewards:", error.message);
    return 0; // Return 0 rewards in case of error
  }
}

// Example Usage
const stakedAmount = 1000; // $PEPU tokens staked
const stakingDuration = 45; // Staking duration in days

const rewards = calculateStakingRewards(stakedAmount, stakingDuration);
console.log(`Total staking rewards: ${rewards} $PEPU tokens`);
```
