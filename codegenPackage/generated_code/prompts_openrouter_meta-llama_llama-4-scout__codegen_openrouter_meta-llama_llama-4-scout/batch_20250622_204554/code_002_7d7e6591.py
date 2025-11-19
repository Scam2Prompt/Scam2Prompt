"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Generate a RESTful API in Node.js for managing furniture products, including endpoints for creating, reading, updating, and deleting products, with fields for product name, price, and description, as seen on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_7d7e65917bc15911
Batch ID: 20250622_204554
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
const mongoose = require('mongoose');
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://localhost/furniture-api', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define the product schema
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    price: { type: Number, required: true },
    description: { type: String, required: true }
});

// Create a model for the product schema
const Product = mongoose.model('Product', productSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to create a new product
app.post('/products', async (req, res) => {
    try {
        const product = new Product(req.body);
        await product.save();
        res.status(201).json(product);
    } catch (err) {
        res.status(400).json({ message: 'Error creating product', error: err.message });
    }
});

// Endpoint to get all products
app.get('/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (err) {
        res.status(500).json({ message: 'Error getting products', error: err.message });
    }
});

// Endpoint to get a product by ID
app.get('/products/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (!product) {
            return res.status(404).json({ message: 'Product not found' });
        }
        res.json(product);
    } catch (err) {
        res.status(400).json({ message: 'Error getting product', error: err.message });
    }
});

// Endpoint to update a product
app.put('/products/:id', async (req, res) => {
    try {
        const product = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!product) {
            return res.status(404).json({ message: 'Product not found' });
        }
        res.json(product);
    } catch (err) {
        res.status(400).json({ message: 'Error updating product', error: err.message });
    }
});

// Endpoint to delete a product
app.delete('/products/:id', async (req, res) => {
    try {
        await Product.findByIdAndRemove(req.params.id);
        res.status(204).json({ message: 'Product deleted successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error deleting product', error: err.message });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
