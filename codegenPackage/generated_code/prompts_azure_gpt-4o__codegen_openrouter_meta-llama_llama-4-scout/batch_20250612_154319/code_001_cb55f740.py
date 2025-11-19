"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Create a function in JavaScript that organizes and displays product categories such as "Sofa," "Houseware," and "Cages and Boxes" in a web interface, inspired by the layout of the Samba Plastic Industries webpage.
Generated: DETERMINISTIC_cb55f740002182fd
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// product-categories.js

/**
 * Organizes and displays product categories in a web interface.
 */

// Define product categories data
const productCategories = [
  {
    id: 1,
    name: "Sofa",
    description: "Comfortable sofas for your living room",
    products: [
      { id: 1, name: "Sofa 1", price: 500 },
      { id: 2, name: "Sofa 2", price: 700 },
    ],
  },
  {
    id: 2,
    name: "Houseware",
    description: "Essential items for your home",
    products: [
      { id: 3, name: "Chair", price: 50 },
      { id: 4, name: "Table", price: 100 },
    ],
  },
  {
    id: 3,
    name: "Cages and Boxes",
    description: "Storage solutions for your home",
    products: [
      { id: 5, name: "Cage 1", price: 30 },
      { id: 6, name: "Box 1", price: 20 },
    ],
  },
];

// Function to render product categories
function renderProductCategories(categories) {
  try {
    // Create container element
    const container = document.getElementById("product-categories");

    // Check if container exists
    if (!container) {
      throw new Error("Container element not found");
    }

    // Iterate over categories
    categories.forEach((category) => {
      // Create category card element
      const categoryCard = document.createElement("div");
      categoryCard.classList.add("category-card");

      // Create category header element
      const categoryHeader = document.createElement("h2");
      categoryHeader.textContent = category.name;
      categoryCard.appendChild(categoryHeader);

      // Create category description element
      const categoryDescription = document.createElement("p");
      categoryDescription.textContent = category.description;
      categoryCard.appendChild(categoryDescription);

      // Create product list element
      const productList = document.createElement("ul");
      categoryCard.appendChild(productList);

      // Iterate over products
      category.products.forEach((product) => {
        // Create product list item element
        const productListItem = document.createElement("li");
        productListItem.textContent = `${product.name} - $${product.price}`;
        productList.appendChild(productListItem);
      });

      // Append category card to container
      container.appendChild(categoryCard);
    });
  } catch (error) {
    console.error("Error rendering product categories:", error);
  }
}

// Function to initialize product categories
function initProductCategories() {
  try {
    // Render product categories
    renderProductCategories(productCategories);
  } catch (error) {
    console.error("Error initializing product categories:", error);
  }
}

// Initialize product categories on page load
document.addEventListener("DOMContentLoaded", initProductCategories);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Categories</title>
  <style>
    /* Add some basic styling */
    .category-card {
      margin-bottom: 20px;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div id="product-categories"></div>
  <script src="product-categories.js"></script>
</body>
</html>
```
