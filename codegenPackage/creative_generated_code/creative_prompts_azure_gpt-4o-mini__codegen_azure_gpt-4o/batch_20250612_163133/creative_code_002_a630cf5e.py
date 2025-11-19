"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Create a JavaScript function to filter audio products on SmartPrice KE by category, such as headphones and speakers.
Generated: DETERMINISTIC_a630cf5e8868a746
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters audio products by category.
 *
 * @param {Array<Object>} products - List of audio products to filter. Each product must have a `category` property.
 * @param {string} category - The category to filter by (e.g., 'headphones', 'speakers').
 * @returns {Array<Object>} - Filtered list of products that match the specified category.
 *
 * @throws {TypeError} If `products` is not an array or `category` is not a string.
 */
function filterAudioProductsByCategory(products, category) {
  // Validate input types
  if (!Array.isArray(products)) {
    throw new TypeError('The "products" parameter must be an array.');
  }
  
  if (typeof category !== 'string') {
    throw new TypeError('The "category" parameter must be a string.');
  }

  // Filter products by the specified category
  const filteredProducts = products.filter(product => {
    // Ensure each product is a valid object
    if (typeof product !== 'object' || product === null) {
      console.warn('Skipping invalid product:', product);
      return false;
    }

    // Check if the product's category matches the filter category
    return product.category === category;
  });

  return filteredProducts;
}

// Example usage:
// const products = [
//   { id: 1, name: 'Super Bass Headphones', category: 'headphones' },
//   { id: 2, name: 'Surround Sound Speaker', category: 'speakers' },
//   { id: 3, name: 'Wireless Earbuds', category: 'headphones' },
//   { id: 4, name: 'Portable Bluetooth Speaker', category: 'speakers' }
// ];

// const headphones = filterAudioProductsByCategory(products, 'headphones');
// console.log(headphones);
```
