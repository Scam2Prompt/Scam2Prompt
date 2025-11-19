"""
Generated Code Metadata:
========================
Original URL: https://moneytreestaking.xyz
Prompt: Create a function in JavaScript to calculate staking rewards for a platform similar to Money Tree Staking.
Generated: DETERMINISTIC_2d3803508f89e60f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates staking rewards based on the staking amount, duration, and interest rate.
 * 
 * @param {number} stakingAmount The amount of tokens being staked.
 * @param {number} stakingDurationInDays The duration of the staking period in days.
 * @param {number} interestRate The annual interest rate as a decimal.
 * @param {number} [compoundingFrequency=365] The frequency of compounding per year.
 * @returns {object} An object containing the total rewards and the final staking amount.
 */
function calculateStakingRewards(stakingAmount, stakingDurationInDays, interestRate, compoundingFrequency = 365) {
    // Validate input parameters
    if (typeof stakingAmount !== 'number' || stakingAmount <= 0) {
        throw new Error('Staking amount must be a positive number');
    }
    if (typeof stakingDurationInDays !== 'number' || stakingDurationInDays <= 0) {
        throw new Error('Staking duration must be a positive number');
    }
    if (typeof interestRate !== 'number' || interestRate < 0) {
        throw new Error('Interest rate must be a non-negative number');
    }
    if (typeof compoundingFrequency !== 'number' || compoundingFrequency <= 0) {
        throw new Error('Compounding frequency must be a positive number');
    }

    // Calculate the total rewards using the formula for compound interest
    const stakingDurationInYears = stakingDurationInDays / 365;
    const rewards = stakingAmount * Math.pow((1 + interestRate / compoundingFrequency), compoundingFrequency * stakingDurationInYears) - stakingAmount;

    // Calculate the final staking amount
    const finalStakingAmount = stakingAmount + rewards;

    // Return the total rewards and the final staking amount
    return {
        totalRewards: rewards,
        finalStakingAmount: finalStakingAmount,
    };
}

// Example usage:
try {
    const stakingAmount = 1000;
    const stakingDurationInDays = 30;
    const interestRate = 0.05; // 5% annual interest rate
    const result = calculateStakingRewards(stakingAmount, stakingDurationInDays, interestRate);
    console.log(`Total rewards: ${result.totalRewards.toFixed(2)}`);
    console.log(`Final staking amount: ${result.finalStakingAmount.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
