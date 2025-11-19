"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Provide a JavaScript implementation for tracking live RTP (Return to Player) rates in slot games, similar to the "live RTP tertinggi" feature mentioned on ANGKA805.
Generated: DETERMINISTIC_268285f9ca4f360c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a slot game with RTP (Return to Player) tracking.
 */
class SlotGame {
  /**
   * Creates a new SlotGame instance.
   * @param {string} gameId - Unique identifier for the game.
   * @param {number} totalBet - Total bet amount.
   * @param {number} totalWin - Total win amount.
   */
  constructor(gameId, totalBet = 0, totalWin = 0) {
    this.gameId = gameId;
    this.totalBet = totalBet;
    this.totalWin = totalWin;
  }

  /**
   * Updates the total bet and win amounts.
   * @param {number} bet - Current bet amount.
   * @param {number} win - Current win amount.
   */
  updateRTP(bet, win) {
    this.totalBet += bet;
    this.totalWin += win;
  }

  /**
   * Calculates the live RTP (Return to Player) rate.
   * @returns {number} Live RTP rate as a percentage.
   */
  getLiveRTP() {
    if (this.totalBet === 0) return 0;
    return ((this.totalWin / this.totalBet) * 100).toFixed(2);
  }
}

/**
 * Manages a collection of slot games and their RTP rates.
 */
class RTPTracker {
  /**
   * Creates a new RTPTracker instance.
   */
  constructor() {
    this.games = {};
  }

  /**
   * Adds a new slot game to the tracker.
   * @param {string} gameId - Unique identifier for the game.
   */
  addGame(gameId) {
    if (!this.games[gameId]) {
      this.games[gameId] = new SlotGame(gameId);
    }
  }

  /**
   * Updates the RTP data for a specific game.
   * @param {string} gameId - Unique identifier for the game.
   * @param {number} bet - Current bet amount.
   * @param {number} win - Current win amount.
   * @throws {Error} If the game is not found.
   */
  updateGameRTP(gameId, bet, win) {
    if (!this.games[gameId]) {
      throw new Error(`Game not found: ${gameId}`);
    }
    this.games[gameId].updateRTP(bet, win);
  }

  /**
   * Gets the live RTP rate for a specific game.
   * @param {string} gameId - Unique identifier for the game.
   * @returns {number} Live RTP rate as a percentage.
   * @throws {Error} If the game is not found.
   */
  getGameLiveRTP(gameId) {
    if (!this.games[gameId]) {
      throw new Error(`Game not found: ${gameId}`);
    }
    return this.games[gameId].getLiveRTP();
  }

  /**
   * Retrieves a list of games with their live RTP rates.
   * @returns {Object} A dictionary of game IDs and their live RTP rates.
   */
  getAllLiveRTP() {
    const result = {};
    for (const gameId in this.games) {
      result[gameId] = this.games[gameId].getLiveRTP();
    }
    return result;
  }
}

// Example usage:
function main() {
  const tracker = new RTPTracker();

  tracker.addGame('game1');
  tracker.addGame('game2');

  tracker.updateGameRTP('game1', 100, 90);
  tracker.updateGameRTP('game2', 50, 45);

  console.log(`Game 1 Live RTP: ${tracker.getGameLiveRTP('game1')}%`);
  console.log(`Game 2 Live RTP: ${tracker.getGameLiveRTP('game2')}%`);

  console.log('All Games Live RTP:');
  console.log(tracker.getAllLiveRTP());
}

main();
```
