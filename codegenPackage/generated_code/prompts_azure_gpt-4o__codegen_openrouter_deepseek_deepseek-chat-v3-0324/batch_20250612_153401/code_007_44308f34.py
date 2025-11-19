"""
Generated Code Metadata:
========================
Original URL: https://7a.game
Prompt: Generate JavaScript code to track user activity and display statistics for games like slots and roulette.
Generated: DETERMINISTIC_44308f3439871d57
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
 * User Activity Tracker for Casino Games
 * Tracks user activity and displays statistics for games like slots and roulette.
 */

class UserActivityTracker {
  constructor() {
    this.userSessions = {};
    this.gameStats = {
      slots: {
        plays: 0,
        wins: 0,
        losses: 0,
        totalWagered: 0,
        totalWon: 0
      },
      roulette: {
        plays: 0,
        wins: 0,
        losses: 0,
        totalWagered: 0,
        totalWon: 0
      }
    };
  }

  /**
   * Starts a new user session
   * @param {string} userId - Unique identifier for the user
   * @param {string} gameType - Type of game (slots or roulette)
   */
  startSession(userId, gameType) {
    if (!userId || !gameType) {
      console.error('Error: userId and gameType are required');
      return;
    }

    if (!['slots', 'roulette'].includes(gameType)) {
      console.error('Error: Invalid game type. Must be "slots" or "roulette"');
      return;
    }

    this.userSessions[userId] = {
      gameType,
      startTime: new Date(),
      wagers: [],
      results: []
    };
  }

  /**
   * Records a game play
   * @param {string} userId - Unique identifier for the user
   * @param {number} wager - Amount wagered
   * @param {boolean} win - Whether the play resulted in a win
   * @param {number} [winAmount=0] - Amount won (if applicable)
   */
  recordPlay(userId, wager, win, winAmount = 0) {
    if (!this.userSessions[userId]) {
      console.error('Error: No active session for this user');
      return;
    }

    const session = this.userSessions[userId];
    const gameType = session.gameType;

    // Update session data
    session.wagers.push(wager);
    session.results.push({ win, winAmount });

    // Update game statistics
    this.gameStats[gameType].plays++;
    this.gameStats[gameType].totalWagered += wager;

    if (win) {
      this.gameStats[gameType].wins++;
      this.gameStats[gameType].totalWon += winAmount;
    } else {
      this.gameStats[gameType].losses++;
    }
  }

  /**
   * Ends a user session
   * @param {string} userId - Unique identifier for the user
   */
  endSession(userId) {
    if (!this.userSessions[userId]) {
      console.error('Error: No active session for this user');
      return;
    }

    const session = this.userSessions[userId];
    session.endTime = new Date();
    session.duration = (session.endTime - session.startTime) / 1000; // in seconds

    // Calculate session statistics
    session.totalWagered = session.wagers.reduce((sum, wager) => sum + wager, 0);
    session.totalWon = session.results.reduce((sum, result) => sum + (result.win ? result.winAmount : 0), 0);
    session.netResult = session.totalWon - session.totalWagered;
    session.winRate = session.results.filter(r => r.win).length / session.results.length || 0;

    return session;
  }

  /**
   * Gets statistics for a specific game type
   * @param {string} gameType - Type of game (slots or roulette)
   * @returns {object} Game statistics
   */
  getGameStats(gameType) {
    if (!['slots', 'roulette'].includes(gameType)) {
      console.error('Error: Invalid game type. Must be "slots" or "roulette"');
      return null;
    }

    const stats = this.gameStats[gameType];
    return {
      ...stats,
      winRate: stats.wins / stats.plays || 0,
      averageWager: stats.totalWagered / stats.plays || 0,
      averageWin: stats.wins > 0 ? stats.totalWon / stats.wins : 0
    };
  }

  /**
   * Gets all user sessions
   * @returns {object} All user sessions
   */
  getAllSessions() {
    return this.userSessions;
  }

  /**
   * Gets a specific user session
   * @param {string} userId - Unique identifier for the user
   * @returns {object} User session data
   */
  getUserSession(userId) {
    return this.userSessions[userId] || null;
  }

  /**
   * Resets all statistics and sessions
   */
  resetAll() {
    this.userSessions = {};
    this.gameStats = {
      slots: {
        plays: 0,
        wins: 0,
        losses: 0,
        totalWagered: 0,
        totalWon: 0
      },
      roulette: {
        plays: 0,
        wins: 0,
        losses: 0,
        totalWagered: 0,
        totalWon: 0
      }
    };
  }
}

// Example usage:
/*
const tracker = new UserActivityTracker();

// Start a session
tracker.startSession('user123', 'slots');

// Record plays
tracker.recordPlay('user123', 10, true, 20);
tracker.recordPlay('user123', 10, false);
tracker.recordPlay('user123', 20, true, 50);

// End session
const sessionStats = tracker.endSession('user123');

// Get game statistics
const slotsStats = tracker.getGameStats('slots');
console.log(slotsStats);
*/
```
