"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Write a function in JavaScript to filter products by age group (e.g., "0–12 miesięcy" or "1–3 lata") and category, as outlined on the Milly Mally platform.
Generated: DETERMINISTIC_5bacf193e96925a0
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of products by age group and category.
 * 
 * @param {Array} products - Array of product objects, each containing 'ageGroup' and 'category' properties.
 * @param {string} ageGroup - The age group to filter products by (e.g., "0–12 miesięcy", "1–3 lata").
 * @param {string} category - The category to filter products by.
 * @returns {Array} - Array of filtered products that match the specified age group and category.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function filterProducts(products, ageGroup, category) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: products should be an array.");
    }
    if (typeof ageGroup !== 'string' || typeof category !== 'string') {
        throw new Error("Invalid input: ageGroup and category should be strings.");
    }

    // Filter products based on age group and category
    return products.filter(product => {
        return product.ageGroup === ageGroup && product.category === category;
    });
}

// Example usage
try {
    const products = [
        { id: 1, name: "Toy Car", ageGroup: "0–12 miesięcy", category: "Toys" },
        { id: 2, name: "Building Blocks", ageGroup: "1–3 lata", category: "Toys" },
        { id: 3, name: "Baby Walker", ageGroup: "0–12 miesięcy", category: "Baby Gear" },
        { id: 4, name: "Puzzle", ageGroup: "1–3 lata", category: "Games" }
    ];

    const filteredProducts = filterProducts(products, "1–3 lata", "Toys");
    console.log(filteredProducts);
} catch (error) {
    console.error(error.message);
}
```
