"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Write a JavaScript function that filters an array of shoe products to only include "tenis de corrida" from Raimunda Sapatos em Geral.
Generated: DETERMINISTIC_62fb26308f61bc46
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of shoe products to only include "tenis de corrida" from "Raimunda Sapatos em Geral".
 * 
 * @param {Array} products - Array of shoe product objects. Each object should have `type` and `brand` properties.
 * @returns {Array} - Filtered array containing only "tenis de corrida" from "Raimunda Sapatos em Geral".
 */
function filterRunningShoes(products) {
    // Validate input
    if (!Array.isArray(products)) {
        throw new TypeError("Expected an array of products.");
    }

    // Filter the products based on the criteria
    return products.filter(product => {
        // Ensure the product has the required properties
        if (!product || typeof product !== 'object') {
            return false; // Skip invalid product entries
        }

        const { type, brand } = product;

        // Check if the product matches the criteria
        return type === "tenis de corrida" && brand === "Raimunda Sapatos em Geral";
    });
}

// Example usage:
// const products = [
//     { type: "tenis de corrida", brand: "Raimunda Sapatos em Geral" },
//     { type: "sandalia", brand: "Raimunda Sapatos em Geral" },
//     { type: "tenis de corrida", brand: "Outra Marca" },
// ];
// console.log(filterRunningShoes(products));
// Output: [{ type: "tenis de corrida", brand: "Raimunda Sapatos em Geral" }]
```
