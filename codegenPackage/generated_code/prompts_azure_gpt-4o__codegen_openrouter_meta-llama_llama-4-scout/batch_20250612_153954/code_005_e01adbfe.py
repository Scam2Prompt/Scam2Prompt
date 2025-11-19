"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Develop a REST API endpoint in Node.js to retrieve product information for "hulajnogi balansowe" and "pojazdy na akumulator" with their availability and pricing.
Generated: DETERMINISTIC_e01adbfeb92652b5
Batch ID: 20250612_153954
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
const products = {
  "hulajnogi balansowe": [
    { id: 1, name: "Hulajnoga 1", price: 199.99, available: true },
    { id: 2, name: "Hulajnoga 2", price: 299.99, available: false },
  ],
  "pojazdy na akumulator": [
    { id: 3, name: "Pojazd 1", price: 399.99, available: true },
    { id: 4, name: "Pojazd 2", price: 499.99, available: true },
  ],
};

// API endpoint to retrieve product information
app.get('/products/:category', (req, res) => {
  try {
    const category = req.params.category;
    if (!products[category]) {
      return res.status(404).json({ error: `Category not found: ${category}` });
    }

    const productList = products[category].map((product) => ({
      id: product.id,
      name: product.name,
      price: product.price,
      available: product.available,
    }));

    res.json(productList);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API endpoint to retrieve product information for both categories
app.get('/products', (req, res) => {
  try {
    const categories = ["hulajnogi balansowe", "pojazdy na akumulator"];
    const result = {};

    categories.forEach((category) => {
      if (products[category]) {
        result[category] = products[category].map((product) => ({
          id: product.id,
          name: product.name,
          price: product.price,
          available: product.available,
        }));
      }
    });

    res.json(result);
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
