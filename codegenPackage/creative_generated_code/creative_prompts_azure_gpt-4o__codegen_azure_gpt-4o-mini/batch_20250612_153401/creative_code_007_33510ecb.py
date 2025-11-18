"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libointeriors.net
Prompt: Generate a JavaScript function to estimate the number of carpet tiles needed for a given room size, using specifications for nylon and polypropylene tiles from Libo Interiors.
Generated: DETERMINISTIC_33510ecb2278dad7
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Estimates the number of carpet tiles needed for a given room size.
 * 
 * @param {number} roomLength - The length of the room in meters.
 * @param {number} roomWidth - The width of the room in meters.
 * @param {string} tileType - The type of tile ('nylon' or 'polypropylene').
 * @returns {number} The estimated number of carpet tiles needed.
 * @throws {Error} Throws an error if room dimensions are non-positive or if tile type is invalid.
 */
function estimateCarpetTiles(roomLength, roomWidth, tileType) {
    // Validate input parameters
    if (roomLength <= 0 || roomWidth <= 0) {
        throw new Error("Room dimensions must be positive numbers.");
    }

    // Define tile sizes in square meters
    const tileSizes = {
        nylon: 1.0, // Example size for nylon tile (1 square meter)
        polypropylene: 0.9 // Example size for polypropylene tile (0.9 square meter)
    };

    // Validate tile type and get the corresponding tile size
    const tileSize = tileSizes[tileType.toLowerCase()];
    if (!tileSize) {
        throw new Error("Invalid tile type. Please use 'nylon' or 'polypropylene'.");
    }

    // Calculate the area of the room
    const roomArea = roomLength * roomWidth;

    // Calculate the number of tiles needed, rounding up to ensure full coverage
    const numberOfTiles = Math.ceil(roomArea / tileSize);

    return numberOfTiles;
}

// Example usage
try {
    const tilesNeeded = estimateCarpetTiles(5, 4, 'nylon');
    console.log(`Number of tiles needed: ${tilesNeeded}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
