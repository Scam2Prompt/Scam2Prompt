"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapepoocoine.blogspot.com
Prompt: Write a JavaScript function that filters an array of shoe products to only include "tenis de corrida" from Raimunda Sapatos em Geral.
Generated: DETERMINISTIC_62fb26308f61bc46
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of shoe products to only include "tenis de corrida" from "Raimunda Sapatos em Geral".
 *
 * @param {Array} products - Array of shoe products. Each product should be an object with `type` and `brand` properties.
 * @returns {Array} A filtered array containing only "tenis de corrida" from "Raimunda Sapatos em Geral".
 */
function filterRunningShoes(products) {
  // Ensure the input is an array
  if (!Array.isArray(products)) {
    throw new Error('Invalid input: Expected an array of products.');
  }

  // Filter the products based on type and brand
  return products.filter(product => {
    // Validate each product structure
    if (!product || typeof product !== 'object' || !product.type || !product.brand) {
      console.warn('Invalid product skipped:', product); // Log issues but continue processing
      return false;
    }

    // Return whether the product meets the filter criteria
    return product.type === 'tenis de corrida' && product.brand === 'Raimunda Sapatos em Geral';
  });
}

// Example usage:
const products = [
  { type: 'tenis de corrida', brand: 'Raimunda Sapatos em Geral' },
  { type: 'sandalia', brand: 'Raimunda Sapatos em Geral' },
  { type: 'tenis de corrida', brand: 'Outra Marca' },
  { type: 'botas', brand: 'Raimunda Sapatos em Geral' }
];

const filteredProducts = filterRunningShoes(products);
console.log(filteredProducts); // Output: [{ type: 'tenis de corrida', brand: 'Raimunda Sapatos em Geral' }]
```
