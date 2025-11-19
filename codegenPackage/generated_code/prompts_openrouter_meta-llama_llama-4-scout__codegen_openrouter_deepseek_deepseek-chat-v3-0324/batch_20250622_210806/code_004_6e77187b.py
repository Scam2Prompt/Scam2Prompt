"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: "Create a JavaScript function to filter search results for figure skating costumes based on color, size, and price, similar to the filtering options on the IceStyle website."
Generated: DETERMINISTIC_6e77187be6e780e0
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters figure skating costumes based on color, size, and price criteria.
 * @param {Array} costumes - Array of costume objects to filter
 * @param {Object} filters - Filter criteria object
 * @param {Array} [filters.colors] - Array of color strings to match
 * @param {Array} [filters.sizes] - Array of size strings to match
 * @param {Object} [filters.price] - Price range object
 * @param {number} [filters.price.min] - Minimum price
 * @param {number} [filters.price.max] - Maximum price
 * @returns {Array} Filtered array of costume objects
 */
function filterCostumes(costumes, filters) {
    if (!Array.isArray(costumes)) {
        throw new TypeError('Costumes must be an array');
    }

    if (!filters || typeof filters !== 'object') {
        return costumes;
    }

    return costumes.filter(costume => {
        // Validate costume object structure
        if (!costume || typeof costume !== 'object') {
            return false;
        }

        // Check color filter
        if (filters.colors && Array.isArray(filters.colors) && filters.colors.length > 0) {
            if (!costume.color || !filters.colors.includes(costume.color.toLowerCase())) {
                return false;
            }
        }

        // Check size filter
        if (filters.sizes && Array.isArray(filters.sizes) && filters.sizes.length > 0) {
            if (!costume.sizes || !costume.sizes.some(size => filters.sizes.includes(size))) {
                return false;
            }
        }

        // Check price filter
        if (filters.price && typeof filters.price === 'object') {
            const { min, max } = filters.price;
            const costumePrice = costume.price || 0;

            if (typeof min === 'number' && costumePrice < min) {
                return false;
            }
            if (typeof max === 'number' && costumePrice > max) {
                return false;
            }
        }

        return true;
    });
}

// Example usage:
/*
const costumes = [
    { id: 1, name: 'Elegance', color: 'blue', sizes: ['S', 'M'], price: 299 },
    { id: 2, name: 'Sparkle', color: 'red', sizes: ['M', 'L'], price: 350 },
    { id: 3, name: 'Twirl', color: 'blue', sizes: ['XS', 'S'], price: 250 }
];

const filters = {
    colors: ['blue'],
    sizes: ['S'],
    price: { min: 200, max: 300 }
};

const filteredCostumes = filterCostumes(costumes, filters);
console.log(filteredCostumes);
*/
```
