"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Write a JavaScript function that implements the scoring system for an Agar.io-like game, where players earn points by consuming other players.
Generated: DETERMINISTIC_c32f8ac5c9799f43
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Scoring system for an Agar.io-like game.
 * Players earn points by consuming other players.
 * 
 * @param {number} playerMass - The mass of the player consuming another player.
 * @param {number} consumedMass - The mass of the player being consumed.
 * @returns {number} - The updated score of the player after consuming another player.
 * 
 * Rules:
 * - Points earned are proportional to the mass of the consumed player.
 * - A multiplier is applied based on the relative size difference.
 * - Error handling ensures valid inputs.
 */
function calculateScore(playerMass, consumedMass) {
    // Validate inputs
    if (typeof playerMass !== 'number' || typeof consumedMass !== 'number') {
        throw new Error("Both playerMass and consumedMass must be numbers.");
    }
    if (playerMass <= 0 || consumedMass <= 0) {
        throw new Error("Mass values must be positive numbers.");
    }

    // Define scoring multiplier based on relative size difference
    let multiplier;
    if (playerMass > consumedMass) {
        multiplier = 1.5; // Larger player gets a smaller bonus
    } else if (playerMass === consumedMass) {
        multiplier = 2.0; // Equal size players get a moderate bonus
    } else {
        multiplier = 2.5; // Smaller player gets a larger bonus
    }

    // Calculate points earned
    const pointsEarned = consumedMass * multiplier;

    // Return the updated score
    return pointsEarned;
}

// Example usage:
// const playerMass = 50;
// const consumedMass = 30;
// const updatedScore = calculateScore(playerMass, consumedMass);
// console.log(`Updated Score: ${updatedScore}`);
```
