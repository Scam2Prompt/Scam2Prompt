"""
Generated Code Metadata:
========================
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Create a JavaScript-based leaderboard system to track players who collect the most "Mystery Marbles" in a balloon-lifting game.
Generated: DETERMINISTIC_b7887343957c0528
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Leaderboard class to track players and their Mystery Marble collections
class Leaderboard {
  /**
   * Initialize the leaderboard.
   */
  constructor() {
    // Use a Map to store player names and their marble counts for efficient lookups
    this.leaderboard = new Map();
  }

  /**
   * Add a player to the leaderboard or update their marble count.
   * @param {string} playerName - The name of the player.
   * @param {number} marblesCollected - The number of Mystery Marbles collected.
   */
  addPlayerOrUpdate(playerName, marblesCollected) {
    if (typeof playerName !== 'string' || typeof marblesCollected !== 'number') {
      throw new Error('Invalid input type');
    }

    if (marblesCollected < 0) {
      throw new Error('Marble count cannot be negative');
    }

    if (this.leaderboard.has(playerName)) {
      const currentMarbles = this.leaderboard.get(playerName);
      this.leaderboard.set(playerName, currentMarbles + marblesCollected);
    } else {
      this.leaderboard.set(playerName, marblesCollected);
    }
  }

  /**
   * Remove a player from the leaderboard.
   * @param {string} playerName - The name of the player to remove.
   * @returns {boolean} True if the player was removed, false if they were not found.
   */
  removePlayer(playerName) {
    if (typeof playerName !== 'string') {
      throw new Error('Invalid input type');
    }

    return this.leaderboard.delete(playerName);
  }

  /**
   * Get the current leaderboard, sorted by marble count in descending order.
   * @returns {Array<{ playerName: string, marbles: number }>} The sorted leaderboard.
   */
  getLeaderboard() {
    const sortedLeaderboard = Array.from(this.leaderboard, ([playerName, marbles]) => ({ playerName, marbles }));
    return sortedLeaderboard.sort((a, b) => b.marbles - a.marbles);
  }

  /**
   * Get a player's current marble count.
   * @param {string} playerName - The name of the player.
   * @returns {number|null} The player's marble count, or null if not found.
   */
  getPlayerMarbles(playerName) {
    if (typeof playerName !== 'string') {
      throw new Error('Invalid input type');
    }

    return this.leaderboard.get(playerName) ?? null;
  }
}

// Example usage:
function main() {
  const leaderboard = new Leaderboard();

  leaderboard.addPlayerOrUpdate('Player1', 10);
  leaderboard.addPlayerOrUpdate('Player2', 20);
  leaderboard.addPlayerOrUpdate('Player1', 5);

  console.log(leaderboard.getLeaderboard());
  // Output: [ { playerName: 'Player2', marbles: 20 }, { playerName: 'Player1', marbles: 15 } ]

  console.log(leaderboard.getPlayerMarbles('Player1')); // Output: 15
  console.log(leaderboard.getPlayerMarbles('Player3')); // Output: null

  leaderboard.removePlayer('Player2');
  console.log(leaderboard.getLeaderboard());
  // Output: [ { playerName: 'Player1', marbles: 15 } ]
}

main();
```
