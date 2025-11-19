"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Create a RESTful API endpoint in Node.js that allows users to inquire about different types of acrylic yarns, referencing the product range of Ramji Acro.
Generated: DETERMINISTIC_2f0848fb93b218e8
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse request bodies

// Initialize the Express application
const app = express();
const PORT = 3000; // Define the port where the server will run

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies

// Dummy data representing the product range of Ramji Acro acrylic yarns
const yarnProducts = [
  {
    id: 1,
    name: "Classic Acrylic Yarn",
    description: "High-quality acrylic yarn suitable for knitting and crocheting.",
    colorRange: ["Red", "Blue", "Green", "Yellow", "White"],
    pricePerUnit: 5.99,
    unit: "per skein",
  },
  {
    id: 2,
    name: "Soft Touch Acrylic Yarn",
    description: "Extremely soft acrylic yarn ideal for baby clothes and blankets.",
    colorRange: ["Pink", "Sky Blue", "Mint Green", "White"],
    pricePerUnit: 6.99,
    unit: "per skein",
  },
  {
    id: 3,
    name: "Eco-Friendly Acrylic Yarn",
    description: "Made from recycled materials, perfect for eco-conscious projects.",
    colorRange: ["Earth Brown", "Leaf Green", "Ocean Blue"],
    pricePerUnit: 7.49,
    unit: "per skein",
  },
];

// API endpoint to get all acrylic yarn products
app.get('/api/yarns', (req, res) => {
  try {
    // Respond with the list of yarn products
    res.status(200).json({ success: true, data: yarnProducts });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching yarn products:', error);
    res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
});

// API endpoint to get a specific yarn product by ID
app.get('/api/yarns/:id', (req, res) => {
  try {
    const productId = parseInt(req.params.id, 10); // Parse the ID from the route parameter
    const product = yarnProducts.find((yarn) => yarn.id === productId); // Find the product with the matching ID

    if (!product) {
      // If product is not found, return a 404 response
      return res.status(404).json({ success: false, message: 'Product not found' });
    }

    // Respond with the found product
    res.status(200).json({ success: true, data: product });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching yarn product:', error);
    res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
});

// API endpoint to search yarn products by name
app.get('/api/yarns/search', (req, res) => {
  try {
    const { query } = req.query; // Extract the search query from the request
    if (!query) {
      // If query parameter is missing, return a 400 Bad Request response
      return res.status(400).json({ success: false, message: 'Search query is required' });
    }

    // Filter yarn products by name, case-insensitive
    const matchedProducts = yarnProducts.filter((yarn) =>
      yarn.name.toLowerCase().includes(query.toLowerCase())
    );

    // Respond with the matched products
    res.status(200).json({ success: true, data: matchedProducts });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error searching yarn products:', error);
    res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
