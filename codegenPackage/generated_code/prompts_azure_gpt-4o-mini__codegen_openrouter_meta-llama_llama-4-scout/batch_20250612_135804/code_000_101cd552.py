"""
Generated Code Metadata:
========================
Original URL: https://doodles.team
Prompt: Generate a code snippet that demonstrates how to implement a doodle feature in a web application.
Generated: DETERMINISTIC_101cd552abdc8e91
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// doodle.js

/**
 * Doodle class representing a simple doodle feature.
 */
class Doodle {
  /**
   * Creates a new Doodle instance.
   * @param {HTMLCanvasElement} canvas - The canvas element to render the doodle on.
   */
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.drawing = false;
    this.lastX = 0;
    this.lastY = 0;
    this.lineWidth = 5;
    this.lineColor = 'black';

    // Add event listeners for mouse and touch events
    this.canvas.addEventListener('mousedown', this.startDrawing.bind(this));
    this.canvas.addEventListener('mousemove', this.draw.bind(this));
    this.canvas.addEventListener('mouseup', this.stopDrawing.bind(this));
    this.canvas.addEventListener('touchstart', this.startDrawing.bind(this));
    this.canvas.addEventListener('touchmove', this.draw.bind(this));
    this.canvas.addEventListener('touchend', this.stopDrawing.bind(this));
  }

  /**
   * Starts drawing on the canvas.
   * @param {MouseEvent|TouchEvent} event - The event that triggered the drawing start.
   */
  startDrawing(event) {
    this.drawing = true;
    if (event.type === 'mousedown' || event.type === 'touchstart') {
      this.lastX = event.clientX || event.touches[0].clientX;
      this.lastY = event.clientY || event.touches[0].clientY;
    }
  }

  /**
   * Draws a line on the canvas.
   * @param {MouseEvent|TouchEvent} event - The event that triggered the drawing.
   */
  draw(event) {
    if (!this.drawing) return;

    const x = event.clientX || event.touches[0].clientX;
    const y = event.clientY || event.touches[0].clientY;

    this.ctx.beginPath();
    this.ctx.moveTo(this.lastX, this.lastY);
    this.ctx.lineTo(x, y);
    this.ctx.strokeStyle = this.lineColor;
    this.ctx.lineWidth = this.lineWidth;
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

  /**
   * Sets the line color.
   * @param {string} color - The new line color.
   */
  setLineColor(color) {
    this.lineColor = color;
  }

  /**
   * Sets the line width.
   * @param {number} width - The new line width.
   */
  setLineWidth(width) {
    this.lineWidth = width;
  }
}

// Example usage:
const canvas = document.getElementById('doodle-canvas');
const doodle = new Doodle(canvas);

// Set line color and width
doodle.setLineColor('red');
doodle.setLineWidth(10);

// Clear the canvas
// doodle.clear();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Doodle Feature</title>
  <style>
    #doodle-canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="doodle-canvas" width="800" height="600"></canvas>
  <script src="doodle.js"></script>
</body>
</html>
```
