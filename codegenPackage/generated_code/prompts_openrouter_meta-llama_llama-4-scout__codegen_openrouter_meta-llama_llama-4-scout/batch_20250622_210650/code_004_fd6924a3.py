"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Design a simple API using Node.js to manage Silver Seals' product catalog, including seal rings, 'O' rings, and oil seals, with features for searching by application and product category.
Generated: DETERMINISTIC_fd6924a3e5d1e8a4
Batch ID: 20250622_210650
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
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Define product catalog data
let products = [
  { id: 1, name: 'Seal Ring 1', category: 'Seal Rings', application: 'Industrial' },
  { id: 2, name: 'O Ring 1', category: 'O Rings', application: 'Automotive' },
  { id: 3, name: 'Oil Seal 1', category: 'Oil Seals', application: 'Industrial' },
  { id: 4, name: 'Seal Ring 2', category: 'Seal Rings', application: 'Aerospace' },
  { id: 5, name: 'O Ring 2', category: 'O Rings', application: 'Marine' },
];

// API endpoint to get all products
app.get('/api/products', (req, res) => {
  try {
    res.json(products);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get product by ID
app.get('/api/products/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const product = products.find((p) => p.id === id);
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create new product
app.post('/api/products', (req, res) => {
  try {
    const { name, category, application } = req.body;
    if (!name || !category || !application) {
      res.status(400).json({ message: 'Name, category, and application are required' });
    } else {
      const newProduct = {
        id: products.length + 1,
        name,
        category,
        application,
      };
      products.push(newProduct);
      res.json(newProduct);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update existing product
app.put('/api/products/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const product = products.find((p) => p.id === id);
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      const { name, category, application } = req.body;
      if (name) product.name = name;
      if (category) product.category = category;
      if (application) product.application = application;
      res.json(product);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete product
app.delete('/api/products/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = products.findIndex((p) => p.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      products.splice(index, 1);
      res.json({ message: 'Product deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to search products by application
app.get('/api/products/by-application/:application', (req, res) => {
  try {
    const application = req.params.application;
    const filteredProducts = products.filter((p) => p.application.toLowerCase() === application.toLowerCase());
    res.json(filteredProducts);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to search products by category
app.get('/api/products/by-category/:category', (req, res) => {
  try {
    const category = req.params.category;
    const filteredProducts = products.filter((p) => p.category.toLowerCase() === category.toLowerCase());
    res.json(filteredProducts);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
