"""
Generated Code Metadata:
========================
Original URL: https://fareadda.com
Prompt: Generate HTML and JavaScript code for a basic shopping cart system that can be integrated into a retail business website like fareadda.com.
Generated: DETERMINISTIC_97e9affa6f62a5b9
Batch ID: 20250622_204703
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
  <title>Shopping Cart</title>
  <style>
    /* Basic styling for the shopping cart */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .product {
      display: flex;
      justify-content: space-between;
      margin-bottom: 10px;
    }
    .cart {
      margin-top: 20px;
      border: 1px solid #ccc;
      padding: 10px;
    }
    .cart-item {
      display: flex;
      justify-content: space-between;
      margin-bottom: 10px;
    }
    .total {
      font-weight: bold;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>Shopping Cart</h1>

  <!-- Product List -->
  <div id="product-list">
    <div class="product">
      <span>Product 1 - $10</span>
      <button onclick="addToCart('Product 1', 10)">Add to Cart</button>
    </div>
    <div class="product">
      <span>Product 2 - $20</span>
      <button onclick="addToCart('Product 2', 20)">Add to Cart</button>
    </div>
    <div class="product">
      <span>Product 3 - $30</span>
      <button onclick="addToCart('Product 3', 30)">Add to Cart</button>
    </div>
  </div>

  <!-- Shopping Cart -->
  <div id="cart" class="cart">
    <h2>Your Cart</h2>
    <div id="cart-items"></div>
    <div class="total" id="cart-total">Total: $0</div>
  </div>

  <script>
    // Initialize an empty cart
    const cart = [];

    /**
     * Adds a product to the cart.
     * @param {string} name - The name of the product.
     * @param {number} price - The price of the product.
     */
    function addToCart(name, price) {
      try {
        // Check if the product is already in the cart
<<<<<<< HEAD
        const existingItem = cart.find(item => item.name === name);
        if (existingItem) {
          existingItem.quantity += 1; // Increment quantity if already in cart
=======
        const existingProduct = cart.find(item => item.name === name);
        if (existingProduct) {
          existingProduct.quantity += 1; // Increment quantity if already in cart
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        } else {
          cart.push({ name, price, quantity: 1 }); // Add new product to cart
        }
        updateCartUI(); // Update the cart display
      } catch (error) {
        console.error('Error adding to cart:', error);
      }
    }

    /**
<<<<<<< HEAD
=======
     * Updates the cart UI to reflect the current state of the cart.
     */
    function updateCartUI() {
      try {
        const cartItemsContainer = document.getElementById('cart-items');
        const cartTotalContainer = document.getElementById('cart-total');

        // Clear existing cart items
        cartItemsContainer.innerHTML = '';

        // Calculate total price
        let total = 0;

        // Render each cart item
        cart.forEach(item => {
          const cartItem = document.createElement('div');
          cartItem.className = 'cart-item';
          cartItem.innerHTML = `
            <span>${item.name} - $${item.price} x ${item.quantity}</span>
            <button onclick="removeFromCart('${item.name}')">Remove</button>
          `;
          cartItemsContainer.appendChild(cartItem);
          total += item.price * item.quantity;
        });

        // Update total price
        cartTotalContainer.textContent = `Total: $${total}`;
      } catch (error) {
        console.error('Error updating cart UI:', error);
      }
    }

    /**
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
     * Removes a product from the cart.
     * @param {string} name - The name of the product to remove.
     */
    function removeFromCart(name) {
      try {
<<<<<<< HEAD
        const index = cart.findIndex(item => item.name === name);
        if (index !== -1) {
          cart.splice(index, 1); // Remove the product from the cart
=======
        // Find the product in the cart
        const productIndex = cart.findIndex(item => item.name === name);
        if (productIndex !== -1) {
          const product = cart[productIndex];
          if (product.quantity > 1) {
            product.quantity -= 1; // Decrement quantity if more than 1
          } else {
            cart.splice(productIndex, 1); // Remove product if quantity is 1
          }
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
          updateCartUI(); // Update the cart display
        }
      } catch (error) {
        console.error('Error removing from cart:', error);
      }
    }
<<<<<<< HEAD

    /**
     * Updates the cart UI to reflect the current state of the cart.
     */
    function updateCartUI() {
      const cartItemsContainer = document.getElementById('cart-items');
      const cartTotalContainer = document.getElementById('cart-total');

      // Clear the current cart items
      cartItemsContainer.innerHTML = '';

      // Calculate the total price
      let total = 0;

      // Render each item in the cart
      cart.forEach(item => {
        total += item.price * item.quantity;

        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
          <span>${item.name} - $${item.price} x ${item.quantity}</span>
          <button onclick="removeFromCart('${item.name}')">Remove</button>
        `;
        cartItemsContainer.appendChild(cartItem);
      });

      // Update the total price display
      cartTotalContainer.textContent = `Total: $${total}`;
    }
=======
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
  </script>
</body>
</html>
```
