"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: "Generate a RESTful API endpoint in Node.js to manage furniture products, including sofas, beds, and chairs, with properties like name, price, and dimensions."
Generated: DETERMINISTIC_fa2f6ecfc370b06a
Batch ID: 20250622_205211
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
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory database for furniture products
let furnitureProducts = [];

// Furniture product schema
/**
 * @typedef {Object} FurnitureProduct
 * @property {string} id - Unique identifier
 * @property {string} name - Product name
 * @property {string} type - Product type (sofa, bed, chair)
 * @property {number} price - Product price
 * @property {Object} dimensions - Product dimensions
 * @property {number} dimensions.length - Length in cm
 * @property {number} dimensions.width - Width in cm
 * @property {number} dimensions.height - Height in cm
 */

// Helper function to validate furniture product
const validateFurnitureProduct = (product) => {
  if (!product.name || typeof product.name !== 'string') {
    return { valid: false, message: 'Invalid or missing product name' };
  }
  if (!product.type || !['sofa', 'bed', 'chair'].includes(product.type)) {
    return { valid: false, message: 'Invalid or missing product type' };
  }
  if (!product.price || typeof product.price !== 'number' || product.price <= 0) {
    return { valid: false, message: 'Invalid or missing price' };
  }
  if (!product.dimensions || 
      typeof product.dimensions.length !== 'number' || product.dimensions.length <= 0 ||
      typeof product.dimensions.width !== 'number' || product.dimensions.width <= 0 ||
      typeof product.dimensions.height !== 'number' || product.dimensions.height <= 0) {
    return { valid: false, message: 'Invalid or missing dimensions' };
  }
  return { valid: true };
};

// GET all furniture products
app.get('/api/products', (req, res) => {
  try {
    res.status(200).json(furnitureProducts);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET a specific furniture product by ID
app.get('/api/products/:id', (req, res) => {
  try {
    const product = furnitureProducts.find(p => p.id === req.params.id);
    if (!product) {
      return res.status(404).json({ error: 'Product not found' });
    }
    res.status(200).json(product);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// POST a new furniture product
app.post('/api/products', (req, res) => {
  try {
    const validation = validateFurnitureProduct(req.body);
    if (!validation.valid) {
      return res.status(400).json({ error: validation.message });
    }

    const newProduct = {
      id: uuidv4(),
      name: req.body.name,
      type: req.body.type,
      price: req.body.price,
      dimensions: req.body.dimensions
    };

    furnitureProducts.push(newProduct);
    res.status(201).json(newProduct);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// PUT update an existing furniture product
app.put('/api/products/:id', (req, res) => {
  try {
    const productIndex = furnitureProducts.findIndex(p => p.id === req.params.id);
    if (productIndex === -1) {
      return res.status(404).json({ error: 'Product not found' });
    }

    const validation = validateFurnitureProduct(req.body);
    if (!validation.valid) {
      return res.status(400).json({ error: validation.message });
    }

    furnitureProducts[productIndex] = {
      id: req.params.id,
      name: req.body.name,
      type: req.body.type,
      price: req.body.price,
      dimensions: req.body.dimensions
    };

    res.status(200).json(furnitureProducts[productIndex]);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// DELETE a furniture product
app.delete('/api/products/:id', (req, res) => {
  try {
    const productIndex = furnitureProducts.findIndex(p => p.id === req.params.id);
    if (productIndex === -1) {
      return res.status(404).json({ error: 'Product not found' });
    }

    furnitureProducts = furnitureProducts.filter(p => p.id !== req.params.id);
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
