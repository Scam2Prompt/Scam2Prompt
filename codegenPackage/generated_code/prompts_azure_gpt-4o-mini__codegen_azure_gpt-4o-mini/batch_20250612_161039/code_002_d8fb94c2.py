"""
Generated Code Metadata:
========================
Original URL: https://issowork.com
Prompt: Create a JavaScript function that filters clothing items by category (e.g., dresses, jackets) on an e-commerce site like ISSO, emphasizing minimalist fashion.
Generated: DETERMINISTIC_d8fb94c28b126c16
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters clothing items by category.
 * 
 * @param {Array} items - An array of clothing items, where each item is an object containing properties like 'name', 'category', and 'price'.
 * @param {string} category - The category to filter items by (e.g., 'dresses', 'jackets').
 * @returns {Array} - An array of clothing items that belong to the specified category.
 * @throws {Error} - Throws an error if the input items are not an array or if the category is not a string.
 */
function filterClothingByCategory(items, category) {
    // Validate input types
    if (!Array.isArray(items)) {
        throw new Error('The first argument must be an array of clothing items.');
    }
    if (typeof category !== 'string') {
        throw new Error('The category must be a string.');
    }

    // Filter items by the specified category
    const filteredItems = items.filter(item => {
        // Ensure each item has a category property and it matches the specified category
        return item.category && item.category.toLowerCase() === category.toLowerCase();
    });

    return filteredItems;
}

// Example usage
const clothingItems = [
    { name: 'Summer Dress', category: 'dresses', price: 49.99 },
    { name: 'Leather Jacket', category: 'jackets', price: 89.99 },
    { name: 'Casual T-Shirt', category: 'tops', price: 19.99 },
    { name: 'Evening Gown', category: 'dresses', price: 129.99 },
];

try {
    const dresses = filterClothingByCategory(clothingItems, 'dresses');
    console.log('Filtered Dresses:', dresses);
} catch (error) {
    console.error('Error filtering items:', error.message);
}
```
