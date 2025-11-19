"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secured-greenbitcoin.pages.dev
Prompt: Create a JavaScript function to calculate potential rewards from staking $GBTC based on the current staking percentage and token amount.
Generated: DETERMINISTIC_dfef0733380ceee9
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential rewards from staking $GBTC.
 * 
 * @param {number} tokenAmount - The amount of $GBTC tokens staked.
 * @param {number} stakingPercentage - The annual staking percentage (e.g., 5 for 5%).
 * @param {number} durationInDays - The staking duration in days.
 * @returns {number} - The potential reward earned from staking.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateStakingRewards(tokenAmount, stakingPercentage, durationInDays) {
  // Input validation
  if (typeof tokenAmount !== 'number' || tokenAmount <= 0) {
    throw new Error("Invalid token amount. Must be a positive number.");
  }
  if (typeof stakingPercentage !== 'number' || stakingPercentage <= 0) {
    throw new Error("Invalid staking percentage. Must be a positive number.");
  }
  if (typeof durationInDays !== 'number' || durationInDays <= 0) {
    throw new Error("Invalid duration. Must be a positive number.");
  }

  // Constants
  const DAYS_IN_YEAR = 365;

  // Calculate annual rewards
  const annualReward = (tokenAmount * stakingPercentage) / 100;

  // Calculate rewards for the given duration
  const rewardsForDuration = (annualReward / DAYS_IN_YEAR) * durationInDays;

  // Return the calculated reward
  return rewardsForDuration;
}

// Example usage:
try {
  const tokenAmount = 1000; // Amount of GBTC tokens staked
  const stakingPercentage = 5; // Annual staking rate in percentage
  const durationInDays = 30; // Duration in days

  const rewards = calculateStakingRewards(tokenAmount, stakingPercentage, durationInDays);
  console.log(`Potential staking rewards: $${rewards.toFixed(2)} GBTC`);
} catch (error) {
  console.error(error.message);
}
```
