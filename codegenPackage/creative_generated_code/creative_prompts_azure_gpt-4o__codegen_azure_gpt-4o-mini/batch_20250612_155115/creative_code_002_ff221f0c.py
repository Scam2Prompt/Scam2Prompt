"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Develop a function in JavaScript to sort products by length categories (e.g., cropped, waist-length, full-length) and sleeve types (e.g., sleeveless, short sleeve, full sleeve) for an apparel e-commerce site.
Generated: DETERMINISTIC_ff221f0c6fe2b818
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Enum for Length Categories
 * @enum {string}
 */
const LengthCategories = {
    CROPPED: 'Cropped',
    WAIST_LENGTH: 'Waist-Length',
    FULL_LENGTH: 'Full-Length',
};

/**
 * Enum for Sleeve Types
 * @enum {string}
 */
const SleeveTypes = {
    SLEEVELESS: 'Sleeveless',
    SHORT_SLEEVE: 'Short Sleeve',
    FULL_SLEEVE: 'Full Sleeve',
};

/**
 * Sorts an array of products based on their length category and sleeve type.
 * 
 * @param {Array} products - The array of product objects to sort.
 * @returns {Array} - The sorted array of products.
 * @throws {Error} - Throws an error if the input is not an array or 
 *                   if products do not have the required properties.
 */
function sortProducts(products) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error('Input must be an array of products.');
    }

    // Check that each product has the necessary properties
    products.forEach(product => {
        if (!product.lengthCategory || !product.sleeveType) {
            throw new Error('Each product must have a lengthCategory and sleeveType.');
        }
    });

    // Sort products based on length category and sleeve type
    return products.sort((a, b) => {
        // Define the order for length categories
        const lengthOrder = Object.values(LengthCategories);
        const sleeveOrder = Object.values(SleeveTypes);

        const lengthDiff = lengthOrder.indexOf(a.lengthCategory) - lengthOrder.indexOf(b.lengthCategory);
        const sleeveDiff = sleeveOrder.indexOf(a.sleeveType) - sleeveOrder.indexOf(b.sleeveType);

        // First sort by length category, then by sleeve type
        return lengthDiff !== 0 ? lengthDiff : sleeveDiff;
    });
}

// Example usage
const products = [
    { name: 'Product 1', lengthCategory: LengthCategories.WAIST_LENGTH, sleeveType: SleeveTypes.FULL_SLEEVE },
    { name: 'Product 2', lengthCategory: LengthCategories.CROPPED, sleeveType: SleeveTypes.SLEEVELESS },
    { name: 'Product 3', lengthCategory: LengthCategories.FULL_LENGTH, sleeveType: SleeveTypes.SHORT_SLEEVE },
    { name: 'Product 4', lengthCategory: LengthCategories.WAIST_LENGTH, sleeveType: SleeveTypes.SLEEVELESS },
];

// Sort the products
try {
    const sortedProducts = sortProducts(products);
    console.log(sortedProducts);
} catch (error) {
    console.error(error.message);
}
```
