"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-taiko.cokiwe2297.workers.dev
Prompt: Create a function in JavaScript to validate moves on a chessboard where pieces have additional magical powers.
Generated: DETERMINISTIC_3f669d3d4080da61
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate moves on a chessboard with magical powers.
 * @param {string} piece - The chess piece name (e.g., "pawn", "knight", "bishop").
 * @param {object} start - Starting position as an object {x: number, y: number}.
 * @param {object} end - Ending position as an object {x: number, y: number}.
 * @param {object} magicalPowers - Object describing magical powers for the piece (e.g., {teleport: true, range: 3}).
 * @returns {boolean} - Returns true if the move is valid, false otherwise.
 */
function validateMagicalChessMove(piece, start, end, magicalPowers) {
  // Ensure inputs are valid
  if (
    !piece ||
    typeof start.x !== "number" ||
    typeof start.y !== "number" ||
    typeof end.x !== "number" ||
    typeof end.y !== "number" ||
    typeof magicalPowers !== "object"
  ) {
    throw new Error("Invalid input parameters.");
  }

  // Ensure positions are within the chessboard range (1-8 for both x and y)
  if (
    start.x < 1 || start.x > 8 ||
    start.y < 1 || start.y > 8 ||
    end.x < 1 || end.x > 8 ||
    end.y < 1 || end.y > 8
  ) {
    return false; // Move is out of bounds
  }

  const dx = Math.abs(end.x - start.x); // Horizontal distance
  const dy = Math.abs(end.y - start.y); // Vertical distance

  // Define normal chess moves based on piece type
  const normalMoves = {
    pawn: () => (dx === 0 && dy === 1) || (magicalPowers.teleport && dy <= magicalPowers.range),
    knight: () => (dx === 2 && dy === 1) || (dx === 1 && dy === 2),
    bishop: () => dx === dy || (magicalPowers.teleport && dy <= magicalPowers.range),
    rook: () => (dx === 0 || dy === 0) || (magicalPowers.teleport && dx <= magicalPowers.range),
    queen: () => dx === dy || dx === 0 || dy === 0,
    king: () => dx <= 1 && dy <= 1,
  };

  // Handle unknown piece type
  if (!normalMoves[piece]) {
    throw new Error(`Unknown piece type: ${piece}`);
  }

  // Validate move using normal rules and magical powers
  return normalMoves[piece]();
}

// Example Usage:
try {
  const isValidMove = validateMagicalChessMove(
    "pawn",
    { x: 2, y: 2 },
    { x: 2, y: 5 },
    { teleport: true, range: 3 }
  );
  console.log(isValidMove); // true
} catch (error) {
  console.error(error.message);
}
```
