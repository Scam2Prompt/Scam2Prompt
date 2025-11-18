"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Create a JavaScript-based leaderboard system to track players who collect the most "Mystery Marbles" in a balloon-lifting game.
Generated: DETERMINISTIC_b7887343957c0528
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Leaderboard class to manage players and their scores
class Leaderboard {
    constructor() {
        this.players = new Map(); // Using a Map for efficient score tracking
    }

    // Add or update player score
    addPlayerScore(playerName, score) {
        if (typeof playerName !== 'string' || typeof score !== 'number') {
            throw new Error('Invalid input: playerName must be a string and score must be a number.');
        }
        
        // Update the player's score if they already exist, otherwise add them
        if (this.players.has(playerName)) {
            this.players.set(playerName, this.players.get(playerName) + score);
        } else {
            this.players.set(playerName, score);
        }
    }

    // Get the leaderboard sorted by score in descending order
    getLeaderboard() {
        // Convert the Map to an array and sort it
        const sortedPlayers = Array.from(this.players.entries())
            .sort((a, b) => b[1] - a[1]); // Sort by score descending
        return sortedPlayers.map(([name, score]) => ({ name, score }));
    }

    // Get the score of a specific player
    getPlayerScore(playerName) {
        if (this.players.has(playerName)) {
            return this.players.get(playerName);
        } else {
            throw new Error(`Player ${playerName} not found.`);
        }
    }
}

// Example usage and error handling
try {
    const leaderboard = new Leaderboard();
    
    // Adding player scores
    leaderboard.addPlayerScore('Alice', 10);
    leaderboard.addPlayerScore('Bob', 15);
    leaderboard.addPlayerScore('Alice', 5); // Alice collects more marbles

    // Fetching and displaying the leaderboard
    console.log('Current Leaderboard:', leaderboard.getLeaderboard());

    // Fetching a specific player's score
    console.log('Alice\'s Score:', leaderboard.getPlayerScore('Alice'));

} catch (error) {
    console.error('An error occurred:', error.message);
}
```
