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
 * Calculates the weighted prize pool distribution for competitive races in WhelpS: Slipstream.
 * 
 * @param {number} totalEntries - The total number of entries in the race.
 * @param {number} entryFee - The fee for entering the race.
 * @param {number} houseFeePercentage - The percentage of the total entry fees taken by the house (0-100).
 * @returns {Object} An object containing the total prize pool and the individual prize distribution.
 * 
 * @throws {Error} Will throw an error if inputs are invalid.
 */
function calculatePrizeDistribution(totalEntries, entryFee, houseFeePercentage) {
    // Validate inputs
    if (typeof totalEntries !== 'number' || totalEntries <= 0) {
        throw new Error('Total entries must be a positive number.');
    }
    if (typeof entryFee !== 'number' || entryFee < 0) {
        throw new Error('Entry fee must be a non-negative number.');
    }
    if (typeof houseFeePercentage !== 'number' || houseFeePercentage < 0 || houseFeePercentage > 100) {
        throw new Error('House fee percentage must be between 0 and 100.');
    }

    // Calculate total entry fees
    const totalEntryFees = totalEntries * entryFee;

    // Calculate house fee
    const houseFee = (houseFeePercentage / 100) * totalEntryFees;

    // Calculate total prize pool after house fees
    const totalPrizePool = totalEntryFees - houseFee;

    // Determine prize distribution (example: 1st - 50%, 2nd - 30%, 3rd - 20%)
    const prizeDistribution = {
        firstPlace: totalPrizePool * 0.5,
        secondPlace: totalPrizePool * 0.3,
        thirdPlace: totalPrizePool * 0.2,
    };

    return {
        totalPrizePool: totalPrizePool,
        prizeDistribution: prizeDistribution,
    };
}

// Example usage
try {
    const result = calculatePrizeDistribution(10, 5, 10);
    console.log('Total Prize Pool:', result.totalPrizePool);
    console.log('Prize Distribution:', result.prizeDistribution);
} catch (error) {
    console.error('Error calculating prize distribution:', error.message);
}
```
