"""
Generated Code Metadata:
========================
Original URL: https://gvika.in
Prompt: "Create a JavaScript function to implement a product filtering system based on categories like 'Home Decor' and 'Customized Gift' as seen on Gvika."
Generated: DETERMINISTIC_ae6062377824d2af
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of products based on the selected category.
 * 
 * @param {Array} products - The array of product objects to filter.
 * @param {string} category - The category to filter products by.
 * @returns {Array} - An array of products that belong to the specified category.
 * @throws {Error} - Throws an error if the products array is not an array or if the category is not a string.
 */
function filterProductsByCategory(products, category) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new Error('The products parameter must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('The category parameter must be a string.');
    }

    // Filter products based on the specified category
    return products.filter(product => product.category === category);
}

// Example usage
const products = [
    { id: 1, name: 'Wall Art', category: 'Home Decor' },
    { id: 2, name: 'Customized Mug', category: 'Customized Gift' },
    { id: 3, name: 'Throw Pillow', category: 'Home Decor' },
    { id: 4, name: 'Personalized Keychain', category: 'Customized Gift' }
];

try {
    const filteredProducts = filterProductsByCategory(products, 'Home Decor');
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
