"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Create a JavaScript function to filter audio products on SmartPrice KE by category, such as headphones and speakers.
Generated: DETERMINISTIC_a630cf5e8868a746
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters audio products from a given array based on the specified category.
 * 
 * @param {Array<Object>} products - The array of audio products to filter.
 * @param {string} category - The category to filter the products by, e.g., 'headphones' or 'speakers'.
 * @returns {Array<Object>} - An array of products that belong to the specified category.
 * @throws {Error} - Throws an error if the products array is not an array or if the category is not a string.
 */
function filterAudioProductsByCategory(products, category) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new Error('The products parameter must be an array.');
    }
    if (typeof category !== 'string') {
        throw new Error('The category parameter must be a string.');
    }

    // Filter products by the specified category
    const filteredProducts = products.filter(product => product.category === category);

    return filteredProducts;
}

// Example usage:
try {
    const audioProducts = [
        { id: 1, name: 'Wireless Headphones', category: 'headphones' },
        { id: 2, name: 'Bluetooth Speaker', category: 'speakers' },
        { id: 3, name: 'Noise Cancelling Headphones', category: 'headphones' }
    ];

    const categoryToFilter = 'headphones';
    const filteredHeadphones = filterAudioProductsByCategory(audioProducts, categoryToFilter);
    console.log(filteredHeadphones);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
