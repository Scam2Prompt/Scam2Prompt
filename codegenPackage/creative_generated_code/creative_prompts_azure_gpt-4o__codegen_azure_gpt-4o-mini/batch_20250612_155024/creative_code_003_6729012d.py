"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-staking.vercel.app
Prompt: Create a JavaScript function to calculate estimated staking rewards for the Sui network.
Generated: DETERMINISTIC_6729012da9820b1f
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates estimated staking rewards for the Sui network.
 * 
 * @param {number} stakedAmount - The amount of SUI tokens staked.
 * @param {number} annualPercentageYield - The expected annual percentage yield (APY) as a decimal (e.g., 0.15 for 15%).
 * @param {number} stakingPeriod - The period in days for which the staking rewards are calculated.
 * @returns {number} The estimated staking rewards for the specified period.
 * @throws {Error} Throws an error if any input parameter is invalid.
 */
function calculateStakingRewards(stakedAmount, annualPercentageYield, stakingPeriod) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Invalid staked amount. It must be a positive number.');
    }
    if (typeof annualPercentageYield !== 'number' || annualPercentageYield < 0) {
        throw new Error('Invalid annual percentage yield. It cannot be negative.');
    }
    if (typeof stakingPeriod !== 'number' || stakingPeriod <= 0) {
        throw new Error('Invalid staking period. It must be a positive number in days.');
    }

    // Calculate daily yield from annual yield
    const dailyYield = annualPercentageYield / 365;

    // Calculate estimated rewards for the staking period
    const estimatedRewards = stakedAmount * dailyYield * stakingPeriod;

    return estimatedRewards;
}

// Example usage
try {
    const stakedAmount = 1000; // Amount of SUI staked
    const annualPercentageYield = 0.15; // 15% APY
    const stakingPeriod = 30; // Calculate rewards for 30 days

    const rewards = calculateStakingRewards(stakedAmount, annualPercentageYield, stakingPeriod);
    console.log(`Estimated staking rewards: ${rewards.toFixed(2)} SUI`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
