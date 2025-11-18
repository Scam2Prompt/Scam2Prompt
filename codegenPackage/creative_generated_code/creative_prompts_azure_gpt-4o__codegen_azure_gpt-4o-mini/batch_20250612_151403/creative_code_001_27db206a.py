"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Create a function in JavaScript that filters a list of promotional products by sustainability criteria, such as "recyclable materials" and "customizable options," based on Grupo ProBolsa's offerings.
Generated: DETERMINISTIC_27db206aba82ff15
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of promotional products based on sustainability criteria.
 * 
 * @param {Array<Object>} products - An array of product objects to filter.
 * @param {Object} criteria - An object containing sustainability criteria.
 * @param {boolean} criteria.recyclable - Whether to filter for recyclable materials.
 * @param {boolean} criteria.customizable - Whether to filter for customizable options.
 * @returns {Array<Object>} - An array of products that meet the sustainability criteria.
 * 
 * @throws {TypeError} - Throws an error if the products array is not an array or if criteria is not an object.
 */
function filterSustainableProducts(products, criteria) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products.');
    }
    
    if (typeof criteria !== 'object' || criteria === null) {
        throw new TypeError('Expected criteria to be an object.');
    }

    // Destructure criteria with default values
    const { recyclable = false, customizable = false } = criteria;

    // Filter products based on criteria
    return products.filter(product => {
        const meetsRecyclableCriteria = recyclable ? product.materials.includes('recyclable') : true;
        const meetsCustomizableCriteria = customizable ? product.customizable : true;

        return meetsRecyclableCriteria && meetsCustomizableCriteria;
    });
}

// Example usage (uncomment to test):
// const promotionalProducts = [
//     { name: 'Eco Pen', materials: ['recyclable'], customizable: true },
//     { name: 'Plastic Bottle', materials: ['non-recyclable'], customizable: false },
//     { name: 'Tote Bag', materials: ['recyclable'], customizable: true },
// ];

// const criteria = { recyclable: true, customizable: false };
// const sustainableProducts = filterSustainableProducts(promotionalProducts, criteria);
// console.log(sustainableProducts);
```
