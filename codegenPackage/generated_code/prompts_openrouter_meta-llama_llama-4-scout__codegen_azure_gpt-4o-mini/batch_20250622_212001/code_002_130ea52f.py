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
 * Calculates staking rewards based on the staking amount, duration, and annual interest rate.
 * 
 * @param {number} stakingAmount - The amount of tokens staked.
 * @param {number} durationInDays - The duration for which the tokens are staked, in days.
 * @param {number} annualInterestRate - The annual interest rate as a percentage (e.g., 5 for 5%).
 * @returns {number} - The calculated staking rewards.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateStakingRewards(stakingAmount, durationInDays, annualInterestRate) {
    // Validate inputs
    if (typeof stakingAmount !== 'number' || stakingAmount <= 0) {
        throw new Error('Invalid staking amount. It must be a positive number.');
    }
    if (typeof durationInDays !== 'number' || durationInDays <= 0) {
        throw new Error('Invalid duration. It must be a positive number.');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate < 0) {
        throw new Error('Invalid annual interest rate. It must be a non-negative number.');
    }

    // Calculate daily interest rate
    const dailyInterestRate = annualInterestRate / 100 / 365;

    // Calculate total rewards
    const totalRewards = stakingAmount * dailyInterestRate * durationInDays;

    return totalRewards;
}

// Example usage
try {
    const stakingAmount = 1000; // Amount in tokens
    const durationInDays = 30; // Duration in days
    const annualInterestRate = 5; // Annual interest rate in percentage

    const rewards = calculateStakingRewards(stakingAmount, durationInDays, annualInterestRate);
    console.log(`Staking rewards: ${rewards.toFixed(2)} tokens`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
