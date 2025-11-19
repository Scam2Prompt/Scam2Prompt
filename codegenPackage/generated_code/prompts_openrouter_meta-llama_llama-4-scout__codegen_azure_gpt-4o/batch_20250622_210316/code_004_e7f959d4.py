"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: "Create a JavaScript function to filter and sort products on a webpage, similar to the product listings on activesport.cz, based on user input."
Generated: DETERMINISTIC_e7f959d4d3a19214
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and sorts products based on user input.
 * @param {Array} products - Array of product objects. Each product should have properties like name, price, category, etc.
 * @param {Object} filters - Object containing filter criteria (e.g., { category: 'Shoes', priceRange: [50, 150] }).
 * @param {Object} sortOptions - Object containing sort criteria (e.g., { key: 'price', order: 'asc' }).
 * @returns {Array} - Filtered and sorted array of products.
 */
function filterAndSortProducts(products, filters, sortOptions) {
  try {
    // Validate input
    if (!Array.isArray(products)) {
      throw new Error("Invalid products array.");
    }
    if (typeof filters !== "object" || typeof sortOptions !== "object") {
      throw new Error("Invalid filters or sortOptions object.");
    }

    // Filter products based on criteria
    let filteredProducts = products.filter((product) => {
      let isValid = true;

      // Apply category filter
      if (filters.category && product.category !== filters.category) {
        isValid = false;
      }

      // Apply price range filter
      if (
        filters.priceRange &&
        (product.price < filters.priceRange[0] || product.price > filters.priceRange[1])
      ) {
        isValid = false;
      }

      return isValid;
    });

    // Sort products based on criteria
    let sortedProducts = filteredProducts.sort((a, b) => {
      const { key, order } = sortOptions;

      if (!key || !order) {
        throw new Error("Invalid sortOptions key or order.");
      }

      if (order === "asc") {
        return a[key] > b[key] ? 1 : a[key] < b[key] ? -1 : 0;
      } else if (order === "desc") {
        return a[key] < b[key] ? 1 : a[key] > b[key] ? -1 : 0;
      } else {
        throw new Error("Invalid sort order. Use 'asc' or 'desc'.");
      }
    });

    return sortedProducts;
  } catch (error) {
    console.error("Error in filterAndSortProducts:", error.message);
    return [];
  }
}

// Example usage:
const products = [
  { name: "Running Shoes", price: 100, category: "Shoes" },
  { name: "Basketball Shoes", price: 150, category: "Shoes" },
  { name: "Tennis Racket", price: 200, category: "Equipment" },
];

const filters = { category: "Shoes", priceRange: [50, 150] };
const sortOptions = { key: "price", order: "asc" };

const result = filterAndSortProducts(products, filters, sortOptions);
console.log(result);
```
