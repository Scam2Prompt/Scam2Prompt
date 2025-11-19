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
 * Filters furniture items based on user-selected categories.
 * @param {Array<Object>} items - Array of furniture items where each item is an object with a 'category' property.
 * @param {Array<String>} selectedCategories - Array of categories selected by the user (e.g., ['beds', 'cabinets', 'tables']).
 * @returns {Array<Object>} - Array of furniture items that match the selected categories.
 */
function filterFurnitureItems(items, selectedCategories) {
  // Validate inputs
  if (!Array.isArray(items)) {
    throw new Error("The 'items' parameter must be an array.");
  }
  if (!Array.isArray(selectedCategories)) {
    throw new Error("The 'selectedCategories' parameter must be an array.");
  }

  // Filter items based on the selected categories
  return items.filter(item => {
    // Ensure each item has a 'category' property
    if (!item.hasOwnProperty('category') || typeof item.category !== 'string') {
      throw new Error("Each furniture item must have a valid 'category' property.");
    }
    // Check if the item's category is in the selected categories
    return selectedCategories.includes(item.category.toLowerCase());
  });
}

// Example usage:

// Array of furniture items
const furnitureItems = [
  { id: 1, name: 'King Size Bed', category: 'beds' },
  { id: 2, name: 'Wardrobe Cabinet', category: 'cabinets' },
  { id: 3, name: 'Dining Table', category: 'tables' },
  { id: 4, name: 'Sofa Set', category: 'sofas' }
];

// User-selected categories
const selectedCategories = ['beds', 'tables'];

// Filtering the furniture items
try {
  const filteredItems = filterFurnitureItems(furnitureItems, selectedCategories);
  console.log('Filtered Items:', filteredItems);
} catch (error) {
  console.error('Error:', error.message);
}
```
