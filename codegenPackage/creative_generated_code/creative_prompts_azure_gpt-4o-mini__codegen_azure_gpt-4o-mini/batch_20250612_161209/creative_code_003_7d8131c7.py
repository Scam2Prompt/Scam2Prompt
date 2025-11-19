"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deva.cl
Prompt: Develop a function in JavaScript that filters a list of construction hardware products to display only those that meet the quality standards set by DEVA, including locks and picaportes.
Generated: DETERMINISTIC_7d8131c7596ff148
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of construction hardware products based on quality standards set by DEVA.
 * The function specifically looks for products that are either 'lock' or 'picaporte' types
 * and checks if they meet the quality standard.
 *
 * @param {Array} products - The array of construction hardware products to filter.
 * @param {string} qualityStandard - The quality standard to be met (e.g., 'DEVA').
 * @returns {Array} - A new array containing only products that meet the quality standards.
 * @throws {Error} - Throws an error if the input is not an array or if any product is missing required properties.
 */
function filterQualityProducts(products, qualityStandard) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array.');
    }
    
    // Filter products based on type and quality standard
    return products.filter(product => {
        // Validate product structure
        if (!product || typeof product !== 'object' || !product.type || !product.quality) {
            throw new Error('Invalid product structure: Each product must be an object with type and quality properties.');
        }

        // Check if product type is 'lock' or 'picaporte' and meets the quality standard
        return (product.type === 'lock' || product.type === 'picaporte') && product.quality === qualityStandard;
    });
}

// Example usage
const hardwareProducts = [
    { type: 'lock', quality: 'DEVA' },
    { type: 'picaporte', quality: 'DEVA' },
    { type: 'nail', quality: 'DEVA' },
    { type: 'picaporte', quality: 'non-DEVA' },
    { type: 'lock', quality: 'non-DEVA' }
];

try {
    const filteredProducts = filterQualityProducts(hardwareProducts, 'DEVA');
    console.log(filteredProducts); // Outputs the filtered array of quality products
} catch (error) {
    console.error(error.message); // Handle any errors that may occur during filtering
}
```
