"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Create a RESTful API endpoint in Node.js that allows users to inquire about different types of acrylic yarns, referencing the product range of Ramji Acro.
Generated: DETERMINISTIC_2f0848fb93b218e8
Batch ID: 20250612_160853
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

// Define the product range of Ramji Acro
const ramjiAcroProducts = {
  "acrylic-blend": [
    { id: 1, name: "Acrylic Blend 1", weight: "100g", color: "Red" },
    { id: 2, name: "Acrylic Blend 2", weight: "200g", color: "Blue" },
  ],
  "pure-acrylic": [
    { id: 3, name: "Pure Acrylic 1", weight: "150g", color: "Green" },
    { id: 4, name: "Pure Acrylic 2", weight: "250g", color: "Yellow" },
  ],
  "fancy-yarn": [
    { id: 5, name: "Fancy Yarn 1", weight: "120g", color: "Pink" },
    { id: 6, name: "Fancy Yarn 2", weight: "220g", color: "Purple" },
  ],
};

// API endpoint to inquire about different types of acrylic yarns
app.get('/api/ramji-acro/products/:yarnType', (req, res) => {
  try {
    const yarnType = req.params.yarnType.toLowerCase();
    if (!ramjiAcroProducts[yarnType]) {
      return res.status(404).json({ error: `Yarn type '${yarnType}' not found` });
    }
    res.json(ramjiAcroProducts[yarnType]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API endpoint to get all products
app.get('/api/ramji-acro/products', (req, res) => {
  try {
    const allProducts = Object.values(ramjiAcroProducts).flat();
    res.json(allProducts);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API endpoint to get a specific product by ID
app.get('/api/ramji-acro/products/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const allProducts = Object.values(ramjiAcroProducts).flat();
    const product = allProducts.find((p) => p.id === id);
    if (!product) {
      return res.status(404).json({ error: `Product with ID ${id} not found` });
    }
    res.json(product);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
