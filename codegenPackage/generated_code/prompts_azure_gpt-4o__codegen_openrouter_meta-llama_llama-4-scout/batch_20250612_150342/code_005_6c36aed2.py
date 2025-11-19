"""
Generated Code Metadata:
========================
Original URL: https://claim-taiko.cokiwe2297.workers.dev
Prompt: Write code to implement a drop-in magical ability system for chess pieces using JavaScript.
Generated: DETERMINISTIC_6c36aed2db2bf7a7
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a chess piece with magical abilities.
 */
class ChessPiece {
  /**
   * Creates a new ChessPiece instance.
   * @param {string} name - The name of the chess piece.
   * @param {string} color - The color of the chess piece.
   */
  constructor(name, color) {
    this.name = name;
    this.color = color;
    this.abilities = [];
  }

  /**
   * Adds a magical ability to the chess piece.
   * @param {MagicalAbility} ability - The ability to add.
   */
  addAbility(ability) {
    this.abilities.push(ability);
  }

  /**
   * Uses a magical ability.
   * @param {string} abilityName - The name of the ability to use.
   * @param {object} context - The context in which the ability is used.
   * @throws {Error} If the ability does not exist.
   */
  useAbility(abilityName, context) {
    const ability = this.abilities.find(a => a.name === abilityName);
    if (!ability) {
      throw new Error(`Ability '${abilityName}' does not exist.`);
    }
    ability.use(context);
  }
}

/**
 * Represents a magical ability.
 */
class MagicalAbility {
  /**
   * Creates a new MagicalAbility instance.
   * @param {string} name - The name of the ability.
   * @param {function} use - The function to call when the ability is used.
   */
  constructor(name, use) {
    this.name = name;
    this.use = use;
  }
}

/**
 * Represents a chess board.
 */
class ChessBoard {
  /**
   * Creates a new ChessBoard instance.
   */
  constructor() {
    this.pieces = [];
  }

  /**
   * Adds a chess piece to the board.
   * @param {ChessPiece} piece - The piece to add.
   */
  addPiece(piece) {
    this.pieces.push(piece);
  }

  /**
   * Gets a chess piece by name.
   * @param {string} name - The name of the piece to get.
   * @returns {ChessPiece|null} The piece, or null if not found.
   */
  getPiece(name) {
    return this.pieces.find(p => p.name === name) || null;
  }
}

// Example usage:

// Create a new chess board
const board = new ChessBoard();

// Create chess pieces
const king = new ChessPiece('King', 'white');
const queen = new ChessPiece('Queen', 'white');

// Create magical abilities
const kingAbility = new MagicalAbility('Heal', context => {
  console.log(`Healing ${context.target} for 10 HP.`);
});

const queenAbility = new MagicalAbility('Shield', context => {
  console.log(`Shielding ${context.target} for 5 seconds.`);
});

// Add abilities to pieces
king.addAbility(kingAbility);
queen.addAbility(queenAbility);

// Add pieces to board
board.addPiece(king);
board.addPiece(queen);

// Use abilities
king.useAbility('Heal', { target: 'King' });
queen.useAbility('Shield', { target: 'Queen' });

// Try using non-existent ability
try {
  king.useAbility('Teleport', {});
} catch (error) {
  console.error(error.message);
}
```
