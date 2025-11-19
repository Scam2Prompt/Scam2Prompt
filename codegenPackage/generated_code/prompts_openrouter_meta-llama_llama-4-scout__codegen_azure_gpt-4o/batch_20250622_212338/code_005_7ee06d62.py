"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Write a JavaScript function to calculate batting average and on-base percentage for slowpitch softball players using statistics calculators.
Generated: DETERMINISTIC_7ee06d6271902f58
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculate batting average and on-base percentage for a slowpitch softball player.
 * 
 * @param {Object} stats - An object containing the player's statistics.
 * @param {number} stats.hits - Total number of hits.
 * @param {number} stats.atBats - Total number of at-bats.
 * @param {number} stats.walks - Total number of walks.
 * @param {number} stats.hitByPitch - Total number of times hit by pitch.
 * @returns {Object} - An object containing batting average and on-base percentage.
 */
function calculateSoftballStats(stats) {
    // Validate input
    if (!stats || typeof stats !== 'object') {
        throw new Error("Invalid input: stats must be an object.");
    }

    const { hits, atBats, walks, hitByPitch } = stats;

    if (
        typeof hits !== 'number' || hits < 0 ||
        typeof atBats !== 'number' || atBats < 0 ||
        typeof walks !== 'number' || walks < 0 ||
        typeof hitByPitch !== 'number' || hitByPitch < 0
    ) {
        throw new Error("Invalid input: stats properties must be non-negative numbers.");
    }

    if (atBats === 0) {
        throw new Error("Invalid input: atBats cannot be zero.");
    }

    // Calculate batting average
    const battingAverage = hits / atBats;

    // Calculate on-base percentage
    const onBasePercentage = (hits + walks + hitByPitch) / (atBats + walks + hitByPitch);

    // Return the results rounded to three decimal places
    return {
        battingAverage: parseFloat(battingAverage.toFixed(3)),
        onBasePercentage: parseFloat(onBasePercentage.toFixed(3))
    };
}

// Example usage:
try {
    const playerStats = {
        hits: 50,
        atBats: 150,
        walks: 20,
        hitByPitch: 5
    };

    const results = calculateSoftballStats(playerStats);
    console.log("Batting Average:", results.battingAverage);
    console.log("On-Base Percentage:", results.onBasePercentage);
} catch (error) {
    console.error("Error:", error.message);
}
```
