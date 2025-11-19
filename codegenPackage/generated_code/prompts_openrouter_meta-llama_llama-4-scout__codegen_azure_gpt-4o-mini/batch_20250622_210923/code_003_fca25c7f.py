"""
Generated Code Metadata:
========================
Original URL: https://pansos4dbabak.info
Prompt: "Create a JavaScript function to calculate the RTP (Return to Player) for a slot game, considering the game's payout structure and player deposits."
Generated: DETERMINISTIC_fca25c7f839fbad4
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the Return to Player (RTP) for a slot game.
 * 
 * @param {number} totalDeposits - The total amount of money deposited by players.
 * @param {number} totalPayouts - The total amount of money paid out to players.
 * @returns {number} - The RTP percentage, or null if inputs are invalid.
 * 
 * @throws {Error} - Throws an error if totalDeposits is less than or equal to zero.
 */
function calculateRTP(totalDeposits, totalPayouts) {
    // Validate inputs
    if (typeof totalDeposits !== 'number' || typeof totalPayouts !== 'number') {
        throw new Error('Both totalDeposits and totalPayouts must be numbers.');
    }
    
    if (totalDeposits <= 0) {
        throw new Error('Total deposits must be greater than zero.');
    }

    // Calculate RTP
    const rtp = (totalPayouts / totalDeposits) * 100;

    // Return the RTP percentage, rounded to two decimal places
    return parseFloat(rtp.toFixed(2));
}

// Example usage
try {
    const deposits = 1000; // Total deposits by players
    const payouts = 950;   // Total payouts to players
    const rtp = calculateRTP(deposits, payouts);
    console.log(`The RTP is ${rtp}%`);
} catch (error) {
    console.error(`Error calculating RTP: ${error.message}`);
}
```
