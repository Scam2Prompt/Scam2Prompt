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
 * Filters a list of promotional products by sustainability criteria.
 * 
 * @param {Array<Object>} products - Array of product objects to filter. Each product object should include properties like `name`, `materials`, and `options`.
 * @param {Object} criteria - Sustainability criteria with keys `recyclableMaterials` and `customizableOptions` (boolean values).
 * @returns {Array<Object>} - Array of products that meet the sustainability criteria.
 */
function filterSustainableProducts(products, criteria) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new TypeError("Expected 'products' to be an array.");
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new TypeError("Expected 'criteria' to be a non-null object.");
    }

    // Destructure criteria and set defaults
    const { recyclableMaterials = false, customizableOptions = false } = criteria;

    // Filter products based on the criteria
    return products.filter(product => {
        if (typeof product !== 'object' || product === null) {
            console.warn("Skipping invalid product:", product);
            return false; // Skip invalid product entries
        }

        const { materials, options } = product;

        // Ensure properties exist and are valid
        const isRecyclable = recyclableMaterials ? Array.isArray(materials) && materials.includes("recyclable") : true;
        const isCustomizable = customizableOptions ? Array.isArray(options) && options.includes("customizable") : true;

        return isRecyclable && isCustomizable;
    });
}

// Example usage
const products = [
    { name: "Eco Tote Bag", materials: ["recyclable", "cotton"], options: ["customizable", "logo print"] },
    { name: "Plastic Bottle", materials: ["plastic"], options: ["customizable"] },
    { name: "Paper Notebook", materials: ["paper", "recyclable"], options: [] },
];

const criteria = {
    recyclableMaterials: true,
    customizableOptions: true
};

const sustainableProducts = filterSustainableProducts(products, criteria);
console.log(sustainableProducts); // Output: [ { name: 'Eco Tote Bag', materials: [ 'recyclable', 'cotton' ], options: [ 'customizable', 'logo print' ] } ]
```
