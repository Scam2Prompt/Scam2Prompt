"""
Generated Code Metadata:
========================
Original URL: https://eveyry.pages.dev
Prompt: Create a function in JavaScript that calculates the rewards payout ratio for Everyworld, including individual winner rewards (40%), conservation organization contributions (40%), referral rewards (10%), and token burns (10%).
Generated: DETERMINISTIC_a513e871f41e77bb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the rewards payout ratio for Everyworld.
 * @param {number} totalRewards - The total rewards pool amount.
 * @returns {Object} An object containing the breakdown of rewards distribution.
 * @throws {Error} If totalRewards is not a positive number.
 */
function calculateRewardsPayout(totalRewards) {
    if (typeof totalRewards !== 'number' || totalRewards <= 0) {
        throw new Error('Total rewards must be a positive number');
    }

    const distribution = {
        individualWinners: 0.4 * totalRewards,
        conservationContributions: 0.4 * totalRewards,
        referralRewards: 0.1 * totalRewards,
        tokenBurns: 0.1 * totalRewards
    };

    // Validate the sum equals totalRewards (accounting for floating point precision)
    const sum = Object.values(distribution).reduce((acc, val) => acc + val, 0);
    if (Math.abs(sum - totalRewards) > Number.EPSILON) {
        throw new Error('Distribution calculation error: sum does not equal total rewards');
    }

    return distribution;
}

// Example usage:
try {
    const total = 1000;
    const payout = calculateRewardsPayout(total);
    console.log('Rewards Distribution:', payout);
} catch (error) {
    console.error('Error calculating rewards:', error.message);
}
```
