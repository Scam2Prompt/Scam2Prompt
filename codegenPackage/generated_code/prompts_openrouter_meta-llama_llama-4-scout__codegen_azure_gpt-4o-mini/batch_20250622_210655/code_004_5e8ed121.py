"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Write a JavaScript function to create a dynamic furniture product filter, similar to the one used on Navkar Furniture's website.
Generated: DETERMINISTIC_5e8ed121db96845c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates a dynamic furniture product filter.
 * This function filters an array of furniture products based on selected criteria.
 * 
 * @param {Array} products - An array of furniture product objects.
 * @param {Object} filters - An object containing filter criteria.
 * @returns {Array} - An array of filtered furniture products.
 */
function filterFurnitureProducts(products, filters) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected products to be an array');
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new TypeError('Expected filters to be an object');
    }

    // Filter products based on criteria
    return products.filter(product => {
        // Check for each filter criterion
        for (const key in filters) {
            if (filters[key] && product[key] !== filters[key]) {
                return false; // Exclude product if it doesn't match the filter
            }
        }
        return true; // Include product if it matches all filters
    });
}

// Example usage
const furnitureProducts = [
    { id: 1, type: 'chair', color: 'red', material: 'wood' },
    { id: 2, type: 'table', color: 'brown', material: 'metal' },
    { id: 3, type: 'sofa', color: 'blue', material: 'fabric' },
    { id: 4, type: 'chair', color: 'blue', material: 'plastic' },
];

// Example filter criteria
const filterCriteria = {
    type: 'chair',
    color: 'blue'
};

try {
    const filteredProducts = filterFurnitureProducts(furnitureProducts, filterCriteria);
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
