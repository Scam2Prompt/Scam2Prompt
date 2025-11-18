"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Write a script in JavaScript to manage "upgrades" in the Khaby Lame Coin game, where each level increases the number of coins earned per tap. Ensure the script handles multiple upgrade levels.
Generated: DETERMINISTIC_842bcea0f008e48f
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Khaby Lame Coin Game Upgrade Manager
 * This script manages upgrades for increasing the number of coins earned per tap.
 */

class UpgradeManager {
    constructor() {
        this.currentLevel = 0; // Current upgrade level
        this.coinsPerTap = 1;  // Initial coins earned per tap
        this.upgradeCost = 10;  // Cost of the next upgrade
    }

    /**
     * Method to tap and earn coins based on the current upgrade level.
     * @returns {number} - Number of coins earned from the tap.
     */
    tap() {
        console.log(`Coins earned: ${this.coinsPerTap}`);
        return this.coinsPerTap;
    }

    /**
     * Method to purchase an upgrade if enough coins are available.
     * @param {number} availableCoins - The number of coins the player has.
     * @throws Will throw an error if not enough coins are available for the upgrade.
     */
    purchaseUpgrade(availableCoins) {
        if (availableCoins < this.upgradeCost) {
            throw new Error('Not enough coins for upgrade.');
        }
        
        // Deduct the upgrade cost from available coins
        availableCoins -= this.upgradeCost;
        
        // Level up and increase coins per tap
        this.currentLevel++;
        this.coinsPerTap *= 2; // Double the coins per tap
        this.upgradeCost *= 1.5; // Increase upgrade cost by 50%

        console.log(`Upgrade purchased! Current level: ${this.currentLevel}, New coins per tap: ${this.coinsPerTap}, Next upgrade cost: ${Math.round(this.upgradeCost)}`);
        
        return availableCoins; // Return remaining coins
    }

    /**
     * Method to get the current upgrade level and stats.
     * @returns {Object} - Current upgrade stats.
     */
    getStatus() {
        return {
            level: this.currentLevel,
            coinsPerTap: this.coinsPerTap,
            upgradeCost: Math.round(this.upgradeCost)
        };
    }
}

// Example usage
const upgradeManager = new UpgradeManager();

let playerCoins = 50; // Simulated player coins

try {
    console.log(upgradeManager.tap()); // Tap to earn coins
    playerCoins = upgradeManager.purchaseUpgrade(playerCoins); // Attempt to purchase an upgrade
    console.log(upgradeManager.getStatus()); // Display current status
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
