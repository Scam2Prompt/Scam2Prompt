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
 * @param {number} totalPrizePool - The total prize pool to be distributed.
 * @param {Array<{id: string, position: number, weight: number}>} participants - Array of participant objects containing id, position, and weight.
 * @param {number} houseFeePercentage - The percentage of the prize pool taken as house fee (0-100).
 * @param {number} entryFee - The fixed entry fee per participant.
 * @returns {Object} An object containing:
 *   - prizeDistribution: Array of objects with participant id and their prize amount
 *   - houseFee: The total house fee deducted
 *   - totalEntryFees: The total entry fees collected
 *   - error: String message if any error occurred
 */
function calculatePrizeDistribution(totalPrizePool, participants, houseFeePercentage, entryFee) {
    // Validate inputs
    if (totalPrizePool <= 0) {
        return { error: 'Total prize pool must be greater than zero' };
    }
    
    if (!Array.isArray(participants) || participants.length === 0) {
        return { error: 'Participants must be a non-empty array' };
    }
    
    if (houseFeePercentage < 0 || houseFeePercentage > 100) {
        return { error: 'House fee percentage must be between 0 and 100' };
    }
    
    if (entryFee < 0) {
        return { error: 'Entry fee cannot be negative' };
    }
    
    // Calculate total entry fees
    const totalEntryFees = participants.length * entryFee;
    
    // Calculate house fee
    const houseFee = totalPrizePool * (houseFeePercentage / 100);
    const distributablePool = totalPrizePool - houseFee;
    
    // Sort participants by position (ascending)
    const sortedParticipants = [...participants].sort((a, b) => a.position - b.position);
    
    // Calculate total weight for normalization
    const totalWeight = sortedParticipants.reduce((sum, participant) => sum + participant.weight, 0);
    
    if (totalWeight <= 0) {
        return { error: 'Total participant weights must be greater than zero' };
    }
    
    // Calculate prize for each participant
    const prizeDistribution = sortedParticipants.map(participant => {
        const prize = (participant.weight / totalWeight) * distributablePool;
        return {
            id: participant.id,
            prize: parseFloat(prize.toFixed(2)) // Round to 2 decimal places
        };
    });
    
    return {
        prizeDistribution,
        houseFee: parseFloat(houseFee.toFixed(2)),
        totalEntryFees: parseFloat(totalEntryFees.toFixed(2)),
        error: null
    };
}

// Example usage:
// const result = calculatePrizeDistribution(10000, [
//     {id: 'player1', position: 1, weight: 50},
//     {id: 'player2', position: 2, weight: 30},
//     {id: 'player3', position: 3, weight: 20}
// ], 10, 100);
// console.log(result);
```
