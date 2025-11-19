"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: "Generate a JavaScript function to filter tire products by size and type on the Itamarati Online website, using the product specifications listed on the page."
Generated: DETERMINISTIC_9c424605ea160466
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters tire products by size and type.
 * 
 * @param {Array} products - Array of tire product objects. Each object should have `size` and `type` properties.
 * @param {string} size - The desired tire size to filter by (e.g., "205/55R16").
 * @param {string} type - The desired tire type to filter by (e.g., "All-Season").
 * @returns {Array} - Array of filtered tire products matching the specified size and type.
 */
function filterTireProducts(products, size, type) {
  // Validate input parameters
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: 'products' must be an array.");
  }
  if (typeof size !== "string" || typeof type !== "string") {
    throw new Error("Invalid input: 'size' and 'type' must be strings.");
  }

  // Filter products based on size and type
  const filteredProducts = products.filter(product => {
    // Ensure product has the required properties
    if (!product.size || !product.type) {
      console.warn("Skipping product due to missing 'size' or 'type' property:", product);
      return false;
    }

    // Match size and type
    return product.size === size && product.type === type;
  });

  return filteredProducts;
}

// Example usage:
// Assuming `tireProducts` is an array of tire product objects fetched from the Itamarati Online website.
const tireProducts = [
  { id: 1, size: "205/55R16", type: "All-Season", brand: "BrandA" },
  { id: 2, size: "195/65R15", type: "Winter", brand: "BrandB" },
  { id: 3, size: "205/55R16", type: "All-Season", brand: "BrandC" },
  { id: 4, size: "205/55R16", type: "Summer", brand: "BrandD" }
];

const filtered = filterTireProducts(tireProducts, "205/55R16", "All-Season");
console.log(filtered);
// Output: [
//   { id: 1, size: "205/55R16", type: "All-Season", brand: "BrandA" },
//   { id: 3, size: "205/55R16", type: "All-Season", brand: "BrandC" }
// ]
```
