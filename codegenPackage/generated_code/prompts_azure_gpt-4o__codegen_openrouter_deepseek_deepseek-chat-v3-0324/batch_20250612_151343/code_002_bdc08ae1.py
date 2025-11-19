"""
Generated Code Metadata:
========================
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Create a function in JavaScript to filter products by category, such as "Silicone baking molds" or "Edible glitter," and sort them by price from the Condi Shop catalog.
Generated: DETERMINISTIC_bdc08ae1d0ee96cc
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and sorts products from the Condi Shop catalog by category and price.
 * @param {Array} products - Array of product objects from the Condi Shop catalog.
 * @param {string} category - Category to filter by (e.g., "Silicone baking molds").
 * @param {string} [sortOrder='asc'] - Sorting order ('asc' for ascending, 'desc' for descending).
 * @returns {Array} Filtered and sorted array of products.
 * @throws {Error} If products is not an array or category is not a string.
 */
function filterAndSortProducts(products, category, sortOrder = 'asc') {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }
    if (typeof category !== 'string') {
        throw new Error('Category must be a string');
    }

    // Filter products by category (case-insensitive)
    const filteredProducts = products.filter(product => 
        product.category && 
        product.category.toLowerCase() === category.toLowerCase()
    );

    // Sort products by price
    return filteredProducts.sort((a, b) => {
        if (typeof a.price !== 'number' || typeof b.price !== 'number') {
            return 0;
        }
        return sortOrder.toLowerCase() === 'asc' ? 
            a.price - b.price : 
            b.price - a.price;
    });
}

// Example usage:
// const filteredProducts = filterAndSortProducts(condiShopCatalog, "Silicone baking molds", "desc");
```
