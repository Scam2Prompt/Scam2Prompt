"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Create a function in JavaScript that calculates the potential staking rewards for $MIND token holders based on the dynamic APY rates provided during the presale.
Generated: DETERMINISTIC_763d7f9a9d65ab3a
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential staking rewards for $MIND token holders based on dynamic APY rates.
 *
 * @param {number} principal - The amount of $MIND tokens being staked.
 * @param {number} apy - The annual percentage yield (APY) expressed as a percentage (e.g., 20 for 20% APY).
 * @param {number} days - The number of days the tokens will be staked.
 * @returns {number} - The potential staking rewards in $MIND tokens.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateStakingRewards(principal, apy, days) {
  // Input validation
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error('Invalid principal amount. It must be a positive number.');
  }
  if (typeof apy !== 'number' || apy < 0) {
    throw new Error('Invalid APY. It must be a non-negative number.');
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error('Invalid number of days. It must be a positive number.');
  }

  // Convert APY percentage to a decimal (e.g., 20% -> 0.20)
  const apyDecimal = apy / 100;

  // Calculate daily APY rate
  const dailyRate = apyDecimal / 365;

  // Calculate rewards
  const rewards = principal * dailyRate * days;

  // Return the rewards rounded to 4 decimal places for precision
  return parseFloat(rewards.toFixed(4));
}

// Example usage
try {
  const principal = 1000; // Amount of $MIND tokens
  const apy = 20; // APY in percentage
  const days = 30; // Number of days staked

  const rewards = calculateStakingRewards(principal, apy, days);
  console.log(`Potential staking rewards: ${rewards} $MIND tokens`);
} catch (error) {
  console.error(`Error calculating staking rewards: ${error.message}`);
}
```
