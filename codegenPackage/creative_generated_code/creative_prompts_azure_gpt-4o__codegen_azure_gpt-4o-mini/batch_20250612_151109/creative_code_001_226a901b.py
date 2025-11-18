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
 * Calculates the number of tiles needed to cover a given area.
 * 
 * @param {number} areaWidth - The width of the area to be covered (in meters).
 * @param {number} areaHeight - The height of the area to be covered (in meters).
 * @param {number} tileWidth - The width of a single tile (in meters).
 * @param {number} tileHeight - The height of a single tile (in meters).
 * @returns {number} The number of tiles required to cover the area.
 * @throws {Error} Throws an error if any of the inputs are non-positive numbers.
 */
function calculateTiles(areaWidth, areaHeight, tileWidth, tileHeight) {
    // Validate input parameters
    if (areaWidth <= 0 || areaHeight <= 0 || tileWidth <= 0 || tileHeight <= 0) {
        throw new Error("All dimensions must be positive numbers.");
    }

    // Calculate the area of the wall or floor
    const area = areaWidth * areaHeight;

    // Calculate the area of a single tile
    const tileArea = tileWidth * tileHeight;

    // Calculate the number of tiles needed (rounding up to ensure full coverage)
    const numberOfTiles = Math.ceil(area / tileArea);

    return numberOfTiles;
}

// Example usage:
// const tilesNeeded = calculateTiles(5, 3, 0.5, 0.5);
// console.log(`Tiles needed: ${tilesNeeded}`);
```
