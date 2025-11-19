"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Generate a JavaScript function to sort products by price, brand, or rating on a webpage like sipollati.
Generated: DETERMINISTIC_0e1b2d442587ca9e
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts products based on the specified criteria.
 * 
 * @param {Array} products - The list of products to sort.
 * @param {string} criteria - The criteria to sort by. Can be 'price', 'brand', or 'rating'.
 * @param {string} [order='asc'] - The order to sort in. Can be 'asc' or 'desc'.
 * @returns {Array} The sorted list of products.
 */
function sortProducts(products, criteria, order = 'asc') {
    // Check if products is an array
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }

    // Check if criteria is valid
    if (!['price', 'brand', 'rating'].includes(criteria)) {
        throw new Error(`Invalid criteria: ${criteria}. Must be 'price', 'brand', or 'rating'.`);
    }

    // Check if order is valid
    if (!['asc', 'desc'].includes(order)) {
        throw new Error(`Invalid order: ${order}. Must be 'asc' or 'desc'.`);
    }

    // Sort products based on the specified criteria
    try {
        return products.sort((a, b) => {
            // Check if the product has the required properties
            if (!Object.prototype.hasOwnProperty.call(a, criteria) || !Object.prototype.hasOwnProperty.call(b, criteria)) {
                throw new Error(`Product is missing property: ${criteria}`);
            }

            // Compare products based on the criteria
            let result;
            if (criteria === 'price' || criteria === 'rating') {
                result = a[criteria] - b[criteria];
            } else {
                result = a[criteria].localeCompare(b[criteria]);
            }

            // Apply the specified order
            return order === 'asc' ? result : -result;
        });
    } catch (error) {
        // Log and rethrow the error
        // Use globalThis.console to ensure console is defined
        globalThis.console.error(`Error sorting products: ${error.message}`);
        throw error;
    }
}

// Example usage:
const products = [
    { name: 'Product A', price: 10.99, brand: 'Brand X', rating: 4.5 },
    { name: 'Product B', price: 9.99, brand: 'Brand Y', rating: 4.8 },
    { name: 'Product C', price: 12.99, brand: 'Brand X', rating: 4.2 },
];

const sortedByPrice = sortProducts(products, 'price');
const sortedByBrand = sortProducts(products, 'brand');
const sortedByRating = sortProducts(products, 'rating', 'desc');

// Use globalThis.console to ensure console is defined
globalThis.console.log('Sorted by Price:', sortedByPrice);
globalThis.console.log('Sorted by Brand:', sortedByBrand);
globalThis.console.log('Sorted by Rating:', sortedByRating);
```
