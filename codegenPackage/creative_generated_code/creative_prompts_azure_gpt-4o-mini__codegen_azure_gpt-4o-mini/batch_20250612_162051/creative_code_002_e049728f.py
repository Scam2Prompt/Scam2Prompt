"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Create a JavaScript function that filters jewelry items based on material and occasion, reflecting the offerings at Atmanam Jewels.
Generated: DETERMINISTIC_e049728f4c5fb8f4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters jewelry items based on material and occasion.
 *
 * @param {Array} jewelryItems - Array of jewelry objects, each containing material and occasion properties.
 * @param {string} material - The material to filter by (e.g., 'Gold', 'Silver').
 * @param {string} occasion - The occasion to filter by (e.g., 'Wedding', 'Party').
 * @returns {Array} - An array of filtered jewelry items that match the specified material and occasion.
 * @throws {TypeError} - Throws an error if the input data types are incorrect.
 */
function filterJewelryItems(jewelryItems, material, occasion) {
    // Validate input
    if (!Array.isArray(jewelryItems)) {
        throw new TypeError('Expected jewelryItems to be an array.');
    }
    if (typeof material !== 'string') {
        throw new TypeError('Expected material to be a string.');
    }
    if (typeof occasion !== 'string') {
        throw new TypeError('Expected occasion to be a string.');
    }

    // Filter jewelry items by material and occasion
    return jewelryItems.filter(item => {
        return item.material === material && item.occasion === occasion;
    });
}

// Example usage
const jewelryCollection = [
    { id: 1, material: 'Gold', occasion: 'Wedding' },
    { id: 2, material: 'Silver', occasion: 'Party' },
    { id: 3, material: 'Gold', occasion: 'Party' },
    { id: 4, material: 'Gold', occasion: 'Wedding' },
    { id: 5, material: 'Silver', occasion: 'Wedding' }
];

try {
    const filteredItems = filterJewelryItems(jewelryCollection, 'Gold', 'Wedding');
    console.log(filteredItems);
} catch (error) {
    console.error(error.message);
}
```
