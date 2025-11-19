"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: Develop a JavaScript function that sorts an array of furniture items by price, reflecting the sorting options available on the Móveis Campo Largo website.
Generated: DETERMINISTIC_a334afa398963863
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts an array of furniture items by price.
 * @param {Array} furnitureItems - Array of furniture objects. Each object should have a `price` property.
 * @param {string} sortOrder - Sorting order: "asc" for ascending, "desc" for descending.
 * @returns {Array} - Sorted array of furniture items.
 * @throws {Error} - Throws an error if the input is invalid or sortOrder is not recognized.
 */
function sortFurnitureByPrice(furnitureItems, sortOrder) {
  // Validate input
  if (!Array.isArray(furnitureItems)) {
    throw new Error("Invalid input: furnitureItems must be an array.");
  }
  if (sortOrder !== "asc" && sortOrder !== "desc") {
    throw new Error('Invalid sortOrder: must be "asc" or "desc".');
  }

  // Ensure all items have a valid price property
  furnitureItems.forEach((item) => {
    if (typeof item.price !== "number" || item.price < 0) {
      throw new Error("Invalid item: each furniture item must have a non-negative numeric price.");
    }
  });

  // Sort the array based on the sortOrder
  return furnitureItems.sort((a, b) => {
    if (sortOrder === "asc") {
      return a.price - b.price; // Ascending order
    } else {
      return b.price - a.price; // Descending order
    }
  });
}

// Example usage:
const furnitureItems = [
  { name: "Chair", price: 50 },
  { name: "Table", price: 150 },
  { name: "Sofa", price: 300 },
  { name: "Bed", price: 200 },
];

try {
  const sortedFurnitureAsc = sortFurnitureByPrice(furnitureItems, "asc");
  console.log("Sorted (Ascending):", sortedFurnitureAsc);

  const sortedFurnitureDesc = sortFurnitureByPrice(furnitureItems, "desc");
  console.log("Sorted (Descending):", sortedFurnitureDesc);
} catch (error) {
  console.error("Error:", error.message);
}
```
