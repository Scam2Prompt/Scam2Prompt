"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Develop a function in JavaScript to sort products by length categories (e.g., cropped, waist-length, full-length) and sleeve types (e.g., sleeveless, short sleeve, full sleeve) for an apparel e-commerce site.
Generated: DETERMINISTIC_ff221f0c6fe2b818
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sorts products into categories based on length and sleeve type.
 * 
 * @param {Array} products - Array of product objects. Each product should have `length` and `sleeveType` properties.
 * @returns {Object} An object with categorized products based on length and sleeve type.
 * 
 * Example format for products:
 * [
 *   { id: 1, name: 'Product A', length: 'cropped', sleeveType: 'sleeveless' },
 *   { id: 2, name: 'Product B', length: 'full-length', sleeveType: 'short sleeve' }
 * ]
 * 
 * Example output:
 * {
 *   cropped: {
 *     sleeveless: [ ...products ],
 *     shortSleeve: [ ...products ],
 *     fullSleeve: [ ...products ]
 *   },
 *   waistLength: { ... },
 *   fullLength: { ... }
 * }
 */
function categorizeProductsByLengthAndSleeveType(products) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Input must be an array of products.");
  }

  // Define valid categories
  const lengthCategories = ['cropped', 'waist-length', 'full-length'];
  const sleeveCategories = ['sleeveless', 'short sleeve', 'full sleeve'];

  // Initialize result object
  const categorizedProducts = {};

  // Populate the result object with empty arrays for each category
  lengthCategories.forEach(length => {
    categorizedProducts[length] = {};
    sleeveCategories.forEach(sleeve => {
      categorizedProducts[length][sleeve] = [];
    });
  });

  // Iterate through products and categorize them
  products.forEach(product => {
    const { length, sleeveType } = product;

    // Ensure the product has valid categories
    if (!lengthCategories.includes(length) || !sleeveCategories.includes(sleeveType)) {
      console.warn(`Skipping product with invalid category:`, product);
      return; // Skip invalid products
    }

    // Categorize the product
    categorizedProducts[length][sleeveType].push(product);
  });

  return categorizedProducts;
}

// Example usage
const products = [
  { id: 1, name: 'Cropped Sleeveless Top', length: 'cropped', sleeveType: 'sleeveless' },
  { id: 2, name: 'Full-Length Short Sleeve Shirt', length: 'full-length', sleeveType: 'short sleeve' },
  { id: 3, name: 'Waist-Length Full Sleeve Sweater', length: 'waist-length', sleeveType: 'full sleeve' },
  { id: 4, name: 'Invalid Product', length: 'unknown', sleeveType: 'unknown' }
];

const categorized = categorizeProductsByLengthAndSleeveType(products);
console.log(JSON.stringify(categorized, null, 2));
```
