"""
Generated Code Metadata:
========================
Original URL: https://www.aquatic-green.ir
Prompt: "Write a JavaScript function to filter Trust brand products by category (e.g., skincare, haircare) and price range."
Generated: DETERMINISTIC_b4bf4073b9a69679
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters Trust brand products by category and price range.
 * 
 * @param {Object[]} products - Array of product objects.
 * @param {string} category - Category to filter by (e.g., skincare, haircare).
 * @param {number} minPrice - Minimum price to filter by.
 * @param {number} maxPrice - Maximum price to filter by.
 * @returns {Object[]} Filtered array of product objects.
 */
function filterTrustProductsByCategoryAndPrice(products, category, minPrice, maxPrice) {
    // Check if products is an array
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }

    // Check if category is a string
    if (typeof category !== 'string') {
        throw new Error('Category must be a string');
    }

    // Check if minPrice and maxPrice are numbers
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Min price and max price must be numbers');
    }

    // Check if minPrice is less than or equal to maxPrice
    if (minPrice > maxPrice) {
        throw new Error('Min price must be less than or equal to max price');
    }

    // Filter products by category and price range
    return products
        .filter(product => product.brand === 'Trust' && product.category === category)
        .filter(product => product.price >= minPrice && product.price <= maxPrice);
}

// Example usage:
const products = [
    { id: 1, brand: 'Trust', category: 'skincare', price: 10.99 },
    { id: 2, brand: 'Trust', category: 'haircare', price: 9.99 },
    { id: 3, brand: 'Other', category: 'skincare', price: 12.99 },
    { id: 4, brand: 'Trust', category: 'skincare', price: 15.99 },
    { id: 5, brand: 'Trust', category: 'haircare', price: 7.99 },
];

try {
    const filteredProducts = filterTrustProductsByCategoryAndPrice(products, 'skincare', 10, 15);
    // Use globalThis.console to ensure console is defined
    globalThis.console.log(filteredProducts);
} catch (error) {
    globalThis.console.error(error.message);
}
```
