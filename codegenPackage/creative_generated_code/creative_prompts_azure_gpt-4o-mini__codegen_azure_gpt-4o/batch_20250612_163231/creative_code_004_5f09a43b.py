"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Write a function in JavaScript that calculates the potential rewards from staking $MPEPE tokens based on the current staking parameters.
Generated: DETERMINISTIC_5f09a43bff6c7f14
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the potential rewards from staking $MPEPE tokens.
 * 
 * @param {number} stakedAmount - The amount of $MPEPE tokens staked.
 * @param {number} annualPercentageRate - The annual percentage rate (APR) for staking rewards.
 * @param {number} stakingDuration - The duration of staking in days.
 * 
 * @returns {number} - The calculated staking rewards.
 * 
 * @throws {Error} - Throws an error if any of the inputs are invalid.
 */
function calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDuration) {
    // Input validation
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error("Invalid staked amount. Must be a positive number.");
    }
    if (typeof annualPercentageRate !== 'number' || annualPercentageRate <= 0) {
        throw new Error("Invalid APR. Must be a positive number.");
    }
    if (typeof stakingDuration !== 'number' || stakingDuration <= 0) {
        throw new Error("Invalid staking duration. Must be a positive number of days.");
    }

    // Constants
    const DAYS_IN_YEAR = 365; // Number of days in a year

    // Calculate rewards
    const yearlyRewards = (stakedAmount * annualPercentageRate) / 100; // Calculate yearly rewards
    const dailyRewards = yearlyRewards / DAYS_IN_YEAR; // Calculate daily rewards
    const totalRewards = dailyRewards * stakingDuration; // Calculate total rewards for the staking duration

    return totalRewards; // Return the calculated rewards
}

// Example usage
try {
    const stakedAmount = 1000; // Example: 1000 $MPEPE tokens
    const annualPercentageRate = 12; // Example: 12% APR
    const stakingDuration = 30; // Example: Staking for 30 days

    const rewards = calculateStakingRewards(stakedAmount, annualPercentageRate, stakingDuration);
    console.log(`Potential rewards for staking: ${rewards} $MPEPE tokens`);
} catch (error) {
    console.error(error.message); // Handle and log errors
}
```
