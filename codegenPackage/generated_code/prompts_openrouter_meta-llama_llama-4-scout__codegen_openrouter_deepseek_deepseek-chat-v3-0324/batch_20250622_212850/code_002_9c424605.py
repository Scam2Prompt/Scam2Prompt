"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: "Generate a JavaScript function to filter tire products by size and type on the Itamarati Online website, using the product specifications listed on the page."
Generated: DETERMINISTIC_9c424605ea160466
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters tire products by size and type based on product specifications.
 * @param {Array} products - Array of tire product objects to filter.
 * @param {Object} filters - Filter criteria containing size and type.
 * @param {string} [filters.size] - Optional tire size to filter by (e.g., "205/55R16").
 * @param {string} [filters.type] - Optional tire type to filter by (e.g., "Summer", "Winter", "All-Season").
 * @returns {Array} Filtered array of tire products matching the criteria.
 * @throws {Error} If products parameter is not an array or filters is not an object.
 */
function filterTires(products, filters) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Products must be an array");
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new Error("Filters must be an object");
    }

    // Extract filter values
    const { size, type } = filters;

    // Return all products if no filters are provided
    if (!size && !type) {
        return products;
    }

    // Filter products based on criteria
    return products.filter(product => {
        // Check if product has required specifications
        if (!product.specifications) {
            return false;
        }

        let matchesSize = true;
        let matchesType = true;

        // Check size filter if provided
        if (size) {
            matchesSize = product.specifications.size === size;
        }

        // Check type filter if provided
        if (type) {
            matchesType = product.specifications.type === type;
        }

        return matchesSize && matchesType;
    });
}

// Example usage:
/*
const tireProducts = [
    {
        id: 1,
        name: "Premium Tire",
        specifications: {
            size: "205/55R16",
            type: "Summer",
            loadIndex: 91,
            speedRating: "V"
        }
    },
    {
        id: 2,
        name: "All-Weather Tire",
        specifications: {
            size: "215/60R17",
            type: "All-Season",
            loadIndex: 95,
            speedRating: "H"
        }
    }
];

const filteredTires = filterTires(tireProducts, { size: "205/55R16", type: "Summer" });
console.log(filteredTires);
*/
```
