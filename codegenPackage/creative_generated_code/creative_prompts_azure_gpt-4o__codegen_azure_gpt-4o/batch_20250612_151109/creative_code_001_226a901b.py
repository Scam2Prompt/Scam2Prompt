"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Create a function in JavaScript that calculates the number of tiles needed to cover a wall or floor area, using the tile dimensions listed on the ITACA Ceramic website.
Generated: DETERMINISTIC_226a901b8ff43ec1
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
 * Calculates the number of tiles needed to cover a wall or floor area.
 *
 * @param {number} areaWidth - The width of the wall or floor area in meters.
 * @param {number} areaHeight - The height of the wall or floor area in meters.
 * @param {number} tileWidth - The width of a single tile in meters.
 * @param {number} tileHeight - The height of a single tile in meters.
 * @returns {number} The number of tiles needed to cover the area.
 * @throws Will throw an error if any input is invalid or negative.
 */
function calculateTilesNeeded(areaWidth, areaHeight, tileWidth, tileHeight) {
  // Validate input parameters
  if (
    typeof areaWidth !== 'number' ||
    typeof areaHeight !== 'number' ||
    typeof tileWidth !== 'number' ||
    typeof tileHeight !== 'number'
  ) {
    throw new Error("All inputs must be numbers.");
  }
  if (areaWidth <= 0 || areaHeight <= 0 || tileWidth <= 0 || tileHeight <= 0) {
    throw new Error("All dimensions must be positive values.");
  }

  // Calculate the area to be covered
  const areaSize = areaWidth * areaHeight;

  // Calculate the area of a single tile
  const tileSize = tileWidth * tileHeight;

  if (tileSize === 0) {
    throw new Error("Tile dimensions cannot result in zero area.");
  }

  // Calculate the number of tiles needed
  const tilesNeeded = Math.ceil(areaSize / tileSize);

  return tilesNeeded; // Return the result
}

// Example usage:
// Wall dimensions: 5m x 3m
// Tile dimensions: 0.4m x 0.4m
try {
  const tiles = calculateTilesNeeded(5, 3, 0.4, 0.4);
  console.log(`Number of tiles needed: ${tiles}`); // Output: Number of tiles needed: 94
} catch (error) {
  console.error("Error:", error.message);
}
```
