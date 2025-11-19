"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Create a function in JavaScript that filters a list of promotional products by sustainability criteria, such as "recyclable materials" and "customizable options," based on Grupo ProBolsa's offerings.
Generated: DETERMINISTIC_27db206aba82ff15
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters a list of promotional products based on sustainability criteria.
 * 
 * @param {Array} products - An array of product objects to filter.
 * @param {Object} criteria - An object containing sustainability criteria.
 * @param {boolean} criteria.recyclable - Whether to include products made from recyclable materials.
 * @param {boolean} criteria.customizable - Whether to include customizable products.
 * @returns {Array} - An array of products that meet the specified sustainability criteria.
 * @throws {TypeError} - Throws an error if the input products is not an array or criteria is not an object.
 */
function filterSustainableProducts(products, criteria) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected products to be an array.');
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new TypeError('Expected criteria to be an object.');
    }

    // Filter products based on criteria
    return products.filter(product => {
        const meetsRecyclableCriteria = criteria.recyclable ? product.isRecyclable : true;
        const meetsCustomizableCriteria = criteria.customizable ? product.isCustomizable : true;

        return meetsRecyclableCriteria && meetsCustomizableCriteria;
    });
}

// Example usage
const promotionalProducts = [
    { name: 'Eco-Friendly Tote Bag', isRecyclable: true, isCustomizable: true },
    { name: 'Plastic Water Bottle', isRecyclable: false, isCustomizable: false },
    { name: 'Bamboo Pen', isRecyclable: true, isCustomizable: false },
    { name: 'Customizable Notebook', isRecyclable: false, isCustomizable: true }
];

const criteria = {
    recyclable: true,
    customizable: false
};

try {
    const sustainableProducts = filterSustainableProducts(promotionalProducts, criteria);
    console.log('Filtered Sustainable Products:', sustainableProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
