"""
Generated Code Metadata:
========================
Original URL: https://origineth.net
Prompt: "Write a JavaScript function to create a Steam-like game recommendation system based on user tags and game categories."
Generated: DETERMINISTIC_0ac510e788944efe
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Game Recommendation System
 * This function recommends games based on user tags and game categories.
 * 
 * @param {Array} games - List of games. Each game is an object with `name`, `tags`, and `categories`.
 * @param {Array} userTags - List of tags preferred by the user.
 * @param {Array} userCategories - List of categories preferred by the user.
 * @param {number} maxRecommendations - Maximum number of recommendations to return.
 * @returns {Array} - List of recommended games sorted by relevance.
 */
function recommendGames(games, userTags, userCategories, maxRecommendations = 5) {
    // Validate input
    if (!Array.isArray(games) || !Array.isArray(userTags) || !Array.isArray(userCategories)) {
        throw new Error("Invalid input: games, userTags, and userCategories must be arrays.");
    }

    // Calculate relevance score for each game
    const scoredGames = games.map(game => {
        if (!game.name || !Array.isArray(game.tags) || !Array.isArray(game.categories)) {
            throw new Error("Invalid game object structure.");
        }

        let score = 0;

        // Increase score for matching tags
        game.tags.forEach(tag => {
            if (userTags.includes(tag)) {
                score += 2; // Tags have higher weight
            }
        });

        // Increase score for matching categories
        game.categories.forEach(category => {
            if (userCategories.includes(category)) {
                score += 1; // Categories have lower weight
            }
        });

        return { ...game, score };
    });

    // Sort games by relevance score in descending order
    const sortedGames = scoredGames.sort((a, b) => b.score - a.score);

    // Return top recommendations based on maxRecommendations
    return sortedGames.slice(0, maxRecommendations).map(game => game.name);
}

// Example usage
const games = [
    { name: "Game A", tags: ["action", "multiplayer"], categories: ["shooter", "adventure"] },
    { name: "Game B", tags: ["strategy", "singleplayer"], categories: ["puzzle", "simulation"] },
    { name: "Game C", tags: ["action", "singleplayer"], categories: ["adventure", "platformer"] },
    { name: "Game D", tags: ["multiplayer", "strategy"], categories: ["simulation", "shooter"] },
];

const userTags = ["action", "multiplayer"];
const userCategories = ["shooter", "adventure"];

const recommendations = recommendGames(games, userTags, userCategories, 3);
console.log("Recommended Games:", recommendations);
```
