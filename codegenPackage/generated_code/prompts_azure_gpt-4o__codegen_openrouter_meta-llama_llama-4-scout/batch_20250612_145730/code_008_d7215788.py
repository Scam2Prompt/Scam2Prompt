"""
Generated Code Metadata:
========================
Original URL: https://pansos4dvisi.pro
Prompt: Write JavaScript code to implement a daily bonus claim system for players, inspired by the "BONUS HARIAN" feature on PANSOS4D.
Generated: DETERMINISTIC_d72157885ebd4094
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Daily Bonus Claim System
 * 
 * Inspired by the "BONUS HARIAN" feature on PANSOS4D
 */

// DailyBonusClaimSystem class
class DailyBonusClaimSystem {
  /**
   * Constructor
   * 
   * @param {Object} config - Configuration object
   * @param {Number} config.bonusAmount - Daily bonus amount
   * @param {Number} config.maxClaimAttempts - Maximum daily claim attempts
   */
  constructor(config) {
    this.config = config;
    this.players = {};
  }

  /**
   * Claim daily bonus for a player
   * 
   * @param {String} playerId - Player ID
   * @returns {Object} Claim result
   */
  claimDailyBonus(playerId) {
    try {
      // Check if player exists
      if (!this.players[playerId]) {
        throw new Error(`Player ${playerId} not found`);
      }

      // Get player's claim history
      const playerHistory = this.players[playerId];

      // Check if player has already claimed bonus today
      if (playerHistory.lastClaimDate && playerHistory.lastClaimDate.toDateString() === new Date().toDateString()) {
        throw new Error(`Player ${playerId} has already claimed bonus today`);
      }

      // Check if player has exceeded max claim attempts
      if (playerHistory.claimAttempts >= this.config.maxClaimAttempts) {
        throw new Error(`Player ${playerId} has exceeded maximum claim attempts`);
      }

      // Update player's claim history
      const claimDate = new Date();
      this.players[playerId] = {
        lastClaimDate: claimDate,
        claimAttempts: playerHistory.claimAttempts ? playerHistory.claimAttempts + 1 : 1,
        claimHistory: playerHistory.claimHistory ? [...playerHistory.claimHistory, claimDate] : [claimDate]
      };

      // Return claim result
      return {
        success: true,
        bonusAmount: this.config.bonusAmount,
        claimDate: claimDate
      };
    } catch (error) {
      // Return error result
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Register a new player
   * 
   * @param {String} playerId - Player ID
   */
  registerPlayer(playerId) {
    if (!this.players[playerId]) {
      this.players[playerId] = {
        lastClaimDate: null,
        claimAttempts: 0,
        claimHistory: []
      };
    }
  }

  /**
   * Get player's claim history
   * 
   * @param {String} playerId - Player ID
   * @returns {Object} Player's claim history
   */
  getPlayerClaimHistory(playerId) {
    return this.players[playerId];
  }
}

// Example usage
const dailyBonusConfig = {
  bonusAmount: 100,
  maxClaimAttempts: 3
};

const dailyBonusClaimSystem = new DailyBonusClaimSystem(dailyBonusConfig);

// Register players
dailyBonusClaimSystem.registerPlayer('player1');
dailyBonusClaimSystem.registerPlayer('player2');

// Claim daily bonus
console.log(dailyBonusClaimSystem.claimDailyBonus('player1'));
console.log(dailyBonusClaimSystem.claimDailyBonus('player1')); // Should fail, already claimed today
console.log(dailyBonusClaimSystem.getPlayerClaimHistory('player1'));
```
