"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: Create a function in JavaScript that filters Marant's skincare products by cruelty-free status and recyclable packaging, as highlighted on the website.
Generated: DETERMINISTIC_6cafe146c527c93e
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters Marant's skincare products based on cruelty-free status and recyclable packaging.
 * 
 * @param {Array} products - An array of product objects to filter.
 * @param {boolean} isCrueltyFree - The desired cruelty-free status to filter by.
 * @param {boolean} isRecyclable - The desired recyclable packaging status to filter by.
 * @returns {Array} - An array of products that match the specified criteria.
 * @throws {TypeError} - Throws an error if the input is not an array or if the product objects are malformed.
 */
function filterSkincareProducts(products, isCrueltyFree, isRecyclable) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products.');
    }

    // Filter products based on the specified criteria
    return products.filter(product => {
        // Validate product structure
        if (typeof product !== 'object' || product === null) {
            throw new TypeError('Each product must be a non-null object.');
        }

        const { crueltyFree, recyclable } = product;

        // Check if the product has the required properties
        if (typeof crueltyFree !== 'boolean' || typeof recyclable !== 'boolean') {
            throw new TypeError('Product must have boolean properties: crueltyFree and recyclable.');
        }

        // Return true if the product matches the criteria
        return crueltyFree === isCrueltyFree && recyclable === isRecyclable;
    });
}

// Example usage
const skincareProducts = [
    { name: 'Moisturizer', crueltyFree: true, recyclable: true },
    { name: 'Sunscreen', crueltyFree: false, recyclable: true },
    { name: 'Cleanser', crueltyFree: true, recyclable: false },
    { name: 'Serum', crueltyFree: true, recyclable: true }
];

try {
    const filteredProducts = filterSkincareProducts(skincareProducts, true, true);
    console.log(filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
