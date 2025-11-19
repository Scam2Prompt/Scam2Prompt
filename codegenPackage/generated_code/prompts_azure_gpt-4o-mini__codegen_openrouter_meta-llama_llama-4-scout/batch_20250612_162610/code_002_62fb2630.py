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
 * Filters an array of shoe products to only include "tenis de corrida" from Raimunda Sapatos em Geral.
 *
 * @param {Object[]} products - Array of shoe products.
 * @param {string} products[].name - Name of the shoe product.
 * @param {string} products[].brand - Brand of the shoe product.
 * @param {string} products[].type - Type of the shoe product.
 * @returns {Object[]} Filtered array of shoe products.
 */
function filterRunningShoes(products) {
    try {
        // Check if products is an array
        if (!Array.isArray(products)) {
            throw new Error('Input must be an array of objects');
        }

        // Filter products by name and brand
        const filteredProducts = products.filter(product => {
            // Check if product is an object
            if (typeof product !== 'object' || product === null) {
                return false;
            }

            // Check if product has required properties
            if (!('name' in product) || !('brand' in product) || !('type' in product)) {
                return false;
            }

            // Check if product matches the filter criteria
            return product.name.toLowerCase().includes("tenis de corrida") && product.brand.toLowerCase() === "raimunda sapatos em geral";
        });

        return filteredProducts;
    } catch (error) {
        console.error('Error filtering products:', error.message);
        return [];
    }
}

// Example usage:
const products = [
    { name: 'Tenis de Corrida Nike', brand: 'Raimunda Sapatos em Geral', type: 'running' },
    { name: 'Tenis de Futebol Adidas', brand: 'Raimunda Sapatos em Geral', type: 'football' },
    { name: 'Tenis de Corrida Adidas', brand: 'Raimunda Sapatos em Geral', type: 'running' },
    { name: 'Tenis de Corrida Puma', brand: 'Outra Loja', type: 'running' },
];

const filteredProducts = filterRunningShoes(products);
console.log(filteredProducts);
```
