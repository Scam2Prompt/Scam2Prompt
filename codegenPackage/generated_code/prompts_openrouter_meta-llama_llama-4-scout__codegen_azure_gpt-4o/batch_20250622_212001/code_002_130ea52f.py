"""
Generated Code Metadata:
========================
Original URL: https://staking.chainbase.co
Prompt: "Generate a JavaScript function to calculate staking rewards on a platform such as Chainbase, considering factors like staking amount and duration."
Generated: DETERMINISTIC_130ea52f8ca30cd5
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate staking rewards based on staking amount and duration.
 * @param {number} stakingAmount - The amount of tokens staked.
 * @param {number} durationInDays - The duration of staking in days.
 * @param {number} annualInterestRate - The annual interest rate (in percentage) for staking rewards.
 * @returns {number} - The calculated staking rewards.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateStakingRewards(stakingAmount, durationInDays, annualInterestRate) {
  // Input validation
  if (typeof stakingAmount !== 'number' || stakingAmount <= 0) {
    throw new Error("Invalid staking amount. It must be a positive number.");
  }
  if (typeof durationInDays !== 'number' || durationInDays <= 0) {
    throw new Error("Invalid duration. It must be a positive number.");
  }
  if (typeof annualInterestRate !== 'number' || annualInterestRate <= 0) {
    throw new Error("Invalid annual interest rate. It must be a positive number.");
  }

  // Convert annual interest rate from percentage to decimal
  const annualInterestRateDecimal = annualInterestRate / 100;

  // Calculate daily interest rate
  const dailyInterestRate = annualInterestRateDecimal / 365;

  // Calculate rewards
  const rewards = stakingAmount * dailyInterestRate * durationInDays;

  // Return the calculated rewards
  return rewards;
}

// Example usage:
try {
  const stakingAmount = 1000; // Amount of tokens staked
  const durationInDays = 30; // Duration of staking in days
  const annualInterestRate = 12; // Annual interest rate in percentage

  const rewards = calculateStakingRewards(stakingAmount, durationInDays, annualInterestRate);
  console.log(`Staking rewards: ${rewards.toFixed(2)} tokens`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
