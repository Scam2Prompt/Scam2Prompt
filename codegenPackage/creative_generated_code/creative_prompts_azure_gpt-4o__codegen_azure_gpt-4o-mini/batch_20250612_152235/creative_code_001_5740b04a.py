"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Create a function in JavaScript that automates the process of upgrading levels in Hamster Kombat based on the number of coins collected. Use level thresholds such as Bronze (5000 coins), Silver (25,000 coins), and Gold (100,000 coins).
Generated: DETERMINISTIC_5740b04aeab01cfd
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a player in Hamster Kombat.
 */
class HamsterKombatPlayer {
    constructor() {
        this.coins = 0;        // Total coins collected by the player
        this.level = 'Bronze'; // Initial level of the player
    }

    /**
     * Method to add coins to the player's total.
     * @param {number} amount - The amount of coins to add.
     * @throws {Error} Will throw an error if the amount is not a positive number.
     */
    addCoins(amount) {
        if (amount <= 0 || typeof amount !== 'number') {
            throw new Error('Amount must be a positive number.');
        }
        this.coins += amount;
        this.updateLevel(); // Check and update the player's level after adding coins
    }

    /**
     * Method to determine the player's level based on the total coins collected.
     */
    updateLevel() {
        if (this.coins >= 100000) {
            this.level = 'Gold';
        } else if (this.coins >= 25000) {
            this.level = 'Silver';
        } else if (this.coins >= 5000) {
            this.level = 'Bronze';
        } else {
            this.level = 'Newbie'; // Level for players with fewer than 5000 coins
        }
    }

    /**
     * Method to get the current status of the player.
     * @returns {string} A string representation of the player's current coins and level.
     */
    getStatus() {
        return `Coins: ${this.coins}, Level: ${this.level}`;
    }
}

// Example usage
try {
    const player = new HamsterKombatPlayer();
    player.addCoins(6000); // Adds 6000 coins
    console.log(player.getStatus()); // Output: Coins: 6000, Level: Bronze

    player.addCoins(20000); // Adds 20000 coins
    console.log(player.getStatus()); // Output: Coins: 26000, Level: Silver

    player.addCoins(80000); // Adds 80000 coins
    console.log(player.getStatus()); // Output: Coins: 106000, Level: Gold
} catch (error) {
    console.error(error.message); // Log any errors that occur
}
```
