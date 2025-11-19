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
 * Sorts an array of shoe products by category and then by price in ascending order.
 * 
 * @param {Array} shoes - An array of shoe objects, where each object has a 'category' and 'price' property.
 * @returns {Array} - A new array of shoe objects sorted by category and price.
 * 
 * @throws {TypeError} - Throws an error if the input is not an array or if the array elements are not objects with the required properties.
 */
function sortShoesByCategoryAndPrice(shoes) {
    // Validate input
    if (!Array.isArray(shoes)) {
        throw new TypeError('Input must be an array of shoe objects.');
    }

    // Check each shoe object for required properties
    shoes.forEach(shoe => {
        if (typeof shoe !== 'object' || shoe === null || !('category' in shoe) || !('price' in shoe)) {
            throw new TypeError('Each shoe must be an object with "category" and "price" properties.');
        }
    });

    // Sort the shoes array
    return shoes.slice().sort((a, b) => {
        // First, sort by category
        const categoryComparison = a.category.localeCompare(b.category);
        if (categoryComparison !== 0) {
            return categoryComparison;
        }
        // If categories are the same, sort by price
        return a.price - b.price;
    });
}

// Example usage:
const shoeProducts = [
    { category: 'sneakers', price: 60 },
    { category: 'sandals', price: 30 },
    { category: 'sneakers', price: 50 },
    { category: 'boots', price: 100 },
    { category: 'sandals', price: 20 }
];

try {
    const sortedShoes = sortShoesByCategoryAndPrice(shoeProducts);
    console.log(sortedShoes);
} catch (error) {
    console.error(error.message);
}
```
