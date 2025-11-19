"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tntmytariff.com
Prompt: Write a JavaScript function that calculates potential winnings based on the user's bet amount on SLOT777 games.
Generated: DETERMINISTIC_ac617e078aa5018f
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential winnings based on the user's bet amount and the payout multiplier.
 * 
 * @param {number} betAmount - The amount of money the user is betting.
 * @param {number} payoutMultiplier - The multiplier that determines potential winnings.
 * @returns {number} The potential winnings based on the bet amount and payout multiplier.
 * @throws {Error} Throws an error if the betAmount or payoutMultiplier is not a positive number.
 */
function calculatePotentialWinnings(betAmount, payoutMultiplier) {
    // Validate inputs
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Invalid bet amount: Must be a positive number.');
    }
    if (typeof payoutMultiplier !== 'number' || payoutMultiplier <= 0) {
        throw new Error('Invalid payout multiplier: Must be a positive number.');
    }

    // Calculate potential winnings
    const potentialWinnings = betAmount * payoutMultiplier;

    return potentialWinnings;
}

// Example usage:
// Try to calculate winnings with a bet of $10 and a payout multiplier of 5.
try {
    const bet = 10;
    const multiplier = 5;
    const winnings = calculatePotentialWinnings(bet, multiplier);
    console.log(`Potential winnings: $${winnings}`);
} catch (error) {
    console.error(error.message);
}
```
