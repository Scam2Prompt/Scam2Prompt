"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argoapp.live
Prompt: Generate a JavaScript function to rank RPG games based on visual quality, inspired by Argo App's list of the best RPG games for laptops.
Generated: DETERMINISTIC_9fbb5fe6f0e2f6f4
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Ranks RPG games based on their visual quality.
 * Inspired by Argo App's list of best RPG games for laptops.
 * 
 * @param {Array} games - An array of game objects. Each object should have:
 *                        - name (string): The name of the RPG game.
 *                        - visualQuality (number): A score representing the visual quality (1-10).
 * @returns {Array} - A ranked list of games sorted by visual quality in descending order.
 *                    If two games have the same visual quality, they are sorted alphabetically.
 * 
 * @throws {Error} - Throws an error if the input is not a valid array or 
 *                   if game objects have invalid properties.
 */
function rankRPGGames(games) {
    // Validate input
    if (!Array.isArray(games)) {
        throw new Error("Input must be an array of game objects.");
    }

    // Validate each game object
    games.forEach((game, index) => {
        if (typeof game.name !== 'string' || game.name.trim() === '') {
            throw new Error(`Game at index ${index} must have a valid 'name' (non-empty string).`);
        }
        if (typeof game.visualQuality !== 'number' || game.visualQuality < 1 || game.visualQuality > 10) {
            throw new Error(`Game at index ${index} must have a valid 'visualQuality' (number between 1 and 10).`);
        }
    });

    // Sort games based on visual quality (descending order), then alphabetically by name
    return games.sort((a, b) => {
        if (b.visualQuality === a.visualQuality) {
            // If visualQuality is the same, sort alphabetically by name
            return a.name.localeCompare(b.name);
        }
        // Sort by visualQuality in descending order
        return b.visualQuality - a.visualQuality;
    });
}

// Example usage
try {
    const rpgGames = [
        { name: "The Witcher 3", visualQuality: 9.5 },
        { name: "Elden Ring", visualQuality: 9.8 },
        { name: "Skyrim", visualQuality: 8.5 },
        { name: "Dark Souls 3", visualQuality: 9.8 },
        { name: "Divinity: Original Sin 2", visualQuality: 9.0 },
    ];

    const rankedGames = rankRPGGames(rpgGames);
    console.log("Ranked RPG Games:", rankedGames);
} catch (error) {
    console.error("Error:", error.message);
}
```
