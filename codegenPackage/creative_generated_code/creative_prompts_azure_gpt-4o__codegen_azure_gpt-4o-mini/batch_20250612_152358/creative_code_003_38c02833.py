"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milady-dfk.pages.dev
Prompt: Create a script in JavaScript to calculate the "Beetle Points" for users in a decentralized application, based on activity metrics and token holdings, as described in the Milady ecosystem.
Generated: DETERMINISTIC_38c028337c38f2fb
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Beetle Points Calculator for the Milady Ecosystem
 * This script calculates Beetle Points for users based on their activity metrics and token holdings.
 */

class User {
    constructor(id, tokenHoldings, activityMetrics) {
        this.id = id; // Unique identifier for the user
        this.tokenHoldings = tokenHoldings; // Number of tokens held by the user
        this.activityMetrics = activityMetrics; // Activity metrics object
    }
}

/**
 * Calculate Beetle Points based on token holdings and activity metrics.
 * @param {User} user - The user object containing token holdings and activity metrics.
 * @returns {number} - The calculated Beetle Points.
 * @throws {Error} - Throws an error if the user object is invalid.
 */
function calculateBeetlePoints(user) {
    // Validate user input
    if (!user || !(user instanceof User)) {
        throw new Error('Invalid user object.');
    }

    // Base points calculation based on token holdings
    const tokenPoints = user.tokenHoldings * 10; // 10 points per token

    // Activity metrics points calculation
    const activityPoints = user.activityMetrics.reduce((total, metric) => {
        if (metric.type === 'dailyLogin') {
            return total + (metric.value * 5); // 5 points for each daily login
        } else if (metric.type === 'completedTasks') {
            return total + (metric.value * 2); // 2 points for each completed task
        } else {
            return total; // No points for unknown metric types
        }
    }, 0);

    // Total Beetle Points
    return tokenPoints + activityPoints;
}

// Example usage:
try {
    // Sample user data
    const user = new User('user123', 15, [
        { type: 'dailyLogin', value: 3 },
        { type: 'completedTasks', value: 10 }
    ]);

    const beetlePoints = calculateBeetlePoints(user);
    console.log(`User ${user.id} has ${beetlePoints} Beetle Points.`);
} catch (error) {
    console.error('Error calculating Beetle Points:', error.message);
}
```
