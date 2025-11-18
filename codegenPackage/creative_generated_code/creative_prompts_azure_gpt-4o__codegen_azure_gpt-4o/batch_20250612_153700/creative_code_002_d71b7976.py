"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Create a JavaScript function that simulates bursting a hot air balloon and rewards users with "Mystery Marbles" based on the height achieved, as outlined in GOMBLE's game mechanics.
Generated: DETERMINISTIC_d71b79764fb4f885
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates bursting a hot air balloon and rewards users with "Mystery Marbles"
 * based on the height achieved.
 *
 * The number of marbles rewarded is calculated based on the height tiers:
 * - < 100 meters: 1 marble
 * - 100-499 meters: 5 marbles
 * - 500-999 meters: 10 marbles
 * - >= 1000 meters: 20 marbles
 *
 * @param {number} height - The height achieved by the hot air balloon in meters.
 * @returns {number} The number of "Mystery Marbles" rewarded.
 */
function burstHotAirBalloon(height) {
  // Input validation: Ensure height is a non-negative number
  if (typeof height !== 'number' || height < 0) {
    throw new Error("Invalid height: Must be a non-negative number.");
  }

  // Calculate reward based on height tiers
  let rewardMarbles;
  if (height < 100) {
    rewardMarbles = 1;
  } else if (height >= 100 && height <= 499) {
    rewardMarbles = 5;
  } else if (height >= 500 && height <= 999) {
    rewardMarbles = 10;
  } else {
    rewardMarbles = 20;
  }

  return rewardMarbles;
}

// Example usage:
try {
  const heightAchieved = 750; // Replace with actual height achieved in the game
  const marblesRewarded = burstHotAirBalloon(heightAchieved);
  console.log(`Height achieved: ${heightAchieved} meters`);
  console.log(`Mystery Marbles rewarded: ${marblesRewarded}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
