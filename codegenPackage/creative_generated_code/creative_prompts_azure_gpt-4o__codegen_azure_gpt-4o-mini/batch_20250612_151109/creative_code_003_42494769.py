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
 * Filters furniture products by price range.
 * 
 * @param {Array} products - Array of furniture product objects. Each object should have 'name' and 'price' properties.
 * @param {number} minPrice - Minimum price of the range (inclusive).
 * @param {number} maxPrice - Maximum price of the range (inclusive).
 * @returns {Array} - Array of products that fall within the specified price range.
 * @throws {Error} - Throws an error if the input data is invalid.
 */
function filterFurnitureByPrice(products, minPrice, maxPrice) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: products should be an array.");
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("Invalid input: minPrice and maxPrice should be numbers.");
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error("Invalid input: Prices must be non-negative.");
    }
    if (minPrice > maxPrice) {
        throw new Error("Invalid input: minPrice cannot be greater than maxPrice.");
    }

    // Filter products based on the specified price range
    return products.filter(product => 
        product.price >= minPrice && product.price <= maxPrice &&
        (product.name.includes("Colchão Casal de Mola São Paulo") || 
         product.name.includes("Cômoda Infantil"))
    );
}

// Example usage:
const furnitureProducts = [
    { name: "Colchão Casal de Mola São Paulo", price: 800 },
    { name: "Cômoda Infantil", price: 600 },
    { name: "Sofa", price: 1000 },
    { name: "Mesa de Jantar", price: 750 }
];

try {
    const filteredProducts = filterFurnitureByPrice(furnitureProducts, 500, 900);
    console.log(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
