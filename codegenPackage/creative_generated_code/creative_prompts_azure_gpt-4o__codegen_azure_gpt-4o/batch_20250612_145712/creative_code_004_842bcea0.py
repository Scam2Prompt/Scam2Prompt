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
// Khaby Lame Coin Game Upgrade Management Script
// This script handles upgrade levels, where each level increases the coins earned per tap.

// Define the UpgradeManager class
class UpgradeManager {
  constructor(initialCoinsPerTap = 1) {
    // Initialize with default coins per tap
    this.coinsPerTap = initialCoinsPerTap; // Coins earned per tap
    this.upgradeLevel = 0; // Current upgrade level
    this.coins = 0; // Total coins earned
    this.upgrades = [
      { level: 1, cost: 10, bonus: 2 },
      { level: 2, cost: 50, bonus: 5 },
      { level: 3, cost: 150, bonus: 10 },
      { level: 4, cost: 500, bonus: 20 },
      { level: 5, cost: 2000, bonus: 50 },
    ]; // Define the upgrades with level, cost, and bonus
  }

  // Simulates a tap to earn coins
  tap() {
    this.coins += this.coinsPerTap; // Add coins earned from the tap
    console.log(`Coins earned: ${this.coins}`);
  }

  // Handles coin upgrades
  upgrade() {
    const nextUpgrade = this.upgrades[this.upgradeLevel]; // Get the next upgrade level

    if (!nextUpgrade) {
      console.log("All upgrades have been purchased. Maximum level reached!");
      return;
    }

    if (this.coins >= nextUpgrade.cost) {
      this.coins -= nextUpgrade.cost; // Deduct coins for the upgrade
      this.coinsPerTap += nextUpgrade.bonus; // Add the bonus coins per tap
      this.upgradeLevel++; // Increment the upgrade level
      console.log(`Upgrade successful! Level: ${this.upgradeLevel}, Coins per tap: ${this.coinsPerTap}`);
    } else {
      console.log(`Not enough coins for upgrade! Needed: ${nextUpgrade.cost}, Available: ${this.coins}`);
    }
  }

  // Displays the current game status
  showStatus() {
    console.log("====== Game Status ======");
    console.log(`Coins: ${this.coins}`);
    console.log(`Coins per tap: ${this.coinsPerTap}`);
    console.log(`Upgrade Level: ${this.upgradeLevel}`);
    console.log("=========================");
  }
}

// Example usage
const game = new UpgradeManager(); // Initialize the game

game.tap(); // Simulate a tap
game.showStatus(); // Show the current status

game.upgrade(); // Try to upgrade
game.tap(); // Simulate more taps
game.tap();
game.showStatus(); // Show the status again

game.upgrade(); // Try upgrading again
game.showStatus(); // Final status
```
