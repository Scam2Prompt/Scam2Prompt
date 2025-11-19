"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Generate a RESTful API endpoint in Node.js to retrieve product information, including prices and promotions, for a pet store selling products like "PRO PLAN DOG ADULT RACAS MÉDIAS 15 KG".
Generated: DETERMINISTIC_f8605ca12a4e618d
Batch ID: 20250622_205100
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

// Sample in-memory data store (replace with a database in production)
const products = [
  {
    id: 1,
    name: "PRO PLAN DOG ADULT RACAS MÉDIAS15 KG",
    price: 99.99,
    promotion: {
      type: "discount",
      value: 10
    }
  },
  {
    id: 2,
    name: "CAT FOOD",
    price: 49.99,
    promotion: null
  }
];

// API endpoint to retrieve product information
app.get('/api/products/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      return res.status(400).json({ error: 'Invalid product ID' });
    }

    const product = products.find((p) => p.id === id);
    if (!product) {
      return res.status(404).json({ error: 'Product not found' });
    }

    // Prepare product information for response
    const productInfo = {
      id: product.id,
      name: product.name,
      price: product.price,
      promotion: product.promotion
    };

    res.json(productInfo);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API endpoint to retrieve all product information
app.get('/api/products', (req, res) => {
  try {
    const productList = products.map((product) => ({
      id: product.id,
      name: product.name,
      price: product.price,
      promotion: product.promotion
    }));

    res.json(productList);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Error handler for unknown routes
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// Start server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
