"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Write a JavaScript function to filter clothing items by size and price from an online store's product list, similar to the features on Danda Loja.
Generated: DETERMINISTIC_3f492f719b425657
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters clothing items by size and price from a product list.
 *
 * @param {Object[]} products - The list of products.
 * @param {string[]} sizes - The sizes to filter by.
 * @param {number} minPrice - The minimum price to filter by.
 * @param {number} maxPrice - The maximum price to filter by.
 * @returns {Object[]} The filtered list of products.
 */
function filterProducts(products, sizes, minPrice, maxPrice) {
    // Check if products is an array
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }

    // Check if sizes is an array
    if (!Array.isArray(sizes)) {
        throw new Error('Sizes must be an array');
    }

    // Check if minPrice and maxPrice are numbers
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Min price and max price must be numbers');
    }

    // Check if minPrice is less than or equal to maxPrice
    if (minPrice > maxPrice) {
        throw new Error('Min price must be less than or equal to max price');
    }

    // Filter products by size and price
    return products.filter(product => {
        // Check if product has size and price properties
        if (!product.size || !product.price) {
            return false;
        }

        // Check if product size is in sizes array
        const sizeMatch = sizes.includes(product.size);

        // Check if product price is within range
        const priceMatch = product.price >= minPrice && product.price <= maxPrice;

        // Return true if both size and price match
        return sizeMatch && priceMatch;
    });
}

// Example usage:
const products = [
    { id: 1, name: 'T-Shirt', size: 'M', price: 20.00 },
    { id: 2, name: 'Jeans', size: 'L', price: 50.00 },
    { id: 3, name: 'Dress', size: 'S', price: 30.00 },
    { id: 4, name: 'Jacket', size: 'M', price: 40.00 },
    { id: 5, name: 'Shoes', size: 'L', price: 60.00 },
];

const sizes = ['M', 'L'];
const minPrice = 20.00;
const maxPrice = 50.00;

try {
    const filteredProducts = filterProducts(products, sizes, minPrice, maxPrice);
    console.log(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
