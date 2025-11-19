"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Write a JavaScript function that filters men's sandals based on color from the product listings on Emily Sapatos em Geral.
Generated: DETERMINISTIC_623bc8de43bb53c1
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters men's sandals from a list of product listings based on the specified color.
 * 
 * @param {Array<Object>} products - An array of product objects.
 * @param {string} color - The color to filter the men's sandals by.
 * @returns {Array<Object>} - An array of men's sandals that match the specified color.
 * 
 * @throws {TypeError} - Throws an error if the products array is not an array or if color is not a string.
 */
function filterMensSandalsByColor(products, color) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products.');
    }
    if (typeof color !== 'string') {
        throw new TypeError('Expected color to be a string.');
    }

    // Filter for men's sandals that match the specified color
    return products.filter(product => {
        return product.category === 'men\'s sandals' && product.color.toLowerCase() === color.toLowerCase();
    });
}

// Example usage
try {
    const productList = [
        { id: 1, name: 'Comfort Sandal', category: 'men\'s sandals', color: 'black' },
        { id: 2, name: 'Sport Sandal', category: 'men\'s sandals', color: 'blue' },
        { id: 3, name: 'Casual Sandal', category: 'women\'s sandals', color: 'black' },
        { id: 4, name: 'Beach Sandal', category: 'men\'s sandals', color: 'blue' },
    ];

    const filteredSandals = filterMensSandalsByColor(productList, 'blue');
    console.log(filteredSandals);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
