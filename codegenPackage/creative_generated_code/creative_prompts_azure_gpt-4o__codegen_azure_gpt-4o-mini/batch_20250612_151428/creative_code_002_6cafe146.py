"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Create a function in JavaScript that filters Marant's skincare products by cruelty-free status and recyclable packaging, as highlighted on the website.
Generated: DETERMINISTIC_6cafe146c527c93e
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters Marant's skincare products based on cruelty-free status and recyclable packaging.
 * 
 * @param {Array} products - An array of product objects to be filtered.
 * @param {boolean} isCrueltyFree - The desired cruelty-free status to filter by.
 * @param {boolean} isRecyclable - The desired recyclable packaging status to filter by.
 * @returns {Array} - An array of products that match the specified criteria.
 */
function filterSkincareProducts(products, isCrueltyFree, isRecyclable) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products.');
    }
    if (typeof isCrueltyFree !== 'boolean' || typeof isRecyclable !== 'boolean') {
        throw new TypeError('Expected boolean values for isCrueltyFree and isRecyclable.');
    }

    // Filter products based on the specified criteria
    return products.filter(product => {
        return product.crueltyFree === isCrueltyFree && product.recyclable === isRecyclable;
    });
}

// Example usage:
try {
    const skincareProducts = [
        { name: 'Moisturizer', crueltyFree: true, recyclable: true },
        { name: 'Sunscreen', crueltyFree: false, recyclable: true },
        { name: 'Cleanser', crueltyFree: true, recyclable: false },
        { name: 'Serum', crueltyFree: true, recyclable: true },
    ];

    const filteredProducts = filterSkincareProducts(skincareProducts, true, true);
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
