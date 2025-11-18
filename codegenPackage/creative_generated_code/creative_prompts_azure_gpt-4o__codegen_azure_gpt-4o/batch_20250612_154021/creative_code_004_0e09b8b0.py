"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Develop a REST API in Node.js to fetch product details from SmartPrice KE's categories, such as audio devices, video cameras, and wearables, and allow filtering by brand and price.
Generated: DETERMINISTIC_0e09b8b06654ea42
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready Node.js code for your request:

```javascript
// Import necessary modules
const express = require('express'); // Express for creating the REST API
const bodyParser = require('body-parser'); // Middleware to parse JSON request bodies

// Create an instance of the Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Mock product data for SmartPrice KE
const products = [
  { id: 1, category: 'audio devices', brand: 'Sony', price: 100, name: 'Sony Headphones' },
  { id: 2, category: 'audio devices', brand: 'Bose', price: 200, name: 'Bose Speaker' },
  { id: 3, category: 'video cameras', brand: 'Canon', price: 500, name: 'Canon EOS 200D' },
  { id: 4, category: 'video cameras', brand: 'Sony', price: 800, name: 'Sony Alpha 7' },
  { id: 5, category: 'wearables', brand: 'Fitbit', price: 150, name: 'Fitbit Charge 5' },
  { id: 6, category: 'wearables', brand: 'Apple', price: 400, name: 'Apple Watch Series 7' },
];

// Endpoint to fetch product details based on category, brand, and price filters
// URL Example: /products?category=audio devices&brand=Sony&minPrice=50&maxPrice=150
app.get('/products', (req, res) => {
  try {
    // Extract query parameters
    const { category, brand, minPrice, maxPrice } = req.query;

    // Filter products based on query parameters
    let filteredProducts = products;

    if (category) {
      filteredProducts = filteredProducts.filter(product => product.category === category);
    }

    if (brand) {
      filteredProducts = filteredProducts.filter(product => product.brand === brand);
    }

    if (minPrice) {
      filteredProducts = filteredProducts.filter(product => product.price >= parseFloat(minPrice));
    }

    if (maxPrice) {
      filteredProducts = filteredProducts.filter(product => product.price <= parseFloat(maxPrice));
    }

    // Respond with the filtered product list
    res.status(200).json({
      success: true,
      data: filteredProducts,
    });
  } catch (error) {
    // Handle unexpected errors and respond with a meaningful message
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching products',
      error: error.message,
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable for port or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Use this code to create a REST API in Node.js that fulfills the requirements. It includes filtering functionality for category, brand, and price while adhering to best practices.
