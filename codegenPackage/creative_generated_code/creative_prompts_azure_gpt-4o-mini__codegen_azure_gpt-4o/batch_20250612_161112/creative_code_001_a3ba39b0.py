"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loli.bg
Prompt: Write a JavaScript function that filters children's clothing categories on LOLI.BG based on size and type, such as "детски рокли" or "детски обувки".
Generated: DETERMINISTIC_a3ba39b05d748464
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters children's clothing categories based on size and type.
 * @param {Array} items - Array of clothing items to filter. Each item should be an object with `type`, `size`, and other properties.
 * @param {Object} filters - Filters to apply. Should contain `type` and `size` properties.
 * @returns {Array} - Array of filtered clothing items.
 */
function filterChildrenClothing(items, filters) {
  // Validate input parameters
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: 'items' must be an array.");
  }
  if (typeof filters !== "object" || filters === null) {
    throw new Error("Invalid input: 'filters' must be a non-null object.");
  }

  // Extract filter criteria
  const { type, size } = filters;

  // Perform filtering
  return items.filter((item) => {
    // Ensure item has the necessary properties
    if (typeof item !== "object" || item === null || !item.type || !item.size) {
      return false;
    }

    // Match type and size
    const typeMatches = type ? item.type === type : true;
    const sizeMatches = size ? item.size === size : true;

    return typeMatches && sizeMatches;
  });
}

// Example usage:
const clothingItems = [
  { type: "детски рокли", size: "S", name: "Fancy Dress" },
  { type: "детски обувки", size: "M", name: "Running Shoes" },
  { type: "детски рокли", size: "M", name: "Summer Dress" },
];

const filters = { type: "детски рокли", size: "M" };

try {
  const filteredItems = filterChildrenClothing(clothingItems, filters);
  console.log(filteredItems);
  // Output: [{ type: "детски рокли", size: "M", name: "Summer Dress" }]
} catch (error) {
  console.error("Error:", error.message);
}
```
