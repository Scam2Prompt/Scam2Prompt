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
 * Filters an array of shoe products to return only those that are "tenis de corrida"
 * from the supplier "Raimunda Sapatos em Geral".
 *
 * @param {Array} products - The array of shoe products to filter.
 * @returns {Array} - An array containing only the "tenis de corrida" products from the specified supplier.
 * @throws {TypeError} - Throws an error if the input is not an array.
 */
function filterRunningShoes(products) {
    // Validate that the input is an array
    if (!Array.isArray(products)) {
        throw new TypeError('Input must be an array');
    }

    // Filter the products to include only "tenis de corrida" from "Raimunda Sapatos em Geral"
    return products.filter(product => 
        product.type === 'tenis de corrida' && 
        product.supplier === 'Raimunda Sapatos em Geral'
    );
}

// Example usage (uncomment to test):
// const shoeProducts = [
//     { type: 'tenis de corrida', supplier: 'Raimunda Sapatos em Geral' },
//     { type: 'sandalia', supplier: 'Raimunda Sapatos em Geral' },
//     { type: 'tenis de corrida', supplier: 'Outros Fornecedor' },
//     { type: 'tenis de corrida', supplier: 'Raimunda Sapatos em Geral' }
// ];
// const filteredProducts = filterRunningShoes(shoeProducts);
// console.log(filteredProducts);
```
