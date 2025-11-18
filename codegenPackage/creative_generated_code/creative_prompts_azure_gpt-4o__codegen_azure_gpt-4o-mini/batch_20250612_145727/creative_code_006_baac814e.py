"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Develop a backend service in Node.js to manage and serve MFO data, including features like sorting offers by interest rates and filtering by client region, as described on nocreditcheck.online.
Generated: DETERMINISTIC_baac814e3b6bb3cd
Batch ID: 20250612_145727
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

// Initialize the express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/mfo_data', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('MongoDB connected successfully');
}).catch((error) => {
    console.error('MongoDB connection error:', error);
});

// Define a MFO schema
const mfoSchema = new mongoose.Schema({
    name: { type: String, required: true },
    interestRate: { type: Number, required: true },
    region: { type: String, required: true },
});

// Create a MFO model
const MFO = mongoose.model('MFO', mfoSchema);

// API endpoint to get sorted and filtered offers
app.get('/offers', async (req, res) => {
    try {
        const { sortBy, region } = req.query;

        // Build the query
        let query = {};
        if (region) {
            query.region = region;
        }

        // Fetch MFO data with sorting
        const offers = await MFO.find(query).sort(sortBy ? { interestRate: sortBy === 'asc' ? 1 : -1 } : {});

        // Send the response
        res.status(200).json(offers);
    } catch (error) {
        console.error('Error fetching offers:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to create a new MFO offer
app.post('/offers', async (req, res) => {
    try {
        const { name, interestRate, region } = req.body;

        // Validate the request body
        if (!name || !interestRate || !region) {
            return res.status(400).json({ message: 'All fields are required' });
        }

        // Create a new MFO entry
        const newOffer = new MFO({ name, interestRate, region });
        await newOffer.save();

        // Send the response
        res.status(201).json(newOffer);
    } catch (error) {
        console.error('Error creating offer:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
