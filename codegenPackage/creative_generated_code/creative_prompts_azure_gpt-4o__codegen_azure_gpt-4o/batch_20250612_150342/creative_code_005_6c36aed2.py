"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-taiko.cokiwe2297.workers.dev
Prompt: Write code to implement a drop-in magical ability system for chess pieces using JavaScript.
Generated: DETERMINISTIC_6c36aed2db2bf7a7
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Chess Magical Ability System
// Description: This script implements a drop-in magical ability system for chess pieces,
// allowing them to have special powers that can be dynamically added or removed.
// The system is extensible and adheres to best practices, including proper error handling.

class ChessPiece {
  /**
   * Constructor for a chess piece.
   * @param {string} name - Name of the chess piece (e.g., 'Pawn', 'Knight').
   * @param {string} color - Color of the chess piece ('White' or 'Black').
   */
  constructor(name, color) {
    if (!name || !color) {
      throw new Error('Name and color are required to create a chess piece.');
    }
    this.name = name;
    this.color = color;
    this.abilities = new Map(); // Map to store magical abilities
  }

  /**
   * Adds a magical ability to the chess piece.
   * @param {string} abilityName - Name of the magical ability.
   * @param {Function} abilityAction - Function that defines the ability's behavior.
   */
  addAbility(abilityName, abilityAction) {
    if (!abilityName || typeof abilityAction !== 'function') {
      throw new Error('Ability name and a valid function are required to add an ability.');
    }
    this.abilities.set(abilityName, abilityAction);
  }

  /**
   * Removes a magical ability from the chess piece.
   * @param {string} abilityName - Name of the magical ability to remove.
   */
  removeAbility(abilityName) {
    if (!this.abilities.has(abilityName)) {
      throw new Error(`Ability "${abilityName}" does not exist on this piece.`);
    }
    this.abilities.delete(abilityName);
  }

  /**
   * Executes a magical ability.
   * @param {string} abilityName - Name of the magical ability to execute.
   * @param {...any} args - Arguments to pass to the ability function.
   */
  useAbility(abilityName, ...args) {
    const ability = this.abilities.get(abilityName);
    if (!ability) {
      throw new Error(`Ability "${abilityName}" is not available on this piece.`);
    }
    return ability(...args);
  }

  /**
   * Lists all magical abilities available for this chess piece.
   * @returns {Array<string>} Array of ability names.
   */
  listAbilities() {
    return Array.from(this.abilities.keys());
  }
}

// Example usage:

try {
  // Create a chess piece
  const knight = new ChessPiece('Knight', 'White');

  // Add magical abilities
  knight.addAbility('Teleport', (startPosition, endPosition) => {
    return `The ${knight.color} ${knight.name} teleports from ${startPosition} to ${endPosition}.`;
  });
  knight.addAbility('Shield', () => {
    return `The ${knight.color} ${knight.name} raises a magical shield for defense.`;
  });

  // List abilities
  console.log('Abilities:', knight.listAbilities());

  // Use abilities
  console.log(knight.useAbility('Teleport', 'B1', 'C3'));
  console.log(knight.useAbility('Shield'));

  // Remove an ability
  knight.removeAbility('Teleport');

  // Attempt to use a removed ability (will throw an error)
  console.log(knight.useAbility('Teleport', 'B1', 'C3'));
} catch (error) {
  console.error('Error:', error.message);
}
```
