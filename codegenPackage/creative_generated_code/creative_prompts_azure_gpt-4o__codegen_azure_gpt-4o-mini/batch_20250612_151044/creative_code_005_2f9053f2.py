"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking.oxyaorigin.com
Prompt: Create a JavaScript function to calculate estimated staking rewards for a user on the Oxya Origin platform.
Generated: DETERMINISTIC_2f9053f24ee3dec5
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate estimated staking rewards for a user on the Oxya Origin platform.
 * 
 * @param {number} stakedAmount - The amount of tokens staked by the user.
 * @param {number} annualYieldPercentage - The expected annual yield percentage.
 * @param {number} stakingDuration - The duration in days the tokens are staked.
 * @returns {number} The estimated staking rewards.
 * @throws {Error} Throws an error if any input is invalid.
 */
function calculateStakingRewards(stakedAmount, annualYieldPercentage, stakingDuration) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount < 0) {
        throw new Error('Invalid staked amount. It must be a non-negative number.');
    }
    if (typeof annualYieldPercentage !== 'number' || annualYieldPercentage < 0) {
        throw new Error('Invalid annual yield percentage. It must be a non-negative number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration < 0) {
        throw new Error('Invalid staking duration. It must be a non-negative number.');
    }

    // Calculate daily yield from annual yield percentage
    const dailyYieldPercentage = annualYieldPercentage / 365 / 100;

    // Calculate estimated rewards
    const estimatedRewards = stakedAmount * dailyYieldPercentage * stakingDuration;

    return estimatedRewards;
}

// Example usage of the function
try {
    const stakedAmount = 1000; // Amount in tokens
    const annualYieldPercentage = 15; // 15% annual yield
    const stakingDuration = 30; // Duration in days

    const rewards = calculateStakingRewards(stakedAmount, annualYieldPercentage, stakingDuration);
    console.log(`Estimated Staking Rewards: ${rewards.toFixed(2)} tokens`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
