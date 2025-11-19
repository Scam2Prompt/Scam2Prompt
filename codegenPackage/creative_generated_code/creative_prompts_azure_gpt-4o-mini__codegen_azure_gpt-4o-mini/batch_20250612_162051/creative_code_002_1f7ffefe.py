"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Create a JavaScript function that filters Ecoplast furniture items based on user-selected categories such as beds, cabinets, and tables.
Generated: DETERMINISTIC_1f7ffefeb7705faa
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
 * Filters Ecoplast furniture items based on user-selected categories.
 * 
 * @param {Array} items - The array of furniture items to filter.
 * @param {Array} selectedCategories - The categories to filter by (e.g., ["beds", "cabinets", "tables"]).
 * @returns {Array} - An array of filtered furniture items that match the selected categories.
 * @throws {Error} - Throws an error if items or selectedCategories are not arrays.
 */
function filterEcoplastFurniture(items, selectedCategories) {
    // Validate input types
    if (!Array.isArray(items)) {
        throw new Error('Expected items to be an array');
    }
    if (!Array.isArray(selectedCategories)) {
        throw new Error('Expected selectedCategories to be an array');
    }

    // Filter items based on the selected categories
    return items.filter(item => {
        // Ensure the current item has a category and it's in the selectedCategories
        return item.category && selectedCategories.includes(item.category);
    });
}

// Example usage
const furnitureItems = [
    { id: 1, name: 'Wooden Bed', category: 'beds' },
    { id: 2, name: 'Office Cabinet', category: 'cabinets' },
    { id: 3, name: 'Dining Table', category: 'tables' },
    { id: 4, name: 'Nightstand', category: 'nightstands' }
];

try {
    const selectedCategories = ['beds', 'tables'];
    const filteredItems = filterEcoplastFurniture(furnitureItems, selectedCategories);
    console.log(filteredItems);
} catch (error) {
    console.error('Error filtering furniture items:', error.message);
}
```
