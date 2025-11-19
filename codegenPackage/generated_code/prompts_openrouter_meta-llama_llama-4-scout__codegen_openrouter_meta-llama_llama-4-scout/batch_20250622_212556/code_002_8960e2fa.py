"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Generate a code snippet in JavaScript to implement a simple e-commerce functionality for a retail partner of PDC Brush, allowing them to easily purchase products online.
Generated: DETERMINISTIC_8960e2fa8e19e1d8
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ecommerce.js

/**
 * E-commerce functionality for PDC Brush retail partner.
 * Allows retail partners to easily purchase products online.
 */

// Import required modules
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Product data (in a real application, this would be a database)
const products = [
  { id: 1, name: 'PDC Brush', price: 9.99 },
  { id: 2, name: 'PDC Mini Brush', price: 4.99 },
  { id: 3, name: 'PDC Replacement Head', price: 7.99 },
];

// Cart data (in a real application, this would be a database)
let cart = [];

// Get all products
app.get('/products', (req, res) => {
  try {
    res.json(products);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching products' });
  }
});

// Get product by ID
app.get('/products/:id', (req, res) => {
  try {
    const productId = parseInt(req.params.id);
    const product = products.find((p) => p.id === productId);
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching product' });
  }
});

// Add product to cart
app.post('/cart', (req, res) => {
  try {
    const { productId, quantity } = req.body;
    if (!productId || !quantity) {
      res.status(400).json({ message: 'Product ID and quantity are required' });
    } else {
      const product = products.find((p) => p.id === productId);
      if (!product) {
        res.status(404).json({ message: 'Product not found' });
      } else {
        const existingCartItem = cart.find((c) => c.productId === productId);
        if (existingCartItem) {
          existingCartItem.quantity += quantity;
        } else {
          cart.push({ productId, quantity });
        }
        res.json(cart);
      }
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error adding product to cart' });
  }
});

// View cart
app.get('/cart', (req, res) => {
  try {
    const cartItems = cart.map((c) => {
      const product = products.find((p) => p.id === c.productId);
      return { product, quantity: c.quantity };
    });
    res.json(cartItems);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching cart' });
  }
});

// Checkout
app.post('/checkout', (req, res) => {
  try {
    const { paymentMethod } = req.body;
    if (!paymentMethod) {
      res.status(400).json({ message: 'Payment method is required' });
    } else {
      // Simulate payment processing (in a real application, this would be integrated with a payment gateway)
      console.log('Processing payment...');
      cart = [];
      res.json({ message: 'Checkout successful' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error processing checkout' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
