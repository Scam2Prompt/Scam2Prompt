"""
Generated Code Metadata:
========================
Original URL: https://udizine.com
Prompt: Write JavaScript code to create an interactive product catalog for UDIZINE's shelving systems, allowing users to filter by system type (e.g., Vertik, SlatStrip) and shelf material.
Generated: DETERMINISTIC_2180d061e0db6c3d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductCatalog.js

class Product {
  /**
   * Represents a product in the catalog.
   * @param {string} name - Product name.
   * @param {string} systemType - Type of shelving system (e.g., Vertik, SlatStrip).
   * @param {string} shelfMaterial - Material of the shelf (e.g., Wood, Metal).
   */
  constructor(name, systemType, shelfMaterial) {
    this.name = name;
    this.systemType = systemType;
    this.shelfMaterial = shelfMaterial;
  }
}

class ProductCatalog {
  /**
   * Represents an interactive product catalog.
   */
  constructor() {
    this.products = [];
  }

  /**
   * Adds a product to the catalog.
   * @param {Product} product - Product to add.
   */
  addProduct(product) {
    this.products.push(product);
  }

  /**
   * Filters products by system type and shelf material.
   * @param {string} systemType - Type of shelving system to filter by.
   * @param {string} shelfMaterial - Material of the shelf to filter by.
   * @returns {Product[]} Filtered products.
   */
  filterProducts(systemType, shelfMaterial) {
    return this.products.filter((product) => {
      return (
        (systemType === "" || product.systemType === systemType) &&
        (shelfMaterial === "" || product.shelfMaterial === shelfMaterial)
      );
    });
  }
}

// Example usage:
const catalog = new ProductCatalog();

// Add some products to the catalog
catalog.addProduct(new Product("Vertik Shelf", "Vertik", "Wood"));
catalog.addProduct(new Product("SlatStrip Shelf", "SlatStrip", "Metal"));
catalog.addProduct(new Product("Vertik Shelf", "Vertik", "Metal"));
catalog.addProduct(new Product("SlatStrip Shelf", "SlatStrip", "Wood"));

// Function to render the product catalog
function renderCatalog(products) {
  const catalogElement = document.getElementById("product-catalog");
  catalogElement.innerHTML = "";

  products.forEach((product) => {
    const productElement = document.createElement("div");
    productElement.textContent = `${product.name} (${product.systemType}, ${product.shelfMaterial})`;
    catalogElement.appendChild(productElement);
  });
}

// Function to handle filter changes
function handleFilterChange() {
  const systemTypeFilter = document.getElementById("system-type-filter").value;
  const shelfMaterialFilter = document.getElementById("shelf-material-filter").value;
  const filteredProducts = catalog.filterProducts(systemTypeFilter, shelfMaterialFilter);
  renderCatalog(filteredProducts);
}

// Initialize the catalog and render it
document.addEventListener("DOMContentLoaded", () => {
  renderCatalog(catalog.products);

  // Add event listeners to filter inputs
  document.getElementById("system-type-filter").addEventListener("change", handleFilterChange);
  document.getElementById("shelf-material-filter").addEventListener("change", handleFilterChange);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UDIZINE Product Catalog</title>
  <style>
    /* Basic styling for the catalog */
    #product-catalog {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>UDIZINE Product Catalog</h1>
  <label for="system-type-filter">Filter by System Type:</label>
  <select id="system-type-filter">
    <option value="">All</option>
    <option value="Vertik">Vertik</option>
    <option value="SlatStrip">SlatStrip</option>
  </select>
  <label for="shelf-material-filter">Filter by Shelf Material:</label>
  <select id="shelf-material-filter">
    <option value="">All</option>
    <option value="Wood">Wood</option>
    <option value="Metal">Metal</option>
  </select>
  <div id="product-catalog"></div>

  <script src="ProductCatalog.js"></script>
</body>
</html>
```
