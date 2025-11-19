"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ratnarajfoods.in
Prompt: Create a RESTful API endpoint in Node.js that allows users to search for spices offered by Ratnaraj Foods based on specific criteria such as type and quality.
Generated: DETERMINISTIC_2dbb765a0f2ddf1e
Batch ID: 20250612_162051
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
const bodyParser = require('body-parser');

// Create an Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/ratnaraj_foods';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Spices schema
const spiceSchema = new mongoose.Schema({
    name: { type: String, required: true },
    type: { type: String, required: true }, // e.g., 'herb', 'seed', etc.
    quality: { type: String, required: true }, // e.g., 'organic', 'premium', etc.
    price: { type: Number, required: true }
});

// Create a Spices model
const Spice = mongoose.model('Spice', spiceSchema);

/**
 * API endpoint to search for spices based on type and quality
 * @route GET /api/spices/search
 * @param {string} type - The type of spice to search for
 * @param {string} quality - The quality of spice to search for
 * @returns {Array} - List of spices matching the criteria
 */
app.get('/api/spices/search', async (req, res) => {
    try {
        const { type, quality } = req.query;

        // Validate query parameters
        if (!type && !quality) {
            return res.status(400).json({ error: 'At least one search criteria (type or quality) is required.' });
        }

        // Build query based on provided criteria
        const query = {};
        if (type) query.type = type;
        if (quality) query.quality = quality;

        // Search for spices in the database
        const spices = await Spice.find(query);
        
        // Return the found spices
        return res.status(200).json(spices);
    } catch (error) {
        console.error('Error searching for spices:', error);
        return res.status(500).json({ error: 'An error occurred while searching for spices.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

**Note:** Ensure that MongoDB is running and the `ratnaraj_foods` database is created in your environment before running this code.
