"""
Generated Code Metadata:
========================
Original URL: https://accessthepooc00in.blogspot.com
Prompt: Write a JavaScript function to sort a list of shoe products by category (e.g., sneakers, sandals) and then by price in ascending order.
Generated: DETERMINISTIC_3107ea0608bb0b90
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts a list of shoe products by category and then by price in ascending order.
 * @param {Array} products - Array of shoe product objects. Each object should have 'category' and 'price' properties.
 * @returns {Array} - Sorted array of shoe products.
 */
function sortShoesByCategoryAndPrice(products) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Input must be an array of products.");
  }

  // Ensure all products have the required properties
  products.forEach((product) => {
    if (typeof product.category !== "string" || typeof product.price !== "number") {
      throw new Error("Each product must have a 'category' (string) and 'price' (number).");
    }
  });

  // Sort the products by category and then by price
  return products.sort((a, b) => {
    // Compare categories (alphabetical order)
    if (a.category < b.category) return -1;
    if (a.category > b.category) return 1;

    // If categories are the same, compare prices (ascending order)
    return a.price - b.price;
  });
}

// Example usage:
const shoes = [
  { category: "sneakers", price: 50 },
  { category: "sandals", price: 20 },
  { category: "sneakers", price: 30 },
  { category: "sandals", price: 25 },
];

try {
  const sortedShoes = sortShoesByCategoryAndPrice(shoes);
  console.log(sortedShoes);
} catch (error) {
  console.error("Error:", error.message);
}
```
