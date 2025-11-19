"""
Generated Code Metadata:
========================
Original URL: https://debank.cz
Prompt: Develop a JavaScript function that filters furniture items based on categories like bedroom, children's room, and kitchen from an online catalog.
Generated: DETERMINISTIC_38a53d58e2f6630b
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters furniture items based on given categories.
 * 
 * @param {Array} items - Array of furniture items to filter
 * @param {Array} categories - Array of categories to filter by
 * @returns {Array} Filtered array of furniture items matching any of the categories
 * @throws {Error} If items or categories are not arrays
 */
function filterFurnitureByCategory(items, categories) {
    // Validate input parameters
    if (!Array.isArray(items) || !Array.isArray(categories)) {
        throw new Error('Both items and categories must be arrays');
    }

    // Return filtered items
    return items.filter(item => {
        // Check if item has a category and it matches any of the desired categories
        return item.category && categories.includes(item.category.toLowerCase());
    });
}

// Example usage:
/*
const furnitureCatalog = [
    { id: 1, name: 'Queen Bed', category: 'bedroom', price: 599 },
    { id: 2, name: 'Dresser', category: 'bedroom', price: 299 },
    { id: 3, name: 'Crib', category: 'children\'s room', price: 199 },
    { id: 4, name: 'High Chair', category: 'children\'s room', price: 89 },
    { id: 5, name: 'Dining Table', category: 'kitchen', price: 499 },
    { id: 6, name: 'Bar Stool', category: 'kitchen', price: 79 }
];

const filteredItems = filterFurnitureByCategory(furnitureCatalog, ['bedroom', 'kitchen']);
console.log(filteredItems);
*/
```
