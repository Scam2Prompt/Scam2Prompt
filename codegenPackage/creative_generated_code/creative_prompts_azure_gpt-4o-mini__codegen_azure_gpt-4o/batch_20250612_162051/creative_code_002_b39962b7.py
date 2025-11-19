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
 * Filters furniture items based on user-selected categories.
 * 
 * @param {Array} items - Array of furniture items. Each item is an object with properties like `name` and `category`.
 * @param {Array} selectedCategories - Array of user-selected categories to filter by (e.g., ["Giường Nhựa", "Tủ Bếp"]).
 * @returns {Array} - Array of filtered furniture items that belong to the selected categories.
 */
function filterFurnitureItems(items, selectedCategories) {
    // Validate inputs
    if (!Array.isArray(items)) {
        throw new Error("Invalid input: 'items' must be an array.");
    }
    if (!Array.isArray(selectedCategories)) {
        throw new Error("Invalid input: 'selectedCategories' must be an array.");
    }

    // Filter items based on the selected categories
    return items.filter(item => {
        // Ensure the item has a valid 'category' property
        if (!item || !item.category) {
            console.warn("Skipping item due to missing 'category' property:", item);
            return false;
        }
        // Check if the item's category matches one of the selected categories
        return selectedCategories.includes(item.category);
    });
}

// Example usage:

// Array of furniture items
const furnitureItems = [
    { id: 1, name: "Giường Nhựa Cao Cấp", category: "Giường Nhựa" },
    { id: 2, name: "Tủ Bếp Gỗ Công Nghiệp", category: "Tủ Bếp" },
    { id: 3, name: "Bàn Làm Việc", category: "Bàn Làm Việc" },
    { id: 4, name: "Tủ Quần Áo", category: "Tủ Quần Áo" }
];

// User-selected categories
const selectedCategories = ["Giường Nhựa", "Tủ Bếp"];

// Filtered items
const filteredItems = filterFurnitureItems(furnitureItems, selectedCategories);

// Output the filtered items
console.log(filteredItems);
// Expected output:
// [
//   { id: 1, name: "Giường Nhựa Cao Cấp", category: "Giường Nhựa" },
//   { id: 2, name: "Tủ Bếp Gỗ Công Nghiệp", category: "Tủ Bếp" }
// ]
```
