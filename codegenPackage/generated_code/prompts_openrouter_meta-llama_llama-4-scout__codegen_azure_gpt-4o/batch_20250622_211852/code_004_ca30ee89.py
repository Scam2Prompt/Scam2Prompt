"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Write a JavaScript code snippet to implement a product sorting feature, similar to the one on Dandaloja's collection page, allowing users to sort items by price, name, or popularity.
Generated: DETERMINISTIC_ca30ee890c435b43
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Sorting Feature
 * Allows users to sort a list of products by price, name, or popularity.
 * 
 * Usage:
 * Call the `sortProducts` function with the desired sort criteria ('price', 'name', or 'popularity').
 * Example: sortProducts(products, 'price');
 */

// Sample product data
const products = [
  { name: "Product A", price: 30, popularity: 85 },
  { name: "Product B", price: 20, popularity: 95 },
  { name: "Product C", price: 50, popularity: 75 },
  { name: "Product D", price: 40, popularity: 90 },
];

/**
 * Sorts an array of products based on the specified criteria.
 * @param {Array} products - Array of product objects to be sorted.
 * @param {string} criteria - Sorting criteria ('price', 'name', or 'popularity').
 * @returns {Array} - Sorted array of products.
 */
function sortProducts(products, criteria) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: products must be an array.");
  }
  if (!['price', 'name', 'popularity'].includes(criteria)) {
    throw new Error("Invalid criteria: must be 'price', 'name', or 'popularity'.");
  }

  // Perform sorting based on criteria
  return products.slice().sort((a, b) => {
    if (criteria === 'price' || criteria === 'popularity') {
      // Numeric sorting
      return a[criteria] - b[criteria];
    } else if (criteria === 'name') {
      // Alphabetical sorting
      return a[criteria].localeCompare(b[criteria]);
    }
  });
}

// Example usage
try {
  console.log("Sorted by price:", sortProducts(products, 'price'));
  console.log("Sorted by name:", sortProducts(products, 'name'));
  console.log("Sorted by popularity:", sortProducts(products, 'popularity'));
} catch (error) {
  console.error("Error:", error.message);
}
```
