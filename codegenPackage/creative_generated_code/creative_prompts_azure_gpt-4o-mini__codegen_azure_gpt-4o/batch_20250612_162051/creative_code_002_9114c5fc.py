"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Create a JavaScript function that filters products by price and popularity, similar to the sorting options available on Rope-Bunny.de.
Generated: DETERMINISTIC_9114c5fcd6f63f3a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and sorts products based on price and popularity.
 * 
 * @param {Array} products - Array of product objects. Each product should have `price` and `popularity` properties.
 * @param {Object} filterOptions - Options for filtering and sorting.
 * @param {number} filterOptions.minPrice - Minimum price for filtering (inclusive).
 * @param {number} filterOptions.maxPrice - Maximum price for filtering (inclusive).
 * @param {string} filterOptions.sortBy - Sorting criteria: 'price' or 'popularity'.
 * @param {string} filterOptions.order - Sort order: 'asc' for ascending or 'desc' for descending.
 * @returns {Array} - Filtered and sorted array of products.
 */
function filterAndSortProducts(products, filterOptions) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("The products parameter must be an array.");
  }

  if (!filterOptions || typeof filterOptions !== "object") {
    throw new Error("The filterOptions parameter must be an object.");
  }

  const { minPrice, maxPrice, sortBy, order } = filterOptions;

  if (typeof minPrice !== "number" || typeof maxPrice !== "number") {
    throw new Error("minPrice and maxPrice must be numbers.");
  }

  if (!['price', 'popularity'].includes(sortBy)) {
    throw new Error("sortBy must be either 'price' or 'popularity'.");
  }

  if (!['asc', 'desc'].includes(order)) {
    throw new Error("order must be either 'asc' or 'desc'.");
  }

  // Filter products by price range
  const filteredProducts = products.filter(product => {
    return product.price >= minPrice && product.price <= maxPrice;
  });

  // Sort products by the specified criteria and order
  const sortedProducts = filteredProducts.sort((a, b) => {
    if (sortBy === 'price') {
      return order === 'asc' ? a.price - b.price : b.price - a.price;
    } else if (sortBy === 'popularity') {
      return order === 'asc' ? a.popularity - b.popularity : b.popularity - a.popularity;
    }
  });

  return sortedProducts;
}

// Example usage:
const products = [
  { name: "Product A", price: 50, popularity: 70 },
  { name: "Product B", price: 25, popularity: 90 },
  { name: "Product C", price: 75, popularity: 50 },
  { name: "Product D", price: 40, popularity: 80 },
];

const filterOptions = {
  minPrice: 30,
  maxPrice: 70,
  sortBy: "price",
  order: "asc",
};

const result = filterAndSortProducts(products, filterOptions);
console.log(result);
```
