"""
Generated Code Metadata:
========================
Original URL: https://sevenkleather.com
Prompt: "Generate a RESTful API endpoint in Node.js for retrieving product details, such as description, price, and images, for a leather handbag or wallet."
Generated: DETERMINISTIC_05052816f385d6a3
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Express framework for building APIs
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000; // Use environment variable for port or default to 3000

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Mock database for product details
const products = [
  {
    id: 1,
    name: 'Leather Handbag',
    description: 'A premium leather handbag with elegant design.',
    price: 150.0,
    images: ['handbag1.jpg', 'handbag2.jpg']
  },
  {
    id: 2,
    name: 'Leather Wallet',
    description: 'A stylish leather wallet with multiple compartments.',
    price: 50.0,
    images: ['wallet1.jpg', 'wallet2.jpg']
  }
];

// Route: GET /api/products/:id
// Description: Retrieve product details by ID
app.get('/api/products/:id', (req, res) => {
  try {
    const productId = parseInt(req.params.id, 10); // Parse product ID from URL
    if (isNaN(productId)) {
      // Validate that the ID is a number
      return res.status(400).json({ error: 'Invalid product ID. Must be a number.' });
    }

    // Find the product in the mock database
    const product = products.find((p) => p.id === productId);

    if (!product) {
      // If product not found, return 404
      return res.status(404).json({ error: 'Product not found.' });
    }

    // Return product details
    res.status(200).json(product);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error retrieving product details:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
