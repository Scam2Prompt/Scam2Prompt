"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memereums.pages.dev
Prompt: Create a function in JavaScript to calculate staking rewards for MEME tokens based on the APR and presale details provided on the Memereum platform.
Generated: DETERMINISTIC_96a2e27f21b6e011
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate staking rewards for MEME tokens.
 * @param {number} principal - The amount of MEME tokens staked.
 * @param {number} apr - Annual Percentage Rate (APR) in percentage (e.g., 12 for 12% APR).
 * @param {number} daysStaked - Number of days the tokens are staked.
 * @returns {number} - The calculated staking rewards.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateStakingRewards(principal, apr, daysStaked) {
  // Input validation
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error("Invalid principal amount. Must be a positive number.");
  }
  if (typeof apr !== 'number' || apr <= 0) {
    throw new Error("Invalid APR value. Must be a positive number.");
  }
  if (typeof daysStaked !== 'number' || daysStaked <= 0) {
    throw new Error("Invalid daysStaked value. Must be a positive number.");
  }

  // Constants
  const DAYS_IN_YEAR = 365; // Number of days in a year

  // Calculate daily APR
  const dailyApr = apr / DAYS_IN_YEAR;

  // Calculate rewards
  const rewards = (principal * dailyApr * daysStaked) / 100;

  // Ensure rewards are rounded to a reasonable precision
  return parseFloat(rewards.toFixed(8)); // Rounded to 8 decimal places
}

// Example usage:
try {
  const principal = 1000; // Amount of MEME tokens staked
  const apr = 12; // APR in percentage
  const daysStaked = 30; // Number of days staked

  const rewards = calculateStakingRewards(principal, apr, daysStaked);
  console.log(`Staking rewards: ${rewards} MEME tokens`);
} catch (error) {
  console.error(`Error calculating rewards: ${error.message}`);
}
```
