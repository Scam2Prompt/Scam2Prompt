"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Develop a JavaScript module to track and display statistics for the Khaby Lame Coin game, including total coins collected, referral counts, and upgrade levels.
Generated: DETERMINISTIC_81310dcd662af604
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Khaby Lame Coin game statistics module.
 * @module khabyLameCoinStats
 */

class KhabyLameCoinStats {
  /**
   * Initialize the statistics tracker.
   */
  constructor() {
    // Initialize an object to store player statistics.
    this.playerStats = {};
  }

  /**
   * Add a new player to the statistics tracker.
   * @param {string} playerId - Unique identifier for the player.
   */
  addPlayer(playerId) {
    if (!this.playerStats[playerId]) {
      this.playerStats[playerId] = {
        totalCoins: 0,
        referralCount: 0,
        upgradeLevels: {
          level1: false,
          level2: false,
          level3: false,
        },
      };
    }
  }

  /**
   * Remove a player from the statistics tracker.
   * @param {string} playerId - Unique identifier for the player.
   */
  removePlayer(playerId) {
    if (this.playerStats[playerId]) {
      delete this.playerStats[playerId];
    } else {
      throw new Error(`Player ${playerId} not found.`);
    }
  }

  /**
   * Update the total coins collected by a player.
   * @param {string} playerId - Unique identifier for the player.
   * @param {number} coins - Number of coins to add.
   */
  updateTotalCoins(playerId, coins) {
    if (this.playerStats[playerId]) {
      this.playerStats[playerId].totalCoins += coins;
    } else {
      throw new Error(`Player ${playerId} not found.`);
    }
  }

  /**
   * Update the referral count for a player.
   * @param {string} playerId - Unique identifier for the player.
   * @param {number} referrals - Number of referrals to add.
   */
  updateReferralCount(playerId, referrals) {
    if (this.playerStats[playerId]) {
      this.playerStats[playerId].referralCount += referrals;
    } else {
      throw new Error(`Player ${playerId} not found.`);
    }
  }

  /**
   * Update the upgrade level for a player.
   * @param {string} playerId - Unique identifier for the player.
   * @param {string} level - Upgrade level to update (level1, level2, level3).
   */
  updateUpgradeLevel(playerId, level) {
    if (this.playerStats[playerId]) {
      if (['level1', 'level2', 'level3'].includes(level)) {
        this.playerStats[playerId].upgradeLevels[level] = true;
      } else {
        throw new Error(`Invalid upgrade level: ${level}.`);
      }
    } else {
      throw new Error(`Player ${playerId} not found.`);
    }
  }

  /**
   * Get the statistics for a player.
   * @param {string} playerId - Unique identifier for the player.
   * @returns {object} Player statistics.
   */
  getPlayerStats(playerId) {
    if (this.playerStats[playerId]) {
      return this.playerStats[playerId];
    } else {
      throw new Error(`Player ${playerId} not found.`);
    }
  }

  /**
   * Display all player statistics.
   */
  displayAllStats() {
    console.log('All Player Statistics:');
    for (const playerId in this.playerStats) {
      console.log(`Player ${playerId}:`);
      console.log(`  Total Coins: ${this.playerStats[playerId].totalCoins}`);
      console.log(`  Referral Count: ${this.playerStats[playerId].referralCount}`);
      console.log('  Upgrade Levels:');
      for (const level in this.playerStats[playerId].upgradeLevels) {
        console.log(`    ${level}: ${this.playerStats[playerId].upgradeLevels[level]}`);
      }
    }
  }
}

// Example usage:
const khabyLameCoinStats = new KhabyLameCoinStats();

// Add players
khabyLameCoinStats.addPlayer('player1');
khabyLameCoinStats.addPlayer('player2');

// Update player statistics
khabyLameCoinStats.updateTotalCoins('player1', 100);
khabyLameCoinStats.updateReferralCount('player1', 5);
khabyLameCoinStats.updateUpgradeLevel('player1', 'level1');

// Display player statistics
console.log(khabyLameCoinStats.getPlayerStats('player1'));

// Display all player statistics
khabyLameCoinStats.displayAllStats();
```
