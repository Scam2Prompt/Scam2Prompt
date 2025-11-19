"""
Generated Code Metadata:
========================
Original URL: https://argoapp.live
Prompt: Generate a JavaScript function to rank RPG games based on visual quality, inspired by Argo App's list of the best RPG games for laptops.
Generated: DETERMINISTIC_9fbb5fe6f0e2f6f4
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Ranks RPG games based on visual quality.
 * @param {Array} games - Array of game objects to be ranked.
 * @param {Object} criteria - Criteria for ranking (weights for different visual aspects).
 * @returns {Array} Ranked array of game objects with added rank and score properties.
 * @throws {Error} If games parameter is not an array or criteria is invalid.
 */
function rankRpgGamesByVisualQuality(games, criteria = {
    textureQuality: 0.4,
    lighting: 0.3,
    artDirection: 0.2,
    animation: 0.1
}) {
    // Validate input
    if (!Array.isArray(games)) {
        throw new Error('Games parameter must be an array');
    }

    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('Criteria must be an object');
    }

    // Validate criteria weights sum to 1
    const weightsSum = Object.values(criteria).reduce((sum, weight) => sum + weight, 0);
    if (Math.abs(weightsSum - 1) > 0.0001) { // Account for floating point precision
        throw new Error('Criteria weights must sum to 1');
    }

    // Calculate visual quality score for each game
    const scoredGames = games.map(game => {
        // Validate game has required properties
        if (!game.visualScores || typeof game.visualScores !== 'object') {
            console.warn(`Game ${game.name || 'unnamed'} missing visualScores, skipping`);
            return null;
        }

        let score = 0;
        for (const [aspect, weight] of Object.entries(criteria)) {
            if (game.visualScores[aspect] === undefined) {
                console.warn(`Game ${game.name} missing ${aspect} score, using 0`);
                continue;
            }
            score += game.visualScores[aspect] * weight;
        }

        return {
            ...game,
            visualQualityScore: score
        };
    }).filter(game => game !== null); // Remove null entries from skipped games

    // Sort games by score in descending order
    const rankedGames = scoredGames.sort((a, b) => b.visualQualityScore - a.visualQualityScore);

    // Add rank position
    return rankedGames.map((game, index) => ({
        ...game,
        rank: index + 1
    }));
}

// Example usage:
/*
const games = [
    {
        name: "The Witcher 3",
        visualScores: {
            textureQuality: 9,
            lighting: 9,
            artDirection: 10,
            animation: 8
        }
    },
    {
        name: "Cyberpunk 2077",
        visualScores: {
            textureQuality: 10,
            lighting: 10,
            artDirection: 9,
            animation: 7
        }
    }
];

const rankedGames = rankRpgGamesByVisualQuality(games);
console.log(rankedGames);
*/
```
