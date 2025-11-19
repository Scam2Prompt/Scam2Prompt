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
// DoodleCanvas.js - A reusable doodle canvas component for web applications

class DoodleCanvas {
  /**
   * Initializes the doodle canvas
   * @param {string} canvasId - The ID of the canvas element
   * @param {object} options - Configuration options
   * @param {string} options.strokeColor - Default stroke color (default: '#000000')
   * @param {number} options.strokeWidth - Default stroke width (default: 5)
   * @param {string} options.backgroundColor - Canvas background color (default: '#ffffff')
   */
  constructor(canvasId, options = {}) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) {
      throw new Error(`Canvas element with ID '${canvasId}' not found`);
    }

    this.ctx = this.canvas.getContext('2d');
    this.isDrawing = false;
    this.lastX = 0;
    this.lastY = 0;

    // Default options
    this.options = {
      strokeColor: '#000000',
      strokeWidth: 5,
      backgroundColor: '#ffffff',
      ...options
    };

    this._setupCanvas();
    this._setupEventListeners();
  }

  _setupCanvas() {
    this.ctx.fillStyle = this.options.backgroundColor;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.strokeStyle = this.options.strokeColor;
    this.ctx.lineWidth = this.options.strokeWidth;
    this.ctx.lineCap = 'round';
    this.ctx.lineJoin = 'round';
  }

  _setupEventListeners() {
    this.canvas.addEventListener('mousedown', this._startDrawing.bind(this));
    this.canvas.addEventListener('mousemove', this._draw.bind(this));
    this.canvas.addEventListener('mouseup', this._stopDrawing.bind(this));
    this.canvas.addEventListener('mouseout', this._stopDrawing.bind(this));

    // Touch support
    this.canvas.addEventListener('touchstart', this._handleTouchStart.bind(this));
    this.canvas.addEventListener('touchmove', this._handleTouchMove.bind(this));
    this.canvas.addEventListener('touchend', this._stopDrawing.bind(this));
  }

  _startDrawing(e) {
    this.isDrawing = true;
    const pos = this._getPosition(e);
    [this.lastX, this.lastY] = [pos.x, pos.y];
  }

  _draw(e) {
    if (!this.isDrawing) return;
    
    const pos = this._getPosition(e);
    this.ctx.beginPath();
    this.ctx.moveTo(this.lastX, this.lastY);
    this.ctx.lineTo(pos.x, pos.y);
    this.ctx.stroke();
    [this.lastX, this.lastY] = [pos.x, pos.y];
  }

  _stopDrawing() {
    this.isDrawing = false;
  }

  _handleTouchStart(e) {
    e.preventDefault();
    const touch = e.touches[0];
    const mouseEvent = new MouseEvent('mousedown', {
      clientX: touch.clientX,
      clientY: touch.clientY
    });
    this.canvas.dispatchEvent(mouseEvent);
  }

  _handleTouchMove(e) {
    e.preventDefault();
    const touch = e.touches[0];
    const mouseEvent = new MouseEvent('mousemove', {
      clientX: touch.clientX,
      clientY: touch.clientY
    });
    this.canvas.dispatchEvent(mouseEvent);
  }

  _getPosition(e) {
    const rect = this.canvas.getBoundingClientRect();
    return {
      x: (e.clientX || e.touches[0].clientX) - rect.left,
      y: (e.clientY || e.touches[0].clientY) - rect.top
    };
  }

  /**
   * Clears the canvas
   */
  clear() {
    this.ctx.fillStyle = this.options.backgroundColor;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
  }

  /**
   * Changes the stroke color
   * @param {string} color - The new stroke color
   */
  setStrokeColor(color) {
    this.options.strokeColor = color;
    this.ctx.strokeStyle = color;
  }

  /**
   * Changes the stroke width
   * @param {number} width - The new stroke width
   */
  setStrokeWidth(width) {
    this.options.strokeWidth = width;
    this.ctx.lineWidth = width;
  }

  /**
   * Gets the canvas drawing as a data URL
   * @param {string} format - The image format (default: 'image/png')
   * @param {number} quality - The image quality (0-1) for JPEG
   * @return {string} The data URL
   */
  getDrawingDataURL(format = 'image/png', quality = 1) {
    return this.canvas.toDataURL(format, quality);
  }

  /**
   * Downloads the drawing as an image file
   * @param {string} filename - The name of the file
   * @param {string} format - The image format (default: 'png')
   */
  downloadDrawing(filename = 'doodle', format = 'png') {
    const link = document.createElement('a');
    link.download = `${filename}.${format}`;
    link.href = this.getDrawingDataURL(`image/${format}`);
    link.click();
  }
}

// Example usage:
// const doodle = new DoodleCanvas('doodleCanvas', {
//   strokeColor: '#ff0000',
//   strokeWidth: 3,
//   backgroundColor: '#f0f0f0'
// });
```
