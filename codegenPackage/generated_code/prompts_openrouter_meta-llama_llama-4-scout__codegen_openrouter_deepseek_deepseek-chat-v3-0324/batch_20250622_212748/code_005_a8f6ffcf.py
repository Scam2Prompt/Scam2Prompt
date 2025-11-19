"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Create a RESTful API using Node.js to handle CRUD operations for Yobugo's product catalog, including endpoints for creating, reading, updating, and deleting products.
Generated: DETERMINISTIC_a8f6ffcff0971c9f
Batch ID: 20250622_212748
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/yobugo_catalog', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Product Schema
const productSchema = new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  description: { type: String, required: true },
  price: { type: Number, required: true, min: 0 },
  category: { type: String, required: true },
  stock: { type: Number, required: true, min: 0 },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Product Model
const Product = mongoose.model('Product', productSchema);

// Helper function for error handling
const handleError = (res, error, statusCode = 500) => {
  console.error(error);
  res.status(statusCode).json({ error: error.message });
};

// Routes

// Create a new product
app.post('/api/products', async (req, res) => {
  try {
    const { name, description, price, category, stock } = req.body;
    
    if (!name || !description || !price || !category || !stock) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const product = new Product({
      name,
      description,
      price,
      category,
      stock
    });

    const savedProduct = await product.save();
    res.status(201).json(savedProduct);
  } catch (error) {
    handleError(res, error);
  }
});

// Get all products
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find().sort({ createdAt: -1 });
    res.json(products);
  } catch (error) {
    handleError(res, error);
  }
});

// Get a single product by ID
app.get('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) {
      return res.status(404).json({ error: 'Product not found' });
    }
    res.json(product);
  } catch (error) {
    handleError(res, error);
  }
});

// Update a product
app.put('/api/products/:id', async (req, res) => {
  try {
    const { name, description, price, category, stock } = req.body;
    
    if (!name || !description || !price || !category || !stock) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const updatedProduct = await Product.findByIdAndUpdate(
      req.params.id,
      {
        name,
        description,
        price,
        category,
        stock,
        updatedAt: Date.now()
      },
      { new: true }
    );

    if (!updatedProduct) {
      return res.status(404).json({ error: 'Product not found' });
    }

    res.json(updatedProduct);
  } catch (error) {
    handleError(res, error);
  }
});

// Delete a product
app.delete('/api/products/:id', async (req, res) => {
  try {
    const deletedProduct = await Product.findByIdAndDelete(req.params.id);
    if (!deletedProduct) {
      return res.status(404).json({ error: 'Product not found' });
    }
    res.status(204).send();
  } catch (error) {
    handleError(res, error);
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date() });
});

// Error handling middleware
app.use((err, req, res, next) => {
  handleError(res, err);
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
