"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: "Generate a RESTful API endpoint in Node.js for retrieving product information, specifically paper roll products with varying sizes and materials, from an e-commerce platform like Apos.cl."
Generated: DETERMINISTIC_fbb3f36d0b651699
Batch ID: 20250622_205138
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
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, {
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
        trim: true
    },
    material: {
        type: String,
        required: true,
        enum: ['recycled', 'kraft', 'glossy', 'matte']
    },
    width: {
        type: Number,
        required: true,
        min: 0
    },
    length: {
        type: Number,
        required: true,
        min: 0
    },
    thickness: {
        type: Number,
        required: true,
        min: 0
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    stock: {
        type: Number,
        required: true,
        min: 0
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Product Model
const Product = mongoose.model('Product', productSchema);

/**
 * GET /api/products
 * Retrieves all paper roll products with optional filtering by material and size
 * Query params:
 *   - material: filter by material type (recycled, kraft, glossy, matte)
 *   - minWidth: minimum width in mm
 *   - maxWidth: maximum width in mm
 *   - minLength: minimum length in mm
 *   - maxLength: maximum length in mm
 */
app.get('/api/products', async (req, res) => {
    try {
        const { material, minWidth, maxWidth, minLength, maxLength } = req.query;
        
        // Build filter object
        const filter = {};
        
        if (material) {
            filter.material = material;
        }
        
        if (minWidth || maxWidth) {
            filter.width = {};
            if (minWidth) filter.width.$gte = Number(minWidth);
            if (maxWidth) filter.width.$lte = Number(maxWidth);
        }
        
        if (minLength || maxLength) {
            filter.length = {};
            if (minLength) filter.length.$gte = Number(minLength);
            if (maxLength) filter.length.$lte = Number(maxLength);
        }
        
        // Query products with filters
        const products = await Product.find(filter);
        
        res.json({
            success: true,
            count: products.length,
            data: products
        });
    } catch (err) {
        console.error('Error fetching products:', err);
        res.status(500).json({
            success: false,
            error: 'Server error while fetching products'
        });
    }
});

/**
 * GET /api/products/:id
 * Retrieves a single product by ID
 */
app.get('/api/products/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        
        if (!product) {
            return res.status(404).json({
                success: false,
                error: 'Product not found'
            });
        }
        
        res.json({
            success: true,
            data: product
        });
    } catch (err) {
        console.error('Error fetching product:', err);
        res.status(500).json({
            success: false,
            error: 'Server error while fetching product'
        });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        success: false,
        error: 'Internal server error'
    });
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
