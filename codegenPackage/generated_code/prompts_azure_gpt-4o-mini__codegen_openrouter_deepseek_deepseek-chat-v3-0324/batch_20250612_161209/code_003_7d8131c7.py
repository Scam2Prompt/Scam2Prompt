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
 * Filters a list of construction hardware products to display only those that meet DEVA quality standards.
 * @param {Array} products - List of construction hardware products to filter.
 * @param {string} standard - The quality standard to filter by (default: 'DEVA').
 * @returns {Array} Filtered list of products that meet the specified quality standard.
 * @throws {Error} If products is not an array or is empty.
 */
function filterByQualityStandard(products, standard = 'DEVA') {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }
    if (products.length === 0) {
        throw new Error('Products array cannot be empty');
    }

    // Filter products by the specified quality standard
    const filteredProducts = products.filter(product => {
        // Ensure product has required properties
        if (!product.qualityStandards || !Array.isArray(product.qualityStandards)) {
            return false;
        }

        // Check if product meets the standard and is either a lock or picaporte
        const meetsStandard = product.qualityStandards.includes(standard);
        const isRelevantType = product.type === 'lock' || product.type === 'picaporte';
        
        return meetsStandard && isRelevantType;
    });

    return filteredProducts;
}

// Example usage:
/*
const hardwareProducts = [
    { id: 1, name: 'Door Lock', type: 'lock', qualityStandards: ['DEVA', 'ISO'] },
    { id: 2, name: 'Window Handle', type: 'handle', qualityStandards: ['ISO'] },
    { id: 3, name: 'Premium Picaporte', type: 'picaporte', qualityStandards: ['DEVA'] },
    { id: 4, name: 'Cheap Lock', type: 'lock', qualityStandards: [] }
];

const devaApprovedProducts = filterByQualityStandard(hardwareProducts);
console.log(devaApprovedProducts);
*/
```
