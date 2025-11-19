"""
Generated Code Metadata:
========================
Original URL: https://celinedionshop.com
Prompt: Generate a RESTful API using Node.js and Express.js to manage Celine Dion merchandise inventory, including endpoints for creating, reading, updating, and deleting products.
Generated: DETERMINISTIC_71a173c05fe53303
Batch ID: 20250622_212358
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
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define product schema
const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  quantity: Number,
});

// Create product model
const Product = mongoose.model('Product', productSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all products
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find().exec();
    res.json(products);
  } catch (error) {
    res.status(500).json({ message: 'Failed to retrieve products' });
  }
});

// Get product by ID
app.get('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id).exec();
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (error) {
    res.status(500).json({ message: 'Failed to retrieve product' });
  }
});

// Create new product
app.post('/api/products', async (req, res) => {
  try {
    const product = new Product(req.body);
    await product.save();
    res.status(201).json(product);
  } catch (error) {
    res.status(400).json({ message: 'Failed to create product' });
  }
});

// Update existing product
app.put('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    }).exec();
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (error) {
    res.status(400).json({ message: 'Failed to update product' });
  }
});

// Delete product
app.delete('/api/products/:id', async (req, res) => {
  try {
    await Product.findByIdAndRemove(req.params.id).exec();
    res.status(204).json({ message: 'Product deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Failed to delete product' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// For running this file 
// node app.js 
// Make sure to install required packages 
// npm install express mongoose dotenv
```
