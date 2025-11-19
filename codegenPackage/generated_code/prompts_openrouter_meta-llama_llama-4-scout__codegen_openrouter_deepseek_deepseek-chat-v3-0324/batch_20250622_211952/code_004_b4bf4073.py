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
 * @param {Array} products - Array of product objects to filter.
 * @param {string} category - The category to filter by (e.g., 'skincare', 'haircare').
 * @param {number} minPrice - The minimum price of products to include.
 * @param {number} maxPrice - The maximum price of products to include.
 * @returns {Array} Filtered array of products matching the criteria.
 * @throws {Error} If inputs are invalid or products array is not provided.
 */
function filterTrustProducts(products, category, minPrice, maxPrice) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array.');
    }
    if (typeof category !== 'string' || category.trim() === '') {
        throw new Error('Category must be a non-empty string.');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number' || minPrice < 0 || maxPrice < 0) {
        throw new Error('Price range must be valid positive numbers.');
    }
    if (minPrice > maxPrice) {
        throw new Error('Minimum price must be less than or equal to maximum price.');
    }

    // Normalize category for case-insensitive comparison
    const normalizedCategory = category.toLowerCase().trim();

    // Filter products by category and price range
    return products.filter(product => {
        // Validate product structure
        if (!product || typeof product !== 'object') {
            console.warn('Invalid product encountered during filtering:', product);
            return false;
        }

        // Check if product matches Trust brand, category, and price range
        const isTrustBrand = product.brand && product.brand.toLowerCase() === 'trust';
        const matchesCategory = product.category && product.category.toLowerCase() === normalizedCategory;
        const inPriceRange = product.price >= minPrice && product.price <= maxPrice;

        return isTrustBrand && matchesCategory && inPriceRange;
    });
}

// Example usage:
/*
const products = [
    { brand: 'Trust', category: 'skincare', price: 25.99, name: 'Face Cream' },
    { brand: 'Trust', category: 'haircare', price: 15.50, name: 'Shampoo' },
    { brand: 'Other', category: 'skincare', price: 30.00, name: 'Serum' },
    { brand: 'Trust', category: 'skincare', price: 12.00, name: 'Cleanser' }
];

try {
    const filteredProducts = filterTrustProducts(products, 'skincare', 10, 30);
    console.log(filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
*/
```
