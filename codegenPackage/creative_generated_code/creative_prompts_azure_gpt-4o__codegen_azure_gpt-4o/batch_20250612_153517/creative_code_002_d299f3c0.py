"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Create a script in JavaScript to filter products by category (e.g., "Electrice," "Constructii," "Gradina") and display the filtered results dynamically on a webpage.
Generated: DETERMINISTIC_d299f3c06144fe3a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Script to dynamically filter products by category and display the results on a webpage

// Sample product data
const products = [
  { id: 1, name: "Drill Machine", category: "Electrice" },
  { id: 2, name: "Hammer", category: "Constructii" },
  { id: 3, name: "Lawn Mower", category: "Gradina" },
  { id: 4, name: "Screwdriver Set", category: "Electrice" },
  { id: 5, name: "Cement Bag", category: "Constructii" },
  { id: 6, name: "Garden Hose", category: "Gradina" },
];

// Function to filter products by category
function filterProductsByCategory(category) {
  // Filter products based on the selected category
  return products.filter(product => product.category === category);
}

// Function to dynamically update the product list on the webpage
function updateProductList(filteredProducts) {
  const productListContainer = document.getElementById("product-list");

  // Clear existing content
  productListContainer.innerHTML = "";

  // Handle case where no products match the filter
  if (filteredProducts.length === 0) {
    productListContainer.innerHTML = "<p>No products found for the selected category.</p>";
    return;
  }

  // Generate and append product items
  filteredProducts.forEach(product => {
    const productItem = document.createElement("div");
    productItem.className = "product-item";
    productItem.textContent = `${product.name} (${product.category})`;
    productListContainer.appendChild(productItem);
  });
}

// Event listener for category selection
document.getElementById("category-select").addEventListener("change", event => {
  const selectedCategory = event.target.value;

  try {
    // Filter products and update the product list
    const filteredProducts = filterProductsByCategory(selectedCategory);
    updateProductList(filteredProducts);
  } catch (error) {
    console.error("Error filtering products:", error);
    alert("An error occurred while filtering products. Please try again.");
  }
});

// HTML structure and styling
document.body.innerHTML = `
  <div>
    <label for="category-select">Select Category:</label>
    <select id="category-select">
      <option value="Electrice">Electrice</option>
      <option value="Constructii">Constructii</option>
      <option value="Gradina">Gradina</option>
    </select>
  </div>
  <div id="product-list" style="margin-top: 20px;">
    <p>Select a category to see the products.</p>
  </div>
`;

document.body.style.fontFamily = "Arial, sans-serif";

const productListStyle = document.createElement("style");
productListStyle.textContent = `
  .product-item {
    padding: 5px 10px;
    border: 1px solid #ccc;
    margin: 5px 0;
    background-color: #f9f9f9;
  }
`;
document.head.appendChild(productListStyle);
```
