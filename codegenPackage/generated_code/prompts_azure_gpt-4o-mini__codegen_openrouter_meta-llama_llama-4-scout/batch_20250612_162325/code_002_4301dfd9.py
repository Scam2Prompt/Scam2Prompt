"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Create a JavaScript function that dynamically displays a list of home furniture products like "میز ناهار خوری" and "کمد لباس" when a user selects a category from a dropdown menu.
Generated: DETERMINISTIC_4301dfd99fa1c161
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// furniture.js

/**
 * Represents a home furniture product.
 */
class FurnitureProduct {
  /**
   * Creates a new FurnitureProduct instance.
   * @param {string} name - The name of the product.
   * @param {string} category - The category of the product.
   */
  constructor(name, category) {
    this.name = name;
    this.category = category;
  }
}

/**
 * Represents a furniture store.
 */
class FurnitureStore {
  /**
   * Creates a new FurnitureStore instance.
   */
  constructor() {
    this.products = [];
    this.categories = [];
  }

  /**
   * Adds a product to the store.
   * @param {FurnitureProduct} product - The product to add.
   */
  addProduct(product) {
    this.products.push(product);
    if (!this.categories.includes(product.category)) {
      this.categories.push(product.category);
    }
  }

  /**
   * Gets products by category.
   * @param {string} category - The category to filter by.
   * @returns {FurnitureProduct[]} The products in the specified category.
   */
  getProductsByCategory(category) {
    return this.products.filter((product) => product.category === category);
  }

  /**
   * Gets all categories.
   * @returns {string[]} The categories.
   */
  getCategories() {
    return this.categories;
  }
}

// Example usage:
const store = new FurnitureStore();

// Add some products
store.addProduct(new FurnitureProduct("میز ناهار خوری", "میز"));
store.addProduct(new FurnitureProduct("کمد لباس", "کمد"));
store.addProduct(new FurnitureProduct("تخت خواب", "تخت"));
store.addProduct(new FurnitureProduct("میز تلویزیون", "میز"));

// Get categories and products
const categories = store.getCategories();
const categorySelect = document.getElementById("category-select");
const productList = document.getElementById("product-list");

// Populate category select
categories.forEach((category) => {
  const option = document.createElement("option");
  option.value = category;
  option.textContent = category;
  categorySelect.appendChild(option);
});

// Add event listener to category select
categorySelect.addEventListener("change", (event) => {
  const selectedCategory = event.target.value;
  const products = store.getProductsByCategory(selectedCategory);

  // Clear product list
  productList.innerHTML = "";

  // Add products to list
  products.forEach((product) => {
    const listItem = document.createElement("li");
    listItem.textContent = product.name;
    productList.appendChild(listItem);
  });
});

// Initialize product list with first category
const initialCategory = categories[0];
const initialProducts = store.getProductsByCategory(initialCategory);

// Add initial products to list
initialProducts.forEach((product) => {
  const listItem = document.createElement("li");
  listItem.textContent = product.name;
  productList.appendChild(listItem);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Furniture Store</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #category-select {
      width: 200px;
      height: 30px;
      font-size: 16px;
    }
    #product-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #product-list li {
      padding: 10px;
      border-bottom: 1px solid #ccc;
    }
  </style>
</head>
<body>
  <h1>Furniture Store</h1>
  <select id="category-select"></select>
  <ul id="product-list"></ul>

  <script src="furniture.js"></script>
</body>
</html>
```
