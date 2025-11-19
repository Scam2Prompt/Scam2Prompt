"""
Generated Code Metadata:
========================
Original URL: https://tubephanoi.vn
Prompt: Create a JavaScript function that filters Ecoplast furniture items based on user-selected categories, such as "Giường Nhựa" or "Tủ Bếp," as seen on tubephanoi.vn.
Generated: DETERMINISTIC_b39962b768ed0697
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
 * Filters Ecoplast furniture items based on user-selected categories.
 * 
 * @param {Array} items - The array of furniture items to filter.
 * @param {string} category - The category to filter by (e.g., "Giường Nhựa", "Tủ Bếp").
 * @returns {Array} - An array of filtered furniture items that match the selected category.
 * @throws {Error} - Throws an error if the input items are not an array or if the category is not a string.
 */
function filterEcoplastFurniture(items, category) {
    // Validate input types
    if (!Array.isArray(items)) {
        throw new Error("The 'items' parameter must be an array.");
    }
    if (typeof category !== 'string') {
        throw new Error("The 'category' parameter must be a string.");
    }

    // Filter items based on the selected category
    const filteredItems = items.filter(item => item.category === category);

    return filteredItems;
}

// Example usage
try {
    const furnitureItems = [
        { id: 1, name: "Giường Nhựa 1", category: "Giường Nhựa" },
        { id: 2, name: "Tủ Bếp 1", category: "Tủ Bếp" },
        { id: 3, name: "Giường Nhựa 2", category: "Giường Nhựa" },
        { id: 4, name: "Bàn Nhựa", category: "Bàn" }
    ];

    const selectedCategory = "Giường Nhựa";
    const result = filterEcoplastFurniture(furnitureItems, selectedCategory);
    console.log(result); // Output: Filtered items based on the selected category
} catch (error) {
    console.error("Error filtering furniture items:", error.message);
}
```
