"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-en.web.app
Prompt: Develop a staking calculator in JavaScript that takes into account the $QUBE token rewards pool and calculates potential earnings for investors.
Generated: DETERMINISTIC_3bc7e1130a0ce8ec
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Staking Calculator for $QUBE token rewards pool
 */

class StakingCalculator {
  /**
   * Constructor for StakingCalculator
   * @param {number} rewardsPool - The total $QUBE token rewards pool
   * @param {number} stakingDuration - The staking duration in days
   * @param {number} totalStaked - The total amount of $QUBE tokens staked
   */
  constructor(rewardsPool, stakingDuration, totalStaked) {
    this.rewardsPool = rewardsPool;
    this.stakingDuration = stakingDuration;
    this.totalStaked = totalStaked;
  }

  /**
   * Calculates the daily rewards rate
   * @returns {number} The daily rewards rate
   */
  calculateDailyRewardsRate() {
    // Assuming the rewards pool is distributed evenly over the staking duration
    return this.rewardsPool / this.stakingDuration;
  }

  /**
   * Calculates the potential earnings for an investor
   * @param {number} stakedAmount - The amount of $QUBE tokens staked by the investor
   * @returns {number} The potential earnings for the investor
   */
  calculatePotentialEarnings(stakedAmount) {
    // Calculate the percentage of the total staked amount
    const stakedPercentage = stakedAmount / this.totalStaked;

    // Calculate the daily rewards for the investor
    const dailyRewards = this.calculateDailyRewardsRate() * stakedPercentage;

    // Calculate the total potential earnings for the staking duration
    return dailyRewards * this.stakingDuration;
  }

  /**
   * Calculates the APY (Annual Percentage Yield) for the investor
   * @param {number} stakedAmount - The amount of $QUBE tokens staked by the investor
   * @returns {number} The APY for the investor
   */
  calculateAPY(stakedAmount) {
    // Calculate the potential earnings for the investor
    const potentialEarnings = this.calculatePotentialEarnings(stakedAmount);

    // Calculate the APY
    return (potentialEarnings / stakedAmount) * 100;
  }
}

// Example usage
try {
  const rewardsPool = 1000000; // $QUBE token rewards pool
  const stakingDuration = 30; // Staking duration in days
  const totalStaked = 5000000; // Total amount of $QUBE tokens staked

  const stakingCalculator = new StakingCalculator(rewardsPool, stakingDuration, totalStaked);

  const stakedAmount = 10000; // Amount of $QUBE tokens staked by the investor
  const potentialEarnings = stakingCalculator.calculatePotentialEarnings(stakedAmount);
  const apy = stakingCalculator.calculateAPY(stakedAmount);

  console.log(`Potential earnings: $${potentialEarnings.toFixed(2)}`);
  console.log(`APY: ${apy.toFixed(2)}%`);
} catch (error) {
  console.error('Error:', error.message);
}
```
