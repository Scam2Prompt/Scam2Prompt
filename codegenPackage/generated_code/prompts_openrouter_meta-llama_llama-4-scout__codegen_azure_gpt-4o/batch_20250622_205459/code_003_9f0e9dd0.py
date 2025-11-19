"""
Generated Code Metadata:
========================
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Create a simple e-commerce website using HTML, CSS, and JavaScript, inspired by the design and layout of Papelaria Matriz, with a shopping cart and product listing features.
Generated: DETERMINISTIC_9f0e9dd01178ef5a
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papelaria Matriz - E-Commerce</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Papelaria Matriz</h1>
      <nav>
        <ul>
          <li><a href="#products">Products</a></li>
          <li><a href="#cart">Cart</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Product Listing Section -->
  <section id="products" class="container">
    <h2>Our Products</h2>
    <div class="product-list">
      <!-- Example Product -->
      <div class="product" data-id="1" data-name="Notebook" data-price="10.99">
        <img src="notebook.jpg" alt="Notebook">
        <h3>Notebook</h3>
        <p>$10.99</p>
        <button class="add-to-cart">Add to Cart</button>
      </div>
      <div class="product" data-id="2" data-name="Pen" data-price="1.99">
        <img src="pen.jpg" alt="Pen">
        <h3>Pen</h3>
        <p>$1.99</p>
        <button class="add-to-cart">Add to Cart</button>
      </div>
      <!-- Add more products as needed -->
    </div>
  </section>

  <!-- Shopping Cart Section -->
  <section id="cart" class="container">
    <h2>Your Cart</h2>
    <table>
      <thead>
        <tr>
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody id="cart-items">
        <!-- Cart items will be dynamically added here -->
      </tbody>
    </table>
    <div class="cart-total">
      <h3>Total: $<span id="cart-total">0.00</span></h3>
    </div>
  </section>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, table, th, td {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f4f4f4;
  color: #333;
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
header {
  background: #333;
  color: #fff;
  padding: 1rem 0;
}

header h1 {
  text-align: center;
}

header nav ul {
  list-style: none;
  text-align: center;
}

header nav ul li {
  display: inline;
  margin: 0 10px;
}

header nav ul li a {
  color: #fff;
  text-decoration: none;
}

/* Product Section */
#products {
  margin: 2rem 0;
}

.product-list {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.product {
  background: #fff;
  border: 1px solid #ddd;
  padding: 1rem;
  text-align: center;
  width: calc(33.333% - 1rem);
}

.product img {
  max-width: 100%;
  height: auto;
}

.product h3 {
  margin: 0.5rem 0;
}

.product p {
  color: #007BFF;
}

.product button {
  background: #007BFF;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.product button:hover {
  background: #0056b3;
}

/* Cart Section */
#cart {
  margin: 2rem 0;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 0.5rem;
  text-align: center;
}

.cart-total {
  text-align: right;
  margin-top: 1rem;
}
```

```javascript
// script.js

// Shopping Cart Data
let cart = [];

// Function to update the cart display
function updateCart() {
  const cartItems = document.getElementById('cart-items');
  const cartTotal = document.getElementById('cart-total');
  cartItems.innerHTML = '';
  let total = 0;

  cart.forEach(item => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${item.name}</td>
      <td>$${item.price.toFixed(2)}</td>
      <td>${item.quantity}</td>
      <td>$${(item.price * item.quantity).toFixed(2)}</td>
      <td><button class="remove-item" data-id="${item.id}">Remove</button></td>
    `;
    cartItems.appendChild(row);
    total += item.price * item.quantity;
  });

  cartTotal.textContent = total.toFixed(2);

  // Add event listeners to remove buttons
  document.querySelectorAll('.remove-item').forEach(button => {
    button.addEventListener('click', removeFromCart);
  });
}

// Function to add a product to the cart
function addToCart(event) {
  const product = event.target.closest('.product');
  const id = product.dataset.id;
  const name = product.dataset.name;
  const price = parseFloat(product.dataset.price);

  const existingItem = cart.find(item => item.id === id);
  if (existingItem) {
    existingItem.quantity += 1;
  } else {
    cart.push({ id, name, price, quantity: 1 });
  }

  updateCart();
}

// Function to remove a product from the cart
function removeFromCart(event) {
  const id = event.target.dataset.id;
  cart = cart.filter(item => item.id !== id);
  updateCart();
}

// Add event listeners to "Add to Cart" buttons
document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', addToCart);
});

// Initialize cart display
updateCart();
```
