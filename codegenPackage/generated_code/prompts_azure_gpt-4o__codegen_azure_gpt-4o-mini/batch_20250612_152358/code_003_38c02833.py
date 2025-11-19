"""
Generated Code Metadata:
========================
Original URL: https://milady-dfk.pages.dev
Prompt: Create a script in JavaScript to calculate the "Beetle Points" for users in a decentralized application, based on activity metrics and token holdings, as described in the Milady ecosystem.
Generated: DETERMINISTIC_38c028337c38f2fb
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Beetle Points Calculator for the Milady Ecosystem
 * This script calculates Beetle Points based on user activity metrics and token holdings.
 * 
 * @module BeetlePointsCalculator
 */

class BeetlePointsCalculator {
    constructor() {
        // Initialize user data storage
        this.users = new Map();
    }

    /**
     * Adds a user to the system.
     * @param {string} userId - Unique identifier for the user.
     * @param {number} tokenHoldings - Amount of tokens held by the user.
     * @param {number} activityScore - Activity score based on user interactions.
     */
    addUser(userId, tokenHoldings, activityScore) {
        if (!userId || typeof tokenHoldings !== 'number' || typeof activityScore !== 'number') {
            throw new Error('Invalid input: userId must be a string, tokenHoldings and activityScore must be numbers.');
        }
        this.users.set(userId, { tokenHoldings, activityScore });
    }

    /**
     * Calculates Beetle Points for a given user.
     * @param {string} userId - Unique identifier for the user.
     * @returns {number} - Calculated Beetle Points.
     * @throws {Error} - Throws an error if the user does not exist.
     */
    calculateBeetlePoints(userId) {
        if (!this.users.has(userId)) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }

        const { tokenHoldings, activityScore } = this.users.get(userId);
        
        // Example calculation: Beetle Points = (Token Holdings * 2) + (Activity Score * 3)
        const beetlePoints = (tokenHoldings * 2) + (activityScore * 3);
        return beetlePoints;
    }

    /**
     * Calculates Beetle Points for all users.
     * @returns {Map<string, number>} - A map of user IDs to their calculated Beetle Points.
     */
    calculateAllBeetlePoints() {
        const results = new Map();
        for (const [userId] of this.users) {
            try {
                const points = this.calculateBeetlePoints(userId);
                results.set(userId, points);
            } catch (error) {
                console.error(`Error calculating points for user ${userId}: ${error.message}`);
            }
        }
        return results;
    }
}

// Example usage
try {
    const calculator = new BeetlePointsCalculator();
    calculator.addUser('user1', 10, 5);
    calculator.addUser('user2', 20, 3);
    
    console.log('Beetle Points for user1:', calculator.calculateBeetlePoints('user1'));
    console.log('Beetle Points for user2:', calculator.calculateBeetlePoints('user2'));
    
    const allPoints = calculator.calculateAllBeetlePoints();
    console.log('All Beetle Points:', allPoints);
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
