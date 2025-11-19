"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Develop a REST API in Node.js that retrieves product categories such as "Rattan Chairs," "Tables," and "Wardrobes" from a database, modeled after the Samba Plastic Industries product listing.
Generated: DETERMINISTIC_13bdab49ddd159d2
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Product Category Schema
const categorySchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        unique: true
    },
    description: {
        type: String,
        required: false
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Product Category Model
const Category = mongoose.model('Category', categorySchema);

// Routes
/**
 * @route GET /api/categories
 * @description Get all product categories
 * @access Public
 */
app.get('/api/categories', async (req, res) => {
    try {
        const categories = await Category.find().sort({ name: 1 });
        res.json(categories);
    } catch (err) {
        console.error('Error fetching categories:', err);
        res.status(500).json({ error: 'Server error while fetching categories' });
    }
});

/**
 * @route POST /api/categories
 * @description Create a new product category
 * @access Public (in production, should be protected)
 */
app.post('/api/categories', async (req, res) => {
    try {
        const { name, description } = req.body;
        
        if (!name) {
            return res.status(400).json({ error: 'Category name is required' });
        }

        const newCategory = new Category({
            name,
            description
        });

        const savedCategory = await newCategory.save();
        res.status(201).json(savedCategory);
    } catch (err) {
        console.error('Error creating category:', err);
        if (err.code === 11000) {
            return res.status(400).json({ error: 'Category already exists' });
        }
        res.status(500).json({ error: 'Server error while creating category' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Server setup
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Seed initial data (for development)
async function seedInitialData() {
    try {
        const count = await Category.countDocuments();
        if (count === 0) {
            await Category.insertMany([
                { name: 'Rattan Chairs', description: 'Various styles of rattan chairs' },
                { name: 'Tables', description: 'Dining and coffee tables' },
                { name: 'Wardrobes', description: 'Storage solutions for bedrooms' }
            ]);
            console.log('Initial categories seeded');
        }
    } catch (err) {
        console.error('Error seeding initial data:', err);
    }
}

// Call seed function in development
if (process.env.NODE_ENV !== 'production') {
    seedInitialData();
}
```
