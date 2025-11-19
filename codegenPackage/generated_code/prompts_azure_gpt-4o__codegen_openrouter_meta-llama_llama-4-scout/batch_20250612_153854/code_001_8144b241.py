"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate JavaScript code to implement a drawing canvas with options for text input, font selection (Arial, Times New Roman, etc.), and adjustable font size, as described on Monad Whiteboard NFT.
Generated: DETERMINISTIC_8144b241d52f2aab
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DrawingCanvas.js

class DrawingCanvas {
  /**
   * Creates a new DrawingCanvas instance.
   * 
   * @param {HTMLCanvasElement} canvasElement - The canvas element to draw on.
   */
  constructor(canvasElement) {
    this.canvas = canvasElement;
    this.ctx = canvasElement.getContext('2d');
    this.textInput = '';
    this.fontFamily = 'Arial';
    this.fontSize = 24;
    this.isDrawing = false;
    this.lastX = 0;
    this.lastY = 0;

    // Bind event listeners
    this.canvas.addEventListener('mousedown', this.handleMouseDown.bind(this));
    this.canvas.addEventListener('mousemove', this.handleMouseMove.bind(this));
    this.canvas.addEventListener('mouseup', this.handleMouseUp.bind(this));
  }

  /**
   * Handles mouse down event.
   * 
   * @param {MouseEvent} event - The mouse down event.
   */
  handleMouseDown(event) {
    this.isDrawing = true;
    this.lastX = event.offsetX;
    this.lastY = event.offsetY;
  }

  /**
   * Handles mouse move event.
   * 
   * @param {MouseEvent} event - The mouse move event.
   */
  handleMouseMove(event) {
    if (!this.isDrawing) return;

    const x = event.offsetX;
    const y = event.offsetY;

    this.ctx.beginPath();
    this.ctx.moveTo(this.lastX, this.lastY);
    this.ctx.lineTo(x, y);
    this.ctx.stroke();

    this.lastX = x;
    this.lastY = y;
  }

  /**
   * Handles mouse up event.
   * 
   * @param {MouseEvent} event - The mouse up event.
   */
  handleMouseUp() {
    this.isDrawing = false;
  }

  /**
   * Sets the text input.
   * 
   * @param {string} text - The text input.
   */
  setTextInput(text) {
    this.textInput = text;
    this.drawText();
  }

  /**
   * Sets the font family.
   * 
   * @param {string} fontFamily - The font family.
   */
  setFontFamily(fontFamily) {
    this.fontFamily = fontFamily;
    this.drawText();
  }

  /**
   * Sets the font size.
   * 
   * @param {number} fontSize - The font size.
   */
  setFontSize(fontSize) {
    this.fontSize = fontSize;
    this.drawText();
  }

  /**
   * Draws the text on the canvas.
   */
  drawText() {
    this.ctx.font = `${this.fontSize}px ${this.fontFamily}`;
    this.ctx.textAlign = 'left';
    this.ctx.textBaseline = 'top';
    this.ctx.fillStyle = 'black';
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.fillText(this.textInput, 10, 10);
  }
}

// Example usage
const canvasElement = document.getElementById('drawing-canvas');
const drawingCanvas = new DrawingCanvas(canvasElement);

const textInputElement = document.getElementById('text-input');
textInputElement.addEventListener('input', (event) => {
  drawingCanvas.setTextInput(event.target.value);
});

const fontFamilySelectElement = document.getElementById('font-family-select');
fontFamilySelectElement.addEventListener('change', (event) => {
  drawingCanvas.setFontFamily(event.target.value);
});

const fontSizeInputElement = document.getElementById('font-size-input');
fontSizeInputElement.addEventListener('input', (event) => {
  drawingCanvas.setFontSize(parseInt(event.target.value, 10));
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Drawing Canvas</title>
  <style>
    #drawing-canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="drawing-canvas" width="800" height="600"></canvas>
  <input id="text-input" type="text" placeholder="Text input">
  <select id="font-family-select">
    <option value="Arial">Arial</option>
    <option value="Times New Roman">Times New Roman</option>
    <option value="Courier New">Courier New</option>
  </select>
  <input id="font-size-input" type="number" value="24">

  <script src="DrawingCanvas.js"></script>
</body>
</html>
```
