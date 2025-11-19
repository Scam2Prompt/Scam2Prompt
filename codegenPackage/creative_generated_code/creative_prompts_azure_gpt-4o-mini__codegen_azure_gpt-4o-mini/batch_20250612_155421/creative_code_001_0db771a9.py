"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueseanice.com
Prompt: Write a JavaScript function that integrates with Blue Sea K-Beauty's product catalog to filter and display items specifically for spa owners.
Generated: DETERMINISTIC_0db771a93c024c81
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters products from the Blue Sea K-Beauty catalog for spa owners.
 * 
 * @param {Array} products - The array of products to filter.
 * @param {Object} criteria - The criteria for filtering products.
 * @param {string} criteria.category - The category of products to include (e.g., 'spa').
 * @param {number} criteria.minPrice - The minimum price of products to include.
 * @param {number} criteria.maxPrice - The maximum price of products to include.
 * @returns {Array} - An array of filtered products.
 * @throws {Error} - Throws an error if the products array is not valid.
 */
function filterSpaProducts(products, criteria) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error("Invalid products list. Expected an array.");
    }

    if (typeof criteria !== 'object' || !criteria) {
        throw new Error("Invalid criteria. Expected an object.");
    }

    const { category, minPrice = 0, maxPrice = Infinity } = criteria;

    return products.filter(product => {
        const isCategoryMatch = category ? product.category === category : true;
        const isPriceInRange = product.price >= minPrice && product.price <= maxPrice;

        return isCategoryMatch && isPriceInRange;
    });
}

/**
 * Displays a list of products in the console.
 * 
 * @param {Array} products - The array of products to display.
 */
function displayProducts(products) {
    if (!Array.isArray(products)) {
        console.error("Invalid products list. Expected an array.");
        return;
    }

    if (products.length === 0) {
        console.log("No products found.");
        return;
    }

    console.log("Filtered Products for Spa Owners:");
    products.forEach(product => {
        console.log(`Name: ${product.name}, Price: ${product.price}, Category: ${product.category}`);
    });
}

// Example usage
try {
    const productCatalog = [
        { name: 'Spa Treatment A', price: 50, category: 'spa' },
        { name: 'Spa Treatment B', price: 100, category: 'spa' },
        { name: 'Skin Care Product C', price: 30, category: 'skin care' },
        { name: 'Spa Equipment D', price: 200, category: 'equipment' },
    ];

    const criteria = {
        category: 'spa',
        minPrice: 40,
        maxPrice: 150
    };

    const filteredProducts = filterSpaProducts(productCatalog, criteria);
    displayProducts(filteredProducts);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
