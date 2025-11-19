"""
Generated Code Metadata:
========================
Original URL: https://poocoinmod.blogspot.com
Prompt: Write a function in JavaScript that filters an array of shoe products to include only "sandalias coloridas" and "tenis de corrida" based on the Eleiton Sapatos em Geral catalog.
Generated: DETERMINISTIC_7d2041217cbb1301
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of shoe products to include only "sandalias coloridas" and "tenis de corrida".
 *
 * @param {Object[]} products - Array of shoe products.
 * @param {string} products[].name - Name of the shoe product.
 * @return {Object[]} Filtered array of shoe products.
 */
function filterShoeProducts(products) {
    // Check if products is an array
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }

    // Define the allowed product names
    const allowedProductNames = ['sandalias coloridas', 'tenis de corrida'];

    // Use the filter method to create a new array with only the allowed products
    return products.filter(product => {
        // Check if product has a name property
        if (!Object.prototype.hasOwnProperty.call(product, 'name')) {
            return false;
        }

        // Check if product name is in the allowed product names
        return allowedProductNames.includes(product.name.toLowerCase());
    });
}

// Example usage:
const products = [
    { id: 1, name: 'Sandalias Coloridas' },
    { id: 2, name: 'Tenis de Corrida' },
    { id: 3, name: 'Bolsa de Couro' },
    { id: 4, name: 'Sandalias Coloridas' },
    { id: 5, name: 'Chinelo' },
];

try {
    const filteredProducts = filterShoeProducts(products);
    // Use globalThis.console to make sure console is defined
    globalThis.console.log(filteredProducts);
} catch (error) {
    globalThis.console.error(error.message);
}
```
