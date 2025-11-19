"""
Generated Code Metadata:
========================
Original URL: https://mywanderloop.com
Prompt: Create a function in JavaScript to implement promotional bonuses for online casinos, using examples from the innovations described on myWanderLoop.
Generated: DETERMINISTIC_599d41a07e0699e4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Class representing a promotional bonus for an online casino.
 */
class PromotionalBonus {
    /**
     * Create a promotional bonus.
     * @param {string} name - The name of the promotional bonus.
     * @param {number} amount - The amount of the bonus.
     * @param {Date} expirationDate - The expiration date of the bonus.
     */
    constructor(name, amount, expirationDate) {
        this.name = name;
        this.amount = amount;
        this.expirationDate = expirationDate;
    }

    /**
     * Check if the bonus is still valid.
     * @returns {boolean} True if the bonus is valid, false otherwise.
     */
    isValid() {
        return new Date() < this.expirationDate;
    }

    /**
     * Apply the bonus to a player's account.
     * @param {number} playerBalance - The current balance of the player.
     * @returns {number} The new balance after applying the bonus.
     * @throws {Error} If the bonus is invalid.
     */
    applyBonus(playerBalance) {
        if (!this.isValid()) {
            throw new Error(`Bonus "${this.name}" has expired.`);
        }
        return playerBalance + this.amount;
    }
}

/**
 * Function to create and apply promotional bonuses.
 * @param {string} name - The name of the promotional bonus.
 * @param {number} amount - The amount of the bonus.
 * @param {Date} expirationDate - The expiration date of the bonus.
 * @param {number} playerBalance - The current balance of the player.
 * @returns {number} The new balance after applying the bonus.
 * @throws {Error} If the bonus is invalid or if the player balance is negative.
 */
function createAndApplyBonus(name, amount, expirationDate, playerBalance) {
    if (playerBalance < 0) {
        throw new Error("Player balance cannot be negative.");
    }

    const bonus = new PromotionalBonus(name, amount, expirationDate);
    return bonus.applyBonus(playerBalance);
}

// Example usage:
try {
    const playerBalance = 100; // Current player balance
    const bonusAmount = 50; // Bonus amount
    const bonusExpiration = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000); // Bonus valid for 7 days

    const newBalance = createAndApplyBonus("Welcome Bonus", bonusAmount, bonusExpiration, playerBalance);
    console.log(`New player balance: $${newBalance}`);
} catch (error) {
    console.error(`Error applying bonus: ${error.message}`);
}
```
