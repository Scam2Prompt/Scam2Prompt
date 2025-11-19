"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Generate a JavaScript code snippet to create a virtual wine tasting guide, like the one offered by FestiVin de Caraquet.
Generated: DETERMINISTIC_e6bf12c888b3a68f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WineTastingGuide.js

/**
 * Represents a wine in the tasting guide.
 */
class Wine {
  /**
   * Creates a new Wine instance.
   * @param {string} name - The name of the wine.
   * @param {string} description - A brief description of the wine.
   * @param {string} origin - The origin of the wine.
   * @param {string} grapeVariety - The grape variety used to make the wine.
   */
  constructor(name, description, origin, grapeVariety) {
    this.name = name;
    this.description = description;
    this.origin = origin;
    this.grapeVariety = grapeVariety;
  }
}

/**
 * Represents a wine tasting guide.
 */
class WineTastingGuide {
  /**
   * Creates a new WineTastingGuide instance.
   */
  constructor() {
    this.wines = [];
  }

  /**
   * Adds a wine to the guide.
   * @param {Wine} wine - The wine to add.
   */
  addWine(wine) {
    if (!(wine instanceof Wine)) {
      throw new Error('Invalid wine object');
    }
    this.wines.push(wine);
  }

  /**
   * Removes a wine from the guide by name.
   * @param {string} name - The name of the wine to remove.
   * @returns {boolean} True if the wine was removed, false otherwise.
   */
  removeWine(name) {
    const index = this.wines.findIndex(wine => wine.name === name);
    if (index !== -1) {
      this.wines.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Gets a list of all wines in the guide.
   * @returns {Wine[]} A list of wines.
   */
  getWines() {
    return [...this.wines];
  }

  /**
   * Searches for wines by origin.
   * @param {string} origin - The origin to search for.
   * @returns {Wine[]} A list of wines from the specified origin.
   */
  searchByOrigin(origin) {
    return this.wines.filter(wine => wine.origin.toLowerCase().includes(origin.toLowerCase()));
  }
}

// Example usage:
function main() {
  const guide = new WineTastingGuide();

  const wine1 = new Wine('Wine 1', 'Description 1', 'Caraquet', 'Grape Variety 1');
  const wine2 = new Wine('Wine 2', 'Description 2', 'Moncton', 'Grape Variety 2');
  const wine3 = new Wine('Wine 3', 'Description 3', 'Caraquet', 'Grape Variety 3');

  guide.addWine(wine1);
  guide.addWine(wine2);
  guide.addWine(wine3);

  console.log('All Wines:');
  guide.getWines().forEach(wine => {
    console.log(`Name: ${wine.name}, Origin: ${wine.origin}`);
  });

  console.log('\nWines from Caraquet:');
  guide.searchByOrigin('Caraquet').forEach(wine => {
    console.log(`Name: ${wine.name}, Origin: ${wine.origin}`);
  });

  guide.removeWine('Wine 2');

  console.log('\nWines after removal:');
  guide.getWines().forEach(wine => {
    console.log(`Name: ${wine.name}, Origin: ${wine.origin}`);
  });
}

try {
  main();
} catch (error) {
  console.error(error.message);
}
```
