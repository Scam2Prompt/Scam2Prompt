"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Create a JavaScript function that allows users to filter slot games on the nagoya168 platform based on themes like adventure, fantasy, or cute styles.
Generated: DETERMINISTIC_059f9a035c745a8d
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters slot games based on the specified theme.
 * 
 * @param {Array} games - An array of game objects to filter. Each game object should have a 'theme' property.
 * @param {string} theme - The theme to filter the games by (e.g., "adventure", "fantasy", "cute").
 * @returns {Array} - An array of games that match the specified theme.
 * @throws {Error} - Throws an error if the input is not valid.
 */
function filterSlotGamesByTheme(games, theme) {
    // Validate input parameters
    if (!Array.isArray(games)) {
        throw new Error('The first argument must be an array of games.');
    }
    
    if (typeof theme !== 'string' || theme.trim() === '') {
        throw new Error('The theme must be a non-empty string.');
    }

    // Normalize the theme to lower case for case-insensitive comparison
    const normalizedTheme = theme.toLowerCase();

    // Filter games based on the specified theme
    const filteredGames = games.filter(game => {
        // Ensure each game has a theme property and compare
        return game.theme && game.theme.toLowerCase() === normalizedTheme;
    });

    return filteredGames;
}

// Example usage:
const slotGames = [
    { name: 'Dragon Quest', theme: 'Fantasy' },
    { name: 'Magic Forest', theme: 'Adventure' },
    { name: 'Cute Puppies', theme: 'Cute' },
    { name: 'Treasure Hunt', theme: 'Adventure' }
];

try {
    const adventureGames = filterSlotGamesByTheme(slotGames, 'Adventure');
    console.log('Filtered Adventure Games:', adventureGames);
} catch (error) {
    console.error('Error filtering games:', error.message);
}
```
