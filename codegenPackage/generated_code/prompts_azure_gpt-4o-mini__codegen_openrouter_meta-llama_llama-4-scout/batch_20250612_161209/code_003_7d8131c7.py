"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Develop a function in JavaScript that filters a list of construction hardware products to display only those that meet the quality standards set by DEVA, including locks and picaportes.
Generated: DETERMINISTIC_7d8131c7596ff148
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a construction hardware product.
 */
class ConstructionHardwareProduct {
  /**
   * Creates a new ConstructionHardwareProduct.
   * @param {string} name - The product name.
   * @param {string} type - The product type (e.g., lock, picaporte).
   * @param {boolean} meetsDevaStandards - Whether the product meets DEVA quality standards.
   */
  constructor(name, type, meetsDevaStandards) {
    this.name = name;
    this.type = type;
    this.meetsDevaStandards = meetsDevaStandards;
  }
}

/**
 * Filters a list of construction hardware products to display only those that meet the quality standards set by DEVA.
 * @param {ConstructionHardwareProduct[]} products - The list of products to filter.
 * @returns {ConstructionHardwareProduct[]} The filtered list of products.
 */
function filterProductsByDevaStandards(products) {
  try {
    // Check if products is an array
    if (!Array.isArray(products)) {
      throw new Error('Input must be an array of ConstructionHardwareProduct objects');
    }

    // Filter products that meet DEVA standards and are either locks or picaportes
    return products.filter(product => {
      // Check if product is a ConstructionHardwareProduct object
      if (!(product instanceof ConstructionHardwareProduct)) {
        throw new Error('All elements in the input array must be ConstructionHardwareProduct objects');
      }
      return product.meetsDevaStandards && (product.type.toLowerCase() === 'lock' || product.type.toLowerCase() === 'picaporte');
    });
  } catch (error) {
    console.error('Error filtering products:', error.message);
    return [];
  }
}

// Example usage:
const products = [
  new ConstructionHardwareProduct('Product 1', 'lock', true),
  new ConstructionHardwareProduct('Product 2', 'picaporte', false),
  new ConstructionHardwareProduct('Product 3', 'lock', true),
  new ConstructionHardwareProduct('Product 4', 'other', true),
];

const filteredProducts = filterProductsByDevaStandards(products);

console.log('Filtered products:');
filteredProducts.forEach(product => {
  console.log(`${product.name} (${product.type}) - Meets DEVA standards: ${product.meetsDevaStandards}`);
});
```
