"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-wienerdogai.pages.dev
Prompt: Write a JavaScript function to calculate staking rewards for a token like $WAI, based on the total staked tokens and an annual percentage yield (APY).
Generated: DETERMINISTIC_c2c7a0aee04a16fd
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate staking rewards for a token.
 * @param {number} totalStaked - Total tokens staked (e.g., amount of $WAI staked).
 * @param {number} apy - Annual Percentage Yield (APY) as a percentage (e.g., 5 for 5% APY).
 * @param {number} daysStaked - Number of days tokens have been staked.
 * @returns {number} - The staking reward earned.
 * @throws Will throw an error if invalid inputs are provided.
 */
function calculateStakingRewards(totalStaked, apy, daysStaked) {
  // Validate inputs
  if (typeof totalStaked !== "number" || totalStaked <= 0) {
    throw new Error("Invalid totalStaked value. Must be a positive number.");
  }
  if (typeof apy !== "number" || apy <= 0) {
    throw new Error("Invalid APY value. Must be a positive number.");
  }
  if (typeof daysStaked !== "number" || daysStaked <= 0) {
    throw new Error("Invalid daysStaked value. Must be a positive number.");
  }

  // Convert APY percentage to a decimal (e.g., 5% -> 0.05)
  const apyDecimal = apy / 100;

  // Calculate daily reward rate
  const dailyRate = apyDecimal / 365;

  // Calculate staking rewards
  const rewards = totalStaked * dailyRate * daysStaked;

  return rewards;
}

// Example Usage:
try {
  const totalStaked = 1000; // Example: 1000 tokens staked
  const apy = 5; // Example: 5% APY
  const daysStaked = 30; // Example: Staked for 30 days

  const rewards = calculateStakingRewards(totalStaked, apy, daysStaked);
  console.log(`Staking rewards earned: ${rewards.toFixed(2)} tokens`);
} catch (error) {
  console.error(error.message);
}
```
