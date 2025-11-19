"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Develop a simple API using Node.js to provide information about Infusión's products, including their ingredients, health benefits, and recommended uses.
Generated: DETERMINISTIC_24eaedb7be12bd8f
Batch ID: 20250622_205045
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

// Middleware to handle JSON data
app.use(express.json());

// Infusión's products data
const products = [
  {
    id: 1,
    name: 'Chamomile Tea',
    ingredients: ['Chamomile flowers'],
    healthBenefits: ['Promotes relaxation', 'Improves sleep quality'],
    recommendedUses: ['Before bedtime', 'During stress']
  },
  {
    id: 2,
    name: 'Peppermint Tea',
    ingredients: ['Peppermint leaves'],
    healthBenefits: ['Aids digestion', 'Relieves headaches'],
    recommendedUses: ['After meals', 'During morning']
  },
  {
    id: 3,
    name: 'Ginger Tea',
    ingredients: ['Ginger root'],
    healthBenefits: ['Soothes nausea', 'Reduces inflammation'],
    recommendedUses: ['During morning', 'Before exercise']
  }
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

// API endpoint to create a new product
app.post('/api/products', (req, res) => {
  try {
    const { name, ingredients, healthBenefits, recommendedUses } = req.body;
    if (!name || !ingredients || !healthBenefits || !recommendedUses) {
      res.status(400).json({ message: 'All fields are required' });
    } else {
      const newProduct = {
        id: products.length + 1,
        name,
        ingredients,
        healthBenefits,
        recommendedUses
      };
      products.push(newProduct);
      res.json(newProduct);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update a product
app.put('/api/products/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const product = products.find((p) => p.id === id);
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      const { name, ingredients, healthBenefits, recommendedUses } = req.body;
      if (name) product.name = name;
      if (ingredients) product.ingredients = ingredients;
      if (healthBenefits) product.healthBenefits = healthBenefits;
      if (recommendedUses) product.recommendedUses = recommendedUses;
      res.json(product);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete a product
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

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
