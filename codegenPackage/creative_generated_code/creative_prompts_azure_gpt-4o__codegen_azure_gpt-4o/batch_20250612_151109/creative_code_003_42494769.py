"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write a JavaScript function to filter furniture products by price range, specifically for items like "Colchão Casal de Mola São Paulo" and "Cômoda Infantil," using data scraped from "moveisonlinepelotasbraz."
Generated: DETERMINISTIC_4249476907a2c4ad
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters furniture products by a given price range and specific item names.
 * 
 * @param {Array} products - Array of product objects scraped from "moveisonlinepelotasbraz".
 *                           Each product object should have the following structure:
 *                           { name: string, price: number }
 * @param {number} minPrice - Minimum price for the filter (inclusive).
 * @param {number} maxPrice - Maximum price for the filter (inclusive).
 * @param {Array} targetItems - Array of specific item names to filter by.
 * @returns {Array} - Array of filtered product objects that match the criteria.
 */
function filterFurnitureByPriceAndName(products, minPrice, maxPrice, targetItems) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new Error('Invalid input: products must be an array');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Invalid input: minPrice and maxPrice must be numbers');
    }
    if (!Array.isArray(targetItems)) {
        throw new Error('Invalid input: targetItems must be an array of strings');
    }

    // Filter products based on price range and target item names
    return products.filter(product => {
        // Ensure product has valid structure
        if (typeof product.name !== 'string' || typeof product.price !== 'number') {
            console.warn(`Invalid product structure: ${JSON.stringify(product)}`);
            return false;
        }

        // Check if the product matches the price range and target item names
        const isWithinPriceRange = product.price >= minPrice && product.price <= maxPrice;
        const isTargetItem = targetItems.includes(product.name);

        return isWithinPriceRange && isTargetItem;
    });
}

// Example usage
const scrapedProducts = [
    { name: 'Colchão Casal de Mola São Paulo', price: 1500 },
    { name: 'Cômoda Infantil', price: 800 },
    { name: 'Mesa de Jantar', price: 1200 },
    { name: 'Cadeira de Escritório', price: 400 },
];

const filteredProducts = filterFurnitureByPriceAndName(
    scrapedProducts,
    500, // Minimum price
    2000, // Maximum price
    ['Colchão Casal de Mola São Paulo', 'Cômoda Infantil'] // Target items
);

console.log(filteredProducts);
// Output: 
// [
//    { name: 'Colchão Casal de Mola São Paulo', price: 1500 },
//    { name: 'Cômoda Infantil', price: 800 }
// ]
```
