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
// khabyLameCoinTracker.js

/**
 * KhabyLameCoinTracker - A module to track and display statistics for the Khaby Lame Coin game.
 * This module includes functionality to track total coins collected, referral counts, and upgrade levels.
 */

class KhabyLameCoinTracker {
    constructor() {
        // Initialize the statistics
        this.totalCoins = 0;
        this.referralCounts = 0;
        this.upgradeLevels = 0;
    }

    /**
     * Adds coins to the total coins collected.
     * @param {number} coins - The number of coins to add. Must be a non-negative integer.
     */
    addCoins(coins) {
        if (typeof coins !== 'number' || coins < 0) {
            throw new Error('Invalid input: coins must be a non-negative integer.');
        }
        this.totalCoins += coins;
    }

    /**
     * Increments the referral count by one.
     */
    addReferral() {
        this.referralCounts += 1;
    }

    /**
     * Upgrades the level by a specified amount.
     * @param {number} levels - The number of levels to upgrade. Must be a positive integer.
     */
    upgradeLevel(levels) {
        if (typeof levels !== 'number' || levels <= 0) {
            throw new Error('Invalid input: levels must be a positive integer.');
        }
        this.upgradeLevels += levels;
    }

    /**
     * Retrieves the current statistics.
     * @returns {object} An object containing total coins, referral counts, and upgrade levels.
     */
    getStats() {
        return {
            totalCoins: this.totalCoins,
            referralCounts: this.referralCounts,
            upgradeLevels: this.upgradeLevels
        };
    }

    /**
     * Displays the current statistics in a user-friendly format.
     */
    displayStats() {
        const stats = this.getStats();
        console.log(`Total Coins Collected: ${stats.totalCoins}`);
        console.log(`Referral Counts: ${stats.referralCounts}`);
        console.log(`Upgrade Levels: ${stats.upgradeLevels}`);
    }
}

// Export the module for use in other parts of the application
export default KhabyLameCoinTracker;
```

### Usage Example
```javascript
import KhabyLameCoinTracker from './khabyLameCoinTracker.js';

const tracker = new KhabyLameCoinTracker();

try {
    tracker.addCoins(100);
    tracker.addReferral();
    tracker.upgradeLevel(2);
    tracker.displayStats();
} catch (error) {
    console.error(error.message);
}
```
