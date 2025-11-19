"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: Develop a JavaScript function that sorts an array of furniture items by price, reflecting the sorting options available on the Móveis Campo Largo website.
Generated: DETERMINISTIC_a334afa398963863
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sorts an array of furniture items by price.
 * 
 * @param {Array} furnitureItems - An array of furniture objects. Each object should have a `price` property.
 * @param {string} sortOrder - Sorting order: 'asc' for ascending or 'desc' for descending.
 * @returns {Array} - A new array of furniture items sorted by price.
 * @throws {Error} - Throws an error if the input is invalid or if `sortOrder` is not 'asc' or 'desc'.
 */
function sortFurnitureByPrice(furnitureItems, sortOrder) {
    // Validate input
    if (!Array.isArray(furnitureItems)) {
        throw new Error("Invalid input: furnitureItems must be an array.");
    }
    if (sortOrder !== 'asc' && sortOrder !== 'desc') {
        throw new Error("Invalid sortOrder: must be 'asc' or 'desc'.");
    }

    // Validate the structure of each furniture item
    furnitureItems.forEach(item => {
        if (typeof item !== 'object' || item === null || typeof item.price !== 'number') {
            throw new Error("Invalid input: each furniture item must be an object with a numeric `price` property.");
        }
    });

    // Perform sorting based on the sortOrder
    return furnitureItems.slice().sort((a, b) => {
        return sortOrder === 'asc' ? a.price - b.price : b.price - a.price;
    });
}

// Example usage:
const furniture = [
    { name: "Chair", price: 50 },
    { name: "Table", price: 150 },
    { name: "Sofa", price: 300 },
    { name: "Bed", price: 200 }
];

try {
    const sortedFurnitureAsc = sortFurnitureByPrice(furniture, 'asc');
    console.log("Sorted Ascending:", sortedFurnitureAsc);

    const sortedFurnitureDesc = sortFurnitureByPrice(furniture, 'desc');
    console.log("Sorted Descending:", sortedFurnitureDesc);
} catch (error) {
    console.error(error.message);
}
```
