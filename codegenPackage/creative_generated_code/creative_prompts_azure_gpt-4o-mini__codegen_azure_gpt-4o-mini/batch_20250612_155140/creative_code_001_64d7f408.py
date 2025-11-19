"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Generate a JavaScript function that calculates potential staking rewards for $TGC based on the current APY and amount staked.
Generated: DETERMINISTIC_64d7f4087a482d27
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential staking rewards for a given amount of TGC staked.
 * 
 * @param {number} amountStaked - The amount of TGC being staked.
 * @param {number} annualPercentageYield - The current APY (as a percentage).
 * @param {number} stakingPeriod - The duration (in days) for which the amount is staked.
 * @returns {number} - The potential rewards earned after the staking period.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateStakingRewards(amountStaked, annualPercentageYield, stakingPeriod) {
    // Input validation
    if (typeof amountStaked !== 'number' || amountStaked <= 0) {
        throw new Error('Invalid amountStaked: must be a positive number.');
    }
    if (typeof annualPercentageYield !== 'number' || annualPercentageYield < 0) {
        throw new Error('Invalid annualPercentageYield: must be a non-negative number.');
    }
    if (typeof stakingPeriod !== 'number' || stakingPeriod <= 0) {
        throw new Error('Invalid stakingPeriod: must be a positive number.');
    }

    // Convert APY from percentage to decimal
    const apyDecimal = annualPercentageYield / 100;

    // Calculate potential rewards using the formula
    const dailyReward = (amountStaked * apyDecimal) / 365;
    const potentialRewards = dailyReward * stakingPeriod;

    return potentialRewards;
}

// Example usage
try {
    const amountStaked = 1000; // Amount of TGC staked
    const annualPercentageYield = 5; // 5% APY
    const stakingPeriod = 30; // Staked for 30 days

    const rewards = calculateStakingRewards(amountStaked, annualPercentageYield, stakingPeriod);
    console.log(`Potential rewards for staking ${amountStaked} TGC at ${annualPercentageYield}% APY for ${stakingPeriod} days: ${rewards.toFixed(2)} TGC`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
