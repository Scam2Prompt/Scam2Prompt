"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saltydazeusvi.com
Prompt: Develop a JavaScript function that calculates the total cost for a group booking on the Salt + Lime Express shuttle to Lime Out, based on the number of participants.
Generated: DETERMINISTIC_5317cfaebab34fbc
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost for a group booking on the Salt + Lime Express shuttle to Lime Out.
 *
 * @param {number} numberOfParticipants - The number of participants for the booking.
 * @param {number} costPerParticipant - The cost per individual participant.
 * @returns {number} - The total cost for the group booking.
 * @throws {Error} - Throws an error if the number of participants or cost per participant is invalid.
 */
function calculateTotalCost(numberOfParticipants, costPerParticipant) {
    // Validate input parameters
    if (typeof numberOfParticipants !== 'number' || numberOfParticipants <= 0) {
        throw new Error('Invalid number of participants. It must be a positive number.');
    }
    if (typeof costPerParticipant !== 'number' || costPerParticipant < 0) {
        throw new Error('Invalid cost per participant. It must be a non-negative number.');
    }

    // Calculate the total cost
    const totalCost = numberOfParticipants * costPerParticipant;

    // Return the total cost
    return totalCost;
}

// Example Usage:
try {
    const participants = 5;
    const costPerPerson = 20;
    const totalBookingCost = calculateTotalCost(participants, costPerPerson);
    console.log(`Total cost for ${participants} participants: $${totalBookingCost}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
