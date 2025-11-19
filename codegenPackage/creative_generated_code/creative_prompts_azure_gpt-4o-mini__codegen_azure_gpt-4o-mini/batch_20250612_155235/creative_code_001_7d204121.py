"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinmod.blogspot.com
Prompt: Write a function in JavaScript that filters an array of shoe products to include only "sandalias coloridas" and "tenis de corrida" based on the Eleiton Sapatos em Geral catalog.
Generated: DETERMINISTIC_7d2041217cbb1301
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of shoe products to include only "sandalias coloridas" and "tenis de corrida".
 *
 * @param {Array<Object>} products - An array of shoe product objects.
 * @returns {Array<Object>} - An array containing only the filtered shoe products.
 * @throws {TypeError} - Throws an error if the input is not an array.
 */
function filterShoeProducts(products) {
    // Validate input to ensure it is an array
    if (!Array.isArray(products)) {
        throw new TypeError('Input must be an array of product objects.');
    }

    // Define the criteria for filtering the products
    const desiredTypes = ['sandalias coloridas', 'tenis de corrida'];

    // Use the filter method to return only the desired products
    return products.filter(product => {
        // Check if the product has a type property and if it matches the desired types
        return product.type && desiredTypes.includes(product.type.toLowerCase());
    });
}

// Example usage:
try {
    const shoeProducts = [
        { id: 1, name: 'Sandalia Colorida', type: 'sandalias coloridas' },
        { id: 2, name: 'Tenis de Corrida', type: 'tenis de corrida' },
        { id: 3, name: 'Bota de Couro', type: 'bota' },
    ];

    const filteredProducts = filterShoeProducts(shoeProducts);
    console.log(filteredProducts); // Output: [{id: 1, name: 'Sandalia Colorida', type: 'sandalias coloridas'}, {id: 2, name: 'Tenis de Corrida', type: 'tenis de corrida'}]
} catch (error) {
    console.error(error.message);
}
```
