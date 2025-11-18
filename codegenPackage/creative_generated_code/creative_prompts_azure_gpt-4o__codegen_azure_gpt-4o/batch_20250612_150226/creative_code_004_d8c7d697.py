"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Create a JavaScript function to simulate the process of taming masicks in R-Planet Conquest, factoring in hero skills and artifact availability.
Generated: DETERMINISTIC_d8c7d6976ba39fb3
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the process of taming masicks in R-Planet Conquest.
 * Factors in hero skills and artifact availability.
 *
 * @param {Object} hero - The hero attempting to tame the masick.
 * @param {Number} hero.skillLevel - Hero's skill level (1-100).
 * @param {Array} hero.artifacts - List of artifact names the hero has.
 * @param {Number} masickDifficulty - Difficulty level of the masick (1-100).
 * @returns {Object} - Result of the taming attempt.
 *                    { success: true/false, chance: Number (0-100) }
 */
function tameMasick(hero, masickDifficulty) {
    // Validate inputs
    if (
        typeof hero !== "object" ||
        typeof hero.skillLevel !== "number" ||
        !Array.isArray(hero.artifacts) ||
        typeof masickDifficulty !== "number"
    ) {
        throw new Error("Invalid input parameters.");
    }

    // Constraints for hero skill level and masick difficulty
    if (hero.skillLevel < 1 || hero.skillLevel > 100) {
        throw new Error("Hero skill level must be between 1 and 100.");
    }
    if (masickDifficulty < 1 || masickDifficulty > 100) {
        throw new Error("Masick difficulty must be between 1 and 100.");
    }

    // Base taming chance calculation
    let baseChance = hero.skillLevel - masickDifficulty;

    // Adjust chance based on artifacts
    const artifactBonus = hero.artifacts.reduce((bonus, artifact) => {
        switch (artifact.toLowerCase()) {
            case "masick charm":
                return bonus + 20; // Adds 20% taming chance
            case "ancient staff":
                return bonus + 15; // Adds 15% taming chance
            case "mythical amulet":
                return bonus + 10; // Adds 10% taming chance
            default:
                return bonus; // No bonus for unknown artifacts
        }
    }, 0);

    // Final taming chance
    let tamingChance = baseChance + artifactBonus;

    // Cap taming chance between 0 and 100
    tamingChance = Math.max(0, Math.min(100, tamingChance));

    // Determine success
    const randomRoll = Math.random() * 100; // Random number between 0 and 100
    const success = randomRoll <= tamingChance;

    // Return the result
    return {
        success,
        chance: tamingChance,
    };
}

// Example usage (uncomment below to test):
// const hero = {
//     skillLevel: 75,
//     artifacts: ["Masick Charm", "Ancient Staff"],
// };
// const masickDifficulty = 60;
// console.log(tameMasick(hero, masickDifficulty));
```
