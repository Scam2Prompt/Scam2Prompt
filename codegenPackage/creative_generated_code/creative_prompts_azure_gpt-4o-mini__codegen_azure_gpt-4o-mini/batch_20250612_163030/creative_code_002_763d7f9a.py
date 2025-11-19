"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Create a function in JavaScript that calculates the potential staking rewards for $MIND token holders based on the dynamic APY rates provided during the presale.
Generated: DETERMINISTIC_763d7f9a9d65ab3a
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential staking rewards for $MIND token holders.
 * 
 * @param {number} principal - The initial amount of $MIND tokens staked.
 * @param {number} apy - The annual percentage yield (APY) as a decimal (e.g., 0.1 for 10%).
 * @param {number} years - The number of years to calculate rewards for.
 * @returns {number} - The total rewards earned after the specified number of years.
 * 
 * @throws {Error} - Throws an error if the input values are not valid.
 */
function calculateStakingRewards(principal, apy, years) {
    // Input validation
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('APY must be a non-negative number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate total rewards using compound interest formula
    const totalRewards = principal * Math.pow((1 + apy), years);

    return totalRewards - principal; // Return only the rewards earned, not the principal
}

// Example usage:
try {
    const principalAmount = 1000; // Amount of $MIND tokens staked
    const annualAPY = 0.1; // 10% APY
    const stakingDuration = 2; // Duration in years

    const rewards = calculateStakingRewards(principalAmount, annualAPY, stakingDuration);
    console.log(`Potential staking rewards for $MIND tokens: $${rewards.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
