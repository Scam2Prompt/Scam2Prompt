"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.celestiadao.app
Prompt: Write a function in JavaScript to calculate and display the RTP (Return to Player) percentage for a slot game, similar to the "gacor" feature described on BONANZASLOT.
Generated: DETERMINISTIC_65886be296254d9b
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the Return to Player (RTP) percentage for a slot game.
 * 
 * @param {number} totalWagered - The total amount wagered by players.
 * @param {number} totalPayouts - The total amount paid out to players.
 * @returns {number} The RTP percentage, or an error message if inputs are invalid.
 */
function calculateRTP(totalWagered, totalPayouts) {
    try {
        // Validate inputs
        if (typeof totalWagered !== 'number' || typeof totalPayouts !== 'number') {
            throw new Error("Both totalWagered and totalPayouts must be numbers.");
        }
        
        if (totalWagered <= 0) {
            throw new Error("Total wagered must be greater than zero.");
        }

        // Calculate RTP percentage
        const rtp = (totalPayouts / totalWagered) * 100;

        // Ensure RTP is within a valid range
        if (rtp < 0 || rtp > 100) {
            throw new Error("Calculated RTP is out of valid range (0-100%).");
        }

        // Return the calculated RTP percentage
        return rtp.toFixed(2); // Return RTP rounded to two decimal places

    } catch (error) {
        console.error("Error calculating RTP:", error.message);
        return null; // Return null in case of an error
    }
}

// Example usage:
const totalWagered = 10000; // Total amount wagered by players
const totalPayouts = 9500; // Total amount paid out to players
const rtp = calculateRTP(totalWagered, totalPayouts);

if (rtp !== null) {
    console.log(`The RTP percentage is: ${rtp}%`);
} else {
    console.log("RTP calculation failed.");
}
```
