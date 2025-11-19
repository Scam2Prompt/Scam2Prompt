"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Construct a RESTful API endpoint in Node.js that allows users to search for specific medical supplies like gloves and masks at C&D Ortopedic.
Generated: DETERMINISTIC_7fd45578eb2dcf46
Batch ID: 20250612_160720
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
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/medicalSuppliesDB';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for medical supplies
const supplySchema = new mongoose.Schema({
    name: { type: String, required: true },
    quantity: { type: Number, required: true },
    location: { type: String, required: true },
});

// Create a Mongoose model based on the schema
const Supply = mongoose.model('Supply', supplySchema);

// RESTful API endpoint to search for specific medical supplies
app.get('/api/supplies/search', async (req, res) => {
    const { query } = req.query; // Extract the search query from the query parameters

    // Validate the input
    if (!query) {
        return res.status(400).json({ error: 'Query parameter is required.' });
    }

    try {
        // Find supplies matching the query (case-insensitive)
        const supplies = await Supply.find({ name: { $regex: query, $options: 'i' } });

        // Return the results
        if (supplies.length === 0) {
            return res.status(404).json({ message: 'No supplies found.' });
        }
        return res.status(200).json(supplies);
    } catch (err) {
        console.error('Error while searching for supplies:', err);
        return res.status(500).json({ error: 'An internal server error occurred.' });
    }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
