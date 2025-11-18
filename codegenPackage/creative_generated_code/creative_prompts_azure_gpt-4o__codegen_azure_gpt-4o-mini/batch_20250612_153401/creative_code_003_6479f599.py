"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7a.game
Prompt: Write a function in JavaScript to validate user bets and calculate winnings for a roulette game.
Generated: DETERMINISTIC_6479f599eb5df54f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user bets for a roulette game and calculates winnings.
 * 
 * @param {Object} bet - The user's bet containing the amount and the type of bet.
 * @param {number} winningNumber - The winning number from the roulette spin.
 * @returns {Object} - An object containing the bet amount and the winnings.
 * @throws {Error} - Throws an error if the bet is invalid or the amount is negative.
 */
function validateAndCalculateWinnings(bet, winningNumber) {
    // Basic validation for bet object structure
    if (!bet || typeof bet.amount !== 'number' || typeof bet.type !== 'string') {
        throw new Error('Invalid bet format. Must contain amount and type as a string.');
    }

    // Ensure the bet amount is a positive number
    if (bet.amount < 0) {
        throw new Error('Bet amount cannot be negative.');
    }

    let winnings = 0;

    // Handle different types of bets
    switch (bet.type.toLowerCase()) {
        case 'number':
            // Bet on a single number, payout is 35 to 1
            if (bet.number === winningNumber) {
                winnings = bet.amount * 35;
            }
            break;

        case 'red':
        case 'black':
            // Bet on color, payout is 1 to 1
            const redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];
            const isRed = redNumbers.includes(winningNumber);
            if ((bet.type.toLowerCase() === 'red' && isRed) || 
                (bet.type.toLowerCase() === 'black' && !isRed && winningNumber !== 0)) {
                winnings = bet.amount * 1;
            }
            break;

        case 'even':
        case 'odd':
            // Bet on even or odd, payout is 1 to 1
            const isEven = winningNumber % 2 === 0;
            if ((bet.type.toLowerCase() === 'even' && isEven) || 
                (bet.type.toLowerCase() === 'odd' && !isEven && winningNumber !== 0)) {
                winnings = bet.amount * 1;
            }
            break;

        case 'dozen':
            // Bet on dozens: 1-12, 13-24, 25-36
            if (bet.range === '1-12' && winningNumber >= 1 && winningNumber <= 12) {
                winnings = bet.amount * 2;
            } else if (bet.range === '13-24' && winningNumber >= 13 && winningNumber <= 24) {
                winnings = bet.amount * 2;
            } else if (bet.range === '25-36' && winningNumber >= 25 && winningNumber <= 36) {
                winnings = bet.amount * 2;
            }
            break;

        default:
            throw new Error('Invalid bet type. Valid types are: number, red, black, even, odd, dozen.');
    }

    // Return the result with winnings
    return {
        betAmount: bet.amount,
        winnings: winnings
    };
}

// Example usage:
// try {
//     const bet = { amount: 100, type: 'red' }; // Bet 100 on red
//     const winningNumber = 7; // Winning number is 7
//     const result = validateAndCalculateWinnings(bet, winningNumber);
//     console.log(`Bet Amount: $${result.betAmount}, Winnings: $${result.winnings}`);
// } catch (error) {
//     console.error(error.message);
// }
```
