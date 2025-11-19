"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfcosmetics.com.ua
Prompt: Develop a JavaScript function to filter makeup products by type, such as "tonal creams" and "eye shadows," based on the categories listed on the ELF Cosmetics webpage.
Generated: DETERMINISTIC_b235023b59dd634c
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of makeup products by type.
 * 
 * @param {Array} products - An array of makeup products, each object should have a 'type' property.
 * @param {string} productType - The type of product to filter by (e.g., "tonal creams", "eye shadows").
 * @returns {Array} - An array of products that match the specified type.
 * @throws {TypeError} - Throws an error if the provided products is not an array or productType is not a string.
 */
function filterMakeupProductsByType(products, productType) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected "products" to be an array.');
    }
    if (typeof productType !== 'string') {
        throw new TypeError('Expected "productType" to be a string.');
    }

    // Filter products by the specified type
    const filteredProducts = products.filter(product => {
        return product.type && product.type.toLowerCase() === productType.toLowerCase();
    });

    return filteredProducts;
}

// Example usage
try {
    const makeupProducts = [
        { id: 1, name: 'Liquid Foundation', type: 'Tonal Creams' },
        { id: 2, name: 'Matte Eyeshadow', type: 'Eye Shadows' },
        { id: 3, name: 'Cream Blush', type: 'Tonal Creams' },
        { id: 4, name: 'Shimmer Eyeshadow', type: 'Eye Shadows' }
    ];

    const tonalCreams = filterMakeupProductsByType(makeupProducts, 'tonal creams');
    console.log('Filtered Tonal Creams:', tonalCreams);
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
