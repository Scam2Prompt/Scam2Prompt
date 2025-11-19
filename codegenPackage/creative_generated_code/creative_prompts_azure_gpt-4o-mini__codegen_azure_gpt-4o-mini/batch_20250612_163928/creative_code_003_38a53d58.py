"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.cz
Prompt: Develop a JavaScript function that filters furniture items based on categories like bedroom, children's room, and kitchen from an online catalog.
Generated: DETERMINISTIC_38a53d58e2f6630b
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters furniture items based on specified categories.
 * 
 * @param {Array} items - The array of furniture items to filter.
 * @param {string} category - The category to filter by (e.g., "bedroom", "children", "kitchen").
 * @returns {Array} - An array of furniture items that belong to the specified category.
 * @throws {Error} - Throws an error if the items parameter is not an array or if the category is not a string.
 */
function filterFurnitureByCategory(items, category) {
    // Validate input parameters
    if (!Array.isArray(items)) {
        throw new Error("Invalid input: 'items' should be an array.");
    }
    if (typeof category !== 'string') {
        throw new Error("Invalid input: 'category' should be a string.");
    }

    // Normalize category to lowercase for case-insensitive comparison
    const normalizedCategory = category.toLowerCase();

    // Filter items based on the provided category
    const filteredItems = items.filter(item => {
        return item.category && item.category.toLowerCase() === normalizedCategory;
    });

    return filteredItems;
}

// Example usage
const furnitureCatalog = [
    { id: 1, name: 'Bed Frame', category: 'Bedroom' },
    { id: 2, name: 'Dining Table', category: 'Kitchen' },
    { id: 3, name: 'Bunk Bed', category: 'Children' },
    { id: 4, name: 'Sofa', category: 'Living Room' },
];

// Filtering example
try {
    const bedroomItems = filterFurnitureByCategory(furnitureCatalog, 'Bedroom');
    console.log('Filtered Bedroom Items:', bedroomItems);
} catch (error) {
    console.error(error.message);
}
```
