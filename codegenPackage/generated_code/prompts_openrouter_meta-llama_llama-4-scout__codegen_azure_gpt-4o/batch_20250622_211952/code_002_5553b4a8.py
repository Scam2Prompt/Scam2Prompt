"""
Generated Code Metadata:
========================
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Generate a JavaScript code to create a product catalog page for a sports supplement website, featuring products like Creatine Hardcore and Nutri Whey Protein.
Generated: DETERMINISTIC_5553b4a807a3dc6b
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog Page for a Sports Supplement Website

// Sample product data
const products = [
  {
    id: 1,
    name: "Creatine Hardcore",
    description: "Boost your performance with high-quality creatine.",
    price: 29.99,
    imageUrl: "images/creatine-hardcore.jpg",
  },
  {
    id: 2,
    name: "Nutri Whey Protein",
    description: "Premium whey protein for muscle recovery and growth.",
    price: 49.99,
    imageUrl: "images/nutri-whey-protein.jpg",
  },
];

// Function to create a product card
function createProductCard(product) {
  // Create the main container for the product card
  const card = document.createElement("div");
  card.className = "product-card";

  // Create and append the product image
  const image = document.createElement("img");
  image.src = product.imageUrl;
  image.alt = product.name;
  image.className = "product-image";
  card.appendChild(image);

  // Create and append the product name
  const name = document.createElement("h2");
  name.textContent = product.name;
  name.className = "product-name";
  card.appendChild(name);

  // Create and append the product description
  const description = document.createElement("p");
  description.textContent = product.description;
  description.className = "product-description";
  card.appendChild(description);

  // Create and append the product price
  const price = document.createElement("p");
  price.textContent = `$${product.price.toFixed(2)}`;
  price.className = "product-price";
  card.appendChild(price);

  // Create and append the "Add to Cart" button
  const button = document.createElement("button");
  button.textContent = "Add to Cart";
  button.className = "add-to-cart-button";
  button.addEventListener("click", () => {
    addToCart(product);
  });
  card.appendChild(button);

  return card;
}

// Function to render the product catalog
function renderProductCatalog(products) {
  // Get the container element for the catalog
  const catalogContainer = document.getElementById("product-catalog");

  // Clear any existing content in the container
  catalogContainer.innerHTML = "";

  // Loop through the products and create product cards
  products.forEach((product) => {
    const productCard = createProductCard(product);
    catalogContainer.appendChild(productCard);
  });
}

// Function to handle adding a product to the cart
function addToCart(product) {
  try {
    // Simulate adding the product to the cart (e.g., updating a cart array or making an API call)
    console.log(`Product added to cart: ${product.name}`);
    alert(`${product.name} has been added to your cart.`);
  } catch (error) {
    console.error("Error adding product to cart:", error);
    alert("An error occurred while adding the product to your cart. Please try again.");
  }
}

// Initialize the product catalog on page load
document.addEventListener("DOMContentLoaded", () => {
  renderProductCatalog(products);
});
```

```html
<!-- HTML Structure for the Product Catalog Page -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sports Supplement Product Catalog</title>
  <style>
    /* Basic styles for the product catalog */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    #product-catalog {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      padding: 20px;
      justify-content: center;
    }
    .product-card {
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      width: 300px;
      padding: 20px;
      text-align: center;
    }
    .product-image {
      max-width: 100%;
      border-radius: 8px;
    }
    .product-name {
      font-size: 1.5em;
      margin: 10px 0;
    }
    .product-description {
      color: #555;
      margin: 10px 0;
    }
    .product-price {
      font-size: 1.2em;
      font-weight: bold;
      margin: 10px 0;
    }
    .add-to-cart-button {
      background-color: #28a745;
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: 10px 20px;
      cursor: pointer;
      font-size: 1em;
    }
    .add-to-cart-button:hover {
      background-color: #218838;
    }
  </style>
</head>
<body>
  <header>
    <h1 style="text-align: center; padding: 20px;">Sports Supplement Product Catalog</h1>
  </header>
  <main>
    <div id="product-catalog"></div>
  </main>
  <script src="script.js"></script>
</body>
</html>
```
