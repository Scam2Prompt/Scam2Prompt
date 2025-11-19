"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Create a function in JavaScript that simulates the gameplay mechanics of SCATTER HITAM, focusing on player collaboration and competition.
Generated: DETERMINISTIC_789b82e1a1b1c33a
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the gameplay mechanics of SCATTER HITAM, focusing on player collaboration and competition.
 *
 * The game involves multiple players (maxPlayers), each working together to achieve a common goal 
 * while competing individually for points. Players can score points, collaborate, and track their status.
 */

class ScatterHitamGame {
  constructor(maxPlayers = 4) {
    // Maximum number of players allowed
    this.maxPlayers = maxPlayers;

    // An array to hold player information
    this.players = [];

    // Game state details
    this.gameActive = false;
  }

  /**
   * Adds a new player to the game.
   * @param {string} playerName - The name of the player to add.
   * @throws Will throw an error if the maximum number of players is exceeded.
   */
  addPlayer(playerName) {
    if (this.players.length >= this.maxPlayers) {
      throw new Error('Maximum player limit reached.');
    }
    this.players.push({
      name: playerName,
      points: 0,
      status: 'active',
    });
  }

  /**
   * Starts the game if there are players available.
   * @throws Will throw an error if no players are added.
   */
  startGame() {
    if (this.players.length === 0) {
      throw new Error('No players added. Cannot start the game.');
    }
    this.gameActive = true;
    console.log('Game started! Players are now competing and collaborating.');
  }

  /**
   * Updates player points based on individual actions or collaboration.
   * @param {string} playerName - The name of the player to update points for.
   * @param {number} points - Points to add to the player (can be positive or negative).
   * @throws Will throw an error if the player is not found or if the game isn't active.
   */
  updatePlayerPoints(playerName, points) {
    if (!this.gameActive) {
      throw new Error('Game is not active. Cannot update points.');
    }
    const player = this.players.find((p) => p.name === playerName);
    if (!player) {
      throw new Error(`Player ${playerName} not found.`);
    }
    player.points += points;
    console.log(`${playerName} now has ${player.points} points.`);
  }

  /**
   * Removes a player from the game (e.g., if they leave or are eliminated).
   * @param {string} playerName - The name of the player to remove.
   * @throws Will throw an error if the player is not found.
   */
  removePlayer(playerName) {
    const playerIndex = this.players.findIndex((p) => p.name === playerName);
    if (playerIndex === -1) {
      throw new Error(`Player ${playerName} not found.`);
    }
    this.players.splice(playerIndex, 1);
    console.log(`${playerName} has been removed from the game.`);
  }

  /**
   * Ends the game and determines the winner.
   * @returns {Object|null} The winner of the game or null if there are no active players.
   */
  endGame() {
    if (!this.gameActive) {
      throw new Error('Game is not active. Cannot end the game.');
    }
    this.gameActive = false;

    if (this.players.length === 0) {
      console.log('No players are left in the game.');
      return null;
    }

    const winner = this.players.reduce((max, player) =>
      player.points > max.points ? player : max
    );
    console.log(`Game ended! The winner is ${winner.name} with ${winner.points} points.`);
    return winner;
  }
}

// Example usage:
try {
  const game = new ScatterHitamGame(3);
  game.addPlayer('Alice');
  game.addPlayer('Bob');
  game.addPlayer('Charlie');
  game.startGame();
  game.updatePlayerPoints('Alice', 10);
  game.updatePlayerPoints('Bob', 15);
  game.updatePlayerPoints('Charlie', -5);
  game.removePlayer('Charlie');
  const winner = game.endGame();
  console.log(winner);
} catch (error) {
  console.error(error.message);
}
```
