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
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample product data
const products = [
  {
    id: 1,
    name: 'Herbal Tea Blend',
    ingredients: ['Chamomile', 'Peppermint', 'Lemon Balm'],
    healthBenefits: ['Promotes relaxation', 'Aids digestion', 'Reduces stress'],
    recommendedUses: ['Before bedtime', 'After meals', 'During stressful periods']
  },
  {
    id: 2,
    name: 'Detox Infusion',
    ingredients: ['Dandelion', 'Nettle', 'Ginger'],
    healthBenefits: ['Supports liver function', 'Boosts immunity', 'Reduces inflammation'],
    recommendedUses: ['Morning routine', 'During seasonal changes', 'After indulgent meals']
  },
  {
    id: 3,
    name: 'Energy Boost',
    ingredients: ['Green Tea', 'Ginseng', 'Maca Root'],
    healthBenefits: ['Enhances focus', 'Increases energy', 'Improves stamina'],
    recommendedUses: ['Morning start', 'Pre-workout', 'Mid-afternoon slump']
  }
];

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Get all products
app.get('/products', (req, res) => {
  try {
    res.status(200).json(products);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get product by ID
app.get('/products/:id', (req, res) => {
  try {
    const productId = parseInt(req.params.id);
    const product = products.find(p => p.id === productId);
    
    if (!product) {
      return res.status(404).json({ error: 'Product not found' });
    }
    
    res.status(200).json(product);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
