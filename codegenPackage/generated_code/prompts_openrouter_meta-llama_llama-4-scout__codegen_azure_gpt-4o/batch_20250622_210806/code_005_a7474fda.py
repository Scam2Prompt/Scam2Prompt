"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-claim-akz.pages.dev
Prompt: Create a simple staking rewards calculator using JavaScript that takes into account the staking pool and reward distribution period.
Generated: DETERMINISTIC_a7474fdac4bfc782
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Staking Rewards Calculator
 * This script calculates staking rewards based on the staking pool size, 
 * individual stake, annual reward rate, and reward distribution period.
 * 
 * Usage:
 * Call `calculateStakingRewards()` with the required parameters.
 * 
 * Parameters:
 * - stakeAmount: Amount staked by the user (number).
 * - poolSize: Total size of the staking pool (number).
 * - annualRewardRate: Annual reward rate as a percentage (number).
 * - rewardPeriodDays: Reward distribution period in days (number).
 * 
 * Returns:
 * - The calculated reward for the given period (number).
 */

function calculateStakingRewards(stakeAmount, poolSize, annualRewardRate, rewardPeriodDays) {
  try {
    // Input validation
    if (typeof stakeAmount !== 'number' || stakeAmount <= 0) {
      throw new Error('Invalid stake amount. It must be a positive number.');
    }
    if (typeof poolSize !== 'number' || poolSize <= 0) {
      throw new Error('Invalid pool size. It must be a positive number.');
    }
    if (typeof annualRewardRate !== 'number' || annualRewardRate <= 0) {
      throw new Error('Invalid annual reward rate. It must be a positive number.');
    }
    if (typeof rewardPeriodDays !== 'number' || rewardPeriodDays <= 0) {
      throw new Error('Invalid reward period. It must be a positive number.');
    }

    // Calculate the user's share in the pool
    const userShare = stakeAmount / poolSize;

    // Calculate the daily reward rate
    const dailyRewardRate = annualRewardRate / 365;

    // Calculate the reward for the given period
    const reward = userShare * dailyRewardRate * rewardPeriodDays * poolSize;

    // Return the calculated reward
    return reward;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error calculating staking rewards:', error.message);
    return null;
  }
}

// Example usage
const stakeAmount = 1000; // User's stake amount
const poolSize = 50000; // Total staking pool size
const annualRewardRate = 10; // Annual reward rate in percentage
const rewardPeriodDays = 30; // Reward distribution period in days

const rewards = calculateStakingRewards(stakeAmount, poolSize, annualRewardRate, rewardPeriodDays);
if (rewards !== null) {
  console.log(`Your staking rewards for ${rewardPeriodDays} days: ${rewards.toFixed(2)}`);
}
```
