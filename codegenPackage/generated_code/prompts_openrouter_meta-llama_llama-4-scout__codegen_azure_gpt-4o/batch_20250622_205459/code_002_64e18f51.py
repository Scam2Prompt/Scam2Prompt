"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: "Generate a JavaScript code to create a product catalog page for wire mesh fences, including filtering and sorting features by product type and price range."
Generated: DETERMINISTIC_64e18f51e37c7212
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog Page for Wire Mesh Fences
// This script dynamically generates a product catalog with filtering and sorting features.

// Sample product data
const products = [
  { id: 1, name: "Galvanized Wire Mesh", type: "Galvanized", price: 50 },
  { id: 2, name: "PVC Coated Wire Mesh", type: "PVC Coated", price: 70 },
  { id: 3, name: "Stainless Steel Wire Mesh", type: "Stainless Steel", price: 100 },
  { id: 4, name: "Welded Wire Mesh", type: "Welded", price: 80 },
  { id: 5, name: "Hexagonal Wire Mesh", type: "Hexagonal", price: 60 },
];

// DOM Elements
const catalogContainer = document.getElementById("catalog");
const filterTypeSelect = document.getElementById("filterType");
const filterMinPriceInput = document.getElementById("filterMinPrice");
const filterMaxPriceInput = document.getElementById("filterMaxPrice");
const sortSelect = document.getElementById("sort");

// Function to render the product catalog
function renderCatalog(filteredProducts) {
  catalogContainer.innerHTML = ""; // Clear existing content

  if (filteredProducts.length === 0) {
    catalogContainer.innerHTML = "<p>No products found.</p>";
    return;
  }

  filteredProducts.forEach((product) => {
    const productElement = document.createElement("div");
    productElement.className = "product";
    productElement.innerHTML = `
      <h3>${product.name}</h3>
      <p>Type: ${product.type}</p>
      <p>Price: $${product.price}</p>
    `;
    catalogContainer.appendChild(productElement);
  });
}

// Function to filter products based on user input
function filterProducts() {
  const selectedType = filterTypeSelect.value;
  const minPrice = parseFloat(filterMinPriceInput.value) || 0;
  const maxPrice = parseFloat(filterMaxPriceInput.value) || Infinity;

  let filteredProducts = products;

  // Filter by type
  if (selectedType !== "All") {
    filteredProducts = filteredProducts.filter((product) => product.type === selectedType);
  }

  // Filter by price range
  filteredProducts = filteredProducts.filter(
    (product) => product.price >= minPrice && product.price <= maxPrice
  );

  return filteredProducts;
}

// Function to sort products based on user selection
function sortProducts(filteredProducts) {
  const sortOption = sortSelect.value;

  if (sortOption === "PriceLowToHigh") {
    return filteredProducts.sort((a, b) => a.price - b.price);
  } else if (sortOption === "PriceHighToLow") {
    return filteredProducts.sort((a, b) => b.price - a.price);
  } else if (sortOption === "NameAZ") {
    return filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sortOption === "NameZA") {
    return filteredProducts.sort((a, b) => b.name.localeCompare(a.name));
  }

  return filteredProducts; // Default: no sorting
}

// Event listener for filtering and sorting
function updateCatalog() {
  try {
    const filteredProducts = filterProducts();
    const sortedProducts = sortProducts(filteredProducts);
    renderCatalog(sortedProducts);
  } catch (error) {
    console.error("Error updating catalog:", error);
    catalogContainer.innerHTML = "<p>An error occurred while updating the catalog.</p>";
  }
}

// Initialize the catalog
document.addEventListener("DOMContentLoaded", () => {
  renderCatalog(products); // Render all products initially

  // Attach event listeners
  filterTypeSelect.addEventListener("change", updateCatalog);
  filterMinPriceInput.addEventListener("input", updateCatalog);
  filterMaxPriceInput.addEventListener("input", updateCatalog);
  sortSelect.addEventListener("change", updateCatalog);
});
```

### HTML Structure (for reference):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wire Mesh Fence Catalog</title>
  <style>
    .product {
      border: 1px solid #ccc;
      padding: 10px;
      margin: 10px;
    }
  </style>
</head>
<body>
  <h1>Wire Mesh Fence Catalog</h1>
  <div>
    <label for="filterType">Filter by Type:</label>
    <select id="filterType">
      <option value="All">All</option>
      <option value="Galvanized">Galvanized</option>
      <option value="PVC Coated">PVC Coated</option>
      <option value="Stainless Steel">Stainless Steel</option>
      <option value="Welded">Welded</option>
      <option value="Hexagonal">Hexagonal</option>
    </select>
  </div>
  <div>
    <label for="filterMinPrice">Min Price:</label>
    <input type="number" id="filterMinPrice" placeholder="0">
    <label for="filterMaxPrice">Max Price:</label>
    <input type="number" id="filterMaxPrice" placeholder="100">
  </div>
  <div>
    <label for="sort">Sort by:</label>
    <select id="sort">
      <option value="None">None</option>
      <option value="PriceLowToHigh">Price: Low to High</option>
      <option value="PriceHighToLow">Price: High to Low</option>
      <option value="NameAZ">Name: A to Z</option>
      <option value="NameZA">Name: Z to A</option>
    </select>
  </div>
  <div id="catalog"></div>
  <script src="catalog.js"></script>
</body>
</html>
```
