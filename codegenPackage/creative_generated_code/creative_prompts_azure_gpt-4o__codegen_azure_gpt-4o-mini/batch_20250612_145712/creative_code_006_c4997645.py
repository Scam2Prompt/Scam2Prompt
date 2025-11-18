"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneybux.xyz
Prompt: Develop a JavaScript module to manage user accounts, including tracking TON earnings, quests completed, and withdrawal history.
Generated: DETERMINISTIC_c49976455616f872
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// userAccountManager.js

/**
 * UserAccountManager - A module for managing user accounts
 * 
 * This module allows tracking of user earnings, completed quests, and withdrawal history.
 * 
 * @module UserAccountManager
 */

class UserAccountManager {
    constructor() {
        // Initializes user accounts storage
        this.accounts = {};
    }

    /**
     * Adds a new user account.
     * @param {string} userId - Unique identifier for the user.
     * @throws {Error} If the user already exists.
     */
    addUser(userId) {
        if (this.accounts[userId]) {
            throw new Error(`User with ID ${userId} already exists.`);
        }
        this.accounts[userId] = {
            TON: 0,
            completedQuests: [],
            withdrawalHistory: [],
        };
    }

    /**
     * Records TON earnings for a user.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} amount - Amount of TON to add.
     * @throws {Error} If the user does not exist or amount is invalid.
     */
    recordEarnings(userId, amount) {
        if (!this.accounts[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        if (amount <= 0) {
            throw new Error(`Invalid amount: ${amount}. Amount must be positive.`);
        }
        this.accounts[userId].TON += amount;
    }

    /**
     * Records a completed quest for a user.
     * @param {string} userId - Unique identifier for the user.
     * @param {string} questName - Name of the completed quest.
     * @throws {Error} If the user does not exist or quest name is invalid.
     */
    recordQuestCompletion(userId, questName) {
        if (!this.accounts[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        if (!questName || typeof questName !== 'string') {
            throw new Error(`Invalid quest name: ${questName}.`);
        }
        this.accounts[userId].completedQuests.push(questName);
    }

    /**
     * Records a withdrawal for a user.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} amount - Amount of TON to withdraw.
     * @throws {Error} If the user does not exist, amount is invalid, or insufficient balance.
     */
    recordWithdrawal(userId, amount) {
        if (!this.accounts[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        if (amount <= 0) {
            throw new Error(`Invalid amount: ${amount}. Amount must be positive.`);
        }
        if (this.accounts[userId].TON < amount) {
            throw new Error(`Insufficient balance for user ${userId}.`);
        }

        // Deduct the amount and record the withdrawal
        this.accounts[userId].TON -= amount;
        this.accounts[userId].withdrawalHistory.push(amount);
    }

    /**
     * Retrieves the account information for a user.
     * @param {string} userId - Unique identifier for the user.
     * @returns {Object} User account information.
     * @throws {Error} If the user does not exist.
     */
    getUserAccount(userId) {
        if (!this.accounts[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        return this.accounts[userId];
    }
}

// Export the UserAccountManager module for use in other files
export default UserAccountManager;
```

This code defines a JavaScript module for managing user accounts, including tracking earnings, completed quests, and withdrawal history. Proper error handling and documentation are included to ensure clarity and maintainability.
