"""
Generated Code Metadata:
========================
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Create a JavaScript-based leaderboard system to track players who collect the most "Mystery Marbles" in a balloon-lifting game.
Generated: DETERMINISTIC_b7887343957c0528
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Leaderboard class to manage players and their scores
class Leaderboard {
    constructor() {
        // Initialize an empty array to hold player scores
        this.scores = [];
    }

    // Method to add a player and their score
    addPlayer(playerName, score) {
        // Validate input
        if (typeof playerName !== 'string' || typeof score !== 'number' || score < 0) {
            throw new Error('Invalid player name or score');
        }

        // Check if player already exists
        const existingPlayer = this.scores.find(player => player.name === playerName);
        if (existingPlayer) {
            // Update score if player exists
            existingPlayer.score += score;
        } else {
            // Add new player to the leaderboard
            this.scores.push({ name: playerName, score: score });
        }

        // Sort scores in descending order
        this.scores.sort((a, b) => b.score - a.score);
    }

    // Method to get the top N players
    getTopPlayers(n) {
        // Validate input
        if (typeof n !== 'number' || n <= 0) {
            throw new Error('Invalid number of top players requested');
        }

        // Return the top N players
        return this.scores.slice(0, n);
    }

    // Method to display the leaderboard
    displayLeaderboard() {
        console.log('Leaderboard:');
        this.scores.forEach((player, index) => {
            console.log(`${index + 1}. ${player.name}: ${player.score} Mystery Marbles`);
        });
    }
}

// Example usage
try {
    const leaderboard = new Leaderboard();
    
    // Adding players and their scores
    leaderboard.addPlayer('Alice', 10);
    leaderboard.addPlayer('Bob', 15);
    leaderboard.addPlayer('Charlie', 5);
    leaderboard.addPlayer('Alice', 5); // Alice collects more marbles

    // Display the leaderboard
    leaderboard.displayLeaderboard();

    // Get top 2 players
    const topPlayers = leaderboard.getTopPlayers(2);
    console.log('Top Players:', topPlayers);
} catch (error) {
    console.error('Error:', error.message);
}
```
