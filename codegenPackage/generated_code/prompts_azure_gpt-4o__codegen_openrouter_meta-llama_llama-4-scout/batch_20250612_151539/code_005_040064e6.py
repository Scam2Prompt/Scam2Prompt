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
 * @param {Object[]} participants - Array of participant objects with 'name', 'entryFee', and 'prizePercentage' properties.
 * @param {number} houseFee - The house fee percentage (e.g., 0.1 for 10%).
 * @param {number} totalPrizePool - The total prize pool amount.
 * @returns {Object[]} Array of participant objects with updated 'prizeAmount' property.
 */
function calculatePrizeDistribution(participants, houseFee, totalPrizePool) {
    // Validate input parameters
    if (!Array.isArray(participants) || participants.length === 0) {
        throw new Error('Participants must be a non-empty array');
    }
    if (typeof houseFee !== 'number' || houseFee < 0 || houseFee > 1) {
        throw new Error('House fee must be a number between 0 and 1');
    }
    if (typeof totalPrizePool !== 'number' || totalPrizePool <= 0) {
        throw new Error('Total prize pool must be a positive number');
    }

    // Calculate total entry fees
    const totalEntryFees = participants.reduce((acc, participant) => acc + participant.entryFee, 0);

    // Calculate total available prize pool after house fee
    const availablePrizePool = totalPrizePool * (1 - houseFee);

    // Calculate total prize percentage points
    const totalPrizePercentagePoints = participants.reduce((acc, participant) => acc + participant.prizePercentage, 0);

    // Calculate prize amount per percentage point
    const prizeAmountPerPoint = availablePrizePool / totalPrizePercentagePoints;

    // Calculate prize amount for each participant
    return participants.map(participant => ({
        ...participant,
        prizeAmount: participant.prizePercentage * prizeAmountPerPoint - participant.entryFee,
    }));
}

// Example usage:
const participants = [
    { name: 'Participant 1', entryFee: 10, prizePercentage: 0.3 },
    { name: 'Participant 2', entryFee: 20, prizePercentage: 0.2 },
    { name: 'Participant 3', entryFee: 15, prizePercentage: 0.5 },
];

const houseFee = 0.1; // 10% house fee
const totalPrizePool = 1000;

try {
    const prizeDistribution = calculatePrizeDistribution(participants, houseFee, totalPrizePool);
    console.log(prizeDistribution);
} catch (error) {
    console.error(error.message);
}
```
