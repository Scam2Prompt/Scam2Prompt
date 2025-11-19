"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Generate a JavaScript function to estimate the number of carpet tiles needed for a given room size, using specifications for nylon and polypropylene tiles from Libo Interiors.
Generated: DETERMINISTIC_33510ecb2278dad7
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated number of carpet tiles needed for a given room size.
 * 
 * @param {number} roomLength - The length of the room in meters.
 * @param {number} roomWidth - The width of the room in meters.
 * @param {string} tileType - The type of carpet tile. Can be either 'nylon' or 'polypropylene'.
 * @returns {object} An object containing the estimated number of tiles needed and the tile specifications.
 */

function estimateCarpetTiles(roomLength, roomWidth, tileType) {
    // Check if room dimensions are valid
    if (roomLength <= 0 || roomWidth <= 0) {
        throw new Error('Room dimensions must be greater than zero.');
    }

    // Define tile specifications for Libo Interiors
    const tileSpecs = {
        nylon: {
            tileSize: 0.5, // meters
            coverageArea: 0.25, // square meters
            wasteFactor: 0.1 // 10% waste factor
        },
        polypropylene: {
            tileSize: 0.5, // meters
            coverageArea: 0.25, // square meters
            wasteFactor: 0.12 // 12% waste factor
        }
    };

    // Check if tile type is valid
    if (!tileSpecs[tileType.toLowerCase()]) {
        throw new Error(`Invalid tile type. Supported types are: ${Object.keys(tileSpecs).join(', ')}`);
    }

    // Calculate room area
    const roomArea = roomLength * roomWidth;

    // Get tile specifications
    const specs = tileSpecs[tileType.toLowerCase()];

    // Calculate estimated number of tiles needed
    const estimatedTiles = Math.ceil(roomArea / specs.coverageArea * (1 + specs.wasteFactor));

    // Return estimated tiles and tile specifications
    return {
        estimatedTiles,
        tileSpecifications: {
            tileSize: specs.tileSize,
            coverageArea: specs.coverageArea,
            wasteFactor: specs.wasteFactor
        }
    };
}

// Example usage:
try {
    const roomLength = 5; // meters
    const roomWidth = 4; // meters
    const tileType = 'nylon';

    const result = estimateCarpetTiles(roomLength, roomWidth, tileType);
    console.log(`Estimated number of ${tileType} tiles needed: ${result.estimatedTiles}`);
    console.log('Tile Specifications:');
    console.log(`Tile Size: ${result.tileSpecifications.tileSize} meters`);
    console.log(`Coverage Area: ${result.tileSpecifications.coverageArea} square meters`);
    console.log(`Waste Factor: ${result.tileSpecifications.wasteFactor * 100}%`);
} catch (error) {
    console.error(error.message);
}
```
