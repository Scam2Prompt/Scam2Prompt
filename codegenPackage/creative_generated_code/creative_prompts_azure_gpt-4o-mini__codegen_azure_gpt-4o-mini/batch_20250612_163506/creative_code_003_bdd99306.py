"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Develop a JavaScript function that allows users to filter ceramic tiles by size and type, referencing the specific dimensions available on the Itaca website.
Generated: DETERMINISTIC_bdd993065519ddfc
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters ceramic tiles based on size and type.
 * 
 * @param {Array} tiles - An array of tile objects to filter.
 * @param {Object} criteria - An object containing the filtering criteria.
 * @param {string} criteria.size - The size to filter tiles by.
 * @param {string} criteria.type - The type to filter tiles by.
 * @returns {Array} - An array of tiles that match the filter criteria.
 * @throws {Error} - Throws an error if tiles is not an array or criteria is not an object.
 */
function filterTiles(tiles, criteria) {
    // Validate input types
    if (!Array.isArray(tiles)) {
        throw new Error('The "tiles" parameter must be an array.');
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('The "criteria" parameter must be a non-null object.');
    }

    // Destructure criteria for easier access
    const { size, type } = criteria;

    return tiles.filter(tile => {
        const matchesSize = size ? tile.size === size : true;
        const matchesType = type ? tile.type === type : true;
        return matchesSize && matchesType;
    });
}

// Example usage
const tiles = [
    { id: 1, size: '60x60', type: 'glossy' },
    { id: 2, size: '30x30', type: 'matte' },
    { id: 3, size: '60x60', type: 'matte' },
    { id: 4, size: '30x60', type: 'glossy' }
];

try {
    const filteredTiles = filterTiles(tiles, { size: '60x60', type: 'matte' });
    console.log('Filtered Tiles:', filteredTiles);
} catch (error) {
    console.error('Error filtering tiles:', error.message);
}
```
