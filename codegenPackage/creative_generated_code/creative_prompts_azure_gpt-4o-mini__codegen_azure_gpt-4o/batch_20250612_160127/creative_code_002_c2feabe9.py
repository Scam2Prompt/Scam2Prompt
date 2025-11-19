"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonswallet.top
Prompt: Create a JavaScript function that filters track cycling products by category, such as "Track Bikes" or "Track Helmets," as seen on the Velodrome Shop website.
Generated: DETERMINISTIC_c2feabe90882acaf
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters track cycling products by category.
 * @param {Array<Object>} products - Array of product objects. Each product should have a `name` and `category`.
 * @param {string} category - The category by which to filter the products (e.g., "Track Bikes", "Track Helmets").
 * @returns {Array<Object>} - Filtered array of products belonging to the specified category.
 */
function filterTrackCyclingProducts(products, category) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new TypeError('The "products" parameter must be an array.');
  }
  if (typeof category !== 'string') {
    throw new TypeError('The "category" parameter must be a string.');
  }

  // Filter products by category
  const filteredProducts = products.filter((product) => {
    // Ensure each product has a valid structure
    if (!product || typeof product !== 'object' || !product.category) {
      console.warn('Skipping invalid product:', product);
      return false;
    }

    return product.category === category;
  });

  return filteredProducts;
}

// Example usage:

// Sample product data
const products = [
  { name: 'Velodrome Track Bike 1', category: 'Track Bikes' },
  { name: 'Velodrome Helmet Pro', category: 'Track Helmets' },
  { name: 'Road Bike 3000', category: 'Road Bikes' },
  { name: 'Racing Gloves', category: 'Accessories' },
  { name: 'Velodrome Track Bike 2', category: 'Track Bikes' },
];

// Filtering track bikes
const trackBikes = filterTrackCyclingProducts(products, 'Track Bikes');
console.log('Filtered Track Bikes:', trackBikes);

// Filtering track helmets
const trackHelmets = filterTrackCyclingProducts(products, 'Track Helmets');
console.log('Filtered Track Helmets:', trackHelmets);
```
