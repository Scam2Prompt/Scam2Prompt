"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write a JavaScript function to filter furniture products by price range, specifically for items like "Colchão Casal de Mola São Paulo" and "Cômoda Infantil," using data scraped from "moveisonlinepelotasbraz."
Generated: DETERMINISTIC_4249476907a2c4ad
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters furniture products by a specified price range.
 * 
 * @param {Array} products - An array of furniture product objects.
 * @param {number} minPrice - The minimum price for the filter.
 * @param {number} maxPrice - The maximum price for the filter.
 * @returns {Array} - An array of products that fall within the specified price range.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterFurnitureByPrice(products, minPrice, maxPrice) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: products should be an array.");
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("Invalid input: minPrice and maxPrice should be numbers.");
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error("Invalid input: Prices should be non-negative.");
    }
    if (minPrice > maxPrice) {
        throw new Error("Invalid input: minPrice should not be greater than maxPrice.");
    }

    // Filter products based on the price range
    return products.filter(product => {
        // Ensure product has a price property and it's a number
        if (typeof product.price !== 'number') {
            console.warn(`Product ${product.name} does not have a valid price.`);
            return false; // Exclude products without a valid price
        }
        return product.price >= minPrice && product.price <= maxPrice;
    });
}

// Example usage
const furnitureProducts = [
    { name: "Colchão Casal de Mola São Paulo", price: 1200 },
    { name: "Cômoda Infantil", price: 800 },
    { name: "Sofa Retrátil", price: 1500 },
    { name: "Mesa de Jantar", price: 900 }
];

try {
    const filteredProducts = filterFurnitureByPrice(furnitureProducts, 800, 1300);
    console.log("Filtered Products:", filteredProducts);
} catch (error) {
    console.error("Error filtering products:", error.message);
}
```
