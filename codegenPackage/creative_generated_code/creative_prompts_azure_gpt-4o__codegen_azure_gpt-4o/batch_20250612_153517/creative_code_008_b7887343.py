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
// Leaderboard system for tracking players collecting "Mystery Marbles" in a balloon-lifting game

// Player class to encapsulate player data
class Player {
  constructor(name) {
    this.name = name; // Player's name
    this.score = 0; // Player's score (Mystery Marbles collected)
  }

  // Method to increment player's score
  addScore(points) {
    if (points < 0) {
      throw new Error("Points must be a positive number"); // Error handling for invalid points
    }
    this.score += points;
  }
}

// Leaderboard class to manage the leaderboard
class Leaderboard {
  constructor() {
    this.players = new Map(); // Store players using a Map for efficient lookup
  }

  // Method to add a player to the leaderboard
  addPlayer(name) {
    if (this.players.has(name)) {
      throw new Error(`Player "${name}" already exists on the leaderboard`);
    }
    this.players.set(name, new Player(name));
  }

  // Method to update a player's score
  updateScore(name, points) {
    if (!this.players.has(name)) {
      throw new Error(`Player "${name}" not found on the leaderboard`);
    }
    const player = this.players.get(name);
    player.addScore(points);
  }

  // Method to get the leaderboard sorted by score in descending order
  getRankings() {
    return Array.from(this.players.values())
      .sort((a, b) => b.score - a.score) // Sort players by score
      .map((player, index) => ({
        rank: index + 1,
        name: player.name,
        score: player.score,
      })); // Format ranking data
  }

  // Method to display the leaderboard in a readable format
  printLeaderboard() {
    console.log("=== Leaderboard ===");
    const rankings = this.getRankings();
    if (rankings.length === 0) {
      console.log("No players on the leaderboard yet.");
    } else {
      rankings.forEach(({ rank, name, score }) => {
        console.log(`${rank}. ${name} - ${score} Mystery Marbles`);
      });
    }
    console.log("===================");
  }
}

// Example usage of the leaderboard system
try {
  const leaderboard = new Leaderboard();

  // Add players to the leaderboard
  leaderboard.addPlayer("Alice");
  leaderboard.addPlayer("Bob");
  leaderboard.addPlayer("Charlie");

  // Update scores
  leaderboard.updateScore("Alice", 10);
  leaderboard.updateScore("Bob", 15);
  leaderboard.updateScore("Charlie", 5);
  leaderboard.updateScore("Alice", 20); // Alice collects more marbles

  // Print the leaderboard
  leaderboard.printLeaderboard();
} catch (error) {
  // Handle errors gracefully
  console.error(`Error: ${error.message}`);
}
```
