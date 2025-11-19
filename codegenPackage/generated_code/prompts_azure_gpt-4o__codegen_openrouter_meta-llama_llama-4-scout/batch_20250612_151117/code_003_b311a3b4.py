"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Write a script in JavaScript to calculate the staking rewards for $WAI tokens based on the 153% APY mentioned in the WienerAI documentation.
Generated: DETERMINISTIC_b311a3b4e4610f0d
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the staking rewards for $WAI tokens based on the 153% APY.
 * 
 * @param {number} principal - The initial amount of $WAI tokens staked.
 * @param {number} apy - The annual percentage yield (153% in this case).
 * @param {number} timeInDays - The time period for which the rewards are calculated.
 * @returns {object} An object containing the total rewards and the new balance.
 */
function calculateStakingRewards(principal, apy, timeInDays) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('APY must be a non-negative number.');
    }
    if (typeof timeInDays !== 'number' || timeInDays < 0) {
        throw new Error('Time in days must be a non-negative number.');
    }

    // Convert APY to a decimal
    const apyDecimal = apy / 100;

    // Calculate the daily interest rate
    const dailyInterestRate = apyDecimal / 365;

    // Calculate the total rewards
    const totalRewards = principal * (Math.pow(1 + dailyInterestRate, timeInDays) - 1);

    // Calculate the new balance
    const newBalance = principal + totalRewards;

    return { totalRewards, newBalance };
}

// Example usage:
try {
    const principal = 1000; // Initial amount of $WAI tokens staked
    const apy = 153; // 153% APY
    const timeInDays = 30; // 30-day period

    const { totalRewards, newBalance } = calculateStakingRewards(principal, apy, timeInDays);
    console.log(`Total rewards: ${totalRewards.toFixed(2)} $WAI tokens`);
    console.log(`New balance: ${newBalance.toFixed(2)} $WAI tokens`);
} catch (error) {
    console.error(error.message);
}
```
