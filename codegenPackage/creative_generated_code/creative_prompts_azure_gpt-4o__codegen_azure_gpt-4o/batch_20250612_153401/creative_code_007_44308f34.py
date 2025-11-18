"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7a.game
Prompt: Generate JavaScript code to track user activity and display statistics for games like slots and roulette.
Generated: DETERMINISTIC_44308f3439871d57
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// User Activity Tracker for Games (Slots and Roulette)

// Initialize user activity object
const userActivity = {
  slots: { plays: 0, wins: 0, losses: 0 },
  roulette: { plays: 0, wins: 0, losses: 0 },
};

// Utility function to add activity
function trackActivity(game, result) {
  if (!userActivity[game]) {
    console.error(`Invalid game "${game}" provided.`);
    return;
  }

  // Update the plays count
  userActivity[game].plays += 1;

  // Update wins or losses based on result
  if (result === 'win') {
    userActivity[game].wins += 1;
  } else if (result === 'loss') {
    userActivity[game].losses += 1;
  } else {
    console.error(`Invalid result "${result}" provided.`);
  }
}

// Function to display activity statistics
function displayStatistics() {
  console.log('User Activity Statistics:');
  Object.entries(userActivity).forEach(([game, stats]) => {
    console.log(`Game: ${game}`);
    console.log(`  Plays: ${stats.plays}`);
    console.log(`  Wins: ${stats.wins}`);
    console.log(`  Losses: ${stats.losses}`);
    console.log('-----------------------------');
  });
}

// Simulate game plays
try {
  trackActivity('slots', 'win');   // User won a slots game
  trackActivity('slots', 'loss');  // User lost a slots game
  trackActivity('roulette', 'win'); // User won a roulette game
  trackActivity('roulette', 'loss'); // User lost a roulette game
  trackActivity('slots', 'win');   // Another slots win
} catch (error) {
  console.error('Error tracking activity:', error.message);
}

// Display statistics
displayStatistics();
```
