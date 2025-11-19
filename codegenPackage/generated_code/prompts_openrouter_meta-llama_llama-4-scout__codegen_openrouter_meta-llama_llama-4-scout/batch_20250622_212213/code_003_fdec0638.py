"""
Generated Code Metadata:
========================
Original URL: https://www.cerealclub.io
Prompt: Write a code snippet in JavaScript to implement a simple game strategy for Tài Xỉu SV388.
Generated: DETERMINISTIC_fdec06383b3253cd
Batch ID: 20250622_212213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tài Xỉu SV388 Game Strategy Implementation
 * =======================================
 */

// Define the Game class
class TaiXiuSV388 {
  /**
   * Constructor to initialize the game
   * @param {number} minBet - Minimum bet amount
   * @param {number} maxBet - Maximum bet amount
   */
  constructor(minBet, maxBet) {
    this.minBet = minBet;
    this.maxBet = maxBet;
    this.history = []; // Store game history
  }

  /**
   * Validate bet amount
   * @param {number} betAmount - Bet amount to validate
   * @returns {boolean} True if valid, false otherwise
   */
  isValidBet(betAmount) {
    return betAmount >= this.minBet && betAmount <= this.maxBet;
  }

  /**
   * Generate a random dice roll outcome
   * @returns {number} The sum of three dice rolls
   */
  rollDice() {
    const dice1 = Math.floor(Math.random() * 6) + 1;
    const dice2 = Math.floor(Math.random() * 6) + 1;
    const dice3 = Math.floor(Math.random() * 6) + 1;
    return dice1 + dice2 + dice3;
  }

  /**
   * Determine the game result
   * @param {number} betType - Bet type (0: Tài, 1: Xỉu)
   * @param {number} betAmount - Bet amount
   * @returns {object} Game result (win/loss, amount)
   */
  determineResult(betType, betAmount) {
    if (!this.isValidBet(betAmount)) {
      throw new Error('Invalid bet amount');
    }

    const outcome = this.rollDice();
    this.history.push(outcome);

    let result;
    if (betType === 0) { // Tài
      result = outcome > 10 ? { win: true, amount: betAmount * 2 } : { win: false, amount: 0 };
    } else if (betType === 1) { // Xỉu
      result = outcome <= 10 ? { win: true, amount: betAmount * 2 } : { win: false, amount: 0 };
    } else {
      throw new Error('Invalid bet type');
    }

    return result;
  }

  /**
   * Get game history
   * @returns {number[]} Array of past outcomes
   */
  getHistory() {
    return this.history;
  }
}

// Example usage
function main() {
  try {
    const game = new TaiXiuSV388(1000, 100000);
    const betType = 0; // Tài
    const betAmount = 10000;

    const result = game.determineResult(betType, betAmount);
    console.log(`Game result: ${result.win ? 'Win' : 'Loss'}, Amount: ${result.amount}`);

    console.log(`Game history: ${game.getHistory()}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
