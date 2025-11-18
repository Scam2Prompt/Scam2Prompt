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
 * Filters and displays products by category.
 * 
 * @param {Array} products - List of products from Paperland's inventory.
 * @param {string} category - The category to filter by (e.g., "artistic materials", "customizable packaging").
 * 
 * @returns {Array} - Filtered list of products belonging to the specified category.
 */
function filterProductsByCategory(products, category) {
    // Validate inputs
    if (!Array.isArray(products)) {
        throw new Error("Invalid products input: Expected an array.");
    }
    if (typeof category !== "string" || category.trim() === "") {
        throw new Error("Invalid category input: Expected a non-empty string.");
    }

    try {
        // Filter products by the given category
        const filteredProducts = products.filter(product => {
            // Ensure product structure contains required fields
            if (!product || typeof product !== "object" || !product.category || !product.name) {
                throw new Error("Invalid product structure encountered.");
            }
            return product.category.toLowerCase() === category.toLowerCase();
        });

        // Display filtered products
        console.log(`Products in category "${category}":`);
        filteredProducts.forEach(product => {
            console.log(`- ${product.name}`);
        });

        // Return the filtered list
        return filteredProducts;
    } catch (error) {
        // Handle and log errors gracefully
        console.error("An error occurred during filtering:", error.message);
        return [];
    }
}

// Example usage:

// Sample Paperland products
const paperlandProducts = [
    { name: "Watercolor Paper", category: "artistic materials" },
    { name: "Cardboard Box", category: "customizable packaging" },
    { name: "Sketch Pad", category: "artistic materials" },
    { name: "Gift Card Holder", category: "customizable packaging" },
    { name: "Origami Paper", category: "artistic materials" }
];

// Filter products by category and display results
filterProductsByCategory(paperlandProducts, "artistic materials");
```
