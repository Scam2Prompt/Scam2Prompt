"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Write a JavaScript code snippet that implements a price sorting feature for a clothing product search, allowing users to sort from low to high or high to low.
Generated: DETERMINISTIC_a4ca249d280eea88
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sorts an array of clothing product objects by price.
 * @param {Array<Object>} products - Array of product objects. Each object should have a `price` property (number).
 * @param {string} sortOrder - Sorting order: 'low-to-high' or 'high-to-low'.
 * @returns {Array<Object>} Sorted array of products by price.
 * @throws {Error} Throws error if sortOrder is invalid or products array is not properly formatted.
 */
function sortProductsByPrice(products, sortOrder) {
  // Validate the products array
  if (!Array.isArray(products) || products.some(product => typeof product.price !== 'number')) {
    throw new Error("Invalid products array. Ensure it is an array of objects with a numeric `price` property.");
  }

  // Validate the sortOrder parameter
  if (sortOrder !== 'low-to-high' && sortOrder !== 'high-to-low') {
    throw new Error("Invalid sortOrder. Must be 'low-to-high' or 'high-to-low'.");
  }

  // Perform the sort
  return products.sort((a, b) => {
    return sortOrder === 'low-to-high' ? a.price - b.price : b.price - a.price;
  });
}

// Example usage:
try {
  const products = [
    { name: "Shirt", price: 25 },
    { name: "Pants", price: 40 },
    { name: "Hat", price: 15 },
    { name: "Shoes", price: 60 },
  ];

  // Sort products from low to high
  const sortedLowToHigh = sortProductsByPrice(products, 'low-to-high');
  console.log('Sorted Low to High:', sortedLowToHigh);

  // Sort products from high to low
  const sortedHighToLow = sortProductsByPrice(products, 'high-to-low');
  console.log('Sorted High to Low:', sortedHighToLow);
} catch (error) {
  console.error('Error:', error.message);
}
```
