"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Generate a JavaScript function to sort products by price, brand, or rating on a webpage like sipollati.
Generated: DETERMINISTIC_0e1b2d442587ca9e
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts an array of products based on the specified criteria.
 * @param {Array} products - Array of product objects to be sorted. Each product should have `price`, `brand`, and `rating` properties.
 * @param {string} criteria - The criteria to sort by. Can be 'price', 'brand', or 'rating'.
 * @param {string} order - The order of sorting. Can be 'asc' for ascending or 'desc' for descending.
 * @returns {Array} - A new array of products sorted based on the specified criteria and order.
 * @throws {Error} - Throws an error if the criteria or order is invalid.
 */
function sortProducts(products, criteria, order) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: 'products' must be an array.");
  }
  if (!['price', 'brand', 'rating'].includes(criteria)) {
    throw new Error("Invalid criteria: Must be 'price', 'brand', or 'rating'.");
  }
  if (!['asc', 'desc'].includes(order)) {
    throw new Error("Invalid order: Must be 'asc' or 'desc'.");
  }

  // Perform sorting
  return products.slice().sort((a, b) => {
    let comparison = 0;

    // Compare based on criteria
    if (criteria === 'price' || criteria === 'rating') {
      comparison = a[criteria] - b[criteria];
    } else if (criteria === 'brand') {
      comparison = a[criteria].localeCompare(b[criteria]);
    }

    // Adjust for order
    return order === 'asc' ? comparison : -comparison;
  });
}

// Example usage:
// const products = [
//   { price: 100, brand: 'BrandA', rating: 4.5 },
//   { price: 200, brand: 'BrandB', rating: 4.8 },
//   { price: 150, brand: 'BrandC', rating: 4.2 },
// ];
// const sortedProducts = sortProducts(products, 'price', 'asc');
// console.log(sortedProducts);
```
