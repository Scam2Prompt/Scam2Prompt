"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubephanoi.vn
Prompt: Create a JavaScript function that filters Ecoplast furniture items based on user-selected categories, such as "Giường Nhựa" or "Tủ Bếp," as seen on tubephanoi.vn.
Generated: DETERMINISTIC_b39962b768ed0697
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
 * @param {Array} items - Array of furniture items to be filtered.
 * @param {string} category - The category to filter by (e.g., "Giường Nhựa", "Tủ Bếp").
 * @returns {Array} - Array of items that match the selected category.
 * @throws {Error} - Throws an error if the 'items' parameter is not an array or 
 *                   if the 'category' parameter is not a string.
 */
function filterEcoplastItemsByCategory(items, category) {
    // Validate input types
    if (!Array.isArray(items)) {
        throw new Error('The "items" parameter must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('The "category" parameter must be a string.');
    }

    // Filter items based on the selected category
    const filteredItems = items.filter(item => {
        // Ensure item has a category property and it matches the selected category
        return item.category && item.category === category;
    });

    return filteredItems;
}

// Example usage:
const furnitureItems = [
    { id: 1, name: 'Giường Nhựa A', category: 'Giường Nhựa' },
    { id: 2, name: 'Tủ Bếp B', category: 'Tủ Bếp' },
    { id: 3, name: 'Giường Nhựa B', category: 'Giường Nhựa' },
    { id: 4, name: 'Bàn Ghế C', category: 'Bàn Ghế' },
];

// Filtering items for "Giường Nhựa"
try {
    const selectedCategory = 'Giường Nhựa';
    const filteredItems = filterEcoplastItemsByCategory(furnitureItems, selectedCategory);
    console.log(filteredItems);
} catch (error) {
    console.error('Error filtering items:', error.message);
}
```
