"""
Generated Code Metadata:
========================
Original URL: https://poocoinswasopnet.blogspot.com
Prompt: Create a JavaScript function to filter shoe products by type (e.g., sapatos femininos, sandalias masculinas) and color.
Generated: DETERMINISTIC_9e8dc12a31a1b363
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of shoe products based on type and color.
 * 
 * @param {Array} products - The array of shoe products to filter.
 * @param {string} type - The type of shoe to filter by (e.g., "sapatos femininos", "sandalias masculinas").
 * @param {string} color - The color of the shoe to filter by.
 * @returns {Array} - An array of filtered shoe products.
 * @throws {Error} - Throws an error if the input is not valid.
 */
function filterShoeProducts(products, type, color) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: products must be an array.");
    }
    if (typeof type !== 'string' || typeof color !== 'string') {
        throw new Error("Invalid input: type and color must be strings.");
    }

    // Filter products based on type and color
    return products.filter(product => {
        return product.type === type && product.color === color;
    });
}

// Example usage
const shoeProducts = [
    { id: 1, type: "sapatos femininos", color: "vermelho" },
    { id: 2, type: "sandalias masculinas", color: "azul" },
    { id: 3, type: "sapatos femininos", color: "azul" },
    { id: 4, type: "sandalias masculinas", color: "vermelho" },
];

// Filtering example
try {
    const filteredProducts = filterShoeProducts(shoeProducts, "sapatos femininos", "azul");
    console.log(filteredProducts); // Output: [{ id: 3, type: "sapatos femininos", color: "azul" }]
} catch (error) {
    console.error(error.message);
}
```
