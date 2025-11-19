"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7a.game
Prompt: Generate a simple JavaScript function that simulates a home game (jogo caseiro) for an online casino environment.
Generated: DETERMINISTIC_97a79432fad01ffb
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a simple home game for an online casino environment.
 * The game involves a player betting on a random outcome (1-6).
 * The player wins if the outcome matches their bet.
 *
 * @param {number} playerBet - The number the player is betting on (1 to 6).
 * @param {number} playerStake - The amount the player is betting.
 * @returns {object} - Result of the game containing outcome, win status, and payout.
 */
function playHomeGame(playerBet, playerStake) {
    // Validate playerBet and playerStake inputs
    if (!Number.isInteger(playerBet) || playerBet < 1 || playerBet > 6) {
        throw new Error("Invalid bet. Please choose a number between 1 and 6.");
    }

    if (typeof playerStake !== 'number' || playerStake <= 0) {
        throw new Error("Invalid stake. Please enter a positive number.");
    }

    // Generate a random outcome between 1 and 6
    const outcome = Math.floor(Math.random() * 6) + 1;

    // Determine if the player wins
    const isWin = (outcome === playerBet);
    const payout = isWin ? playerStake * 6 : 0; // Win returns 6 times the stake

    // Return game result
    return {
        outcome: outcome,
        win: isWin,
        payout: payout,
    };
}

// Example usage:
try {
    const result = playHomeGame(3, 10);
    console.log(`Outcome: ${result.outcome}, Win: ${result.win}, Payout: $${result.payout}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
