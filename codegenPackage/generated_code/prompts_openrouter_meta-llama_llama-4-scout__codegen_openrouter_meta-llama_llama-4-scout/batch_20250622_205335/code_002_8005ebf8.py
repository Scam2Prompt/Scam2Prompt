"""
Generated Code Metadata:
========================
Original URL: https://todaythegames.com
Prompt: Generate a JavaScript code example for implementing a leaderboard system for a social casino game, where players can compete against friends and other players for top prizes.
Generated: DETERMINISTIC_8005ebf861d57321
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Leaderboard.js

class Leaderboard {
  /**
   * Initialize a new leaderboard.
   * @param {string} gameId - The ID of the game.
   * @param {number} maxEntries - The maximum number of entries to store.
   */
  constructor(gameId, maxEntries = 100) {
    this.gameId = gameId;
    this.maxEntries = maxEntries;
    this.entries = [];
  }

  /**
   * Add a new entry to the leaderboard.
   * @param {string} playerId - The ID of the player.
   * @param {number} score - The score of the player.
   * @throws {Error} If the score is not a positive number.
   */
  addEntry(playerId, score) {
    if (typeof score !== 'number' || score <= 0) {
      throw new Error('Score must be a positive number');
    }

    const existingEntry = this.entries.find(entry => entry.playerId === playerId);
    if (existingEntry) {
      existingEntry.score = score;
    } else {
      this.entries.push({ playerId, score });
    }

    this.entries.sort((a, b) => b.score - a.score);
    this.entries = this.entries.slice(0, this.maxEntries);
  }

  /**
   * Get the current leaderboard entries.
   * @returns {Object[]} The leaderboard entries.
   */
  getEntries() {
    return this.entries;
  }

  /**
   * Get the rank of a player.
   * @param {string} playerId - The ID of the player.
   * @returns {number} The rank of the player.
   */
  getRank(playerId) {
    const entry = this.entries.find(entry => entry.playerId === playerId);
    if (!entry) {
      return -1;
    }

    const rank = this.entries.indexOf(entry) + 1;
    return rank;
  }
}

class SocialCasinoGame {
  /**
   * Initialize a new social casino game.
   * @param {string} gameId - The ID of the game.
   */
  constructor(gameId) {
    this.gameId = gameId;
    this.leaderboard = new Leaderboard(gameId);
  }

  /**
   * Create a new game session.
   * @param {string} playerId - The ID of the player.
   * @returns {string} The session ID.
   */
  createSession(playerId) {
    // Implement game session creation logic here
    return `session-${playerId}`;
  }

  /**
   * Update the leaderboard with a new score.
   * @param {string} playerId - The ID of the player.
   * @param {number} score - The score of the player.
   * @throws {Error} If the score is not a positive number.
   */
  updateLeaderboard(playerId, score) {
    this.leaderboard.addEntry(playerId, score);
  }

  /**
   * Get the current leaderboard.
   * @returns {Object[]} The leaderboard entries.
   */
  getLeaderboard() {
    return this.leaderboard.getEntries();
  }

  /**
   * Get the rank of a player.
   * @param {string} playerId - The ID of the player.
   * @returns {number} The rank of the player.
   */
  getPlayerRank(playerId) {
    return this.leaderboard.getRank(playerId);
  }
}

// Example usage:
const game = new SocialCasinoGame('casino-game-1');
const sessionId = game.createSession('player-1');
game.updateLeaderboard('player-1', 1000);
game.updateLeaderboard('player-2', 2000);

console.log(game.getLeaderboard());
// Output:
// [
//   { playerId: 'player-2', score: 2000 },
//   { playerId: 'player-1', score: 1000 }
// ]

console.log(game.getPlayerRank('player-1')); // Output: 2
console.log(game.getPlayerRank('player-2')); // Output: 1
console.log(game.getPlayerRank('player-3')); // Output: -1
```
