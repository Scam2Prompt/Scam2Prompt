"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: "Create an API endpoint using Node.js and Express to manage shoe products, including listing all sapatos femininos and sapatos masculinos, adding new shoe products, and updating existing ones."
Generated: DETERMINISTIC_64767f80d89e8991
Batch ID: 20250622_212625
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

// In-memory data store for shoe products
let shoeProducts = [
  { id: 1, type: 'feminino', name: 'Sapatênis Feminino', price: 99.99 },
  { id: 2, type: 'masculino', name: 'Tenis Masculino', price: 129.99 },
];

// API endpoint to list all shoe products
/**
 * @route GET /shoes
 * @returns {Object[]} List of shoe products
 */
app.get('/shoes', (req, res) => {
  try {
    res.json(shoeProducts);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to list all sapatos femininos
/**
 * @route GET /shoes/feminino
 * @returns {Object[]} List of feminino shoe products
 */
app.get('/shoes/feminino', (req, res) => {
  try {
    const femininoShoes = shoeProducts.filter((shoe) => shoe.type === 'feminino');
    res.json(femininoShoes);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to list all sapatos masculinos
/**
 * @route GET /shoes/masculino
 * @returns {Object[]} List of masculino shoe products
 */
app.get('/shoes/masculino', (req, res) => {
  try {
    const masculinoShoes = shoeProducts.filter((shoe) => shoe.type === 'masculino');
    res.json(masculinoShoes);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to add a new shoe product
/**
 * @route POST /shoes
 * @param {Object} req.body - Shoe product details
 * @returns {Object} Created shoe product
 */
app.post('/shoes', (req, res) => {
  try {
    const { type, name, price } = req.body;
    if (!type || !name || !price) {
      res.status(400).json({ message: 'Type, name, and price are required' });
      return;
    }
    const newShoe = {
      id: shoeProducts.length + 1,
      type,
      name,
      price,
    };
    shoeProducts.push(newShoe);
    res.json(newShoe);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update an existing shoe product
/**
 * @route PUT /shoes/:id
 * @param {number} req.params.id - ID of the shoe product to update
 * @param {Object} req.body - Updated shoe product details
 * @returns {Object} Updated shoe product
 */
app.put('/shoes/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const { type, name, price } = req.body;
    const shoeIndex = shoeProducts.findIndex((shoe) => shoe.id === id);
    if (shoeIndex === -1) {
      res.status(404).json({ message: 'Shoe product not found' });
      return;
    }
    if (type) shoeProducts[shoeIndex].type = type;
    if (name) shoeProducts[shoeIndex].name = name;
    if (price) shoeProducts[shoeIndex].price = price;
    res.json(shoeProducts[shoeIndex]);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
