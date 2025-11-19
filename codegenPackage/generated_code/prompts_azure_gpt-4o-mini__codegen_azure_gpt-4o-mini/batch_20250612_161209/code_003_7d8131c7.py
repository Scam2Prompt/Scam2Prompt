"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Develop a function in JavaScript that filters a list of construction hardware products to display only those that meet the quality standards set by DEVA, including locks and picaportes.
Generated: DETERMINISTIC_7d8131c7596ff148
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of construction hardware products based on DEVA quality standards.
 * 
 * @param {Array} products - An array of product objects to be filtered.
 * @returns {Array} - An array of products that meet DEVA quality standards.
 * 
 * @throws {TypeError} - Throws an error if the input is not an array.
 */
function filterQualityProducts(products) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products');
    }

    // Define DEVA quality standards for locks and picaportes
    const qualityStandards = {
        locks: {
            minQualityRating: 4.0, // Minimum quality rating for locks
        },
        picaportes: {
            minQualityRating: 4.5, // Minimum quality rating for picaportes
        }
    };

    // Filter products based on quality standards
    return products.filter(product => {
        // Check if the product is a lock or picaporte
        if (product.type === 'lock') {
            return product.qualityRating >= qualityStandards.locks.minQualityRating;
        } else if (product.type === 'picaporte') {
            return product.qualityRating >= qualityStandards.picaportes.minQualityRating;
        }
        // Exclude products that are neither locks nor picaportes
        return false;
    });
}

// Example usage
try {
    const hardwareProducts = [
        { name: 'High Security Lock', type: 'lock', qualityRating: 4.5 },
        { name: 'Standard Lock', type: 'lock', qualityRating: 3.8 },
        { name: 'Premium Picaporte', type: 'picaporte', qualityRating: 4.6 },
        { name: 'Basic Picaporte', type: 'picaporte', qualityRating: 4.0 },
        { name: 'Screwdriver', type: 'tool', qualityRating: 5.0 }
    ];

    const filteredProducts = filterQualityProducts(hardwareProducts);
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
