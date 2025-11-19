"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopmetlife.pk
Prompt: Construct a RESTful API endpoint in Node.js that returns a list of all skin care products from the ShopMetlife catalog, including their prices and availability.
Generated: DETERMINISTIC_492614d0461ef400
Batch ID: 20250612_161231
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.shopmetlife.com/products?category=skin_care": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
// Required dependencies
const express = require('express');
const axios = require('axios');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Function to fetch skin care products from ShopMetlife catalog
const fetchSkinCareProducts = async () => {
    try {
        // Replace with the actual API endpoint for ShopMetlife
        const response = await axios.get('https://api.shopmetlife.com/products?category=skin_care');
        return response.data;
    } catch (error) {
        console.error('Error fetching products:', error.message);
        throw new Error('Could not retrieve skin care products');
    }
};

// RESTful API endpoint to get skin care products
app.get('/api/skincare-products', async (req, res) => {
    try {
        const products = await fetchSkinCareProducts();
        // Filter only required fields (name, price, availability)
        const filteredProducts = products.map(product => ({
            name: product.name,
            price: product.price,
            availability: product.availability
        }));
        res.status(200).json(filteredProducts);
    } catch (error) {
        // Handle errors and send appropriate response
        console.error('Error in GET /api/skincare-products:', error.message);
        res.status(500).json({ message: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
