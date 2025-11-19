"""
Generated Code Metadata:
========================
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: "Write a code snippet in JavaScript to implement a sorting feature for products on an e-commerce site, similar to the sorting options (popularity, latest, price: low to high, price: high to low) available on the Arts & Culture Alliance online shop."
Generated: DETERMINISTIC_48a3543843dd3d82
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to sort products based on different criteria.
 * @param {Array} products - Array of product objects.
 * @param {String} sortBy - Sorting criteria ('popularity', 'latest', 'priceLowToHigh', 'priceHighToLow').
 * @returns {Array} - Sorted array of products.
 */
function sortProducts(products, sortBy) {
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: 'products' must be an array.");
  }

  if (typeof sortBy !== 'string') {
    throw new Error("Invalid input: 'sortBy' must be a string.");
  }

  switch (sortBy) {
    case 'popularity':
      // Sort by popularity (assuming higher popularity value is better)
      return products.sort((a, b) => b.popularity - a.popularity);

    case 'latest':
      // Sort by latest (assuming 'dateAdded' is a Date object or ISO string)
      return products.sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));

    case 'priceLowToHigh':
      // Sort by price: low to high
      return products.sort((a, b) => a.price - b.price);

    case 'priceHighToLow':
      // Sort by price: high to low
      return products.sort((a, b) => b.price - a.price);

    default:
      throw new Error("Invalid sorting criteria. Valid options are: 'popularity', 'latest', 'priceLowToHigh', 'priceHighToLow'.");
  }
}

// Example usage:
const products = [
  { name: 'Product A', price: 30, popularity: 80, dateAdded: '2023-10-01' },
  { name: 'Product B', price: 20, popularity: 95, dateAdded: '2023-10-05' },
  { name: 'Product C', price: 50, popularity: 70, dateAdded: '2023-09-25' },
];

try {
  const sortedByPriceLowToHigh = sortProducts(products, 'priceLowToHigh');
  console.log('Sorted by Price (Low to High):', sortedByPriceLowToHigh);

  const sortedByPopularity = sortProducts(products, 'popularity');
  console.log('Sorted by Popularity:', sortedByPopularity);
} catch (error) {
  console.error('Error:', error.message);
}
```
