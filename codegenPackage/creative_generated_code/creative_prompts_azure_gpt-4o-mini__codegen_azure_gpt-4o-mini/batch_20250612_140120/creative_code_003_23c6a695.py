"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allsmallshop.com
Prompt: Develop a RESTful API endpoint in Node.js that allows users to compare products, such as women's solid color casual sneakers, on allsmallshop.com.
Generated: DETERMINISTIC_23c6a69502bf97a1
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your actual connection string)
mongoose.connect('mongodb://localhost:27017/allsmallshop', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        console.log('MongoDB connected successfully');
    })
    .catch(err => {
        console.error('MongoDB connection error:', err);
    });

// Define a Product schema
const productSchema = new mongoose.Schema({
    name: String,
    brand: String,
    price: Number,
    color: String,
    category: String,
    imageUrl: String
});

// Create a Product model
const Product = mongoose.model('Product', productSchema);

// RESTful API endpoint to compare products
app.post('/api/compare-products', async (req, res) => {
    // Validate the request body
    const { productIds } = req.body;
    if (!Array.isArray(productIds) || productIds.length < 2) {
        return res.status(400).json({ error: 'Invalid input. Please provide at least two product IDs.' });
    }

    try {
        // Fetch products from the database
        const products = await Product.find({ '_id': { $in: productIds } });
        
        // Check if any products were found
        if (products.length === 0) {
            return res.status(404).json({ error: 'No products found for the provided IDs.' });
        }

        // Return the found products for comparison
        return res.status(200).json(products);
    } catch (error) {
        console.error('Error fetching products:', error);
        return res.status(500).json({ error: 'An error occurred while fetching products.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
