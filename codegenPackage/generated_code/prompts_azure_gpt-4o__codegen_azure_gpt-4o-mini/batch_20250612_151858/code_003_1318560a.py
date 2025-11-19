"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: Write a JavaScript function to dynamically filter products by size, color, and brand (e.g., filtering "Ralph Lauren Men's Shirts" by size and color) for an e-commerce platform like brandsoutlet.qa.
Generated: DETERMINISTIC_1318560a4901efd7
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of products based on specified criteria: size, color, and brand.
 * 
 * @param {Array} products - The array of product objects to filter.
 * @param {Object} filters - An object containing the filter criteria.
 * @param {string} filters.size - The size to filter by (e.g., 'M', 'L').
 * @param {string} filters.color - The color to filter by (e.g., 'Red', 'Blue').
 * @param {string} filters.brand - The brand to filter by (e.g., 'Ralph Lauren').
 * @returns {Array} - An array of products that match the filter criteria.
 * 
 * @throws {TypeError} - Throws an error if products is not an array or filters is not an object.
 */
function filterProducts(products, filters) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected products to be an array.');
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new TypeError('Expected filters to be an object.');
    }

    // Destructure filter criteria with default values
    const { size = '', color = '', brand = '' } = filters;

    // Filter products based on the provided criteria
    return products.filter(product => {
        const matchesSize = size ? product.size === size : true;
        const matchesColor = color ? product.color === color : true;
        const matchesBrand = brand ? product.brand === brand : true;

        return matchesSize && matchesColor && matchesBrand;
    });
}

// Example usage
const products = [
    { id: 1, name: "Ralph Lauren Men's Shirt", size: 'M', color: 'Red', brand: 'Ralph Lauren' },
    { id: 2, name: "Ralph Lauren Men's Shirt", size: 'L', color: 'Blue', brand: 'Ralph Lauren' },
    { id: 3, name: "Nike Men's Shirt", size: 'M', color: 'Red', brand: 'Nike' },
    { id: 4, name: "Adidas Men's Shirt", size: 'M', color: 'Green', brand: 'Adidas' },
];

// Filtering example
try {
    const filteredProducts = filterProducts(products, { size: 'M', color: 'Red', brand: 'Ralph Lauren' });
    console.log(filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
