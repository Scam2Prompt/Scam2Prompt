"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Write a JavaScript function to dynamically filter products by size, color, and brand (e.g., filtering "Ralph Lauren Men's Shirts" by size and color) for an e-commerce platform like brandsoutlet.qa.
Generated: DETERMINISTIC_1318560a4901efd7
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically filter products based on multiple criteria: size, color, and brand.
 * @param {Array} products - Array of product objects to filter. Each product should have keys: size, color, brand.
 * @param {Object} filters - Object containing the filter criteria. Keys: size, color, brand.
 * @returns {Array} - Array of filtered products matching the criteria.
 */
function filterProducts(products, filters) {
  // Validate inputs
  if (!Array.isArray(products)) {
    throw new Error("Invalid data type for 'products'. Expected an array.");
  }
  if (typeof filters !== "object" || filters === null) {
    throw new Error("Invalid data type for 'filters'. Expected a non-null object.");
  }

  // Perform the filtering
  return products.filter(product => {
    try {
      // Check each filter criteria
      const matchesSize = filters.size ? product.size === filters.size : true;
      const matchesColor = filters.color ? product.color === filters.color : true;
      const matchesBrand = filters.brand ? product.brand === filters.brand : true;

      // Return true if all criteria match
      return matchesSize && matchesColor && matchesBrand;
    } catch (err) {
      console.error("Error during filtering:", err);
      return false; // Ignore faulty product entries
    }
  });
}

// Example usage
const products = [
  { id: 1, name: "Ralph Lauren Men's Shirt", size: "M", color: "Blue", brand: "Ralph Lauren" },
  { id: 2, name: "Adidas Running Shoes", size: "10", color: "Black", brand: "Adidas" },
  { id: 3, name: "Ralph Lauren Women's Shirt", size: "S", color: "Red", brand: "Ralph Lauren" },
  { id: 4, name: "Nike Sports Shirt", size: "L", color: "Blue", brand: "Nike" }
];

const filters = {
  size: "M",
  color: "Blue",
  brand: "Ralph Lauren"
};

const filteredProducts = filterProducts(products, filters);
console.log("Filtered Products:", filteredProducts);
```
