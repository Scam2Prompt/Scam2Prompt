"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: "Create a RESTful API in Node.js to manage insurance solutions, including endpoints for retrieving product information, similar to Yexine Rangel's portfolio de soluciones."
Generated: DETERMINISTIC_a2a288ebc2277d9d
Batch ID: 20250622_205111
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your own connection string)
mongoose.connect('mongodb://localhost:27017/insurance', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for insurance products
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    coverage: { type: String, required: true },
});

// Create a Mongoose model for insurance products
const Product = mongoose.model('Product', productSchema);

// Endpoint to retrieve all insurance products
app.get('/api/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.status(200).json(products);
    } catch (error) {
        console.error('Error retrieving products:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to retrieve a single product by ID
app.get('/api/products/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (!product) {
            return res.status(404).json({ message: 'Product not found' });
        }
        res.status(200).json(product);
    } catch (error) {
        console.error('Error retrieving product:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to create a new insurance product
app.post('/api/products', async (req, res) => {
    const { name, description, price, coverage } = req.body;

    // Validate request body
    if (!name || !description || !price || !coverage) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    try {
        const newProduct = new Product({ name, description, price, coverage });
        await newProduct.save();
        res.status(201).json(newProduct);
    } catch (error) {
        console.error('Error creating product:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to update an existing product
app.put('/api/products/:id', async (req, res) => {
    const { name, description, price, coverage } = req.body;

    try {
        const updatedProduct = await Product.findByIdAndUpdate(
            req.params.id,
            { name, description, price, coverage },
            { new: true, runValidators: true }
        );

        if (!updatedProduct) {
            return res.status(404).json({ message: 'Product not found' });
        }

        res.status(200).json(updatedProduct);
    } catch (error) {
        console.error('Error updating product:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to delete a product
app.delete('/api/products/:id', async (req, res) => {
    try {
        const deletedProduct = await Product.findByIdAndDelete(req.params.id);
        if (!deletedProduct) {
            return res.status(404).json({ message: 'Product not found' });
        }
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting product:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
