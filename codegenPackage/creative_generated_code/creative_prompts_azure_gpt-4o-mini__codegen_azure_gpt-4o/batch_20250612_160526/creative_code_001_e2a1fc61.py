"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solitairenetwork.com
Prompt: Write a JavaScript function to implement the scoring system for Mahjong games as described on Solitaire Network, including tile matching logic.
Generated: DETERMINISTIC_e2a1fc61d859f26d
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Scoring system for Mahjong game
 * Implements tile matching logic and calculates score based on matches.
 * @param {Array} board - 2D array representing the Mahjong board.
 * @param {Array} matches - Array of pairs of matched tiles, e.g., [[tile1, tile2], [tile3, tile4]].
 * @returns {Object} - Object containing score and updated board.
 */
function calculateMahjongScore(board, matches) {
  // Constants
  const BASE_SCORE = 100; // Base score for each match
  const MULTIPLIER = 2; // Multiplier for consecutive matches
  const BONUS = 50; // Bonus for clearing the board
  
  // Validate input
  if (!Array.isArray(board) || !Array.isArray(matches)) {
    throw new Error('Invalid input: board and matches must be arrays');
  }

  let score = 0;
  let consecutiveMatches = 0;

  // Process each match
  matches.forEach(([tile1, tile2]) => {
    // Check if the tiles are valid and matchable
    if (tile1 === tile2 && tile1 !== null && tile2 !== null) {
      // Calculate score for the match
      score += BASE_SCORE + (MULTIPLIER * consecutiveMatches);
      consecutiveMatches++;

      // Remove tiles from the board (set to null to mark as cleared)
      board.forEach(row => {
        row.forEach((tile, index) => {
          if (tile === tile1) {
            row[index] = null;
          }
        });
      });
    } else {
      consecutiveMatches = 0; // Reset consecutive matches if no valid match
    }
  });

  // Check if the board is cleared
  const isBoardCleared = board.every(row => row.every(tile => tile === null));
  if (isBoardCleared) {
    score += BONUS; // Add bonus for clearing the board
  }

  return {
    score,
    board,
  };
}

// Example usage:
const mahjongBoard = [
  ['A', 'B', 'A', 'C'],
  ['D', 'A', 'C', 'B'],
  ['A', 'C', 'B', 'D'],
  ['C', 'B', 'A', 'D']
];

const matchedTiles = [
  ['A', 'A'],
  ['B', 'B'],
  ['C', 'C']
];

const result = calculateMahjongScore(mahjongBoard, matchedTiles);
console.log('Score:', result.score);
console.log('Updated Board:', result.board);
```
