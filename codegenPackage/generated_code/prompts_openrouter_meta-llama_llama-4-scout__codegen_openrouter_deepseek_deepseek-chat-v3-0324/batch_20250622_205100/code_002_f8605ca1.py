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
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// Sample product database
const products = [
    {
        id: uuidv4(),
        name: "PRO PLAN DOG ADULT RACAS MÉDIAS 15 KG",
        category: "Dog Food",
        price: 89.99,
        promotion: {
            isActive: true,
            discountPercentage: 15,
            validUntil: "2023-12-31"
        },
        stock: 50,
        description: "Premium dog food for medium breed adult dogs"
    },
    // Add more products as needed
];

/**
 * GET /products - Retrieve all products
 */
app.get('/products', (req, res) => {
    try {
        res.status(200).json(products);
    } catch (error) {
        console.error('Error retrieving products:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /products/:id - Retrieve a specific product by ID
 */
app.get('/products/:id', (req, res) => {
    try {
        const productId = req.params.id;
        const product = products.find(p => p.id === productId);

        if (!product) {
            return res.status(404).json({ error: 'Product not found' });
        }

        res.status(200).json(product);
    } catch (error) {
        console.error('Error retrieving product:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /products/search/:name - Search products by name
 */
app.get('/products/search/:name', (req, res) => {
    try {
        const searchTerm = req.params.name.toLowerCase();
        const matchedProducts = products.filter(p => 
            p.name.toLowerCase().includes(searchTerm)
        );

        if (matchedProducts.length === 0) {
            return res.status(404).json({ error: 'No products found matching the search term' });
        }

        res.status(200).json(matchedProducts);
    } catch (error) {
        console.error('Error searching products:', error);
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
    console.log(`Server is running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
