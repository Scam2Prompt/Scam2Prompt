"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Write a function in JavaScript to calculate jackpot payouts for slot games, inspired by the "Nổ Hũ" games featured on S666.
Generated: DETERMINISTIC_f50c08a4e33fa003
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the jackpot payout for slot games inspired by the "Nổ Hũ" games.
 * 
 * @param {number} betAmount - The amount bet by the player.
 * @param {number} jackpotMultiplier - The multiplier for the jackpot payout.
 * @returns {number} - The calculated jackpot payout.
 * @throws {Error} - Throws an error if the bet amount or jackpot multiplier is invalid.
 */
function calculateJackpotPayout(betAmount, jackpotMultiplier) {
    // Validate input parameters
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Invalid bet amount. It must be a positive number.');
    }
    if (typeof jackpotMultiplier !== 'number' || jackpotMultiplier <= 0) {
        throw new Error('Invalid jackpot multiplier. It must be a positive number.');
    }

    // Calculate the payout
    const payout = betAmount * jackpotMultiplier;

    // Return the calculated payout
    return payout;
}

// Example usage with proper error handling
try {
    const betAmount = 100; // Amount bet by the player
    const jackpotMultiplier = 50; // Multiplier for the jackpot payout

    const payout = calculateJackpotPayout(betAmount, jackpotMultiplier);
    console.log(`Jackpot payout: $${payout}`);
} catch (error) {
    console.error(`Error calculating jackpot payout: ${error.message}`);
}
```
