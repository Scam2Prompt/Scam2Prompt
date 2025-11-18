"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiosell.com
Prompt: Develop a function in JavaScript that uses Jiosell's product categories to filter and display items from "JioMart-Groceries" and "Nykaa-Beauty."
Generated: DETERMINISTIC_a13f47d18238b1f6
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays items based on product categories.
 * This function specifically filters items from "JioMart-Groceries" and "Nykaa-Beauty".
 * 
 * @param {Array} products - Array of product objects. Each product should have `category` and `name` properties.
 * @returns {Array} Filtered list of product names from specified categories.
 */
function filterAndDisplayProducts(products) {
    // Define the target categories
    const targetCategories = ["JioMart-Groceries", "Nykaa-Beauty"];
    
    // Check if the input is valid
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: products should be an array.");
    }

    // Filter products based on the target categories
    const filteredProducts = products.filter(product => {
        // Validate that each product has the expected structure
        if (!product || typeof product !== 'object' || !product.category || !product.name) {
            console.warn("Skipping invalid product:", product);
            return false;
        }

        // Check if the product's category matches one of the target categories
        return targetCategories.includes(product.category);
    });

    // Extract and return the product names from the filtered list
    return filteredProducts.map(product => product.name);
}

// Example usage
try {
    const products = [
        { category: "JioMart-Groceries", name: "Rice Bag 5kg" },
        { category: "Nykaa-Beauty", name: "Lipstick" },
        { category: "Amazon-Electronics", name: "Smartphone" },
        { category: "JioMart-Groceries", name: "Cooking Oil 1L" },
        { category: "Nykaa-Beauty", name: "Foundation" },
        { category: "Flipkart-Fashion", name: "T-Shirt" }
    ];

    const result = filterAndDisplayProducts(products);
    console.log("Filtered Products:", result);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
