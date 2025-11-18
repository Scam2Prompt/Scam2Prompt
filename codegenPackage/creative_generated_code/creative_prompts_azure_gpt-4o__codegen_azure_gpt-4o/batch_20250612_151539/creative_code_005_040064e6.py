"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Write a function in JavaScript to calculate weighted prize pool distribution for competitive races in WhelpS: Slipstream, factoring in entry fees and house fees.
Generated: DETERMINISTIC_040064e6ba4417f7
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the weighted prize pool distribution for competitive races.
 *
 * @param {number[]} weights - Array of weights for each participant (e.g., skill levels, rankings).
 * @param {number[]} entryFees - Array of entry fees paid by each participant.
 * @param {number} houseFeePercentage - Percentage of the total pool taken as the house fee (e.g., 10 for 10%).
 *
 * @returns {Object} - An object containing the total prize pool, house fee, and individual payouts.
 */
function calculatePrizePoolDistribution(weights, entryFees, houseFeePercentage) {
  // Validate inputs
  if (!Array.isArray(weights) || !Array.isArray(entryFees)) {
    throw new Error("Weights and entryFees must be arrays.");
  }
  if (weights.length !== entryFees.length) {
    throw new Error("Weights and entryFees arrays must have the same length.");
  }
  if (typeof houseFeePercentage !== 'number' || houseFeePercentage < 0 || houseFeePercentage > 100) {
    throw new Error("houseFeePercentage must be a number between 0 and 100.");
  }

  // Calculate total entry fees
  const totalEntryFees = entryFees.reduce((sum, fee) => sum + fee, 0);

  // Calculate house fee
  const houseFee = (totalEntryFees * houseFeePercentage) / 100;

  // Calculate prize pool after deducting house fee
  const prizePool = totalEntryFees - houseFee;

  // Calculate total weight
  const totalWeight = weights.reduce((sum, weight) => sum + weight, 0);

  // Calculate payouts for each participant based on their weight
  const payouts = weights.map((weight, index) => ({
    participant: index + 1, // Participant index (starting from 1)
    payout: (weight / totalWeight) * prizePool,
  }));

  // Return results
  return {
    totalPrizePool: prizePool,
    houseFee: houseFee,
    payouts: payouts,
  };
}

// Example usage:
try {
  const weights = [5, 3, 2]; // Example weights for participants
  const entryFees = [100, 100, 100]; // Entry fees paid by participants
  const houseFeePercentage = 10; // House takes 10%

  const result = calculatePrizePoolDistribution(weights, entryFees, houseFeePercentage);
  console.log(result);
} catch (error) {
  console.error(error.message);
}
```
