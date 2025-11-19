"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Suggest a way to implement a shopping cart feature for electronic products on chandkalaco.com using Node.js.
Generated: DETERMINISTIC_5147fa59f44d37c2
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// shoppingCart.js

// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const uuid = require('uuid'); // Generates unique IDs for cart items
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON payloads

// In-memory data store for simplicity (replace with a proper database in production)
const products = [
  { id: '1', name: 'Laptop', price: 1000 },
  { id: '2', name: 'Smartphone', price: 700 },
  { id: '3', name: 'Tablet', price: 400 },
];

const carts = {}; // Stores shopping carts by user ID

/**
 * Get list of available products.
 * Endpoint: GET /products
 */
app.get('/products', (req, res) => {
  res.status(200).json(products);
});

/**
 * Add a product to the shopping cart.
 * Endpoint: POST /cart/:userId
 * Request Body: { "productId": "1", "quantity": 2 }
 */
app.post('/cart/:userId', (req, res) => {
  const { userId } = req.params;
  const { productId, quantity } = req.body;

  // Validate request data
  if (!productId || !quantity || quantity <= 0) {
    return res.status(400).json({ error: 'Invalid productId or quantity' });
  }

  // Find the product
  const product = products.find((p) => p.id === productId);
  if (!product) {
    return res.status(404).json({ error: 'Product not found' });
  }

  // Initialize the user's cart if it doesn't exist
  if (!carts[userId]) {
    carts[userId] = [];
  }

  // Check if the product is already in the cart
  const cartItem = carts[userId].find((item) => item.productId === productId);
  if (cartItem) {
    // Update quantity if product already exists in cart
    cartItem.quantity += quantity;
  } else {
    // Add new product to cart
    carts[userId].push({
      cartItemId: uuid.v4(), // Unique ID for cart item
      productId: product.id,
      name: product.name,
      price: product.price,
      quantity: quantity,
    });
  }

  res.status(200).json({ message: 'Product added to cart', cart: carts[userId] });
});

/**
 * View the user's shopping cart.
 * Endpoint: GET /cart/:userId
 */
app.get('/cart/:userId', (req, res) => {
  const { userId } = req.params;

  // Retrieve cart for the user
  const cart = carts[userId];
  if (!cart) {
    return res.status(404).json({ error: 'Cart not found' });
  }

  res.status(200).json({ cart });
});

/**
 * Remove a product from the shopping cart.
 * Endpoint: DELETE /cart/:userId/:cartItemId
 */
app.delete('/cart/:userId/:cartItemId', (req, res) => {
  const { userId, cartItemId } = req.params;

  // Retrieve cart for the user
  const cart = carts[userId];
  if (!cart) {
    return res.status(404).json({ error: 'Cart not found' });
  }

  // Find the cart item
  const itemIndex = cart.findIndex((item) => item.cartItemId === cartItemId);
  if (itemIndex === -1) {
    return res.status(404).json({ error: 'Cart item not found' });
  }

  // Remove the item from the cart
  cart.splice(itemIndex, 1);

  res.status(200).json({ message: 'Product removed from cart', cart });
});

/**
 * Clear the user's shopping cart.
 * Endpoint: DELETE /cart/:userId
 */
app.delete('/cart/:userId', (req, res) => {
  const { userId } = req.params;

  // Check if cart exists
  if (!carts[userId]) {
    return res.status(404).json({ error: 'Cart not found' });
  }

  // Clear the cart
  delete carts[userId];

  res.status(200).json({ message: 'Cart cleared' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
