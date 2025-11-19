"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Write a JavaScript function that filters men's sandals based on color from the product listings on Emily Sapatos em Geral.
Generated: DETERMINISTIC_623bc8de43bb53c1
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters men's sandals by color from the product listings.
 * @param {Array} productListings - Array of product objects. Each product should have properties `category`, `gender`, `type`, and `color`.
 * @param {string} targetColor - The color to filter sandals by (e.g., "blue").
 * @returns {Array} - Array of men's sandals that match the specified color.
 */
function filterMensSandalsByColor(productListings, targetColor) {
  // Validate input
  if (!Array.isArray(productListings)) {
    throw new Error("Invalid input: productListings must be an array.");
  }

  if (typeof targetColor !== "string") {
    throw new Error("Invalid input: targetColor must be a string.");
  }

  // Filter the product listings
  return productListings.filter(product => {
    // Ensure the product data is structured correctly
    if (
      typeof product !== "object" ||
      !product.category ||
      !product.gender ||
      !product.type ||
      !product.color
    ) {
      console.warn("Skipping invalid product:", product);
      return false;
    }

    // Return true if the product is a men's sandal of the target color
    return (
      product.category.toLowerCase() === "footwear" &&
      product.gender.toLowerCase() === "men" &&
      product.type.toLowerCase() === "sandals" &&
      product.color.toLowerCase() === targetColor.toLowerCase()
    );
  });
}

// Example Usage
const productListings = [
  { category: "Footwear", gender: "Men", type: "Sandals", color: "Blue" },
  { category: "Footwear", gender: "Men", type: "Shoes", color: "Black" },
  { category: "Footwear", gender: "Women", type: "Sandals", color: "Blue" },
  { category: "Footwear", gender: "Men", type: "Sandals", color: "Red" },
];

const filteredSandals = filterMensSandalsByColor(productListings, "Blue");
console.log(filteredSandals); // Output: [{ category: "Footwear", gender: "Men", type: "Sandals", color: "Blue" }]
```
