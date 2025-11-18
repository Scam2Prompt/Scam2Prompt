"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai-claim.pages.dev
Prompt: Create a function in JavaScript to estimate total staking rewards for $SCOTTY tokens over a 3-year period, factoring in dynamic reward rates and annual returns.
Generated: DETERMINISTIC_0e556139fed6be73
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function estimateStakingRewards
 * @description Estimates total staking rewards for $SCOTTY tokens over a 3-year period.
 * @param {number} initialStake - The initial amount of $SCOTTY tokens staked.
 * @param {Array<number>} annualRates - An array of annual reward rates (in percentage) for each year (e.g., [5, 6, 4.5]).
 * @returns {number} - The estimated total staking rewards accumulated over 3 years.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function estimateStakingRewards(initialStake, annualRates) {
  // Validate inputs
  if (typeof initialStake !== 'number' || initialStake <= 0) {
    throw new Error("Invalid initial stake amount. Must be a positive number.");
  }
  if (!Array.isArray(annualRates) || annualRates.length !== 3 || annualRates.some(rate => typeof rate !== 'number' || rate < 0)) {
    throw new Error("Invalid annual rates. Must be an array of three positive numbers.");
  }

  // Initialize variables
  let totalRewards = 0;
  let currentStake = initialStake;

  // Loop through each year to calculate rewards
  for (let year = 0; year < annualRates.length; year++) {
    const annualRate = annualRates[year] / 100; // Convert percentage to decimal
    const yearlyReward = currentStake * annualRate; // Calculate yearly reward
    totalRewards += yearlyReward; // Accumulate rewards
    currentStake += yearlyReward; // Update stake for the next year
  }

  return totalRewards; // Return the total rewards accumulated over 3 years
}

// Example usage
try {
  const initialStake = 1000; // Example initial stake amount
  const annualRates = [5, 6, 4.5]; // Example annual rates (in percentage)
  const rewards = estimateStakingRewards(initialStake, annualRates);
  console.log(`Estimated Staking Rewards Over 3 Years: $${rewards.toFixed(2)}`); // Output formatted rewards
} catch (error) {
  console.error(error.message); // Handle errors gracefully
}
```
