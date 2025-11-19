"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Write a JavaScript function that calculates the optimal point distribution for leveling up in STEPN, based on the strategies provided in the blog.
Generated: DETERMINISTIC_0b51884843618def
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the optimal point distribution for leveling up in STEPN.
 * 
 * @param {number} currentLevel - The current level of the user.
 * @param {number} targetLevel - The desired level to reach.
 * @param {number} basePoints - The base points required for leveling up.
 * @param {number} growthFactor - The growth factor for points required per level.
 * @returns {Object} - An object containing the level, points required, and total points needed.
 * @throws {Error} - Throws an error if currentLevel is not less than targetLevel.
 */
function calculateOptimalPointDistribution(currentLevel, targetLevel, basePoints, growthFactor) {
    // Validate input parameters
    if (currentLevel >= targetLevel) {
        throw new Error("Current level must be less than target level.");
    }
    
    let totalPoints = 0;
    let levelPoints = {};

    // Calculate points required for each level from current to target
    for (let level = currentLevel + 1; level <= targetLevel; level++) {
        // Calculate points required for the current level
        const pointsForLevel = basePoints * Math.pow(growthFactor, level - 1);
        levelPoints[level] = pointsForLevel;
        totalPoints += pointsForLevel;
    }

    return {
        levelPoints: levelPoints,
        totalPoints: totalPoints
    };
}

// Example usage
try {
    const currentLevel = 1;
    const targetLevel = 5;
    const basePoints = 100;
    const growthFactor = 1.5;

    const result = calculateOptimalPointDistribution(currentLevel, targetLevel, basePoints, growthFactor);
    console.log("Optimal Point Distribution:", result);
} catch (error) {
    console.error("Error calculating point distribution:", error.message);
}
```
