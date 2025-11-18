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
// Pacmoon Leaderboard Tracker
// This script dynamically updates and tracks a user's position on the Pacmoon leaderboard.

/**
 * Updates the user's position on the Pacmoon leaderboard.
 * @param {Array<Object>} leaderboard - Array of user objects sorted by score in descending order.
 * @param {Object} user - The user whose position needs to be tracked.
 * @param {number} newScore - The user's new score.
 * @returns {Object} - Updated leaderboard and the user's new position.
 */
function updateLeaderboard(leaderboard, user, newScore) {
  try {
    // Validate inputs
    if (!Array.isArray(leaderboard)) {
      throw new Error("Leaderboard must be an array.");
    }
    if (typeof user !== 'object' || user === null) {
      throw new Error("User must be a valid object.");
    }
    if (typeof newScore !== 'number' || newScore < 0) {
      throw new Error("New score must be a non-negative number.");
    }

    // Update the user's score
    user.score = newScore;

    // Check if the user already exists in the leaderboard
    const existingUserIndex = leaderboard.findIndex(u => u.id === user.id);

    if (existingUserIndex !== -1) {
      // Remove the user from the current position
      leaderboard.splice(existingUserIndex, 1);
    }

    // Add the user back to the leaderboard and sort by score
    leaderboard.push(user);
    leaderboard.sort((a, b) => b.score - a.score);

    // Get the user's new position (index + 1 as leaderboard positions start from 1)
    const newPosition = leaderboard.findIndex(u => u.id === user.id) + 1;

    return {
      leaderboard,
      position: newPosition
    };

  } catch (error) {
    console.error("Error updating leaderboard:", error.message);
    return {
      leaderboard,
      position: null,
      error: error.message
    };
  }
}

// Example Usage:
// const leaderboard = [
//   { id: 1, name: "Alice", score: 100 },
//   { id: 2, name: "Bob", score: 95 },
//   { id: 3, name: "Charlie", score: 90 }
// ];

// const user = { id: 2, name: "Bob", score: 95 };
// const newScore = 105;

// const result = updateLeaderboard(leaderboard, user, newScore);
// console.log("Updated Leaderboard:", result.leaderboard);
// console.log("User's New Position:", result.position);
```
