"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmoons.pages.dev
Prompt: Create a JavaScript function to track and update a user's position on the Pacmoon leaderboard dynamically.
Generated: DETERMINISTIC_2db215ab4a57d37a
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
 * Class representing a leaderboard for the Pacmoon game.
 */
class PacmoonLeaderboard {
    constructor() {
        this.leaderboard = [];
    }

    /**
     * Add a player to the leaderboard.
     * @param {string} playerName - The name of the player.
     * @param {number} score - The score of the player.
     */
    addPlayer(playerName, score) {
        // Check if player already exists
        const existingPlayer = this.leaderboard.find(player => player.name === playerName);
        
        if (existingPlayer) {
            // Update score if player already exists
            existingPlayer.score = score;
        } else {
            // Add new player to leaderboard
            this.leaderboard.push({ name: playerName, score });
        }

        // Sort leaderboard after updating
        this.sortLeaderboard();
    }

    /**
     * Sort the leaderboard by score in descending order.
     */
    sortLeaderboard() {
        this.leaderboard.sort((a, b) => b.score - a.score);
    }

    /**
     * Get the current position of a player in the leaderboard.
     * @param {string} playerName - The name of the player.
     * @returns {number} - The position of the player (1-indexed), or -1 if not found.
     */
    getPlayerPosition(playerName) {
        const index = this.leaderboard.findIndex(player => player.name === playerName);
        return index !== -1 ? index + 1 : -1; // Return 1-indexed position or -1 if not found
    }

    /**
     * Get the entire leaderboard.
     * @returns {Array} - The current leaderboard.
     */
    getLeaderboard() {
        return this.leaderboard;
    }
}

// Example usage:
const leaderboard = new PacmoonLeaderboard();

// Simulate adding players
try {
    leaderboard.addPlayer('Alice', 120);
    leaderboard.addPlayer('Bob', 150);
    leaderboard.addPlayer('Alice', 200); // Update Alice's score
    console.log(leaderboard.getLeaderboard()); // Display current leaderboard
    console.log(`Alice's position: ${leaderboard.getPlayerPosition('Alice')}`); // Get Alice's position
    console.log(`Bob's position: ${leaderboard.getPlayerPosition('Bob')}`); // Get Bob's position
} catch (error) {
    console.error('An error occurred while updating the leaderboard:', error);
}
```
