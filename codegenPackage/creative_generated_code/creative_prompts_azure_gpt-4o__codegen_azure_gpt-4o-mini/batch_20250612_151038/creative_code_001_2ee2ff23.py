"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmonn.pages.dev
Prompt: Create a leaderboard system in JavaScript that tracks and displays the top validators and creators based on $PAC earnings, similar to the functionality described on the Pacmoon site.
Generated: DETERMINISTIC_2ee2ff23ec768a3e
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Leaderboard class to manage validators and creators based on $PAC earnings
class Leaderboard {
    constructor() {
        // Initialize an empty array to store users
        this.users = [];
    }

    /**
     * Adds a new user to the leaderboard.
     * @param {string} username - The username of the user.
     * @param {number} earnings - The $PAC earnings of the user.
     * @throws Will throw an error if the earnings are negative.
     */
    addUser(username, earnings) {
        if (earnings < 0) {
            throw new Error('Earnings cannot be negative.');
        }
        this.users.push({ username, earnings });
    }

    /**
     * Retrieves the top users based on earnings.
     * @param {number} topN - The number of top users to retrieve.
     * @returns {Array} - An array of top users sorted by earnings.
     */
    getTopUsers(topN) {
        // Sort users by earnings in descending order and slice the top N
        return this.users
            .sort((a, b) => b.earnings - a.earnings)
            .slice(0, topN);
    }

    /**
     * Displays the leaderboard in the console.
     * @param {number} topN - The number of top users to display.
     */
    displayLeaderboard(topN) {
        const topUsers = this.getTopUsers(topN);
        console.log('Leaderboard:');
        topUsers.forEach((user, index) => {
            console.log(`${index + 1}. ${user.username} - $PAC Earnings: ${user.earnings}`);
        });
    }
}

// Example usage of the Leaderboard class
try {
    const leaderboard = new Leaderboard();
    
    // Adding users to the leaderboard
    leaderboard.addUser('Validator1', 1500);
    leaderboard.addUser('Creator1', 2300);
    leaderboard.addUser('Validator2', 1200);
    leaderboard.addUser('Creator2', 2900);
    
    // Display the top 3 users
    leaderboard.displayLeaderboard(3);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
