"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: Write a function in JavaScript to validate user bets and calculate winnings for a roulette game.
Generated: DETERMINISTIC_6479f599eb5df54f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a user's bet for a roulette game and calculates potential winnings.
 * @param {Object} bet - The bet object containing type and value.
 * @param {number} betAmount - The amount of money wagered.
 * @param {number} winningNumber - The winning number from the roulette wheel.
 * @returns {Object} An object containing validation result and winnings.
 */
function validateAndCalculateRouletteBet(bet, betAmount, winningNumber) {
    // Validate input types
    if (typeof bet !== 'object' || bet === null) {
        throw new Error('Invalid bet object');
    }
    if (typeof betAmount !== 'number' || betAmount <= 0) {
        throw new Error('Bet amount must be a positive number');
    }
    if (typeof winningNumber !== 'number' || winningNumber < 0 || winningNumber > 36) {
        throw new Error('Winning number must be between 0 and 36');
    }

    // Define valid bet types and their payouts
    const betTypes = {
        'straight': { numbers: 1, payout: 35 },
        'split': { numbers: 2, payout: 17 },
        'street': { numbers: 3, payout: 11 },
        'corner': { numbers: 4, payout: 8 },
        'line': { numbers: 6, payout: 5 },
        'dozen': { numbers: 12, payout: 2 },
        'column': { numbers: 12, payout: 2 },
        'even': { numbers: 18, payout: 1 },
        'odd': { numbers: 18, payout: 1 },
        'red': { numbers: 18, payout: 1 },
        'black': { numbers: 18, payout: 1 },
        'low': { numbers: 18, payout: 1 },
        'high': { numbers: 18, payout: 1 }
    };

    // Validate bet type
    if (!betTypes[bet.type]) {
        return { isValid: false, error: 'Invalid bet type', winnings: 0 };
    }

    // Validate bet value based on type
    const betType = betTypes[bet.type];
    let isValid = true;
    let error = null;

    switch (bet.type) {
        case 'straight':
            if (bet.value < 0 || bet.value > 36) {
                isValid = false;
                error = 'Straight bet must be between 0 and 36';
            }
            break;
        case 'split':
            if (!Array.isArray(bet.value) || bet.value.length !== 2) {
                isValid = false;
                error = 'Split bet requires exactly 2 adjacent numbers';
            }
            break;
        case 'street':
            if (!Array.isArray(bet.value) || bet.value.length !== 3) {
                isValid = false;
                error = 'Street bet requires exactly 3 numbers in a row';
            }
            break;
        case 'corner':
            if (!Array.isArray(bet.value) || bet.value.length !== 4) {
                isValid = false;
                error = 'Corner bet requires exactly 4 numbers forming a square';
            }
            break;
        case 'line':
            if (!Array.isArray(bet.value) || bet.value.length !== 6) {
                isValid = false;
                error = 'Line bet requires exactly 6 numbers in two adjacent rows';
            }
            break;
        case 'dozen':
            if (bet.value < 1 || bet.value > 3) {
                isValid = false;
                error = 'Dozen bet must be 1, 2, or 3';
            }
            break;
        case 'column':
            if (bet.value < 1 || bet.value > 3) {
                isValid = false;
                error = 'Column bet must be 1, 2, or 3';
            }
            break;
        case 'even':
        case 'odd':
        case 'red':
        case 'black':
        case 'low':
        case 'high':
            // No specific value needed for these bets
            break;
        default:
            isValid = false;
            error = 'Unknown bet type';
    }

    if (!isValid) {
        return { isValid, error, winnings: 0 };
    }

    // Check if bet is a winner
    let isWinner = false;
    const redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];

    switch (bet.type) {
        case 'straight':
            isWinner = bet.value === winningNumber;
            break;
        case 'split':
            isWinner = bet.value.includes(winningNumber);
            break;
        case 'street':
            isWinner = bet.value.includes(winningNumber);
            break;
        case 'corner':
            isWinner = bet.value.includes(winningNumber);
            break;
        case 'line':
            isWinner = bet.value.includes(winningNumber);
            break;
        case 'dozen':
            const dozenStart = (bet.value - 1) * 12 + 1;
            isWinner = winningNumber >= dozenStart && winningNumber <= dozenStart + 11;
            break;
        case 'column':
            isWinner = winningNumber % 3 === bet.value % 3 && winningNumber !== 0;
            break;
        case 'even':
            isWinner = winningNumber !== 0 && winningNumber % 2 === 0;
            break;
        case 'odd':
            isWinner = winningNumber % 2 === 1;
            break;
        case 'red':
            isWinner = redNumbers.includes(winningNumber);
            break;
        case 'black':
            isWinner = winningNumber !== 0 && !redNumbers.includes(winningNumber);
            break;
        case 'low':
            isWinner = winningNumber >= 1 && winningNumber <= 18;
            break;
        case 'high':
            isWinner = winningNumber >= 19 && winningNumber <= 36;
            break;
    }

    // Calculate winnings
    const winnings = isWinner ? betAmount * betType.payout + betAmount : 0;

    return {
        isValid: true,
        isWinner,
        winnings,
        payout: betType.payout
    };
}
```
