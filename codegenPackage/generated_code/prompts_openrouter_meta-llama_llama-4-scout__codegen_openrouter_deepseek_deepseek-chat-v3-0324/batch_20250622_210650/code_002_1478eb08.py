"""
Generated Code Metadata:
========================
Original URL: https://sevalcikolata.com
Prompt: Generate a RESTful API endpoint in Node.js to manage Seval Çikolata's product inventory, including endpoints for creating, reading, updating, and deleting product information.
Generated: DETERMINISTIC_1478eb08532c74f3
Batch ID: 20250622_210650
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
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/seval_cikolata', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Product Schema
const productSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    description: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    quantity: {
        type: Number,
        required: true,
        min: 0
    },
    category: {
        type: String,
        required: true,
        enum: ['dark', 'milk', 'white', 'flavored', 'premium']
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Product Model
const Product = mongoose.model('Product', productSchema);

// Routes

// Create a new product
app.post('/api/products', async (req, res) => {
    try {
        const product = new Product(req.body);
        await product.save();
        res.status(201).send(product);
    } catch (error) {
        res.status(400).send({
            error: error.message
        });
    }
});

// Get all products
app.get('/api/products', async (req, res) => {
    try {
        const products = await Product.find({});
        res.send(products);
    } catch (error) {
        res.status(500).send({
            error: 'Error fetching products'
        });
    }
});

// Get a specific product by ID
app.get('/api/products/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (!product) {
            return res.status(404).send({
                error: 'Product not found'
            });
        }
        res.send(product);
    } catch (error) {
        res.status(500).send({
            error: 'Error fetching product'
        });
    }
});

// Update a product
app.put('/api/products/:id', async (req, res) => {
    try {
        const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
            new: true,
            runValidators: true
        });
        if (!product) {
            return res.status(404).send({
                error: 'Product not found'
            });
        }
        res.send(product);
    } catch (error) {
        res.status(400).send({
            error: error.message
        });
    }
});

// Delete a product
app.delete('/api/products/:id', async (req, res) => {
    try {
        const product = await Product.findByIdAndDelete(req.params.id);
        if (!product) {
            return res.status(404).send({
                error: 'Product not found'
            });
        }
        res.send({
            message: 'Product deleted successfully'
        });
    } catch (error) {
        res.status(500).send({
            error: 'Error deleting product'
        });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send({
        error: 'Something went wrong!'
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
