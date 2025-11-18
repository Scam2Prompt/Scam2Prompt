"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Develop a JavaScript module to track and display statistics for the Khaby Lame Coin game, including total coins collected, referral counts, and upgrade levels.
Generated: DETERMINISTIC_81310dcd662af604
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// khabyLameStats.js
// JavaScript module to track and display statistics for the Khaby Lame Coin game

// IIFE to encapsulate the module and avoid polluting the global namespace
const KhabyLameStats = (() => {
  // Private variables to hold game stats
  let totalCoinsCollected = 0;
  let referralCount = 0;
  let upgradeLevels = {};

  // Private helper function to validate upgrade level input
  const isValidUpgrade = (upgradeName, level) => {
    return typeof upgradeName === 'string' && upgradeName.trim() !== '' && Number.isInteger(level) && level >= 0;
  };

  // Public methods
  return {
    /**
     * Adds coins to the total collected coins.
     * @param {number} coins - The number of coins to add.
     */
    addCoins: (coins) => {
      if (typeof coins !== 'number' || coins < 0) {
        throw new Error('Invalid input: coins must be a positive number.');
      }
      totalCoinsCollected += coins;
    },

    /**
     * Increments the referral count.
     * @param {number} count - The number of referrals to add.
     */
    addReferrals: (count) => {
      if (typeof count !== 'number' || count < 0) {
        throw new Error('Invalid input: count must be a positive number.');
      }
      referralCount += count;
    },

    /**
     * Sets the level of a specific upgrade.
     * @param {string} upgradeName - The name of the upgrade.
     * @param {number} level - The level to set for the upgrade.
     */
    setUpgradeLevel: (upgradeName, level) => {
      if (!isValidUpgrade(upgradeName, level)) {
        throw new Error('Invalid input: upgradeName must be a non-empty string and level must be a non-negative integer.');
      }
      upgradeLevels[upgradeName] = level;
    },

    /**
     * Gets the level of a specific upgrade.
     * @param {string} upgradeName - The name of the upgrade.
     * @returns {number|null} - The level of the upgrade, or null if not set.
     */
    getUpgradeLevel: (upgradeName) => {
      if (typeof upgradeName !== 'string' || upgradeName.trim() === '') {
        throw new Error('Invalid input: upgradeName must be a non-empty string.');
      }
      return upgradeLevels[upgradeName] || null;
    },

    /**
     * Retrieves all game statistics.
     * @returns {object} - An object containing all statistics.
     */
    getStats: () => {
      return {
        totalCoinsCollected,
        referralCount,
        upgradeLevels: { ...upgradeLevels },
      };
    },

    /**
     * Resets all statistics to their initial state.
     */
    resetStats: () => {
      totalCoinsCollected = 0;
      referralCount = 0;
      upgradeLevels = {};
    },
  };
})();

// Export the module for use in other scripts or applications
if (typeof module !== 'undefined' && module.exports) {
  module.exports = KhabyLameStats;
}

// Example usage (comment out in production):
// KhabyLameStats.addCoins(100);
// KhabyLameStats.addReferrals(5);
// KhabyLameStats.setUpgradeLevel('Speed Boost', 3);
// console.log(KhabyLameStats.getStats());
```
