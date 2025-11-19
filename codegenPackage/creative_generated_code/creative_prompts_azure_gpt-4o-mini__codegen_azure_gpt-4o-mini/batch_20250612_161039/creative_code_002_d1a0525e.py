"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memesreum-net.pages.dev
Prompt: Create a JavaScript function to calculate potential staking rewards based on the 183% APY offered by Memereum.
Generated: DETERMINISTIC_d1a0525e8e6d436b
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential staking rewards based on the given principal amount,
 * the annual percentage yield (APY), and the duration in days.
 *
 * @param {number} principal - The amount of cryptocurrency staked.
 * @param {number} duration - The duration for which the amount is staked, in days.
 * @param {number} apy - The annual percentage yield (APY) expressed as a decimal (e.g., 183% APY = 1.83).
 * @returns {number} - The potential rewards earned after the specified duration.
 * @throws {Error} - Throws an error if the principal or duration is negative, or if the APY is not a valid number.
 */
function calculateStakingRewards(principal, duration, apy = 1.83) {
    // Validate inputs
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
    }
    if (typeof duration !== 'number' || duration < 0) {
        throw new Error('Duration must be a non-negative number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('APY must be a non-negative number.');
    }

    // Calculate daily interest rate from the APY
    const dailyRate = apy / 365;

    // Calculate potential rewards for the given duration
    const rewards = principal * dailyRate * duration;

    return rewards;
}

// Example usage
try {
    const principalAmount = 1000; // Amount staked
    const stakingDuration = 30; // Duration in days
    const rewards = calculateStakingRewards(principalAmount, stakingDuration);
    console.log(`Potential rewards after ${stakingDuration} days: $${rewards.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
