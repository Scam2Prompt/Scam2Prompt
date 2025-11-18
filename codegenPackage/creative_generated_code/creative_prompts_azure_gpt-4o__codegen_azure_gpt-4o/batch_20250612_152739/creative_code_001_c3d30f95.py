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
 * Function to calculate the rewards payout ratio for Everyworld participants.
 * 
 * The payout structure is as follows:
 * - Individual winners: 40%
 * - Conservation organizations: 40%
 * - Referral rewards: 10%
 * - Token burns: 10%
 * 
 * @param {number} totalRewards - The total rewards amount to be distributed.
 * @returns {object} - An object containing the calculated payout for each category.
 * @throws {Error} - If the totalRewards parameter is not a positive number.
 */

function calculateRewardsPayout(totalRewards) {
  // Input validation
  if (typeof totalRewards !== 'number' || totalRewards <= 0) {
    throw new Error('Invalid input: totalRewards must be a positive number.');
  }

  // Define payout ratios
  const payoutRatios = {
    individualWinners: 0.4, // 40%
    conservationOrganizations: 0.4, // 40%
    referralRewards: 0.1, // 10%
    tokenBurns: 0.1 // 10%
  };

  // Calculate payouts
  const payouts = {
    individualWinners: totalRewards * payoutRatios.individualWinners,
    conservationOrganizations: totalRewards * payoutRatios.conservationOrganizations,
    referralRewards: totalRewards * payoutRatios.referralRewards,
    tokenBurns: totalRewards * payoutRatios.tokenBurns
  };

  // Ensure total payout consistency (sanity check)
  const totalDistributed = Object.values(payouts).reduce((sum, value) => sum + value, 0);
  if (Math.abs(totalDistributed - totalRewards) > 0.01) { // Small tolerance for floating-point arithmetic
    throw new Error('Payout distribution error: Total distributed does not match total rewards.');
  }

  return payouts;
}

// Example usage
try {
  const totalRewards = 10000; // Example total rewards pool
  const payoutResult = calculateRewardsPayout(totalRewards);
  console.log('Payout Result:', payoutResult);
} catch (error) {
  console.error('Error:', error.message);
}
```
