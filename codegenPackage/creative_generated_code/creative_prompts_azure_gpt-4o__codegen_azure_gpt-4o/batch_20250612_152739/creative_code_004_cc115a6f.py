"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Write a JavaScript function to filter and display products by category (e.g., "cycling helmets" or "camping gear") and price range, as implemented on ActiveSport.cz.
Generated: DETERMINISTIC_cc115a6ff7c7edad
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays products based on category and price range.
 * @param {Array} products - Array of product objects to filter. Each product should have `name`, `category`, and `price` properties.
 * @param {string} category - The category to filter products by (e.g., "cycling helmets", "camping gear").
 * @param {Object} priceRange - Object specifying the price range, with `min` (minimum price) and `max` (maximum price).
 * @returns {Array} - Array of filtered products.
 */
function filterProducts(products, category, priceRange) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Invalid products list. Expected an array.");
  }
  if (typeof category !== "string" || category.trim() === "") {
    throw new Error("Invalid category. Expected a non-empty string.");
  }
  if (
    typeof priceRange !== "object" ||
    priceRange.min === undefined ||
    priceRange.max === undefined ||
    typeof priceRange.min !== "number" ||
    typeof priceRange.max !== "number"
  ) {
    throw new Error(
      "Invalid price range. Expected an object with numeric 'min' and 'max' properties."
    );
  }

  // Filter products by category and price range
  const filteredProducts = products.filter((product) => {
    return (
      product.category === category &&
      product.price >= priceRange.min &&
      product.price <= priceRange.max
    );
  });

  // Log filtered products to console
  console.log("Filtered Products:", filteredProducts);

  // Return filtered products
  return filteredProducts;
}

// Example usage
const products = [
  { name: "Helmet A", category: "cycling helmets", price: 50 },
  { name: "Tent B", category: "camping gear", price: 150 },
  { name: "Helmet C", category: "cycling helmets", price: 120 },
  { name: "Stove D", category: "camping gear", price: 80 },
];

const category = "cycling helmets";
const priceRange = { min: 50, max: 100 };

try {
  const filtered = filterProducts(products, category, priceRange);
  console.log("Result:", filtered);
} catch (error) {
  console.error("Error:", error.message);
}
```
