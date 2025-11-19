"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Create a JavaScript function that filters products by price and popularity, similar to the sorting options available on Rope-Bunny.de.
Generated: DETERMINISTIC_9114c5fcd6f63f3a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and sorts an array of products based on price and popularity.
 *
 * @param {Array} products - The array of product objects to filter.
 * @param {number} maxPrice - The maximum price to filter products by.
 * @param {boolean} sortByPopularity - If true, sorts products by popularity; if false, sorts by price.
 * @returns {Array} - The filtered and sorted array of products.
 * @throws {TypeError} - Throws an error if the input is not an array or if products do not have the expected properties.
 */
function filterAndSortProducts(products, maxPrice, sortByPopularity) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('The first argument must be an array of products.');
    }
    if (typeof maxPrice !== 'number') {
        throw new TypeError('The second argument must be a number representing max price.');
    }
    if (typeof sortByPopularity !== 'boolean') {
        throw new TypeError('The third argument must be a boolean indicating sorting preference.');
    }

    // Filter products by maximum price
    const filteredProducts = products.filter(product => {
        // Ensure product has a price property and it's a valid number
        if (typeof product.price !== 'number') {
            throw new TypeError('Each product must have a price property of type number.');
        }
        return product.price <= maxPrice;
    });

    // Sort products based on the specified criteria
    const sortedProducts = filteredProducts.sort((a, b) => {
        if (sortByPopularity) {
            // Sort by popularity (higher is better)
            return b.popularity - a.popularity;
        } else {
            // Sort by price (lower is better)
            return a.price - b.price;
        }
    });

    return sortedProducts;
}

// Example usage
const products = [
    { id: 1, name: 'Product A', price: 20, popularity: 5 },
    { id: 2, name: 'Product B', price: 15, popularity: 3 },
    { id: 3, name: 'Product C', price: 30, popularity: 8 },
    { id: 4, name: 'Product D', price: 10, popularity: 4 },
];

try {
    const result = filterAndSortProducts(products, 25, true);
    console.log(result);
} catch (error) {
    console.error('Error filtering/sorting products:', error.message);
}
```
