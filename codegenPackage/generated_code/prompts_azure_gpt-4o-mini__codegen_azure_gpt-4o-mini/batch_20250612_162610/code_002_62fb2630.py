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
 * Filters an array of shoe products to include only "tenis de corrida" from Raimunda Sapatos em Geral.
 * 
 * @param {Array} products - The array of shoe products to filter.
 * @returns {Array} - An array of filtered shoe products that match the criteria.
 * @throws {TypeError} - Throws an error if the input is not an array.
 */
function filterRunningShoes(products) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products');
    }

    // Filter the products to include only "tenis de corrida" from the specified brand
    return products.filter(product => 
        product.name === 'tenis de corrida' && product.brand === 'Raimunda Sapatos em Geral'
    );
}

// Example usage
try {
    const shoeProducts = [
        { name: 'tenis de corrida', brand: 'Raimunda Sapatos em Geral' },
        { name: 'sandalia', brand: 'Raimunda Sapatos em Geral' },
        { name: 'tenis de corrida', brand: 'Outra Marca' },
        { name: 'tenis de corrida', brand: 'Raimunda Sapatos em Geral' }
    ];

    const filteredProducts = filterRunningShoes(shoeProducts);
    console.log(filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
