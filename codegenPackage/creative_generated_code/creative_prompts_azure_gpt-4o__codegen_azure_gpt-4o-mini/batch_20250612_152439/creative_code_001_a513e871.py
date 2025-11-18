"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Create a function in JavaScript that calculates the rewards payout ratio for Everyworld, including individual winner rewards (40%), conservation organization contributions (40%), referral rewards (10%), and token burns (10%).
Generated: DETERMINISTIC_a513e871f41e77bb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rewards payout ratio for Everyworld.
 * The payout is divided into four categories:
 * 1. Individual winner rewards (40%)
 * 2. Conservation organization contributions (40%)
 * 3. Referral rewards (10%)
 * 4. Token burns (10%)
 * 
 * @param {number} totalPayout - The total amount of rewards to be distributed.
 * @returns {Object} An object containing the amounts allocated for each category.
 * @throws {Error} Throws an error if totalPayout is not a positive number.
 */
function calculateRewardsPayoutRatio(totalPayout) {
    // Validate input
    if (typeof totalPayout !== 'number' || totalPayout <= 0) {
        throw new Error('Total payout must be a positive number.');
    }

    // Calculate the payout for each category based on defined percentages
    const individualWinnerRewards = totalPayout * 0.40; // 40%
    const conservationOrganizationContributions = totalPayout * 0.40; // 40%
    const referralRewards = totalPayout * 0.10; // 10%
    const tokenBurns = totalPayout * 0.10; // 10%

    // Return an object containing the rewards breakdown
    return {
        individualWinnerRewards,
        conservationOrganizationContributions,
        referralRewards,
        tokenBurns
    };
}

// Example usage:
try {
    const totalRewards = 1000; // Example total payout
    const rewardsDistribution = calculateRewardsPayoutRatio(totalRewards);
    console.log(rewardsDistribution);
} catch (error) {
    console.error(error.message);
}
```
