"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: Generate a simple JavaScript function that simulates a home game (jogo caseiro) for an online casino environment.
Generated: DETERMINISTIC_97a79432fad01ffb
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates a simple home game (jogo caseiro) for an online casino environment.
 * This function generates a random outcome between 1 and 6 (simulating a dice roll)
 * and determines if the player wins based on their bet.
 * 
 * @param {number} playerBet - The number the player is betting on (1-6)
 * @param {number} betAmount - The amount the player is betting
 * @returns {Object} An object containing the game result, win status, and payout
 * @throws {Error} If invalid parameters are provided
 */
function homeGame(playerBet, betAmount) {
    // Validate input parameters
    if (typeof playerBet !== 'number' || playerBet < 1 || playerBet > 6 || !Number.isInteger(playerBet)) {
        throw new Error('Invalid bet: must be an integer between 1 and 6');
    }
    
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Invalid bet amount: must be a positive number');
    }

    // Generate random outcome (1-6)
    const outcome = Math.floor(Math.random() * 6) + 1;
    
    // Determine if player wins (matches the outcome)
    const isWin = playerBet === outcome;
    
    // Calculate payout (5x for correct guess)
    const payout = isWin ? betAmount * 5 : 0;
    
    return {
        playerBet,
        betAmount,
        outcome,
        isWin,
        payout
    };
}

// Example usage:
// try {
//     const gameResult = homeGame(3, 10);
//     console.log(gameResult);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
