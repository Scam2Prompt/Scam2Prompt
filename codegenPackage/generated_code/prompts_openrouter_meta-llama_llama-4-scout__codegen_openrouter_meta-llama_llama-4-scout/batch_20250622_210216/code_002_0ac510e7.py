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
 * 
 * This system recommends games to users based on their preferred tags and game categories.
 */

// Define a class for Game
class Game {
    /**
     * Constructor for Game
     * @param {number} id - Unique game ID
     * @param {string} name - Game name
     * @param {string[]} tags - Game tags
     * @param {string[]} categories - Game categories
     */
    constructor(id, name, tags, categories) {
        this.id = id;
        this.name = name;
        this.tags = tags;
        this.categories = categories;
    }
}

// Define a class for User
class User {
    /**
     * Constructor for User
     * @param {number} id - Unique user ID
     * @param {string[]} preferredTags - User's preferred tags
     */
    constructor(id, preferredTags) {
        this.id = id;
        this.preferredTags = preferredTags;
    }
}

// Define a class for GameRecommender
class GameRecommender {
    /**
     * Constructor for GameRecommender
     * @param {Game[]} games - List of games
     */
    constructor(games) {
        this.games = games;
    }

    /**
     * Recommend games to a user based on their preferred tags
     * @param {User} user - User to recommend games to
     * @returns {Game[]} Recommended games
     */
    recommendGames(user) {
        // Filter games that match user's preferred tags
        const recommendedGames = this.games.filter(game => {
            // Check if game has any of user's preferred tags
            return game.tags.some(tag => user.preferredTags.includes(tag));
        });

        return recommendedGames;
    }

    /**
     * Recommend games to a user based on their preferred tags and game categories
     * @param {User} user - User to recommend games to
     * @param {string[]} preferredCategories - User's preferred game categories
     * @returns {Game[]} Recommended games
     */
    recommendGamesAdvanced(user, preferredCategories) {
        // Filter games that match user's preferred tags and categories
        const recommendedGames = this.games.filter(game => {
            // Check if game has any of user's preferred tags
            const hasPreferredTag = game.tags.some(tag => user.preferredTags.includes(tag));

            // Check if game has any of user's preferred categories
            const hasPreferredCategory = game.categories.some(category => preferredCategories.includes(category));

            // Recommend game if it has a preferred tag or category
            return hasPreferredTag || hasPreferredCategory;
        });

        return recommendedGames;
    }
}

// Example usage
try {
    // Create games
    const games = [
        new Game(1, "Game 1", ["action", "adventure"], ["pc", "console"]),
        new Game(2, "Game 2", ["strategy", "rpg"], ["pc", "mobile"]),
        new Game(3, "Game 3", ["sports", "racing"], ["console", "mobile"]),
        new Game(4, "Game 4", ["action", "sports"], ["pc", "console"]),
    ];

    // Create user
    const user = new User(1, ["action", "adventure"]);

    // Create game recommender
    const recommender = new GameRecommender(games);

    // Recommend games to user
    const recommendedGames = recommender.recommendGames(user);
    console.log("Recommended Games:");
    recommendedGames.forEach(game => console.log(game.name));

    // Recommend games to user with categories
    const preferredCategories = ["pc", "console"];
    const recommendedGamesAdvanced = recommender.recommendGamesAdvanced(user, preferredCategories);
    console.log("\nRecommended Games (Advanced):");
    recommendedGamesAdvanced.forEach(game => console.log(game.name));
} catch (error) {
    console.error("Error:", error.message);
}
```
