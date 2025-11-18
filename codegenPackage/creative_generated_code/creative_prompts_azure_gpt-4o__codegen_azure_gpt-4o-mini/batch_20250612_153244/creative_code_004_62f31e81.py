"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galagames-rewards.com
Prompt: Create JavaScript code for a "2048" game that replicates the functionality of Mynet's version.
Generated: DETERMINISTIC_62f31e8175f67244
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// 2048 Game Implementation in JavaScript

// Game class to handle the game's logic and state
class Game2048 {
    constructor(size = 4) {
        this.size = size; // size of the grid
        this.grid = this.initializeGrid(); // initialize the grid
        this.score = 0; // current score
        this.addRandomTile(); // add the first tile
        this.addRandomTile(); // add the second tile
    }

    // Initializes an empty grid
    initializeGrid() {
        return Array.from({ length: this.size }, () => Array(this.size).fill(0));
    }

    // Adds a random tile (2 or 4) to a random empty position in the grid
    addRandomTile() {
        const emptyCells = [];
        this.grid.forEach((row, x) => {
            row.forEach((value, y) => {
                if (value === 0) emptyCells.push({ x, y });
            });
        });

        if (emptyCells.length > 0) {
            const { x, y } = emptyCells[Math.floor(Math.random() * emptyCells.length)];
            this.grid[x][y] = Math.random() < 0.9 ? 2 : 4; // 90% chance for 2, 10% chance for 4
        }
    }

    // Moves the tiles based on the direction
    move(direction) {
        let moved = false;

        switch (direction) {
            case 'UP':
                moved = this.moveTiles((x, y) => [x - 1, y], (a, b) => a === b);
                break;
            case 'DOWN':
                moved = this.moveTiles((x, y) => [x + 1, y], (a, b) => a === b);
                break;
            case 'LEFT':
                moved = this.moveTiles((x, y) => [x, y - 1], (a, b) => a === b);
                break;
            case 'RIGHT':
                moved = this.moveTiles((x, y) => [x, y + 1], (a, b) => a === b);
                break;
            default:
                throw new Error('Invalid direction!');
        }

        if (moved) {
            this.addRandomTile(); // Add a new tile after a successful move
        }
    }

    // Moves tiles based on the provided movement function and merging condition
    moveTiles(getNext, canMerge) {
        let moved = false;

        for (let i = 0; i < this.size; i++) {
            let mergedRow = Array(this.size).fill(false);
            let row = this.grid[i].slice();

            // Filter out non-zero values
            const newRow = row.filter(value => value !== 0);
            let newRowWithMerge = [];

            for (let j = 0; j < newRow.length; j++) {
                if (j < newRow.length - 1 && canMerge(newRow[j], newRow[j + 1]) && !mergedRow[j]) {
                    // Merge tiles
                    newRowWithMerge.push(newRow[j] * 2);
                    this.score += newRow[j] * 2; // Update score
                    mergedRow[j] = true; // Mark as merged
                    j++; // Skip next tile
                } else {
                    newRowWithMerge.push(newRow[j]);
                }
            }

            // Fill the rest of the row with zeros
            while (newRowWithMerge.length < this.size) {
                newRowWithMerge.push(0);
            }

            if (JSON.stringify(row) !== JSON.stringify(newRowWithMerge)) {
                moved = true;
            }

            // Update the grid
            this.grid[i] = newRowWithMerge;
        }

        return moved;
    }

    // Checks if the game is over
    isGameOver() {
        if (this.grid.some(row => row.includes(2048))) {
            return "You win!";
        }

        for (let i = 0; i < this.size; i++) {
            for (let j = 0; j < this.size; j++) {
                if (this.grid[i][j] === 0) return false; // Still empty tiles
                if (i < this.size - 1 && this.grid[i][j] === this.grid[i + 1][j]) return false; // Can merge down
                if (j < this.size - 1 && this.grid[i][j] === this.grid[i][j + 1]) return false; // Can merge right
            }
        }
        return "Game over!";
    }

    // Returns the current state of the game
    getState() {
        return {
            grid: this.grid,
            score: this.score,
            gameOver: this.isGameOver()
        };
    }
}

// Example usage:
// Create a new game instance
const game = new Game2048();
console.log(game.getState()); // Display initial game state

// Use event listeners or UI to capture user input for moves
// Example: game.move('UP'), game.move('DOWN'), game.move('LEFT'), game.move('RIGHT');
```

### Notes:
- This implementation provides the basic functionality of the "2048" game.
- The `move` function handles tile movement and merging.
- The game state can be easily accessed using the `getState` method.
- Ensure proper input handling and user interface management in a real application.
