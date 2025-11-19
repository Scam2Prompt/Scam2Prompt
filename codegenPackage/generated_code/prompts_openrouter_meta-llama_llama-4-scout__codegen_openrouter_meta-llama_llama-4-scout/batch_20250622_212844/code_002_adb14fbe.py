"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Generate a simple quilting pattern using JavaScript, focusing on geometric shapes commonly found in quilts.
Generated: DETERMINISTIC_adb14fbe4360e13d
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// quilting-pattern.js

/**
 * Represents a geometric shape in a quilting pattern.
 */
class Shape {
  /**
   * Creates a new shape.
   * @param {string} type - The type of shape (e.g., square, triangle, circle).
   * @param {number} x - The x-coordinate of the shape.
   * @param {number} y - The y-coordinate of the shape.
   * @param {number} size - The size of the shape.
   */
  constructor(type, x, y, size) {
    this.type = type;
    this.x = x;
    this.y = y;
    this.size = size;
  }

  /**
   * Draws the shape on a canvas.
   * @param {CanvasRenderingContext2D} ctx - The canvas context.
   */
  draw(ctx) {
    switch (this.type) {
      case 'square':
        ctx.fillRect(this.x, this.y, this.size, this.size);
        break;
      case 'triangle':
        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.lineTo(this.x + this.size, this.y);
        ctx.lineTo(this.x + this.size / 2, this.y + this.size);
        ctx.fill();
        break;
      case 'circle':
        ctx.beginPath();
        ctx.arc(this.x + this.size / 2, this.y + this.size / 2, this.size / 2, 0, 2 * Math.PI);
        ctx.fill();
        break;
      default:
        throw new Error(`Unsupported shape type: ${this.type}`);
    }
  }
}

/**
 * Represents a quilting pattern composed of geometric shapes.
 */
class QuiltingPattern {
  /**
   * Creates a new quilting pattern.
   * @param {HTMLCanvasElement} canvas - The canvas to draw on.
   */
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.shapes = [];
  }

  /**
   * Adds a shape to the pattern.
   * @param {Shape} shape - The shape to add.
   */
  addShape(shape) {
    this.shapes.push(shape);
  }

  /**
   * Draws the quilting pattern on the canvas.
   */
  draw() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.shapes.forEach((shape) => shape.draw(this.ctx));
  }
}

// Example usage:
function main() {
  // Create a canvas to draw on.
  const canvas = document.createElement('canvas');
  canvas.width = 800;
  canvas.height = 600;
  document.body.appendChild(canvas);

  // Create a quilting pattern.
  const pattern = new QuiltingPattern(canvas);

  // Add some shapes to the pattern.
  pattern.addShape(new Shape('square', 10, 10, 50));
  pattern.addShape(new Shape('triangle', 70, 10, 50));
  pattern.addShape(new Shape('circle', 10, 70, 50));

  // Draw the quilting pattern.
  try {
    pattern.draw();
  } catch (error) {
    console.error('Error drawing quilting pattern:', error);
  }
}

main();
```
