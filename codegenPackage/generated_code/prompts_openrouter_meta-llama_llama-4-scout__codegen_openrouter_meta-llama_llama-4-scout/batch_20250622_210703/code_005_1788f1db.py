"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write a Node.js code snippet to create a RESTful API for managing orders and inventory for a maritime supply company that offers a wide range of products and services.
Generated: DETERMINISTIC_1788f1db1e06855f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for products
const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  quantity: Number,
  price: Number,
});

// Define schema for orders
const orderSchema = new mongoose.Schema({
  customerName: String,
  productId: { type: mongoose.Schema.Types.ObjectId, ref: 'Product' },
  quantity: Number,
  status: String,
});

// Create models
const Product = mongoose.model('Product', productSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all products
app.get('/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch products' });
  }
});

// Get product by ID
app.get('/products/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch product' });
  }
});

// Create new product
app.post('/products', async (req, res) => {
  try {
    const product = new Product(req.body);
    await product.save();
    res.json(product);
  } catch (err) {
    res.status(400).json({ message: 'Failed to create product' });
  }
});

// Update existing product
app.put('/products/:id', async (req, res) => {
  try {
    const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to update product' });
  }
});

// Delete product
app.delete('/products/:id', async (req, res) => {
  try {
    await Product.findByIdAndRemove(req.params.id);
    res.json({ message: 'Product deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Failed to delete product' });
  }
});

// Get all orders
app.get('/orders', async (req, res) => {
  try {
    const orders = await Order.find().populate('productId');
    res.json(orders);
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch orders' });
  }
});

// Get order by ID
app.get('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id).populate('productId');
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch order' });
  }
});

// Create new order
app.post('/orders', async (req, res) => {
  try {
    const order = new Order(req.body);
    await order.save();
    res.json(order);
  } catch (err) {
    res.status(400).json({ message: 'Failed to create order' });
  }
});

// Update existing order
app.put('/orders/:id', async (req, res) => {
  try {
    const order = await Order.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to update order' });
  }
});

// Delete order
app.delete('/orders/:id', async (req, res) => {
  try {
    await Order.findByIdAndRemove(req.params.id);
    res.json({ message: 'Order deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Failed to delete order' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// .env file
DB_URL="mongodb://localhost:27017/maritime-supply"
PORT=3000
```

```json
// Example product JSON
{
  "name": "Life Jacket",
  "description": "A maritime safety product",
  "quantity": 100,
  "price": 50.0
}
```

```json
// Example order JSON
{
  "customerName": "John Doe",
  "productId": "productId",
  "quantity": 2,
  "status": "pending"
}
```
