"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfcosmetics.com.ua
Prompt: Develop a JavaScript function to filter makeup products by type, such as "tonal creams" and "eye shadows," based on the categories listed on the ELF Cosmetics webpage.
Generated: DETERMINISTIC_b235023b59dd634c
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters makeup products by type from a given list of products.
 * 
 * @param {Array<Object>} products - Array of product objects to filter. Each product should have a `category` property.
 * @param {string} type - The type of makeup product to filter (e.g., "tonal creams", "eye shadows").
 * @returns {Array<Object>} - Array of filtered product objects matching the specified type.
 * @throws {Error} - Throws an error if the input is invalid or if the type is not a string.
 */
function filterMakeupProductsByType(products, type) {
    // Input validation
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: 'products' must be an array.");
    }
    if (typeof type !== "string") {
        throw new Error("Invalid input: 'type' must be a string.");
    }

    // Filter the products by type
    const filteredProducts = products.filter(product => {
        // Ensure the product object contains a valid category
        if (typeof product !== "object" || product === null || !product.category) {
            console.warn("Skipping invalid product:", product);
            return false;
        }
        // Return products matching the specified type
        return product.category.toLowerCase() === type.toLowerCase();
    });

    return filteredProducts;
}

// Example usage:
// Assuming products is an array of product objects fetched from the ELF Cosmetics webpage
const products = [
    { id: 1, name: "Hydrating Camo Concealer", category: "tonal creams" },
    { id: 2, name: "Rose Gold Eyeshadow Palette", category: "eye shadows" },
    { id: 3, name: "Matte Lipstick", category: "lipsticks" },
    { id: 4, name: "Flawless Finish Foundation", category: "tonal creams" }
];
const type = "tonal creams";

try {
    const filteredProducts = filterMakeupProductsByType(products, type);
    console.log("Filtered Products:", filteredProducts);
} catch (error) {
    console.error("Error:", error.message);
}
```
