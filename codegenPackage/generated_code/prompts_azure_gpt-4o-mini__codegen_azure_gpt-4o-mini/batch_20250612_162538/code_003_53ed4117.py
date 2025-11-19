"""
Generated Code Metadata:
========================
Original URL: https://districtchronicles.com
Prompt: Develop a JavaScript function that calculates the potential winnings based on RTP for a slot game, similar to the games available on Pixxie928.
Generated: DETERMINISTIC_53ed411787869f25
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential winnings based on the Return to Player (RTP) percentage.
 * 
 * @param {number} betAmount - The amount of money bet on the slot game.
 * @param {number} rtpPercentage - The Return to Player percentage (between 0 and 100).
 * @returns {number} - The potential winnings based on the RTP.
 * @throws {Error} - Throws an error if betAmount or rtpPercentage are invalid.
 */
function calculatePotentialWinnings(betAmount, rtpPercentage) {
    // Validate input parameters
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Invalid bet amount. It must be a positive number.');
    }
    if (typeof rtpPercentage !== 'number' || rtpPercentage < 0 || rtpPercentage > 100) {
        throw new Error('Invalid RTP percentage. It must be between 0 and 100.');
    }

    // Calculate potential winnings
    const potentialWinnings = (betAmount * rtpPercentage) / 100;

    return potentialWinnings;
}

// Example usage
try {
    const bet = 10; // Example bet amount
    const rtp = 95; // Example RTP percentage
    const winnings = calculatePotentialWinnings(bet, rtp);
    console.log(`Potential winnings: $${winnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
