"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Create a function in JavaScript to filter agricultural products by category (e.g., "Thuốc Ốc") and display product names like "Super Rim 250EC" on a webpage.
Generated: DETERMINISTIC_41f576f4c8c938c3
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters agricultural products by category and displays their names on a webpage.
 * 
 * @param {Array} products - Array of product objects. Each product should have 'name' and 'category' properties.
 * @param {string} category - The category to filter products by.
 */
function displayFilteredProductsByCategory(products, category) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        console.error("Invalid input: 'products' must be an array.");
        return;
    }
    if (typeof category !== "string") {
        console.error("Invalid input: 'category' must be a string.");
        return;
    }

    try {
        // Filter products by the given category
        const filteredProducts = products.filter(product => product.category === category);

        // Clear existing product list on the webpage (if any)
        const productListContainer = document.getElementById("product-list");
        if (!productListContainer) {
            console.error("Error: Element with ID 'product-list' not found.");
            return;
        }
        productListContainer.innerHTML = ""; // Clear existing content

        // Display filtered products
        filteredProducts.forEach(product => {
            const productItem = document.createElement("li");
            productItem.textContent = product.name;
            productListContainer.appendChild(productItem);
        });

        // Handle case where no products match the category
        if (filteredProducts.length === 0) {
            const noProductsMessage = document.createElement("p");
            noProductsMessage.textContent = "No products found for the selected category.";
            productListContainer.appendChild(noProductsMessage);
        }
    } catch (error) {
        console.error("An error occurred while filtering and displaying products:", error);
    }
}

// Example usage:
// Assuming there's an <ul> or <div> element with ID 'product-list' in your HTML
/*
<div id="product-list"></div>
<script>
    const products = [
        { name: "Super Rim 250EC", category: "Thuốc Ốc" },
        { name: "Green Shield", category: "Pesticide" },
        { name: "EcoGrow Fertilizer", category: "Fertilizer" },
        { name: "Snail Killer", category: "Thuốc Ốc" }
    ];

    displayFilteredProductsByCategory(products, "Thuốc Ốc");
</script>
*/
```
