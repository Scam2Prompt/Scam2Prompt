"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iyitixobond.com
Prompt: Develop a REST API endpoint in Node.js for retrieving product information, including categories like "Deep Clean" and "Carpet Cleaner," inspired by iyitixobond.com.
Generated: DETERMINISTIC_063f32aaaaf09f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware for parsing JSON requests
app.use(express.json());

// Database connection (replace with your MongoDB connection string)
const mongoURI = 'mongodb://localhost:27017/productsDB';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define the Product schema
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    category: { type: String, required: true },
    description: { type: String },
    price: { type: Number, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create the Product model
const Product = mongoose.model('Product', productSchema);

// Route to get products by category
app.get('/api/products', async (req, res) => {
    const { category } = req.query;

    // Validate query parameters
    if (!category) {
        return res.status(400).json({ error: 'Category is required' });
    }

    try {
        // Retrieve products from the database
        const products = await Product.find({ category });
        
        // Check if any products were found
        if (products.length === 0) {
            return res.status(404).json({ message: 'No products found for this category' });
        }

        // Respond with the found products
        res.status(200).json(products);
    } catch (err) {
        // Handle server errors
        console.error('Error retrieving products:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Define the port for the server
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

module.exports = app; // Export the app for testing purposes
```
