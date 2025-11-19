"""
Generated Code Metadata:
========================
Original URL: https://endemage.com
Prompt: Generate a RESTful API endpoint in Node.js for retrieving a list of Abaya products from a database, filtered by collection (e.g., Eid Abaya 2025, Ramadan 2024).
Generated: DETERMINISTIC_359482920d764cb1
Batch ID: 20250622_210703
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

// Abaya product schema
const abayaSchema = new mongoose.Schema({
    name: { type: String, required: true },
    collectionName: { type: String, required: true },
    price: { type: Number, required: true },
    description: { type: String },
    colors: { type: [String] },
    sizes: { type: [String] },
    images: { type: [String] },
    createdAt: { type: Date, default: Date.now }
});

// Abaya model
const Abaya = mongoose.model('Abaya', abayaSchema);

/**
 * GET /api/abayas
 * Retrieves abaya products filtered by collection
 * Query params:
 *   - collection: The collection name to filter by (e.g., "Eid Abaya 2025")
 */
app.get('/api/abayas', async (req, res) => {
    try {
        const { collection } = req.query;
        
        let query = {};
        if (collection) {
            query.collectionName = collection;
        }

        const abayas = await Abaya.find(query).sort({ createdAt: -1 });
        
        if (!abayas || abayas.length === 0) {
            return res.status(404).json({ 
                success: false,
                message: 'No abayas found for the specified collection'
            });
        }

        res.status(200).json({
            success: true,
            count: abayas.length,
            data: abayas
        });
    } catch (error) {
        console.error('Error fetching abayas:', error);
        res.status(500).json({
            success: false,
            message: 'Server error while fetching abayas'
        });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        success: false,
        message: 'Internal server error'
    });
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
