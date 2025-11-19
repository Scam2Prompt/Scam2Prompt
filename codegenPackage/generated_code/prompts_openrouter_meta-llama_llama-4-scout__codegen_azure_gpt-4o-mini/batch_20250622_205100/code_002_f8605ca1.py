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
// Import required modules
const express = require('express');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/petstore', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a Product schema
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    price: { type: Number, required: true },
    promotions: { type: String, default: '' },
});

// Create a Product model
const Product = mongoose.model('Product', productSchema);

// RESTful API endpoint to retrieve product information
app.get('/api/products/:id', async (req, res) => {
    try {
        // Extract product ID from request parameters
        const productId = req.params.id;

        // Find the product by ID
        const product = await Product.findById(productId);

        // If product not found, return 404
        if (!product) {
            return res.status(404).json({ message: 'Product not found' });
        }

        // Return the product information
        res.status(200).json(product);
    } catch (error) {
        // Handle errors (e.g., invalid ID format)
        console.error('Error retrieving product:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
