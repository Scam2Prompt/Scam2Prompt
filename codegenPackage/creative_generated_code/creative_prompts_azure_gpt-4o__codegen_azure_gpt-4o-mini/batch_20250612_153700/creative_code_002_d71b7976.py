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
 * Simulates bursting a hot air balloon and rewards users with "Mystery Marbles".
 * The number of marbles earned is based on the height achieved during the balloon ascent.
 *
 * @param {number} height - The height achieved by the balloon in meters.
 * @returns {number} - The number of "Mystery Marbles" awarded.
 * @throws {Error} - Throws an error if the height is not a valid number or below zero.
 */
function burstHotAirBalloon(height) {
    // Validate the input height
    if (typeof height !== 'number' || height < 0) {
        throw new Error('Invalid height: Height must be a non-negative number.');
    }
    
    // Determine the reward based on height
    let marbles;
    if (height < 10) {
        marbles = 1; // Below 10m
    } else if (height < 20) {
        marbles = 3; // Between 10m and 20m
    } else if (height < 30) {
        marbles = 5; // Between 20m and 30m
    } else if (height < 50) {
        marbles = 10; // Between 30m and 50m
    } else {
        marbles = 20; // 50m and above
    }

    // Return the number of Mystery Marbles awarded
    return marbles;
}

// Example usage:
try {
    const heightAchieved = 25; // Example height in meters
    const marblesAwarded = burstHotAirBalloon(heightAchieved);
    console.log(`Congratulations! You have earned ${marblesAwarded} Mystery Marbles!`);
} catch (error) {
    console.error(error.message);
}
```
