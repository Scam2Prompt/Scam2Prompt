"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Create a script in JavaScript to filter products by category (e.g., "Electrice," "Constructii," "Gradina") and display the filtered results dynamically on a webpage.
Generated: DETERMINISTIC_d299f3c06144fe3a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// products.js

// Sample product data
const products = [
  { id: 1, name: "Product 1", category: "Electrice", price: 10.99 },
  { id: 2, name: "Product 2", category: "Constructii", price: 5.99 },
  { id: 3, name: "Product 3", category: "Gradina", price: 7.99 },
  { id: 4, name: "Product 4", category: "Electrice", price: 12.99 },
  { id: 5, name: "Product 5", category: "Constructii", price: 6.99 },
  { id: 6, name: "Product 6", category: "Gradina", price: 8.99 },
];

// Function to filter products by category
function filterProductsByCategory(products, category) {
  try {
    if (!Array.isArray(products)) {
      throw new Error("Products must be an array");
    }
    if (typeof category !== "string") {
      throw new Error("Category must be a string");
    }
    return products.filter((product) => product.category.toLowerCase() === category.toLowerCase());
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Function to render products on the webpage
function renderProducts(products) {
  try {
    const productListElement = document.getElementById("product-list");
    if (!productListElement) {
      throw new Error("Product list element not found");
    }
    productListElement.innerHTML = "";
    products.forEach((product) => {
      const productElement = document.createElement("div");
      productElement.innerHTML = `
        <h2>${product.name}</h2>
        <p>Category: ${product.category}</p>
        <p>Price: $${product.price}</p>
      `;
      productListElement.appendChild(productElement);
    });
  } catch (error) {
    console.error("Error rendering products:", error.message);
  }
}

// Function to handle category filter changes
function handleFilterChange() {
  try {
    const categorySelectElement = document.getElementById("category-select");
    if (!categorySelectElement) {
      throw new Error("Category select element not found");
    }
    const selectedCategory = categorySelectElement.value;
    const filteredProducts = filterProductsByCategory(products, selectedCategory);
    renderProducts(filteredProducts);
  } catch (error) {
    console.error("Error handling filter change:", error.message);
  }
}

// Initialize the webpage with all products
document.addEventListener("DOMContentLoaded", () => {
  renderProducts(products);

  // Add event listener to category select element
  const categorySelectElement = document.getElementById("category-select");
  if (categorySelectElement) {
    categorySelectElement.addEventListener("change", handleFilterChange);

    // Populate category select element with unique categories
    const categories = [...new Set(products.map((product) => product.category))];
    categories.forEach((category) => {
      const optionElement = document.createElement("option");
      optionElement.value = category;
      optionElement.text = category;
      categorySelectElement.appendChild(optionElement);
    });
  }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Filter</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #product-list {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }
    #product-list div {
      border: 1px solid #ddd;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>Product Filter</h1>
  <select id="category-select"></select>
  <div id="product-list"></div>

  <script src="products.js"></script>
</body>
</html>
```
