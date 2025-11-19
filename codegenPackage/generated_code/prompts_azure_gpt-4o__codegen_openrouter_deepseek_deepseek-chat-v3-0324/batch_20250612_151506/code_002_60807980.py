"""
Generated Code Metadata:
========================
Original URL: https://www.meje.cc
Prompt: Create a JavaScript function to filter bathroom sinks by type, such as "Undermount Bathroom Sink" and "Vanity Top Sink," based on the MEJE product categories.
Generated: DETERMINISTIC_608079803c0d2e4e
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters bathroom sinks by type based on MEJE product categories.
 * @param {Array} products - Array of product objects to filter.
 * @param {string} sinkType - The type of sink to filter by (e.g., "Undermount Bathroom Sink", "Vanity Top Sink").
 * @returns {Array} Filtered array of products matching the specified sink type.
 * @throws {Error} If products is not an array or sinkType is not a string.
 */
function filterBathroomSinks(products, sinkType) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }
    if (typeof sinkType !== 'string') {
        throw new Error('Sink type must be a string');
    }

    // Normalize the sink type for case-insensitive comparison
    const normalizedSinkType = sinkType.trim().toLowerCase();

    // Filter products by category
    return products.filter(product => {
        // Ensure product has a category property
        if (!product || !product.category) {
            return false;
        }

        // Normalize product category for comparison
        const normalizedCategory = product.category.toLowerCase();
        return normalizedCategory.includes(normalizedSinkType);
    });
}

// Example usage:
/*
const products = [
    { id: 1, name: "Sink A", category: "Undermount Bathroom Sink" },
    { id: 2, name: "Sink B", category: "Vanity Top Sink" },
    { id: 3, name: "Sink C", category: "Pedestal Sink" }
];

const undermountSinks = filterBathroomSinks(products, "Undermount Bathroom Sink");
console.log(undermountSinks); // Outputs array with Sink A

const vanitySinks = filterBathroomSinks(products, "Vanity Top Sink");
console.log(vanitySinks); // Outputs array with Sink B
*/
```
