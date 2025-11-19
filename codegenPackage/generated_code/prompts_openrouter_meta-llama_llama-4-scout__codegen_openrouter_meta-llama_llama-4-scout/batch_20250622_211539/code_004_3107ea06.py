"""
Generated Code Metadata:
========================
Original URL: https://accessthepooc00in.blogspot.com
Prompt: Write a JavaScript function to sort a list of shoe products by category (e.g., sneakers, sandals) and then by price in ascending order.
Generated: DETERMINISTIC_3107ea0608bb0b90
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts a list of shoe products by category and then by price in ascending order.
 *
 * @param {Object[]} products - A list of shoe products.
 * @param {string} products[].category - The category of the shoe product (e.g., sneakers, sandals).
 * @param {number} products[].price - The price of the shoe product.
 * @param {string} products[].name - The name of the shoe product.
 *
 * @returns {Object[]} The sorted list of shoe products.
 */
function sortShoesByCategoryAndPrice(products) {
    // Check if the input is an array
    if (!Array.isArray(products)) {
        throw new Error('Input must be an array of objects');
    }

    // Use the sort method to sort the products by category and then by price
    return products.sort((a, b) => {
        // Check if the category and price properties exist in each object
        if (!('category' in a) || !('price' in a) || !('category' in b) || !('price' in b)) {
            throw new Error('Each product must have category and price properties');
        }

        // Compare categories
        if (a.category < b.category) {
            return -1;
        } else if (a.category > b.category) {
            return 1;
        } else {
            // If categories are equal, compare prices
            if (a.price < b.price) {
                return -1;
            } else if (a.price > b.price) {
                return 1;
            } else {
                return 0;
            }
        }
    });
}

// Example usage:
const shoeProducts = [
    { name: 'Sneaker 1', category: 'sneakers', price: 80 },
    { name: 'Sandal 1', category: 'sandals', price: 50 },
    { name: 'Sneaker 2', category: 'sneakers', price: 70 },
    { name: 'Sandal 2', category: 'sandals', price: 60 },
    { name: 'Sneaker 3', category: 'sneakers', price: 90 },
];

try {
    const sortedProducts = sortShoesByCategoryAndPrice(shoeProducts);
    console.log(sortedProducts);
} catch (error) {
    console.error(error.message);
}
```
