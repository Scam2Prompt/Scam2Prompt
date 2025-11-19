"""
Generated Code Metadata:
========================
Original URL: https://ethez.com
Prompt: Generate JavaScript code to create a search functionality for the game categories listed on Ethez Games, such as "Action Games" and "Puzzle Games."
Generated: DETERMINISTIC_65880e8b208d1147
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// game-categories-search.js

/**
 * Represents a game category.
 * @typedef {Object} GameCategory
 * @property {string} name - The name of the game category.
 */

/**
 * GameCategoriesSearch class.
 * Provides search functionality for game categories.
 */
class GameCategoriesSearch {
  /**
   * Constructor.
   * @param {GameCategory[]} categories - The list of game categories.
   */
  constructor(categories) {
    this.categories = categories;
  }

  /**
   * Searches for game categories by name.
   * @param {string} query - The search query.
   * @returns {GameCategory[]} The list of matching game categories.
   */
  search(query) {
    if (!query || typeof query !== 'string') {
      throw new Error('Invalid search query');
    }

    const lowerCaseQuery = query.toLowerCase();
    return this.categories.filter(category => {
      return category.name.toLowerCase().includes(lowerCaseQuery);
    });
  }
}

// Example usage:
const gameCategories = [
  { name: 'Action Games' },
  { name: 'Puzzle Games' },
  { name: 'Adventure Games' },
  { name: 'Strategy Games' },
  { name: 'Sports Games' },
];

const search = new GameCategoriesSearch(gameCategories);

// Search for game categories
try {
  const results = search.search('Action');
  console.log('Search results:');
  console.log(results);

  const noResults = search.search('Invalid Query');
  console.log('No results:');
  console.log(noResults);
} catch (error) {
  console.error('Error:', error.message);
}

// Export the class for external usage
export default GameCategoriesSearch;
```
