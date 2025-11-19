"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-claim.pages.dev
Prompt: Create a JavaScript function that calculates potential rewards from staking $PEPU tokens based on the provided staking percentages.
Generated: DETERMINISTIC_037b7d9913bd40c0
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential rewards from staking $PEPU tokens.
 * 
 * @param {number} stakedAmount - The amount of $PEPU tokens staked by the user.
 * @param {number} annualPercentageRate - The annual staking percentage reward (APR) as a percentage (e.g., 10 for 10%).
 * @param {number} stakingDurationDays - The duration of staking in days.
 * 
 * @returns {number} - The calculated staking reward in $PEPU tokens.
 * 
 * @throws {Error} - Throws an error if invalid input values are provided.
 */
function calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDurationDays) {
  // Validate input parameters
  if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
    throw new Error('Invalid staked amount. It must be a positive number.');
  }
  if (typeof annualPercentageRate !== 'number' || annualPercentageRate <= 0) {
    throw new Error('Invalid annual percentage rate (APR). It must be a positive number.');
  }
  if (typeof stakingDurationDays !== 'number' || stakingDurationDays <= 0) {
    throw new Error('Invalid staking duration. It must be a positive number.');
  }

  // Constants
  const daysInYear = 365; // Number of days in a year

  // Calculate daily rate (APR divided by 365)
  const dailyRate = annualPercentageRate / daysInYear / 100;

  // Calculate rewards
  const potentialRewards = stakedAmount * dailyRate * stakingDurationDays;

  // Return rounded rewards for better readability
  return parseFloat(potentialRewards.toFixed(2));
}

// Example usage
try {
  const stakedAmount = 1000; // Example: User stakes 1000 $PEPU tokens
  const annualPercentageRate = 12; // Example: 12% APR
  const stakingDurationDays = 30; // Example: Staking for 30 days

  const rewards = calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDurationDays);
  console.log(`Potential rewards for staking: ${rewards} $PEPU tokens`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
