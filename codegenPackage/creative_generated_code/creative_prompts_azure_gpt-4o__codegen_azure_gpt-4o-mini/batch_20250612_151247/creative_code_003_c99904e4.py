"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperland.com.ar
Prompt: Create a function in JavaScript to filter and display paper and cardboard products by category, such as "artistic materials" or "customizable packaging," based on Paperland's product structure.
Generated: DETERMINISTIC_c99904e4cb015a15
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays paper and cardboard products by category.
 * 
 * @param {Array} products - The array of products to filter.
 * @param {string} category - The category to filter products by.
 * @returns {Array} - An array of filtered products in the specified category.
 * 
 * @throws {Error} - Throws an error if the input is not valid.
 */
function filterProductsByCategory(products, category) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: 'products' must be an array.");
    }
    if (typeof category !== 'string' || category.trim() === "") {
        throw new Error("Invalid input: 'category' must be a non-empty string.");
    }

    // Filter products by the specified category
    const filteredProducts = products.filter(product => {
        return product.category && product.category.toLowerCase() === category.toLowerCase();
    });

    // Display the filtered products
    displayProducts(filteredProducts);
    
    return filteredProducts;
}

/**
 * Displays the list of products in a user-friendly format.
 * 
 * @param {Array} products - The array of products to display.
 */
function displayProducts(products) {
    if (products.length === 0) {
        console.log("No products found in this category.");
        return;
    }

    console.log("Filtered Products:");
    products.forEach(product => {
        console.log(`- ${product.name}: ${product.description}`);
    });
}

// Example usage:
// const products = [
//     { name: "Watercolor Paper", category: "artistic materials", description: "High-quality watercolor paper." },
//     { name: "Custom Box", category: "customizable packaging", description: "A box that can be customized." },
//     { name: "Cardboard Sheets", category: "artistic materials", description: "Durable cardboard sheets." }
// ];

// try {
//     const filtered = filterProductsByCategory(products, "artistic materials");
//     console.log(filtered);
// } catch (error) {
//     console.error(error.message);
// }
```
