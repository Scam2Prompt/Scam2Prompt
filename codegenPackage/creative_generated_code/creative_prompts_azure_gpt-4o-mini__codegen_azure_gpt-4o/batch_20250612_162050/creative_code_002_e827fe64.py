"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Create a JavaScript function to filter and display products based on their categories, such as "Aromáticas" and "Hortalizas," as seen on the Oromáticas website.
Generated: DETERMINISTIC_e827fe646622cc26
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays products based on their categories.
 * 
 * @param {Array} products - An array of product objects. Each object should have a "name" and "category" property.
 * @param {Array} categories - An array of categories to filter products by.
 */
function filterAndDisplayProducts(products, categories) {
    try {
        // Validate input arguments
        if (!Array.isArray(products)) {
            throw new TypeError("The 'products' argument must be an array.");
        }

        if (!Array.isArray(categories)) {
            throw new TypeError("The 'categories' argument must be an array.");
        }

        // Filter products by the specified categories
        const filteredProducts = products.filter(product => {
            if (!product || typeof product.category !== 'string') {
                console.warn("Skipping invalid product:", product);
                return false;
            }
            return categories.includes(product.category);
        });

        // Display the filtered products
        console.log("Filtered Products:");
        if (filteredProducts.length === 0) {
            console.log("No products found for the specified categories.");
        } else {
            filteredProducts.forEach(product => {
                console.log(`- Name: ${product.name}, Category: ${product.category}`);
            });
        }
    } catch (error) {
        // Handle errors gracefully
        console.error("An error occurred while filtering and displaying products:", error.message);
    }
}

// Example usage:
const products = [
    { name: "Mint", category: "Aromáticas" },
    { name: "Basil", category: "Aromáticas" },
    { name: "Lettuce", category: "Hortalizas" },
    { name: "Potato", category: "Tubérculos" },
    { name: "Rosemary", category: "Aromáticas" }
];

const categoriesToFilter = ["Aromáticas", "Hortalizas"];

filterAndDisplayProducts(products, categoriesToFilter);
```
