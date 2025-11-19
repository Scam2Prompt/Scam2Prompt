"""
Generated Code Metadata:
========================
Original URL: https://birunoko.art
Prompt: Write a JavaScript code snippet to simulate a brush stroke effect on a canvas.
Generated: DETERMINISTIC_8b6f95ae83575e24
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BrushStroke.js

class BrushStroke {
  /**
   * Creates a new BrushStroke instance.
   * @param {HTMLCanvasElement} canvas - The canvas element to draw on.
   * @param {Object} options - Brush stroke options.
   * @param {number} options.lineWidth - The width of the brush stroke.
   * @param {string} options.lineCap - The line cap style.
   * @param {string} options.lineJoin - The line join style.
   * @param {number} options.opacity - The opacity of the brush stroke.
   */
  constructor(canvas, options) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.options = Object.assign({
      lineWidth: 5,
      lineCap: 'round',
      lineJoin: 'round',
      opacity: 1,
    }, options);

    // Set up the drawing context
    this.ctx.lineWidth = this.options.lineWidth;
    this.ctx.lineCap = this.options.lineCap;
    this.ctx.lineJoin = this.options.lineJoin;
    this.ctx.globalAlpha = this.options.opacity;

    // Initialize drawing variables
    this.drawing = false;
    this.lastX = 0;
    this.lastY = 0;

    // Add event listeners
    this.canvas.addEventListener('mousedown', (e) => this.startDrawing(e));
    this.canvas.addEventListener('mousemove', (e) => this.draw(e));
    this.canvas.addEventListener('mouseup', () => this.stopDrawing());
  }

  /**
   * Starts drawing on the canvas.
   * @param {MouseEvent} e - The mouse down event.
   */
  startDrawing(e) {
    this.drawing = true;
    this.lastX = e.offsetX;
    this.lastY = e.offsetY;
  }

  /**
   * Draws a line on the canvas.
   * @param {MouseEvent} e - The mouse move event.
   */
  draw(e) {
    if (!this.drawing) return;

    const x = e.offsetX;
    const y = e.offsetY;

    this.ctx.beginPath();
    this.ctx.moveTo(this.lastX, this.lastY);
    this.ctx.lineTo(x, y);
    this.ctx.stroke();

    this.lastX = x;
    this.lastY = y;
  }

  /**
   * Stops drawing on the canvas.
   */
  stopDrawing() {
    this.drawing = false;
  }

  /**
   * Clears the canvas.
   */
  clear() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }
}

// Example usage
function main() {
  const canvas = document.getElementById('canvas');
  const brushStroke = new BrushStroke(canvas, {
    lineWidth: 10,
    lineCap: 'round',
    lineJoin: 'round',
    opacity: 0.5,
  });

  // Clear the canvas after 5 seconds
  setTimeout(() => brushStroke.clear(), 5000);
}

document.addEventListener('DOMContentLoaded', main);
```
