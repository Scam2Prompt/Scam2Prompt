"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Write a JavaScript function that implements the scoring system for an Agar.io-like game, where players earn points by consuming other players.
Generated: DETERMINISTIC_c32f8ac5c9799f43
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a player in the game.
 */
class Player {
  /**
   * Creates a new player.
   * @param {string} id - The player's unique ID.
   * @param {number} mass - The player's initial mass.
   */
  constructor(id, mass) {
    this.id = id;
    this.mass = mass;
    this.score = 0;
  }

  /**
   * Updates the player's score based on the mass of the consumed player.
   * @param {number} mass - The mass of the consumed player.
   */
  updateScore(mass) {
    this.score += Math.floor(mass * 10); // 10 points per unit of mass consumed
  }
}

/**
 * Represents the game state and scoring system.
 */
class Game {
  /**
   * Creates a new game.
   */
  constructor() {
    this.players = {};
  }

  /**
   * Adds a new player to the game.
   * @param {string} id - The player's unique ID.
   * @param {number} mass - The player's initial mass.
   */
  addPlayer(id, mass) {
    if (this.players[id]) {
      throw new Error(`Player with ID ${id} already exists.`);
    }
    this.players[id] = new Player(id, mass);
  }

  /**
   * Removes a player from the game.
   * @param {string} id - The player's unique ID.
   */
  removePlayer(id) {
    if (!this.players[id]) {
      throw new Error(`Player with ID ${id} does not exist.`);
    }
    delete this.players[id];
  }

  /**
   * Consumes one player with another.
   * @param {string} consumerId - The ID of the player consuming another.
   * @param {string} consumedId - The ID of the player being consumed.
   */
  consumePlayer(consumerId, consumedId) {
    if (!this.players[consumerId] || !this.players[consumedId]) {
      throw new Error('Both players must exist in the game.');
    }
    if (consumerId === consumedId) {
      throw new Error('A player cannot consume themselves.');
    }

    const consumer = this.players[consumerId];
    const consumed = this.players[consumedId];

    // Update consumer's mass and score
    consumer.mass += consumed.mass;
    consumer.updateScore(consumed.mass);

    // Remove consumed player
    this.removePlayer(consumedId);
  }

  /**
   * Gets a player's score.
   * @param {string} id - The player's unique ID.
   * @returns {number} The player's score.
   */
  getPlayerScore(id) {
    if (!this.players[id]) {
      throw new Error(`Player with ID ${id} does not exist.`);
    }
    return this.players[id].score;
  }
}

// Example usage:
function main() {
  const game = new Game();

  game.addPlayer('player1', 100);
  game.addPlayer('player2', 50);

  console.log(game.getPlayerScore('player1')); // 0
  console.log(game.getPlayerScore('player2')); // 0

  game.consumePlayer('player1', 'player2');

  console.log(game.getPlayerScore('player1')); // 500
}

main();
```
