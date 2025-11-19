"""
Generated Code Metadata:
========================
Original URL: https://einarmiger-bandit-online.de
Prompt: "Create a JavaScript function to calculate the odds of winning for a given slot machine game, using data from a specific provider like Merkur or Novoline."
Generated: DETERMINISTIC_40cbf4a33565e822
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the odds of winning for a given slot machine game.
 * @param {Object} gameData - The data object containing slot machine details.
 * @param {number} gameData.totalSpins - Total number of spins in the game.
 * @param {number} gameData.winningSpins - Number of spins that result in a win.
 * @returns {number} - The calculated odds of winning (as a percentage).
 * @throws {Error} - Throws an error if input data is invalid.
 */
function calculateWinningOdds(gameData) {
  // Validate input
  if (!gameData || typeof gameData !== 'object') {
    throw new Error("Invalid input: gameData must be an object.");
  }
  if (
    typeof gameData.totalSpins !== 'number' ||
    typeof gameData.winningSpins !== 'number'
  ) {
    throw new Error(
      "Invalid input: totalSpins and winningSpins must be numbers."
    );
  }
  if (gameData.totalSpins <= 0) {
    throw new Error("Invalid input: totalSpins must be greater than zero.");
  }
  if (gameData.winningSpins < 0 || gameData.winningSpins > gameData.totalSpins) {
    throw new Error(
      "Invalid input: winningSpins must be between 0 and totalSpins."
    );
  }

  // Calculate odds
  const odds = (gameData.winningSpins / gameData.totalSpins) * 100;

  // Return the result rounded to two decimal places
  return parseFloat(odds.toFixed(2));
}

// Example usage:
try {
  const merkurGameData = {
    totalSpins: 1000,
    winningSpins: 250,
  };

  const odds = calculateWinningOdds(merkurGameData);
  console.log(`Winning odds: ${odds}%`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
