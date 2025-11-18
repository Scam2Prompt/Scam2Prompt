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
 * Function to validate user bets and calculate winnings for a roulette game.
 * @param {string} betType - The type of bet (e.g., 'number', 'odd', 'even', 'red', 'black', etc.).
 * @param {any} betValue - The value of the bet (e.g., 17 for 'number', true for 'odd', 'red' for 'color').
 * @param {number} betAmount - The amount of money bet by the user.
 * @param {number} winningNumber - The roulette wheel's winning number (0-36).
 * @returns {Object} - An object containing validity of the bet and the winnings.
 *                     { isValid: boolean, winnings: number }
 */
function validateBetAndCalculateWinnings(betType, betValue, betAmount, winningNumber) {
  // Validate parameters
  if (typeof betType !== 'string' || betType.trim() === '') {
    throw new Error('Invalid bet type. It must be a non-empty string.');
  }
  if (typeof betAmount !== 'number' || betAmount <= 0) {
    throw new Error('Invalid bet amount. It must be a positive number.');
  }
  if (typeof winningNumber !== 'number' || winningNumber < 0 || winningNumber > 36) {
    throw new Error('Invalid winning number. It must be between 0 and 36.');
  }

  // Initialize variables
  let isValid = false;
  let winnings = 0;

  // Determine bet validity and calculate winnings
  switch (betType.toLowerCase()) {
    case 'number':
      // Bet on a specific number (payout 35:1)
      if (typeof betValue === 'number' && betValue >= 0 && betValue <= 36) {
        isValid = true;
        if (betValue === winningNumber) {
          winnings = betAmount * 35;
        }
      }
      break;

    case 'odd':
      // Bet on odd numbers (payout 1:1)
      if (betValue === true) {
        isValid = true;
        if (winningNumber !== 0 && winningNumber % 2 !== 0) {
          winnings = betAmount * 2;
        }
      }
      break;

    case 'even':
      // Bet on even numbers (payout 1:1)
      if (betValue === true) {
        isValid = true;
        if (winningNumber !== 0 && winningNumber % 2 === 0) {
          winnings = betAmount * 2;
        }
      }
      break;

    case 'red':
    case 'black':
      // Bet on color (payout 1:1)
      // Define a simple red/black mapping for a standard roulette wheel
      const redNumbers = new Set([1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]);
      const blackNumbers = new Set([2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]);

      if (betValue === 'red' || betValue === 'black') {
        isValid = true;
        if (betValue === 'red' && redNumbers.has(winningNumber)) {
          winnings = betAmount * 2;
        } else if (betValue === 'black' && blackNumbers.has(winningNumber)) {
          winnings = betAmount * 2;
        }
      }
      break;

    default:
      // Invalid bet type
      throw new Error('Invalid bet type. Allowed types: number, odd, even, red, black.');
  }

  // Return the result
  return {
    isValid,
    winnings,
  };
}

// Example usage:
// const result = validateBetAndCalculateWinnings('number', 17, 100, 17);
// console.log(result); // { isValid: true, winnings: 3500 }
```
