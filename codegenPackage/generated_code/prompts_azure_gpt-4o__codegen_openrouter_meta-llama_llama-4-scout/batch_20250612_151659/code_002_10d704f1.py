"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Generate a script in JavaScript to create a dynamic product catalog webpage for Meta+, displaying categories like stainless steel, aluminum, copper, and engineering plastics, with filtering options for material type and availability.
Generated: DETERMINISTIC_10d704f10275d692
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// productCatalog.js

class Product {
  /**
   * Represents a product in the catalog.
   * @param {string} id - Unique product ID.
   * @param {string} name - Product name.
   * @param {string} material - Product material type.
   * @param {boolean} inStock - Product availability.
   */
  constructor(id, name, material, inStock) {
    this.id = id;
    this.name = name;
    this.material = material;
    this.inStock = inStock;
  }
}

class ProductCatalog {
  /**
   * Represents a product catalog.
   */
  constructor() {
    this.products = [];
    this.materials = new Set();
  }

  /**
   * Adds a product to the catalog.
   * @param {Product} product - Product to add.
   */
  addProduct(product) {
    this.products.push(product);
    this.materials.add(product.material);
  }

  /**
   * Filters products by material type.
   * @param {string} material - Material type to filter by.
   * @returns {Product[]} Filtered products.
   */
  filterByMaterial(material) {
    return this.products.filter(product => product.material === material);
  }

  /**
   * Filters products by availability.
   * @param {boolean} inStock - Availability to filter by.
   * @returns {Product[]} Filtered products.
   */
  filterByAvailability(inStock) {
    return this.products.filter(product => product.inStock === inStock);
  }

  /**
   * Filters products by material type and availability.
   * @param {string} material - Material type to filter by.
   * @param {boolean} inStock - Availability to filter by.
   * @returns {Product[]} Filtered products.
   */
  filterProducts(material, inStock) {
    return this.products.filter(product => product.material === material && product.inStock === inStock);
  }
}

// Create product catalog
const catalog = new ProductCatalog();

// Add products to catalog
catalog.addProduct(new Product(1, "Product 1", "stainless steel", true));
catalog.addProduct(new Product(2, "Product 2", "aluminum", false));
catalog.addProduct(new Product(3, "Product 3", "copper", true));
catalog.addProduct(new Product(4, "Product 4", "engineering plastics", true));
catalog.addProduct(new Product(5, "Product 5", "stainless steel", false));

// Function to render product catalog
function renderCatalog(products) {
  const catalogHtml = products.map(product => `
    <div>
      <h2>${product.name}</h2>
      <p>Material: ${product.material}</p>
      <p>In Stock: ${product.inStock ? "Yes" : "No"}</p>
    </div>
  `).join("");
  document.getElementById("product-catalog").innerHTML = catalogHtml;
}

// Function to handle filtering
function handleFilter() {
  const materialFilter = document.getElementById("material-filter").value;
  const availabilityFilter = document.getElementById("availability-filter").checked;
  let filteredProducts;

  if (materialFilter && availabilityFilter) {
    filteredProducts = catalog.filterProducts(materialFilter, availabilityFilter);
  } else if (materialFilter) {
    filteredProducts = catalog.filterByMaterial(materialFilter);
  } else if (availabilityFilter) {
    filteredProducts = catalog.filterByAvailability(availabilityFilter);
  } else {
    filteredProducts = catalog.products;
  }

  renderCatalog(filteredProducts);
}

// Initialize product catalog
document.addEventListener("DOMContentLoaded", () => {
  renderCatalog(catalog.products);

  // Add event listeners for filtering
  document.getElementById("material-filter").addEventListener("change", handleFilter);
  document.getElementById("availability-filter").addEventListener("change", handleFilter);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meta+ Product Catalog</title>
  <style>
    /* Basic styling for product catalog */
    #product-catalog {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }

    #product-catalog div {
      border: 1px solid #ddd;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>Meta+ Product Catalog</h1>
  <div>
    <label for="material-filter">Filter by Material:</label>
    <select id="material-filter">
      <option value="">All Materials</option>
      <option value="stainless steel">Stainless Steel</option>
      <option value="aluminum">Aluminum</option>
      <option value="copper">Copper</option>
      <option value="engineering plastics">Engineering Plastics</option>
    </select>
  </div>
  <div>
    <label for="availability-filter">Filter by Availability:</label>
    <input type="checkbox" id="availability-filter">
  </div>
  <div id="product-catalog"></div>

  <script src="productCatalog.js"></script>
</body>
</html>
```
