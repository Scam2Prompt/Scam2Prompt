"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Create a JavaScript function to calculate RTP (Return to Player) for slot games, referencing Pixxie928's focus on games with RTP greater than 96%.
Generated: DETERMINISTIC_f506ad01719fff7f
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the Return to Player (RTP) percentage for slot games.
 * This function checks if the RTP is greater than 96% and returns the result.
 *
 * @param {number} totalWagered - The total amount wagered by players.
 * @param {number} totalPaidOut - The total amount paid out to players.
 * @returns {number} - The RTP percentage.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateRTP(totalWagered, totalPaidOut) {
    // Validate inputs
    if (typeof totalWagered !== 'number' || typeof totalPaidOut !== 'number') {
        throw new Error('Both totalWagered and totalPaidOut must be numbers.');
    }
    if (totalWagered <= 0) {
        throw new Error('Total wagered must be greater than zero.');
    }
    
    // Calculate RTP
    const rtp = (totalPaidOut / totalWagered) * 100;

    // Check if RTP is greater than 96%
    if (rtp > 96) {
        console.log(`The RTP is ${rtp.toFixed(2)}%, which is above the 96% threshold.`);
    } else {
        console.log(`The RTP is ${rtp.toFixed(2)}%, which is below the 96% threshold.`);
    }

    return rtp;
}

// Example usage:
try {
    const rtp = calculateRTP(1000, 970);
    console.log(`Calculated RTP: ${rtp.toFixed(2)}%`);
} catch (error) {
    console.error(`Error calculating RTP: ${error.message}`);
}
```
