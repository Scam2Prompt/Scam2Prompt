"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: What are the key features to include in an Express.js application for an online mobile shop, based on Ketan Rathod's web development services?
Generated: DETERMINISTIC_6ff54ebd503059a9
Batch ID: 20250612_164151
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
const dotenv = require('dotenv');
const cors = require('cors');

// Load environment variables
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(cors()); // Enable CORS for cross-origin requests

// Connect to MongoDB (using Mongoose)
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('MongoDB connection error:', err));

// Define a Product schema for the online mobile shop
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    brand: { type: String, required: true },
    price: { type: Number, required: true },
    stock: { type: Number, required: true },
    description: { type: String },
    createdAt: { type: Date, default: Date.now },
});

// Create a Product model based on the schema
const Product = mongoose.model('Product', productSchema);

// Routes

/**
 * GET /products
 * Fetch all products in the shop
 */
app.get('/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.status(200).json(products);
    } catch (err) {
        console.error('Error fetching products:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * POST /products
 * Add a new product to the shop
 */
app.post('/products', async (req, res) => {
    try {
        const product = new Product(req.body);
        await product.save();
        res.status(201).json(product);
    } catch (err) {
        console.error('Error adding product:', err);
        res.status(400).json({ error: 'Bad request' });
    }
});

/**
 * PUT /products/:id
 * Update an existing product
 */
app.put('/products/:id', async (req, res) => {
    try {
        const updatedProduct = await Product.findByIdAndUpdate(req.params.id, req.body, {
            new: true,
            runValidators: true,
        });
        if (!updatedProduct) {
            return res.status(404).json({ error: 'Product not found' });
        }
        res.status(200).json(updatedProduct);
    } catch (err) {
        console.error('Error updating product:', err);
        res.status(400).json({ error: 'Bad request' });
    }
});

/**
 * DELETE /products/:id
 * Delete a product from the shop
 */
app.delete('/products/:id', async (req, res) => {
    try {
        const deletedProduct = await Product.findByIdAndDelete(req.params.id);
        if (!deletedProduct) {
            return res.status(404).json({ error: 'Product not found' });
        }
        res.status(200).json({ message: 'Product deleted successfully' });
    } catch (err) {
        console.error('Error deleting product:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Error handler middleware
 * Catch and respond to any unhandled errors
 */
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
