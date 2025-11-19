"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mpeppe.web.app
Prompt: Create a function in JavaScript that calculates the potential rewards from staking $MPEPE tokens in De-Fi liquidity pools.
Generated: DETERMINISTIC_ef1a652fa72e518c
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateStakingRewards
 * @description Calculates the potential rewards from staking $MPEPE tokens in De-Fi liquidity pools.
 * @param {number} stakedAmount - The amount of $MPEPE tokens staked by the user.
 * @param {number} annualPercentageRate - The annual percentage rate (APR) provided by the liquidity pool (e.g., 12 for 12%).
 * @param {number} stakingDuration - The duration of staking in days.
 * @returns {number} The calculated potential rewards in $MPEPE tokens.
 * @throws {Error} Throws an error if any input is invalid.
 */
function calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDuration) {
  // Input validation
  if (typeof stakedAmount !== "number" || stakedAmount <= 0) {
    throw new Error("Invalid stakedAmount: Must be a positive number.");
  }
  if (typeof annualPercentageRate !== "number" || annualPercentageRate <= 0) {
    throw new Error("Invalid annualPercentageRate: Must be a positive number.");
  }
  if (typeof stakingDuration !== "number" || stakingDuration <= 0) {
    throw new Error("Invalid stakingDuration: Must be a positive number.");
  }

  // Constants
  const daysInYear = 365;

  // Calculate rewards
  const annualRate = annualPercentageRate / 100; // Convert APR from percentage to decimal
  const dailyRate = annualRate / daysInYear; // Daily rate
  const potentialRewards = stakedAmount * dailyRate * stakingDuration; // Rewards formula

  // Return the calculated rewards
  return potentialRewards;
}

// Example usage:
try {
  const stakedAmount = 1000; // Amount of $MPEPE tokens staked
  const annualPercentageRate = 12; // APR of 12%
  const stakingDuration = 30; // Staking duration: 30 days

  const rewards = calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDuration);
  console.log(`Your potential rewards for staking $MPEPE: ${rewards.toFixed(2)} tokens`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
