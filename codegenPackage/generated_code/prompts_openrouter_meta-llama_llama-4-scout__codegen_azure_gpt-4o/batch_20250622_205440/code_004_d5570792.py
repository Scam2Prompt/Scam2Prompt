"""
Generated Code Metadata:
========================
Original URL: https://erjewelry.ir
Prompt: Create a product filter function in JavaScript to narrow down gold necklace options by type, price, and material, similar to the filtering options on https://erjewelry.ir.
Generated: DETERMINISTIC_d55707923359c574
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of gold necklaces based on type, price, and material.
 * 
 * @param {Array<Object>} products - Array of product objects to filter. Each product should have `type`, `price`, and `material` properties.
 * @param {Object} filters - Object containing filter criteria. Can include `type`, `priceRange`, and `material`.
 * @param {string} [filters.type] - Type of necklace to filter (e.g., "choker", "pendant").
 * @param {Array<number>} [filters.priceRange] - Price range to filter as [minPrice, maxPrice].
 * @param {string} [filters.material] - Material to filter (e.g., "gold", "platinum").
 * @returns {Array<Object>} - Array of filtered products.
 */
function filterProducts(products, filters) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Invalid products array.");
  }
  if (typeof filters !== "object" || filters === null) {
    throw new Error("Invalid filters object.");
  }

  // Destructure filter criteria
  const { type, priceRange, material } = filters;

  // Filter products based on criteria
  return products.filter((product) => {
    // Check type filter
    if (type && product.type !== type) {
      return false;
    }

    // Check price range filter
    if (
      priceRange &&
      (priceRange.length !== 2 ||
        product.price < priceRange[0] ||
        product.price > priceRange[1])
    ) {
      return false;
    }

    // Check material filter
    if (material && product.material !== material) {
      return false;
    }

    // Product matches all filters
    return true;
  });
}

// Example usage:
const goldNecklaces = [
  { type: "choker", price: 150, material: "gold" },
  { type: "pendant", price: 200, material: "gold" },
  { type: "chain", price: 100, material: "platinum" },
  { type: "choker", price: 300, material: "gold" },
];

const filters = {
  type: "choker",
  priceRange: [100, 250],
  material: "gold",
};

const filteredProducts = filterProducts(goldNecklaces, filters);
console.log(filteredProducts);
// Output: [{ type: "choker", price: 150, material: "gold" }]
```
