"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: Write JavaScript code to create a web-based puzzle game inspired by the "Blockpuz: Block Puzzle" game described on jito.pro, including drag-and-drop functionality for blocks.
Generated: DETERMINISTIC_34f68c94abbb1c95
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// blockpuz.js

class Block {
  /**
   * Represents a block in the puzzle game.
   * @param {number} x - The x-coordinate of the block.
   * @param {number} y - The y-coordinate of the block.
   * @param {number} width - The width of the block.
   * @param {number} height - The height of the block.
   * @param {string} color - The color of the block.
   */
  constructor(x, y, width, height, color) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.color = color;
  }

  /**
   * Draws the block on the canvas.
   * @param {CanvasRenderingContext2D} ctx - The canvas context.
   */
  draw(ctx) {
    ctx.fillStyle = this.color;
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }
}

class PuzzleGame {
  /**
   * Represents the puzzle game.
   * @param {HTMLCanvasElement} canvas - The canvas element.
   */
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.blocks = [];
    this.dragging = false;
    this.selectedBlock = null;
    this.offsetX = 0;
    this.offsetY = 0;

    // Initialize event listeners
    canvas.addEventListener('mousedown', (e) => this.handleMouseDown(e));
    canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
    canvas.addEventListener('mouseup', (e) => this.handleMouseUp(e));
  }

  /**
   * Handles mouse down event.
   * @param {MouseEvent} e - The mouse event.
   */
  handleMouseDown(e) {
    const rect = this.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // Check if a block is clicked
    for (const block of this.blocks) {
      if (x >= block.x && x <= block.x + block.width && y >= block.y && y <= block.y + block.height) {
        this.selectedBlock = block;
        this.dragging = true;
        this.offsetX = x - block.x;
        this.offsetY = y - block.y;
        break;
      }
    }
  }

  /**
   * Handles mouse move event.
   * @param {MouseEvent} e - The mouse event.
   */
  handleMouseMove(e) {
    if (this.dragging) {
      const rect = this.canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      // Update block position
      this.selectedBlock.x = x - this.offsetX;
      this.selectedBlock.y = y - this.offsetY;

      // Redraw the canvas
      this.draw();
    }
  }

  /**
   * Handles mouse up event.
   * @param {MouseEvent} e - The mouse event.
   */
  handleMouseUp(e) {
    this.dragging = false;
    this.selectedBlock = null;
  }

  /**
   * Adds a block to the game.
   * @param {Block} block - The block to add.
   */
  addBlock(block) {
    this.blocks.push(block);
  }

  /**
   * Draws the game on the canvas.
   */
  draw() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw blocks
    for (const block of this.blocks) {
      block.draw(this.ctx);
    }
  }

  /**
   * Checks for collisions between blocks.
   */
  checkCollisions() {
    for (let i = 0; i < this.blocks.length; i++) {
      for (let j = i + 1; j < this.blocks.length; j++) {
        const block1 = this.blocks[i];
        const block2 = this.blocks[j];

        // Check for collision
        if (block1.x < block2.x + block2.width &&
            block1.x + block1.width > block2.x &&
            block1.y < block2.y + block2.height &&
            block1.y + block1.height > block2.y) {
          console.log('Collision detected!');
        }
      }
    }
  }
}

// Example usage
const canvas = document.getElementById('canvas');
const game = new PuzzleGame(canvas);

// Create blocks
const block1 = new Block(10, 10, 50, 50, 'red');
const block2 = new Block(70, 10, 50, 50, 'blue');
const block3 = new Block(10, 70, 50, 50, 'green');

// Add blocks to the game
game.addBlock(block1);
game.addBlock(block2);
game.addBlock(block3);

// Draw the game
game.draw();

// Check for collisions
game.checkCollisions();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blockpuz Game</title>
  <style>
    #canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="canvas" width="400" height="400"></canvas>
  <script src="blockpuz.js"></script>
</body>
</html>
```
