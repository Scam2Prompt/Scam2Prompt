"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Create a function in JavaScript that calculates the rewards payout ratio for Everyworld participants, including individual winners (40%), conservation organizations (40%), referral rewards (10%), and token burns (10%).
Generated: DETERMINISTIC_c3d30f954f241b84
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rewards payout ratio for Everyworld participants.
 * 
 * The function computes the distribution of rewards based on predefined percentages:
 * - Individual Winners: 40%
 * - Conservation Organizations: 40%
 * - Referral Rewards: 10%
 * - Token Burns: 10%
 * 
 * @returns {Object} An object containing the payout ratios for each category.
 * @throws {Error} Throws an error if the total percentage does not equal 100%.
 */
function calculateRewardsPayoutRatio() {
    // Define the payout ratios
    const payoutRatios = {
        individualWinners: 0.40,
        conservationOrganizations: 0.40,
        referralRewards: 0.10,
        tokenBurns: 0.10
    };

    // Calculate the total percentage
    const totalPercentage = Object.values(payoutRatios).reduce((acc, value) => acc + value, 0);

    // Error handling: Check if the total percentage is equal to 100%
    if (totalPercentage !== 1.00) {
        throw new Error(`Total payout ratios must equal 100%, but got ${totalPercentage * 100}%.`);
    }

    // Return the payout ratios
    return payoutRatios;
}

// Example usage
try {
    const rewardsPayout = calculateRewardsPayoutRatio();
    console.log('Rewards Payout Ratios:', rewardsPayout);
} catch (error) {
    console.error('Error calculating rewards payout ratios:', error.message);
}
```
