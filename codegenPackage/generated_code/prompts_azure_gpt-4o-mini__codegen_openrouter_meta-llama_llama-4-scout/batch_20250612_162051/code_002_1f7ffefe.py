"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: Create a JavaScript function that filters Ecoplast furniture items based on user-selected categories such as beds, cabinets, and tables.
Generated: DETERMINISTIC_1f7ffefeb7705faa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Ecoplast Furniture Filter Function
 * 
 * This function filters Ecoplast furniture items based on user-selected categories.
 * 
 * @param {Array} furnitureItems - A list of Ecoplast furniture items.
 * @param {Array} selectedCategories - A list of user-selected categories.
 * 
 * @returns {Array} - A list of filtered furniture items.
 */
function filterFurnitureItems(furnitureItems, selectedCategories) {
    // Check if furnitureItems and selectedCategories are arrays
    if (!Array.isArray(furnitureItems) || !Array.isArray(selectedCategories)) {
        throw new Error('Invalid input type. Both furnitureItems and selectedCategories must be arrays.');
    }

    // Filter furniture items based on selected categories
    return furnitureItems.filter(item => {
        // Check if the item has a category property
        if (!item.category) {
            return false; // or throw an error, depending on the requirements
        }

        // Check if the item's category is in the selected categories
        return selectedCategories.includes(item.category);
    });
}

// Example usage:
const furnitureItems = [
    { id: 1, name: 'Bed 1', category: 'beds' },
    { id: 2, name: 'Cabinet 1', category: 'cabinets' },
    { id: 3, name: 'Table 1', category: 'tables' },
    { id: 4, name: 'Bed 2', category: 'beds' },
    { id: 5, name: 'Cabinet 2', category: 'cabinets' },
];

const selectedCategories = ['beds', 'cabinets'];

try {
    const filteredItems = filterFurnitureItems(furnitureItems, selectedCategories);
    console.log(filteredItems);
} catch (error) {
    console.error(error.message);
}
```
