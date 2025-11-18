"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneytreestaking.xyz
Prompt: Create a function in JavaScript to calculate staking rewards for a platform similar to Money Tree Staking.
Generated: DETERMINISTIC_2d3803508f89e60f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate staking rewards for a given amount staked, annual interest rate, 
 * and staking duration in months.
 *
 * @param {number} stakedAmount - The amount of currency staked.
 * @param {number} annualInterestRate - The annual interest rate (as a percentage).
 * @param {number} stakingDuration - The duration for which the amount is staked (in months).
 * @returns {number} - The calculated staking rewards.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateStakingRewards(stakedAmount, annualInterestRate, stakingDuration) {
    // Input validation
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Invalid staked amount. It must be a positive number.');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate < 0) {
        throw new Error('Invalid annual interest rate. It cannot be negative.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration <= 0) {
        throw new Error('Invalid staking duration. It must be a positive number.');
    }
    
    // Convert annual interest rate from percentage to decimal
    const interestRateDecimal = annualInterestRate / 100;
    
    // Calculate monthly interest rate
    const monthlyInterestRate = interestRateDecimal / 12;

    // Calculate total rewards using the formula: Rewards = Staked Amount * Monthly Rate * Duration
    const rewards = stakedAmount * monthlyInterestRate * stakingDuration;

    // Return the calculated staking rewards
    return parseFloat(rewards.toFixed(2)); // Return rewards rounded to 2 decimal places
}

// Example usage:
// const rewards = calculateStakingRewards(1000, 5, 12);
// console.log(`Staking Rewards: $${rewards}`);
```
