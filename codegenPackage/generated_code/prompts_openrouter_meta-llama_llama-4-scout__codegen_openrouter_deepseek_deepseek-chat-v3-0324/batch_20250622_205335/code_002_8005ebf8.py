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
/**
 * Leaderboard System for Social Casino Game
 * 
 * Features:
 * - Track player scores
 * - Display top players globally and among friends
 * - Handle prize distribution
 * - Secure and efficient data handling
 */

class Leaderboard {
  constructor() {
    this.players = new Map(); // playerId -> {name, score}
    this.friendships = new Map(); // playerId -> Set<friendId>
    this.prizes = [];
  }

  /**
   * Add or update a player's score
   * @param {string} playerId - Unique player identifier
   * @param {string} name - Player display name
   * @param {number} score - Player's latest score
   */
  updatePlayerScore(playerId, name, score) {
    if (!playerId || !name || typeof score !== 'number') {
      throw new Error('Invalid player data');
    }

    if (score < 0) {
      throw new Error('Score cannot be negative');
    }

    this.players.set(playerId, { name, score });
  }

  /**
   * Add a friendship connection between two players
   * @param {string} player1 - First player ID
   * @param {string} player2 - Second player ID
   */
  addFriendship(player1, player2) {
    if (!player1 || !player2) {
      throw new Error('Invalid player IDs');
    }

    if (!this.friendships.has(player1)) {
      this.friendships.set(player1, new Set());
    }
    if (!this.friendships.has(player2)) {
      this.friendships.set(player2, new Set());
    }

    this.friendships.get(player1).add(player2);
    this.friendships.get(player2).add(player1);
  }

  /**
   * Get top N players globally
   * @param {number} limit - Number of top players to return
   * @returns {Array} Sorted array of top players
   */
  getGlobalLeaderboard(limit = 10) {
    return Array.from(this.players.entries())
      .map(([id, data]) => ({ id, ...data }))
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }

  /**
   * Get top N friends for a player
   * @param {string} playerId - Player to get friends for
   * @param {number} limit - Number of top friends to return
   * @returns {Array} Sorted array of top friends
   */
  getFriendsLeaderboard(playerId, limit = 10) {
    if (!this.friendships.has(playerId)) {
      return [];
    }

    const friends = this.friendships.get(playerId);
    return Array.from(friends)
      .filter(friendId => this.players.has(friendId))
      .map(friendId => {
        const { name, score } = this.players.get(friendId);
        return { id: friendId, name, score };
      })
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }

  /**
   * Set prizes for the current leaderboard period
   * @param {Array} prizes - Array of prize objects {position, reward}
   */
  setPrizes(prizes) {
    if (!Array.isArray(prizes)) {
      throw new Error('Prizes must be an array');
    }

    this.prizes = prizes.sort((a, b) => a.position - b.position);
  }

  /**
   * Distribute prizes to top players
   * @returns {Map} Map of playerId -> prize
   */
  distributePrizes() {
    if (this.prizes.length === 0) {
      throw new Error('No prizes configured');
    }

    const globalTop = this.getGlobalLeaderboard(this.prizes[this.prizes.length - 1].position);
    const prizeMap = new Map();

    this.prizes.forEach(prize => {
      const player = globalTop[prize.position - 1];
      if (player) {
        prizeMap.set(player.id, prize.reward);
      }
    });

    return prizeMap;
  }

  /**
   * Get player's current rank globally
   * @param {string} playerId - Player to check
   * @returns {number} Global rank (1-based) or -1 if not found
   */
  getPlayerGlobalRank(playerId) {
    if (!this.players.has(playerId)) {
      return -1;
    }

    const sorted = Array.from(this.players.entries())
      .sort((a, b) => b[1].score - a[1].score);
    
    const index = sorted.findIndex(([id]) => id === playerId);
    return index >= 0 ? index + 1 : -1;
  }
}

// Example usage:
/*
const leaderboard = new Leaderboard();

// Add players
leaderboard.updatePlayerScore('player1', 'Alice', 1000);
leaderboard.updatePlayerScore('player2', 'Bob', 1500);
leaderboard.updatePlayerScore('player3', 'Charlie', 800);

// Add friendships
leaderboard.addFriendship('player1', 'player2');
leaderboard.addFriendship('player1', 'player3');

// Set prizes
leaderboard.setPrizes([
  { position: 1, reward: 'Gold Trophy' },
  { position: 2, reward: 'Silver Trophy' },
  { position: 3, reward: 'Bronze Trophy' }
]);

// Get leaderboards
console.log('Global Leaderboard:', leaderboard.getGlobalLeaderboard());
console.log('Friends Leaderboard for player1:', leaderboard.getFriendsLeaderboard('player1'));

// Distribute prizes
console.log('Prizes Distributed:', leaderboard.distributePrizes());

// Get player rank
console.log('Alice Rank:', leaderboard.getPlayerGlobalRank('player1'));
*/
```
