"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Generate a JavaScript code to create a product catalog page similar to the one on ebrasilbrazz, which displays products with images, names, and prices, and allows users to sort and filter products.
Generated: DETERMINISTIC_3940d676c8830638
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog Page Implementation

// Sample product data (In a real-world scenario, this would come from a database or API)
const products = [
  { id: 1, name: "Product A", price: 25.99, image: "product-a.jpg", category: "Electronics" },
  { id: 2, name: "Product B", price: 15.49, image: "product-b.jpg", category: "Books" },
  { id: 3, name: "Product C", price: 45.00, image: "product-c.jpg", category: "Clothing" },
  { id: 4, name: "Product D", price: 12.99, image: "product-d.jpg", category: "Books" },
  { id: 5, name: "Product E", price: 99.99, image: "product-e.jpg", category: "Electronics" },
];

// DOM Elements
const productContainer = document.getElementById("product-container");
const sortSelect = document.getElementById("sort-select");
const filterSelect = document.getElementById("filter-select");

// Function to render products on the page
function renderProducts(productList) {
  productContainer.innerHTML = ""; // Clear existing products

  productList.forEach((product) => {
    // Create product card
    const productCard = document.createElement("div");
    productCard.className = "product-card";

    // Product image
    const productImage = document.createElement("img");
    productImage.src = product.image;
    productImage.alt = product.name;
    productImage.className = "product-image";

    // Product name
    const productName = document.createElement("h3");
    productName.textContent = product.name;
    productName.className = "product-name";

    // Product price
    const productPrice = document.createElement("p");
    productPrice.textContent = `$${product.price.toFixed(2)}`;
    productPrice.className = "product-price";

    // Append elements to product card
    productCard.appendChild(productImage);
    productCard.appendChild(productName);
    productCard.appendChild(productPrice);

    // Append product card to container
    productContainer.appendChild(productCard);
  });
}

// Function to sort products
function sortProducts(products, criteria) {
  const sortedProducts = [...products];
  if (criteria === "price-asc") {
    sortedProducts.sort((a, b) => a.price - b.price);
  } else if (criteria === "price-desc") {
    sortedProducts.sort((a, b) => b.price - a.price);
  } else if (criteria === "name-asc") {
    sortedProducts.sort((a, b) => a.name.localeCompare(b.name));
  } else if (criteria === "name-desc") {
    sortedProducts.sort((a, b) => b.name.localeCompare(a.name));
  }
  return sortedProducts;
}

// Function to filter products
function filterProducts(products, category) {
  if (category === "all") {
    return products;
  }
  return products.filter((product) => product.category === category);
}

// Event listener for sorting
sortSelect.addEventListener("change", () => {
  const sortCriteria = sortSelect.value;
  const filteredProducts = filterProducts(products, filterSelect.value);
  const sortedProducts = sortProducts(filteredProducts, sortCriteria);
  renderProducts(sortedProducts);
});

// Event listener for filtering
filterSelect.addEventListener("change", () => {
  const selectedCategory = filterSelect.value;
  const filteredProducts = filterProducts(products, selectedCategory);
  const sortedProducts = sortProducts(filteredProducts, sortSelect.value);
  renderProducts(sortedProducts);
});

// Initial render
renderProducts(products);
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Catalog</title>
  <style>
    /* Basic styles for the product catalog */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    #controls {
      display: flex;
      justify-content: space-between;
      padding: 10px;
      background-color: #f4f4f4;
    }
    #product-container {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      padding: 20px;
    }
    .product-card {
      border: 1px solid #ddd;
      border-radius: 5px;
      padding: 10px;
      width: 200px;
      text-align: center;
    }
    .product-image {
      max-width: 100%;
      height: auto;
    }
    .product-name {
      font-size: 18px;
      margin: 10px 0;
    }
    .product-price {
      color: #007BFF;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <div id="controls">
    <select id="sort-select">
      <option value="price-asc">Sort by Price: Low to High</option>
      <option value="price-desc">Sort by Price: High to Low</option>
      <option value="name-asc">Sort by Name: A to Z</option>
      <option value="name-desc">Sort by Name: Z to A</option>
    </select>
    <select id="filter-select">
      <option value="all">All Categories</option>
      <option value="Electronics">Electronics</option>
      <option value="Books">Books</option>
      <option value="Clothing">Clothing</option>
    </select>
  </div>
  <div id="product-container"></div>
  <script src="script.js"></script>
</body>
</html>
```
