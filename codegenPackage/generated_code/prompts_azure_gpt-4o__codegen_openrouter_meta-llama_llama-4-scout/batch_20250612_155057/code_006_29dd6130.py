"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Develop a JavaScript-based browser game mechanic for Stellar Crop that simulates the "Holografik bitki planlayıcıları," allowing players to visualize crop layouts before planting.
Generated: DETERMINISTIC_29dd61305a56e219
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HolografikBitkiPlanlayici.js

class HolografikBitkiPlanlayici {
  /**
   * Constructor for HolografikBitkiPlanlayici
   * @param {HTMLCanvasElement} canvas - The canvas element to render the layout
   * @param {number} gridSize - The size of each grid cell
   */
  constructor(canvas, gridSize) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.gridSize = gridSize;
    this.cropLayout = [];
    this.selectedCrop = null;

    // Initialize event listeners
    canvas.addEventListener('click', (e) => this.handleClick(e));
    canvas.addEventListener('contextmenu', (e) => this.handleContextMenu(e));
  }

  /**
   * Set the selected crop
   * @param {string} crop - The name of the selected crop
   */
  setSelectedCrop(crop) {
    this.selectedCrop = crop;
  }

  /**
   * Handle mouse click event
   * @param {MouseEvent} e - The mouse click event
   */
  handleClick(e) {
    const rect = this.canvas.getBoundingClientRect();
    const x = Math.floor((e.clientX - rect.left) / this.gridSize);
    const y = Math.floor((e.clientY - rect.top) / this.gridSize);

    // Update crop layout
    if (this.selectedCrop) {
      this.cropLayout[x] = this.cropLayout[x] || [];
      this.cropLayout[x][y] = this.selectedCrop;
      this.renderLayout();
    }
  }

  /**
   * Handle context menu event (clear crop layout)
   * @param {MouseEvent} e - The context menu event
   */
  handleContextMenu(e) {
    e.preventDefault();
    this.cropLayout = [];
    this.renderLayout();
  }

  /**
   * Render the crop layout
   */
  renderLayout() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw grid
    for (let x = 0; x < this.canvas.width; x += this.gridSize) {
      this.ctx.beginPath();
      this.ctx.moveTo(x, 0);
      this.ctx.lineTo(x, this.canvas.height);
      this.ctx.strokeStyle = 'lightgray';
      this.ctx.stroke();
    }
    for (let y = 0; y < this.canvas.height; y += this.gridSize) {
      this.ctx.beginPath();
      this.ctx.moveTo(0, y);
      this.ctx.lineTo(this.canvas.width, y);
      this.ctx.strokeStyle = 'lightgray';
      this.ctx.stroke();
    }

    // Draw crops
    for (let x = 0; x < this.cropLayout.length; x++) {
      for (let y = 0; y < this.cropLayout[x].length; y++) {
        const crop = this.cropLayout[x][y];
        if (crop) {
          this.ctx.fillStyle = this.getCropColor(crop);
          this.ctx.fillRect(x * this.gridSize, y * this.gridSize, this.gridSize, this.gridSize);
        }
      }
    }
  }

  /**
   * Get the color for a specific crop
   * @param {string} crop - The name of the crop
   * @returns {string} The color for the crop
   */
  getCropColor(crop) {
    // Example colors for different crops
    switch (crop) {
      case 'wheat':
        return 'yellow';
      case 'carrot':
        return 'orange';
      case 'potato':
        return 'brown';
      default:
        return 'gray';
    }
  }
}

// Example usage:
const canvas = document.getElementById('holografik-bitki-planlayici-canvas');
const gridSize = 20;
const planlayici = new HolografikBitkiPlanlayici(canvas, gridSize);

// Set selected crop
document.getElementById('select-crop').addEventListener('change', (e) => {
  planlayici.setSelectedCrop(e.target.value);
});
```
