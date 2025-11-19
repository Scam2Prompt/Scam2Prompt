"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Write a JavaScript function to dynamically update the product comparison table for categories like "صندلی انتظار آرایشگاه" and "میز ناخن" based on user-selected criteria.
Generated: DETERMINISTIC_86dcb720ba152543
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates the product comparison table based on user-selected criteria.
 * 
 * @param {Object} criteria - An object containing the user's selected criteria.
 * @param {string} criteria.category - The category of products to compare (e.g. "صندلی انتظار آرایشگاه" or "میز ناخن").
 * @param {string} criteria.attribute - The attribute to compare products by (e.g. "price" or "rating").
 * @param {string} criteria.order - The order to display the products in (e.g. "asc" or "desc").
 * @param {Array} products - An array of product objects.
 * @returns {HTMLElement} The updated product comparison table.
 */
function updateProductComparisonTable(criteria, products) {
    // Check if the criteria and products are valid
    if (!criteria || !products) {
        throw new Error("Invalid criteria or products");
    }

    // Filter products by category
    const filteredProducts = products.filter(product => product.category === criteria.category);

    // Sort products by attribute and order
    const sortedProducts = filteredProducts.sort((a, b) => {
        if (criteria.attribute === "price") {
            return criteria.order === "asc" ? a.price - b.price : b.price - a.price;
        } else if (criteria.attribute === "rating") {
            return criteria.order === "asc" ? a.rating - b.rating : b.rating - a.rating;
        } else {
            throw new Error("Invalid attribute");
        }
    });

    // Create the table
    const table = document.createElement("table");
    table.classList.add("product-comparison-table");

    // Create the table header
    const headerRow = document.createElement("tr");
    headerRow.innerHTML = `
        <th>Product</th>
        <th>Price</th>
        <th>Rating</th>
    `;
    table.appendChild(headerRow);

    // Create the table rows
    sortedProducts.forEach(product => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${product.name}</td>
            <td>${product.price}</td>
            <td>${product.rating}/5</td>
        `;
        table.appendChild(row);
    });

    // Return the updated table
    return table;
}

// Example usage:
const products = [
    { category: "صندلی انتظار آرایشگاه", name: "Product 1", price: 100, rating: 4 },
    { category: "صندلی انتظار آرایشگاه", name: "Product 2", price: 200, rating: 5 },
    { category: "میز ناخن", name: "Product 3", price: 50, rating: 3 },
];

const criteria = {
    category: "صندلی انتظار آرایشگاه",
    attribute: "price",
    order: "asc",
};

const table = updateProductComparisonTable(criteria, products);
document.getElementById("product-comparison-table-container").appendChild(table);
```

```css
/* Add this to your CSS file */
.product-comparison-table {
    border-collapse: collapse;
    width: 100%;
}

.product-comparison-table th, .product-comparison-table td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

.product-comparison-table th {
    background-color: #f0f0f0;
}
```

```html
<!-- Add this to your HTML file -->
<div id="product-comparison-table-container"></div>
```
