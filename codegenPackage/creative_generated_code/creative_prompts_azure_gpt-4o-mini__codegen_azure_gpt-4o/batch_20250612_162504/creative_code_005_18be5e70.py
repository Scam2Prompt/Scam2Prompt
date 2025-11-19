"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-i.pages.dev
Prompt: Create a rewards calculator function in JavaScript that estimates potential earnings from staking DOGE20 tokens at different price points.
Generated: DETERMINISTIC_18be5e70dc20f33e
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Rewards Calculator for Staking DOGE20 Tokens
 * This function calculates potential earnings based on the number of tokens staked,
 * staking duration, annual percentage yield (APY), and the expected price of the token.
 *
 * @param {number} stakedTokens - Number of DOGE20 tokens staked.
 * @param {number} stakingDuration - Duration of staking in months.
 * @param {number} annualYieldPercentage - Annual Percentage Yield (APY) as a decimal (e.g., 0.12 for 12%).
 * @param {number} expectedTokenPrice - Expected future price of a single DOGE20 token.
 * @returns {object} An object containing:
 *   - estimatedRewards: Number of DOGE20 tokens earned as rewards.
 *   - estimatedEarningsUSD: The value of the rewards in USD based on the expected token price.
 * @throws Will throw an error if any input is invalid (non-positive number or undefined).
 */

function calculateRewards(stakedTokens, stakingDuration, annualYieldPercentage, expectedTokenPrice) {
  // Input validation
  if (
    typeof stakedTokens !== 'number' || stakedTokens <= 0 ||
    typeof stakingDuration !== 'number' || stakingDuration <= 0 ||
    typeof annualYieldPercentage !== 'number' || annualYieldPercentage <= 0 ||
    typeof expectedTokenPrice !== 'number' || expectedTokenPrice <= 0
  ) {
    throw new Error("All inputs must be positive numbers.");
  }

  // Convert staking duration from months to years
  const stakingDurationInYears = stakingDuration / 12;

  // Calculate estimated rewards in DOGE20 tokens
  const estimatedRewards = stakedTokens * annualYieldPercentage * stakingDurationInYears;

  // Calculate potential earnings in USD based on expected token price
  const estimatedEarningsUSD = estimatedRewards * expectedTokenPrice;

  // Return the results as an object
  return {
    estimatedRewards: parseFloat(estimatedRewards.toFixed(2)),  // Round to 2 decimal places for readability
    estimatedEarningsUSD: parseFloat(estimatedEarningsUSD.toFixed(2)) // Round to 2 decimal places for readability
  };
}

// Example usage:
try {
  const rewards = calculateRewards(1000, 6, 0.12, 0.50); // 1000 tokens staked for 6 months at 12% APY, expected price $0.50
  console.log("Estimated Rewards:", rewards.estimatedRewards, "DOGE20 tokens");
  console.log("Estimated Earnings (USD): $", rewards.estimatedEarningsUSD);
} catch (error) {
  console.error("Error calculating rewards:", error.message);
}
```
