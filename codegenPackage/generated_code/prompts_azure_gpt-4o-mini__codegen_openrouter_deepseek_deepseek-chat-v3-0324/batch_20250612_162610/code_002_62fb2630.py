"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Write a JavaScript function that filters an array of shoe products to only include "tenis de corrida" from Raimunda Sapatos em Geral.
Generated: DETERMINISTIC_62fb26308f61bc46
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of shoe products to only include "tenis de corrida" from "Raimunda Sapatos em Geral".
 * @param {Array} products - Array of shoe product objects
 * @returns {Array} Filtered array containing only matching products
 * @throws {Error} If products is not an array
 */
function filterRunningShoes(products) {
    if (!Array.isArray(products)) {
        throw new Error('Input must be an array of products');
    }

    return products.filter(product => {
        // Check if product has required properties and matches criteria
        return product.type && product.brand && 
               product.type.toLowerCase() === 'tenis de corrida' && 
               product.brand.toLowerCase() === 'raimunda sapatos em geral';
    });
}

// Example usage:
/*
const products = [
    { type: 'Tenis de Corrida', brand: 'Raimunda Sapatos em Geral', price: 199.99 },
    { type: 'Sapato Social', brand: 'Raimunda Sapatos em Geral', price: 249.99 },
    { type: 'Tenis de Corrida', brand: 'Outra Marca', price: 179.99 }
];

try {
    const filteredProducts = filterRunningShoes(products);
    console.log(filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
*/
```
