"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: Write a function in JavaScript to calculate weighted prize pool distribution for competitive races in WhelpS: Slipstream, factoring in entry fees and house fees.
Generated: DETERMINISTIC_040064e6ba4417f7
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the weighted prize pool distribution for competitive races in WhelpS: Slipstream.
 * 
 * @param {number} totalPool - The total prize pool amount.
 * @param {number} entryFee - The total entry fees collected from participants.
 * @param {number} houseFee - The percentage of the total pool taken as house fees (0-100).
 * @param {Array<number>} weights - An array of weights representing the performance of each participant.
 * @returns {Array<number>} - An array representing the prize distribution for each participant.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculatePrizeDistribution(totalPool, entryFee, houseFee, weights) {
    // Validate inputs
    if (typeof totalPool !== 'number' || totalPool < 0) {
        throw new Error('Total pool must be a non-negative number.');
    }
    if (typeof entryFee !== 'number' || entryFee < 0) {
        throw new Error('Entry fee must be a non-negative number.');
    }
    if (typeof houseFee !== 'number' || houseFee < 0 || houseFee > 100) {
        throw new Error('House fee must be a percentage between 0 and 100.');
    }
    if (!Array.isArray(weights) || weights.length === 0 || !weights.every(w => typeof w === 'number' && w >= 0)) {
        throw new Error('Weights must be a non-empty array of non-negative numbers.');
    }

    // Calculate the total house fee
    const totalHouseFee = (houseFee / 100) * totalPool;

    // Calculate the effective prize pool after deducting house fees
    const effectivePrizePool = totalPool - totalHouseFee;

    // Calculate the total weight
    const totalWeight = weights.reduce((acc, weight) => acc + weight, 0);

    // Calculate the prize distribution based on weights
    const prizeDistribution = weights.map(weight => {
        return (weight / totalWeight) * effectivePrizePool;
    });

    return prizeDistribution;
}

// Example usage
try {
    const totalPool = 10000; // Total prize pool
    const entryFee = 2000;   // Total entry fees
    const houseFee = 10;     // House fee percentage
    const weights = [1, 2, 3]; // Weights for participants

    const distribution = calculatePrizeDistribution(totalPool, entryFee, houseFee, weights);
    console.log('Prize Distribution:', distribution);
} catch (error) {
    console.error('Error calculating prize distribution:', error.message);
}
```
