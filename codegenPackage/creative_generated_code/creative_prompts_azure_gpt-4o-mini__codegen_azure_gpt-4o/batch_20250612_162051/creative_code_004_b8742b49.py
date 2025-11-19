"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alakhttiar.com.sa
Prompt: Suggest a JavaScript code to dynamically filter and display products like "شينكو" and "لكسان" based on user input on a WordPress page.
Generated: DETERMINISTIC_b8742b49c35f0202
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to dynamically filter and display products on a WordPress page

// Wrap the code in an IIFE to avoid polluting the global namespace
(() => {
    document.addEventListener("DOMContentLoaded", () => {
        // List of products for filtering
        const products = [
            { id: 1, name: "شينكو" },
            { id: 2, name: "لكسان" },
            { id: 3, name: "عازل حراري" },
            { id: 4, name: "حديد" }
        ];

        // Target DOM elements
        const searchInput = document.getElementById("product-search");
        const productList = document.getElementById("product-list");

        // Function to render the filtered products
        const renderProducts = (filteredProducts) => {
            // Clear the product list before rendering
            productList.innerHTML = "";

            // Check if there are products to display
            if (filteredProducts.length === 0) {
                productList.innerHTML = "<p>No products found.</p>";
                return;
            }

            // Create and append product list items
            filteredProducts.forEach(product => {
                const listItem = document.createElement("li");
                listItem.textContent = product.name;
                productList.appendChild(listItem);
            });
        };

        // Event listener for filtering products based on user input
        searchInput.addEventListener("input", () => {
            const query = searchInput.value.trim().toLowerCase(); // Normalize input for case-insensitive search
            const filteredProducts = products.filter(product =>
                product.name.toLowerCase().includes(query)
            );
            renderProducts(filteredProducts); // Update the product list
        });

        // Initial rendering of all products
        renderProducts(products);
    });
})();

// Example HTML for integration:
// <input type="text" id="product-search" placeholder="Search products..." />
// <ul id="product-list"></ul>
```
