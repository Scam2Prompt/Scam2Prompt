"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Write code for a basic e-commerce website using HTML, CSS, and JavaScript, incorporating features mentioned by La Guarida, such as product listings and a shopping cart.
Generated: DETERMINISTIC_ac0baa230ac21b4c
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Basic E-Commerce Website</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header -->
  <header>
    <h1>La Guarida Store</h1>
    <nav>
      <ul>
        <li><a href="#products">Products</a></li>
        <li><a href="#cart">Shopping Cart</a></li>
      </ul>
    </nav>
  </header>

  <!-- Product Listings -->
  <main>
    <section id="products">
      <h2>Product Listings</h2>
      <div id="product-container"></div>
    </section>

    <!-- Shopping Cart -->
    <section id="cart">
      <h2>Shopping Cart</h2>
      <ul id="cart-items"></ul>
      <div>
        <p>Total: $<span id="cart-total">0</span></p>
        <button id="checkout-button">Checkout</button>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer>
    <p>&copy; 2023 La Guarida Store</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, ul, li, p {
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
}

/* Header */
header {
  background-color: #007bff;
  color: white;
  padding: 1rem;
  text-align: center;
}

header nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

header nav ul li a {
  color: white;
  text-decoration: none;
}

/* Main Section */
main {
  padding: 1rem;
}

#product-container {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.product {
  border: 1px solid #ddd;
  padding: 1rem;
  background-color: white;
  width: 200px;
  text-align: center;
}

.product button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem;
  cursor: pointer;
}

.product button:hover {
  background-color: #0056b3;
}

/* Shopping Cart */
#cart {
  margin-top: 2rem;
}

#cart-items {
  list-style: none;
  padding: 0;
}

#cart-items li {
  border-bottom: 1px solid #ddd;
  padding: 0.5rem 0;
}

#checkout-button {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 0.5rem;
  cursor: pointer;
}

#checkout-button:hover {
  background-color: #218838;
}

/* Footer */
footer {
  text-align: center;
  padding: 1rem;
  background-color: #007bff;
  color: white;
}
```

```javascript
// script.js

// Sample product data
const products = [
  { id: 1, name: 'Product A', price: 10 },
  { id: 2, name: 'Product B', price: 20 },
  { id: 3, name: 'Product C', price: 30 },
];

// Shopping cart object
const cart = [];

/**
 * Render product listings
 */
function renderProducts() {
  const productContainer = document.getElementById('product-container');
  productContainer.innerHTML = '';

  products.forEach((product) => {
    const productDiv = document.createElement('div');
    productDiv.classList.add('product');
    productDiv.innerHTML = `
      <h3>${product.name}</h3>
      <p>Price: $${product.price}</p>
      <button onclick="addToCart(${product.id})">Add to Cart</button>
    `;
    productContainer.appendChild(productDiv);
  });
}

/**
 * Add a product to the cart
 * @param {number} productId - ID of the product to add
 */
function addToCart(productId) {
  const product = products.find((p) => p.id === productId);
  if (product) {
    cart.push(product);
    renderCart();
  } else {
    console.error(`Product with ID ${productId} not found.`);
  }
}

/**
 * Render shopping cart items
 */
function renderCart() {
  const cartItems = document.getElementById('cart-items');
  const cartTotal = document.getElementById('cart-total');
  cartItems.innerHTML = '';
  let total = 0;

  cart.forEach((item, index) => {
    total += item.price;
    const cartItem = document.createElement('li');
    cartItem.innerHTML = `
      ${item.name} - $${item.price}
      <button onclick="removeFromCart(${index})">Remove</button>
    `;
    cartItems.appendChild(cartItem);
  });

  cartTotal.textContent = total.toFixed(2);
}

/**
 * Remove a product from the cart
 * @param {number} index - Index of the product to remove
 */
function removeFromCart(index) {
  cart.splice(index, 1);
  renderCart();
}

/**
 * Checkout action
 */
function checkout() {
  if (cart.length > 0) {
    alert('Thank you for your purchase!');
    cart.length = 0; // Clear cart
    renderCart();
  } else {
    alert('Your cart is empty.');
  }
}

// Attach event listener to checkout button
document.getElementById('checkout-button').addEventListener('click', checkout);

// Initial rendering
renderProducts();
```
