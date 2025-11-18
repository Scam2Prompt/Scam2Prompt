"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lounge.finance
Prompt: Generate a JavaScript function to calculate estimated staking rewards based on the parameters provided by Lounge Finance.
Generated: DETERMINISTIC_5d36c11820d4099b
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates estimated staking rewards based on user inputs.
 * 
 * @param {number} stakedAmount - The amount of tokens staked by the user.
 * @param {number} annualPercentageRate - The annual percentage rate (APR) provided by Lounge Finance (in percentage, e.g., 12.5 for 12.5% APR).
 * @param {number} stakingDurationDays - The duration of staking in days.
 * 
 * @returns {number} - The estimated staking rewards in tokens.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDurationDays) {
    // Input validation
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Invalid staked amount. Must be a positive number.');
    }
    if (typeof annualPercentageRate !== 'number' || annualPercentageRate <= 0) {
        throw new Error('Invalid annual percentage rate (APR). Must be a positive number.');
    }
    if (typeof stakingDurationDays !== 'number' || stakingDurationDays <= 0) {
        throw new Error('Invalid staking duration. Must be a positive number representing days.');
    }

    // Constants
    const DAYS_IN_YEAR = 365;

    // Calculate rewards
    const dailyRate = annualPercentageRate / 100 / DAYS_IN_YEAR; // Convert APR to daily rate
    const rewards = stakedAmount * dailyRate * stakingDurationDays;

    return rewards;
}

// Example usage:
// const result = calculateStakingRewards(1000, 12.5, 30);
// console.log(`Estimated staking rewards: ${result.toFixed(2)} tokens`);
```
