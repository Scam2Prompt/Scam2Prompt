"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Generate JavaScript code for creating a rewards system for an online casino, including features like free spins and bonuses as described in Zeus Fortune.
Generated: DETERMINISTIC_5af95161796982d1
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * RewardsSystem class to manage rewards for an online casino.
 * Features include free spins and bonuses.
 */
class RewardsSystem {
    constructor() {
        this.users = new Map(); // Store user rewards
    }

    /**
     * Adds a new user to the rewards system.
     * @param {string} userId - Unique identifier for the user.
     */
    addUser(userId) {
        if (this.users.has(userId)) {
            throw new Error(`User with ID ${userId} already exists.`);
        }
        this.users.set(userId, { freeSpins: 0, bonuses: 0 });
    }

    /**
     * Adds free spins to a user's account.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} spins - Number of free spins to add.
     */
    addFreeSpins(userId, spins) {
        this.validateUser(userId);
        if (spins <= 0) {
            throw new Error("Number of spins must be greater than zero.");
        }
        this.users.get(userId).freeSpins += spins;
    }

    /**
     * Adds a bonus to a user's account.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} amount - Amount of bonus to add.
     */
    addBonus(userId, amount) {
        this.validateUser(userId);
        if (amount <= 0) {
            throw new Error("Bonus amount must be greater than zero.");
        }
        this.users.get(userId).bonuses += amount;
    }

    /**
     * Redeems free spins for a user.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} spins - Number of free spins to redeem.
     * @returns {boolean} - True if redemption is successful, false otherwise.
     */
    redeemFreeSpins(userId, spins) {
        this.validateUser(userId);
        if (spins <= 0) {
            throw new Error("Number of spins to redeem must be greater than zero.");
        }
        const user = this.users.get(userId);
        if (user.freeSpins < spins) {
            throw new Error("Insufficient free spins.");
        }
        user.freeSpins -= spins;
        return true; // Redemption successful
    }

    /**
     * Redeems a bonus for a user.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} amount - Amount of bonus to redeem.
     * @returns {boolean} - True if redemption is successful, false otherwise.
     */
    redeemBonus(userId, amount) {
        this.validateUser(userId);
        if (amount <= 0) {
            throw new Error("Bonus amount to redeem must be greater than zero.");
        }
        const user = this.users.get(userId);
        if (user.bonuses < amount) {
            throw new Error("Insufficient bonus amount.");
        }
        user.bonuses -= amount;
        return true; // Redemption successful
    }

    /**
     * Validates if the user exists in the rewards system.
     * @param {string} userId - Unique identifier for the user.
     * @throws Will throw an error if the user does not exist.
     */
    validateUser(userId) {
        if (!this.users.has(userId)) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
    }

    /**
     * Retrieves the rewards information for a user.
     * @param {string} userId - Unique identifier for the user.
     * @returns {Object} - Object containing free spins and bonuses.
     */
    getUserRewards(userId) {
        this.validateUser(userId);
        return this.users.get(userId);
    }
}

// Example usage
try {
    const rewardsSystem = new RewardsSystem();
    rewardsSystem.addUser("user123");
    rewardsSystem.addFreeSpins("user123", 10);
    rewardsSystem.addBonus("user123", 50);
    console.log(rewardsSystem.getUserRewards("user123")); // { freeSpins: 10, bonuses: 50 }
    rewardsSystem.redeemFreeSpins("user123", 5);
    rewardsSystem.redeemBonus("user123", 20);
    console.log(rewardsSystem.getUserRewards("user123")); // { freeSpins: 5, bonuses: 30 }
} catch (error) {
    console.error(error.message);
}
```
