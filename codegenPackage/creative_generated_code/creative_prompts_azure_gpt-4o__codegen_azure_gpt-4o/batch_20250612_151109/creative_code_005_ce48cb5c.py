"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Develop a JavaScript application that allows users to select tile sizes and preview how ITACA Ceramic's Belle Forme tiles would look in a virtual room setting.
Generated: DETERMINISTIC_ce48cb5c8df285f7
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ITACA Ceramic Virtual Room Tile Preview Application
 * Allows users to select tile sizes and preview them in a virtual room setting.
 * 
 * Author: [Your Name]
 * Date: [Current Date]
 */

const tileApp = (() => {
  // Application state
  let selectedTileSize = '';
  const tileOptions = ['Small (20x20)', 'Medium (30x30)', 'Large (50x50)'];
  const roomContainer = document.getElementById('room-container');
  const tileSelector = document.getElementById('tile-size-selector');

  /**
   * Initialize the application
   */
  const init = () => {
    populateTileSelector();
    addEventListeners();
  };

  /**
   * Populate the tile size dropdown menu
   */
  const populateTileSelector = () => {
    tileOptions.forEach((size) => {
      const option = document.createElement('option');
      option.value = size;
      option.textContent = size;
      tileSelector.appendChild(option);
    });
  };

  /**
   * Attach event listeners to DOM elements
   */
  const addEventListeners = () => {
    tileSelector.addEventListener('change', handleTileSizeChange);
  };

  /**
   * Handle change in tile size selection
   * @param {Event} event - The change event on the tile size selector
   */
  const handleTileSizeChange = (event) => {
    try {
      selectedTileSize = event.target.value;
      updateRoomPreview();
    } catch (error) {
      console.error('Error updating tile size:', error);
      alert('An error occurred while changing the tile size. Please try again.');
    }
  };

  /**
   * Update the room preview based on the selected tile size
   */
  const updateRoomPreview = () => {
    // Clear the existing room preview
    roomContainer.innerHTML = '';

    // Set tile dimensions based on selected size
    let tileWidth, tileHeight;
    switch (selectedTileSize) {
      case 'Small (20x20)':
        tileWidth = 20;
        tileHeight = 20;
        break;
      case 'Medium (30x30)':
        tileWidth = 30;
        tileHeight = 30;
        break;
      case 'Large (50x50)':
        tileWidth = 50;
        tileHeight = 50;
        break;
      default:
        console.warn('Invalid tile size selected');
        return;
    }

    // Generate a grid of tiles for the preview
    const roomWidth = 600; // Example room width (adjust as needed)
    const roomHeight = 400; // Example room height (adjust as needed)
    const rows = Math.floor(roomHeight / tileHeight);
    const cols = Math.floor(roomWidth / tileWidth);

    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < cols; col++) {
        const tile = document.createElement('div');
        tile.style.width = `${tileWidth}px`;
        tile.style.height = `${tileHeight}px`;
        tile.style.backgroundColor = '#cccccc'; // Example tile color
        tile.style.border = '1px solid #999'; // Example tile border
        tile.style.display = 'inline-block';
        roomContainer.appendChild(tile);
      }
      const lineBreak = document.createElement('br');
      roomContainer.appendChild(lineBreak);
    }
  };

  // Public API
  return {
    init,
  };
})();

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', tileApp.init);
```

### HTML Structure (required for the JavaScript code above to work):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ITACA Ceramic Virtual Room Preview</title>
  <style>
    #room-container {
      margin-top: 20px;
      width: 600px; /* Example room width */
      height: 400px; /* Example room height */
      overflow: hidden;
      border: 2px solid #000;
      position: relative;
    }
  </style>
</head>
<body>
  <div>
    <label for="tile-size-selector">Select Tile Size:</label>
    <select id="tile-size-selector">
      <option value="" disabled selected>Select a size</option>
    </select>
  </div>
  <div id="room-container"></div>

  <script src="app.js"></script>
</body>
</html>
```
