"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Design a simple game mechanic where two Meowgon creatures with matching elements can unlock new opportunities for players, and provide a basic implementation in JavaScript.
Generated: DETERMINISTIC_1cc8dee43f82cc79
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Meowgon Creature Class
 * Represents a creature with elemental properties and matching capabilities.
 */
class Meowgon {
  /**
   * @param {string} name - The name of the Meowgon creature
   * @param {string} element - The elemental type (fire, water, earth, air)
   */
  constructor(name, element) {
    this.name = name;
    this.element = element.toLowerCase();
    this.validateElement();
  }

  /**
   * Validates that the element is one of the allowed types
   * @throws {Error} If element is invalid
   */
  validateElement() {
    const validElements = ['fire', 'water', 'earth', 'air'];
    if (!validElements.includes(this.element)) {
      throw new Error(`Invalid element: ${this.element}. Must be one of: ${validElements.join(', ')}`);
    }
  }
}

/**
 * Game Mechanic Class
 * Handles interactions between Meowgon creatures and opportunity unlocking
 */
class MeowgonGame {
  constructor() {
    this.opportunities = [];
    this.unlockedOpportunities = new Set();
  }

  /**
   * Adds a new opportunity that can be unlocked
   * @param {string} opportunityName - Name of the opportunity
   * @param {string} requiredElement - Element required to unlock
   * @param {number} requiredMatches - Number of matching creatures needed
   */
  addOpportunity(opportunityName, requiredElement, requiredMatches) {
    if (this.opportunities.some(op => op.name === opportunityName)) {
      throw new Error(`Opportunity "${opportunityName}" already exists`);
    }
    this.opportunities.push({
      name: opportunityName,
      element: requiredElement.toLowerCase(),
      matchesRequired: requiredMatches
    });
  }

  /**
   * Attempts to unlock opportunities based on provided Meowgon creatures
   * @param {Meowgon[]} creatures - Array of Meowgon creatures to check
   * @returns {string[]} Array of unlocked opportunity names
   */
  checkForOpportunities(creatures) {
    if (!Array.isArray(creatures) || creatures.length === 0) {
      throw new Error('Must provide at least one Meowgon creature');
    }

    const elementCounts = {};
    creatures.forEach(creature => {
      if (!(creature instanceof Meowgon)) {
        throw new Error('All items must be Meowgon instances');
      }
      elementCounts[creature.element] = (elementCounts[creature.element] || 0) + 1;
    });

    const newlyUnlocked = [];
    this.opportunities.forEach(opportunity => {
      const count = elementCounts[opportunity.element] || 0;
      if (count >= opportunity.matchesRequired && !this.unlockedOpportunities.has(opportunity.name)) {
        this.unlockedOpportunities.add(opportunity.name);
        newlyUnlocked.push(opportunity.name);
      }
    });

    return newlyUnlocked;
  }

  /**
   * Gets all unlocked opportunities
   * @returns {string[]} Array of all unlocked opportunity names
   */
  getUnlockedOpportunities() {
    return Array.from(this.unlockedOpportunities);
  }
}

// Example usage:
/*
const game = new MeowgonGame();

// Add some opportunities
game.addOpportunity('Fire Festival', 'fire', 2);
game.addOpportunity('Water Show', 'water', 3);
game.addOpportunity('Earth Expedition', 'earth', 1);

// Create some Meowgon creatures
const meowgon1 = new Meowgon('Blaze', 'fire');
const meowgon2 = new Meowgon('Sizzle', 'fire');
const meowgon3 = new Meowgon('Bubbles', 'water');

// Check for opportunities with matching creatures
const unlocked = game.checkForOpportunities([meowgon1, meowgon2, meowgon3]);
console.log('Newly unlocked:', unlocked);
console.log('All unlocked:', game.getUnlockedOpportunities());
*/
```
