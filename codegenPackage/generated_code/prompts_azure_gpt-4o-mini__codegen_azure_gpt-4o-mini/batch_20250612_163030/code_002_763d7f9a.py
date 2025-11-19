"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Create a function in JavaScript that calculates the potential staking rewards for $MIND token holders based on the dynamic APY rates provided during the presale.
Generated: DETERMINISTIC_763d7f9a9d65ab3a
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the potential staking rewards for $MIND token holders.
 * 
 * @param {number} stakedAmount - The amount of $MIND tokens staked.
 * @param {number} apy - The annual percentage yield (APY) as a decimal (e.g., 0.05 for 5%).
 * @param {number} stakingDuration - The duration for which the tokens are staked, in days.
 * @returns {number} - The potential rewards earned from staking.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateStakingRewards(stakedAmount, apy, stakingDuration) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Invalid staked amount. It must be a positive number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('Invalid APY. It must be a non-negative number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration <= 0) {
        throw new Error('Invalid staking duration. It must be a positive number.');
    }

    // Calculate the daily interest rate from the APY
    const dailyRate = apy / 365;

    // Calculate the potential rewards
    const potentialRewards = stakedAmount * dailyRate * stakingDuration;

    return potentialRewards;
}

// Example usage
try {
    const stakedAmount = 1000; // Amount of $MIND tokens staked
    const apy = 0.1; // 10% APY
    const stakingDuration = 30; // Staking for 30 days

    const rewards = calculateStakingRewards(stakedAmount, apy, stakingDuration);
    console.log(`Potential staking rewards: $${rewards.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
